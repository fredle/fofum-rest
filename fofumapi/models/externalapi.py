from django.db import models

from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from fofumapi.mixins import ContentRangeHeaderMixin
from rest_framework.viewsets import ModelViewSet
from fofumapi.pagination import CustomPagination

class ExternalAPI(models.Model):
    name = models.CharField(max_length=100)
    base_url = models.URLField()
    api_key = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    access = models.CharField(max_length=200)

    class Meta:
        db_table = 'externalapi'

    def __str__(self):
        return self.name

class ExternalAPISerializer(ModelSerializer):
    class Meta:
        model = ExternalAPI
        fields = '__all__'

class ExternalAPIViewSet(ContentRangeHeaderMixin, ModelViewSet):
    queryset = ExternalAPI.objects.all()
    serializer_class = ExternalAPISerializer
    pagination_class = CustomPagination



"""
Many DeFi platforms offer free APIs, though usage limits and available features can vary. Here's a list of notable APIs and their access details:

DefiLlama API

Access: Free with open-source data.
Details: Provides comprehensive DeFi protocol data, including total value locked (TVL) and yield rates. 
DEFI LLAMA
CoinGecko API

Access: Free tier available; paid plans offer higher rate limits and additional features.
Details: Offers cryptocurrency market data, including prices, market capitalization, and historical data. 
COINGECKO
CoinMarketCap API

Access: Free tier with limited access; paid plans provide enhanced features and higher rate limits.
Details: Delivers extensive cryptocurrency data, including rankings, historical data, and exchange information.
Zapper API

Access: Free for non-commercial use; commercial use requires approval.
Details: Aggregates DeFi data, allowing users to track assets across multiple protocols and wallets.
Zerion API

Access: Free for personal use; commercial use may require a partnership.
Details: Provides access to DeFi portfolio data, including assets, debts, and transaction history.
1inch API

Access: Free with rate limits; higher limits may require approval.
Details: Offers data on decentralized exchange (DEX) aggregations, including swap rates and liquidity sources.
KyberSwap API

Access: Free with rate limits; commercial use may require approval.
Details: Provides access to liquidity protocols and DEX aggregation data.
Aave API

Access: Free with open access.
Details: Offers data on lending and borrowing rates, as well as protocol statistics.
Compound API

Access: Free with open access.
Details: Provides data on interest rates, market details, and user balances within the Compound protocol.
Uniswap Subgraph

Access: Free with open access.
Details: Allows querying of Uniswap data, including pools, swaps, and liquidity positions.
SushiSwap API

Access: Free with open access.
Details: Provides data on SushiSwap pools, swaps, and liquidity mining opportunities.
Balancer API

Access: Free with open access.
Details: Offers data on Balancer pools, including token balances, pool swaps, and liquidity provider information.
Curve Finance API

Access: Free with open access.
Details: Provides data on Curve pools, including liquidity, volume, and yield rates.
PancakeSwap API

Access: Free with open access.
Details: Offers data on PancakeSwap pools, swaps, and yield farming opportunities on Binance Smart Chain.
Beefy Finance API

Access: Free with open access.
Details: Aggregates yield farming opportunities across multiple chains and protocols.
Harvest Finance API

Access: Free with open access.
Details: Provides data on automated yield farming strategies and returns.
Yearn Finance API

Access: Free with open access.
Details: Offers data on Yearn vaults, strategies, and performance metrics.
Alchemix API

Access: Free with open access.
Details: Provides data on self-repaying loans and yield strategies.
Rari Capital API

Access: Free with open access.
Details: Offers data on yield aggregation and lending pools.
Idle Finance API

Access: Free with open access.
Details: Provides data on yield optimization strategies across multiple protocols.

"""