from django.contrib import admin
from django.urls import path,include

admin.site.site_header = 'Ecommerce API'
admin.site.site_title = 'Ecommerce API'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',include('products.urls')),
    path('cart/',include('cart.urls')),
]
