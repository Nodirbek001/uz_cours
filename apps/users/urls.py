from django.urls import path
from rest_framework.authtoken import views

from apps.users.api_endpoints import registration, profile
from apps.users.api_endpoints.registration import SendVerificationCode
from apps.users.api_endpoints.registration import VerifyCode
from apps.users.api_endpoints.registration import SetPassword
from apps.users.api_endpoints.profile import ChangePassword
from apps.users.api_endpoints.profile import GetProfile
from apps.users.api_endpoints.profile import UpdateProfile
from apps.users.api_endpoints.profile import Logout

urlpatterns = [
    # registiration
    path(
        'register/send-verification-code',
        SendVerificationCode.SendVerificationCodeAPIView.as_view(),
        name='send_verification_code'
    ),
    path("register/verify-code/", registration.VerifyCode.VerifyCodeAPIView.as_view(), name="register-verify-code"),
    path("register/set-password/", registration.SetPassword.SetPasswordAPIView.as_view(), name="register-set-password"),
    # login
    path("login/", views.obtain_auth_token, name='login-username-password'),
    # profile
    path("profile/change-password/", profile.ChangePassword.ChangePasswordAPIView.as_view(),
         name="profile-change-password"),
    path("profile/get-profile/", profile.GetProfile.GetProfileAPIView.as_view(), name="profile-get-profile"),
    path("profile/update/", profile.UpdateProfile.UpdateProfileAPIView.as_view(), name="profile-update"),
    #log out
    path("profile/logout/", profile.Logout.LogoutAPIView.as_view(), name="profile-logout")
    #change phone number or email
    #number

]
