from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from weather.utils import (
    get_update_time_message, retrieve_weather_data
)
from weather.constants import OPEN_WEATHER_UNITS
from settings.models import Setting


class WeatherAPIView(APIView):

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        setting = Setting.objects.filter(user=user_id).first()
        if not setting:
            return Response(data={"error": "No weather data available"}, status=status.HTTP_400_BAD_REQUEST)

        time_message = get_update_time_message(setting)
        if time_message:
            return Response(data={"error": f"Weather data can be updated again in {time_message}."}, status=status.HTTP_400_BAD_REQUEST)

        weather_data = retrieve_weather_data(setting)
        if not weather_data:
            return Response(data={"error": "No weather data available"}, status=status.HTTP_400_BAD_REQUEST)

        weather_data["message"] = "Weather data updated";
        return Response(data=weather_data, status=status.HTTP_200_OK)
