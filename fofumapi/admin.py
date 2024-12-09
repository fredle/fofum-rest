from django.contrib import admin
from fofumapi.models.blockchain import Blockchain
from fofumapi.models.protocol import Protocol
from fofumapi.models.opportunity import Opportunity
from fofumapi.models.externalapi import ExternalAPI


admin.site.register(Blockchain)
admin.site.register(Protocol)
admin.site.register(Opportunity)
admin.site.register(ExternalAPI)



# Register your models here.


