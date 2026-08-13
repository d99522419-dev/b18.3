from django.urls import path

from .api_views import custom_login, custom_register, get_out, profile, deactivate_account
from .otp_views import SendOTPCodeView, ResetPasswordView, VerifyOTPCodeView



urlpatterns = [
    path("login/", custom_login),
    path("register/", custom_register),
    path("logout/", get_out),
    path("profile/", profile),
    path("deactive/", deactivate_account),
    path("otp-send/", SendOTPCodeView.as_view()),
    path("otp-verify/", VerifyOTPCodeView.as_view()),
    path("reset-password/", ResetPasswordView.as_view())
]
