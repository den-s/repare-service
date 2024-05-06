import datetime as dt, jwt
from repair_service.settings import SECRET_KEY
from django.utils.translation import gettext as _
from repair_service.settings import TOKEN_LIFETIME_MINUTES, REFRESH_TOKEN_LIFETIME_DAYS

TOKEN_EXPIRED_EXCEPTION = {
    "type": "token_expired",
    "description": _("Token expired error"),
}

TOKEN_INVALID_EXCEPTION = {
    "type": "token_invalid",
    "description": _("Invalid token error"),
}


class Token:
    def __init__(self, token=None, refresh_token=None) -> None:
        self.refresh_token = refresh_token
        self.token = token

    def generate(self, user_id, is_refresh=False) -> str:
        pl = {
            "id": user_id,
            "iat": dt.datetime.now(dt.timezone.utc),
        }

        if is_refresh:
            exp = dt.datetime.now(dt.timezone.utc) + dt.timedelta(
                days=REFRESH_TOKEN_LIFETIME_DAYS
            )
        else:
            exp = dt.datetime.now(dt.timezone.utc) + dt.timedelta(
                minutes=TOKEN_LIFETIME_MINUTES
            )

        payload = dict(pl, **{"exp": exp})
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    def decode(self, is_refresh=False) -> dict[str, str]:
        token = self.token if not is_refresh else self.refresh_token
        if not token:
            raise jwt.exceptions.InvalidTokenError

        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    def refresh(self):
        if not self.refresh_token:
            raise jwt.exceptions.InvalidTokenError

        data = self.decode(is_refresh=True)
        return self.generate(data["id"])
