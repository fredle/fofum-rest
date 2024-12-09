from django.db import models
from rest_framework import serializers, viewsets
from fofumapi.pagination import CustomPagination
from fofumapi.mixins import ContentRangeHeaderMixin
from rest_framework.viewsets import ModelViewSet

class Blockchain(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    rpc_url = models.URLField(blank=True, null=True)
    
    class Meta:
        db_table = 'blockchain'

    def __str__(self):
        return self.name

class BlockchainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blockchain
        fields = '__all__'

class BlockchainViewSet(ContentRangeHeaderMixin, ModelViewSet):
    queryset = Blockchain.objects.all()
    serializer_class = BlockchainSerializer
    pagination_class = CustomPagination

