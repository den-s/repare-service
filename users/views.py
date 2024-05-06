import jwt
from rest_framework.views import APIView, Response
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
from django.utils.translation import gettext as _
from repair_service.decorators import time_logger
from users.serializers import UserSerializer
from users.models import User
from users.token import Token, TOKEN_EXPIRED_EXCEPTION, TOKEN_INVALID_EXCEPTION


class LoginView(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        try:
            user = User.objects.get(email=email)

        except User.DoesNotExist:
            raise AuthenticationFailed("Incorrect email")

        if not user.check_password(password):
            return Response(
                {
                    "type": "incorrect_password",
                    "description": _("The Password is incorrect"),
                }
            )

        userdata = UserSerializer(data=user)
        userdata.is_valid()

        token = Token()
        jwt = token.generate(user_id=user.id)
        jwt_refresh = Token().generate(user_id=user.id, is_refresh=True)

        response = Response({"token": jwt, "refresh": jwt_refresh})
        return response


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        return response


class TokenRefreshView(APIView):
    def post(self, request):
        token_data = request.data.get("refresh")
        try:
            token = Token(refresh_token=token_data).refresh()
            return Response({"token": token})
        except jwt.exceptions.ExpiredSignatureError:
            return JsonResponse(TOKEN_EXPIRED_EXCEPTION, status=403)
        except jwt.exceptions.InvalidTokenError:
            return JsonResponse(TOKEN_INVALID_EXCEPTION, status=403)


class UserView(APIView):
    @time_logger
    def get(self, request, id=None):
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
        except User.DoesNotExist:
            return Response(
                {
                    "type": "incorrect_email",
                    "description": _("The Email is incorrect"),
                }
            )

        return Response(serializer.data)


class UsersView(APIView):
    @time_logger
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        data = {item["id"]: dict(item) for item in serializer.data}
        return Response(data)
