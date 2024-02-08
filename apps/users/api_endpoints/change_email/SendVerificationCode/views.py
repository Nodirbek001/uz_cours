from django.core.cache import cache
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import gettext_lazy as _

from apps.users.api_endpoints.change_email.SendVerificationCode.serializers import SendVerificationCodeSerializer
from apps.users.services.generators import generate_verification_code
from apps.users.services.message_senders import send_verification_code_email


class SendVerificationAPICodeView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    #@swagger_auto_schema(request_body=SendVerificationCodeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = SendVerificationCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        new_email = serializer.validated_data['new_email']
        if cache.get(user.id) is not None:
            return Response(
                data={"error": "Verification code is already sent"},
                status=status.HTTP_400_BAD_REQUEST
            )

        code = generate_verification_code()
        send_verification_code_email(new_email, code)

        cache_data = {
            "new_email": new_email,
            "code": code,
        }
        cache.set(user.id, cache_data)
        return Response(data={"message": _("Verification code was send successfully")}, status=status.HTTP_200_OK)


__all__ = ['SendVerificationAPICodeView']
