"""
Main URL configurations for fEMR-OnChain-Core. This redirects to the other apps in this project.
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView

from main.auth_views import change_password, required_change_password

urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("main/assets/favicon.ico")),
    ),
    path("admin/", admin.site.urls),
    path("", include("main.urls", namespace="main")),
    path("app_mr/", include("app_mr.urls", namespace="app_mr")),
    path("messages/", include("clinic_messages.urls", namespace="clinic_messages")),
    path("silk/", include("silk.urls", namespace="silk")),
    re_path(r"session_security/", include("session_security.urls")),
    re_path(
        r"^password_reset/$",
        auth_views.PasswordResetView.as_view(
            template_name="auth/password_reset.html",
            email_template_name="auth/password_reset_email.html",
        ),
        name="password_reset",
    ),
    re_path(
        r"^password_reset/done/$",
        auth_views.PasswordResetDoneView.as_view(
            template_name="auth/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="auth/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    re_path(
        r"^reset/done/$",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="auth/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("change_password/", change_password, name="change_password"),
    path(
        "required_change_password/",
        required_change_password,
        name="required_change_password",
    ),
]
