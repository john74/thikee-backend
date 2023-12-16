from django.urls import path

from weather import views


app_name = "weather"

urlpatterns = [
    path("", views.WeatherAPIView.as_view(), name="list"),
]