from django.db import models
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from fofumapi.pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
import django_filters
from fofumapi.mixins import ContentRangeHeaderMixin

class Opportunity(models.Model):
    TYPE_CHOICES = [
        ('staking', 'Staking'),
        ('lending', 'Lending'),
        ('farming', 'Yield Farming'),
    ]

    protocol = models.ForeignKey('Protocol', on_delete=models.CASCADE, related_name='opportunities')
    name = models.CharField(max_length=100)
    opportunity_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    apy = models.DecimalField(max_digits=10, decimal_places=2)  # Annual Percentage Yield
    risk_score = models.IntegerField()  # A score out of 100
    liquidity = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)  # Total liquidity in USD
    token = models.CharField(max_length=50)  # Token name (e.g., "USDC", "DAI")

    class Meta:
        db_table = 'opportunity'

    def __str__(self):
        return f"{self.name} - {self.protocol.name}"

class OpportunitySerializer(ModelSerializer):
    class Meta:
        model = Opportunity
        fields = '__all__'
class OpportunityFilter(FilterSet):
    risk_score = django_filters.NumberFilter(field_name='risk_score', lookup_expr='exact')
    risk_score__lte = django_filters.NumberFilter(field_name='risk_score', lookup_expr='lte')
    risk_score__gte = django_filters.NumberFilter(field_name='risk_score', lookup_expr='gte')
    apy = django_filters.NumberFilter(field_name='apy', lookup_expr='exact')
    apy__lte = django_filters.NumberFilter(field_name='apy', lookup_expr='lte')
    apy__gte = django_filters.NumberFilter(field_name='apy', lookup_expr='gte')
    liquidity = django_filters.NumberFilter(field_name='liquidity', lookup_expr='exact')
    liquidity__lte = django_filters.NumberFilter(field_name='liquidity', lookup_expr='lte')
    liquidity__gte = django_filters.NumberFilter(field_name='liquidity', lookup_expr='gte')
    name = django_filters.CharFilter(field_name='name', lookup_expr='exact')
    name__icontains = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    opportunity_type = django_filters.CharFilter(field_name='opportunity_type', lookup_expr='exact')
    token = django_filters.CharFilter(field_name='token', lookup_expr='exact')
    token__icontains = django_filters.CharFilter(field_name='token', lookup_expr='icontains')
    protocol__name = django_filters.CharFilter(field_name='protocol__name', lookup_expr='exact')
    protocol__name__icontains = django_filters.CharFilter(field_name='protocol__name', lookup_expr='icontains')

    class Meta:
        model = Opportunity
        fields = []

class OpportunityViewSet(ContentRangeHeaderMixin, ModelViewSet):
    queryset = Opportunity.objects.all()
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = OpportunityFilter
    pagination_class = CustomPagination
    pagination_class = CustomPagination
    serializer_class = OpportunitySerializer

