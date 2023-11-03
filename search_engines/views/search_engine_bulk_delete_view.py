from django.core.exceptions import ValidationError

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from search_engines.models import SearchEngine
from search_engines.serializers import SearchEngineSerializer


class SearchEngineBulkDeleteAPIView(APIView):
    search_engine_serializer_class = SearchEngineSerializer

    def delete(self, request, *args, **kwargs):
        search_engine_ids = request.data.get('ids', [])
        all_search_engines = SearchEngine.objects.all()

        search_engines_to_delete = all_search_engines.filter(id__in=search_engine_ids)
        search_engines_to_delete.delete()

        all_search_engines = all_search_engines.exclude(id__in=search_engines_to_delete.values('id'))
        default_engine = all_search_engines.get(is_default=True)
        non_default_engines = all_search_engines.filter(is_default=False)

        serialized_default_engine = self.search_engine_serializer_class(default_engine).data
        serialized_non_default_engines = self.search_engine_serializer_class(non_default_engines, many=True).data

        response_data = {
            "default": serialized_default_engine,
            "nonDefault": serialized_non_default_engines,
        }

        return Response(data=response_data, status=status.HTTP_200_OK)