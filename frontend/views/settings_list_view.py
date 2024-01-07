from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from bookmarks.models import (
    Bookmark, BookmarkCategory, BookmarkSubCategory
)
from bookmarks.serializers import (
    BookmarkSerializer, BookmarkCategorySerializer,
    ShortcutSerializer, BookmarkSubCategorySerializer
)
from bookmarks.utils import (
    group_bookmarks, group_bookmark_categories,
)
from weather.utils import retrieve_weather_data
from search_engines.models import SearchEngine
from search_engines.serializers import SearchEngineSerializer
from settings.models import Setting
from settings.serializers import SettingSerializer
from users.models import User
from users.serializers import UserSerializer



class SettingsListAPIView(APIView):
    bookmark_serializer_class = BookmarkSerializer
    bookmark_category_serializer_class = BookmarkCategorySerializer
    bookmark_sub_category_serializer_class = BookmarkSubCategorySerializer
    shortcut_serializer_class = ShortcutSerializer
    search_engine_serializer_class = SearchEngineSerializer
    user_serializer_class = UserSerializer
    setting_serializer_class = SettingSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.user.id).first()
        if not user:
            return Response(data={"error": "No user found"}, status=status.HTTP_200_OK)

        serialized_user = self.user_serializer_class(user).data
        user_id = user.id

        all_bookmark_categories = BookmarkCategory.objects.filter(user=user_id)
        serialized_categories = self.bookmark_category_serializer_class(all_bookmark_categories, many=True).data

        response_data = {
            "categories": serialized_categories,
        }

        return Response(data=response_data, status=status.HTTP_200_OK)
