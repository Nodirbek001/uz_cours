from django.core.cache import cache
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import gettext_lazy as _

from apps.users.api_endpoints.registration.VerifyCode.serializers import VerifyCodeSerializer


class VerifyCodeAPIView(APIView):
    @swagger_auto_schema(request_body=VerifyCodeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = VerifyCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_or_email = serializer.validated_data['phone_or_email']
        session = serializer.validated_data['session']
        code = serializer.validated_data['code']
        cache_data = cache.get(phone_or_email, None)
        if cache_data is None:
            return Response(
                data={"error": _("varification code expired or email/phone_number invalid")},
                status=status.HTTP_400_BAD_REQUEST
            )

        if cache_data["code"] != code:
            return Response(data={"error": _("Incorrect code")})
        session_cache_data = cache.get(session)
        print(session)
        print(cache.get(session))
        session_cache_data.update({"is_verified": True})
        cache.set(session, session_cache_data)

        return Response(data={"message": _("You verification code successfully")}, status=status.HTTP_200_OK)


__all__ = ['VerifyCodeAPIView']
