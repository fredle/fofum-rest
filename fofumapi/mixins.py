from rest_framework.response import Response

class ContentRangeHeaderMixin:
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        total_count = self.filter_queryset(self.get_queryset()).count()
        response['Content-Range'] = f'items {self.paginator.page.start_index()}-{self.paginator.page.end_index()}/{total_count}'
        return response