from django.contrib import admin
from .models import ContactInfo,Banner,Category,Brand,Product

# Register your models here.
admin.site.register(ContactInfo)
admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)

