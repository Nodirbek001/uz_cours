from django.core.cache import cache
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from apps.users.api_endpoints.registration.SendVerificationCode.serializers import SendVerificationCodeSerializer
from apps.users.choices import VIA_PHONE_NUMBER, VIA_EMAIL
from apps.users.services.generators import generate_auth_session, generate_verification_code
from apps.users.services.message_senders import send_verification_code_sms, send_verification_code_email


class SendVerificationCodeAPIView(APIView):
    @swagger_auto_schema(request_body=SendVerificationCodeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = SendVerificationCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        session = generate_auth_session()
        print(session)
        if data['auth_type'] is VIA_PHONE_NUMBER:
            phone_number = data['phone_number']
            if cache.get(phone_number, None) is not None:
                return Response(
                    data={"error": "Verification code is alredy sent. Please wait for a while before continue"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            code = generate_verification_code()
            send_verification_code_sms(phone_number, code)
            phone_data = {
                "session": session,
                "code": code,
            }
            cache.set(phone_number, phone_data, 120)
            data.update({"username": phone_number})
            print(cache.get(phone_number))
        if data['auth_type'] is VIA_EMAIL:

            email = data['email']
            if cache.get(email, None) is not None:
                return Response(
                    data={"error": "Verification code is already sent"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            code = generate_verification_code()
            send_verification_code_email(email, code)
            email_data = {
                "session": session,
                "code": code,
            }
            cache.set(email, email_data, 120)
            data.update({"username": email})

        cache.set(session, data, 360)
        print(cache.get(session))
        data.update({"session": session})

        serializer = SendVerificationCodeSerializer(data=data)
        if serializer.is_valid():
            # Access the serialized data
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        else:
            # Handle validation errors
            errors = serializer.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)


__all__ = ["SendVerificationCodeAPIView"]
