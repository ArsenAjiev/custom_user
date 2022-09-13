from django.contrib import admin
from showrooms.models import ShowroomProfile, ShowroomCar, TransactionToCustomer

admin.site.register(ShowroomProfile)
admin.site.register(ShowroomCar)
admin.site.register(TransactionToCustomer)
