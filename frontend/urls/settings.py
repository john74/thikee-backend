from django.urls import path

from frontend import views


app_name = "user_settings"

urlpatterns = [
    path("settings/", views.SettingsListAPIView.as_view(), name="settings"),
]