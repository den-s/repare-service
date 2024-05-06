from django.http import JsonResponse
import jwt
from django.utils import translation
from django.utils.translation import gettext as _
from users.token import TOKEN_EXPIRED_EXCEPTION, TOKEN_INVALID_EXCEPTION, Token


class AdminLocaleMiddleware:

    def __init__(self, process_request):
        self.process_request = process_request

    def __call__(self, request):
        if request.path.startswith("/admin"):
            translation.activate("ru")
            request.LANGUAGE_CODE = translation.get_language()

        response = self.process_request(request)

        return response


class AuthMiddleware:

    def __init__(self, process_request):
        self.process_request = process_request

    def __call__(self, request):
        is_non_authorized_paths = (
            len(
                list(
                    filter(
                        lambda p: p in request.path,
                        [
                            "admin",
                            "login",
                            "logout",
                            "token/refresh",
                        ],
                    )
                )
            )
            > 0
        )
        if not is_non_authorized_paths:
            session_token = request.headers.get("Authorization")
            if session_token and session_token.split(" ")[0] == "Bearer":
                try:
                    Token(
                        token=session_token.split(" ")[-1],
                    ).decode()
                    return self.process_request(request)
                except jwt.exceptions.ExpiredSignatureError:
                    return JsonResponse(TOKEN_EXPIRED_EXCEPTION, status=403)
                except jwt.exceptions.InvalidTokenError:
                    return JsonResponse(TOKEN_INVALID_EXCEPTION, status=403)
            else:
                return JsonResponse(TOKEN_INVALID_EXCEPTION, status=403)

        return self.process_request(request)
