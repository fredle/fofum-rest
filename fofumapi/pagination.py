from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math
import json

class CustomPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response(data)

    def paginate_queryset(self, queryset, request, view=None):
        filter_param = request.query_params.get('filter')
        range_param = request.query_params.get('range')
        sort_param = request.query_params.get('sort')

        if filter_param:
            filter_dict = json.loads(filter_param)
            queryset = queryset.filter(**filter_dict)

        if sort_param:
            sort_list = json.loads(sort_param)
            sort_list = [f"{'-' if s == 'DESC' else ''}{field}" for field, s in zip(sort_list[::2], sort_list[1::2])]
            queryset = queryset.order_by(*sort_list)

        if range_param:
            range_list = json.loads(range_param)
            self.page_size = range_list[1] - range_list[0] + 1
            queryset = queryset[range_list[0]:range_list[1] + 1]

        return super().paginate_queryset(queryset, request, view)