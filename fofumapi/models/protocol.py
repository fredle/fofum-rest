from django.db import models
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from fofumapi.pagination import CustomPagination
from fofumapi.mixins import ContentRangeHeaderMixin

class Protocol(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    blockchain = models.ForeignKey('Blockchain', on_delete=models.CASCADE, related_name='protocols')

    class Meta:
        db_table = 'protocol'

    def __str__(self):
        return self.name

class ProtocolSerializer(ModelSerializer):
    class Meta:
        model = Protocol
        fields = '__all__'


class ProtocolViewSet(ContentRangeHeaderMixin, ModelViewSet):

    queryset = Protocol.objects.all()
    serializer_class = ProtocolSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset