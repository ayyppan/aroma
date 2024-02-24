from django.contrib import admin
from myhome.models import Part, Service_type, Service_price, customer, Billing, Org_Bank, UserProfileInfo

# Register your models here.
admin.site.register(Part)
admin.site.register(Service_type)
admin.site.register(Service_price)
admin.site.register(customer)
admin.site.register(Billing)
admin.site.register(Org_Bank)
admin.site.register(UserProfileInfo)
