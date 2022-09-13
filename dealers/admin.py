from django.contrib import admin
from dealers.models import DealerProfile, DealerCar, TransactionToShowroom

admin.site.register(DealerProfile)
admin.site.register(DealerCar)
admin.site.register(TransactionToShowroom)
