from django.urls import path,include
from . import views

app_name = 'cart'

urlpatterns = [
    path('add',views.AddToCartView.as_view(),name="add")
]