from django.urls import path

from apps.users.api_endpoints import registration
from apps.users.api_endpoints.registration import SendVerificationCode
from apps.users.api_endpoints.registration import VerifyCode
from apps.users.api_endpoints.registration import SetPassword

urlpatterns = [
    path(
        'register/send-verification-code',
        SendVerificationCode.SendVerificationCodeAPIView.as_view(),
        name='send_verification_code'
    ),
    path("register/verify-code/", registration.VerifyCode.VerifyCodeAPIView.as_view(), name="register-verify-code"),
    path("register/set-password/", registration.SetPassword.SetPasswordAPIView.as_view(), name="register-set-password"),
]
