from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    path('<int:id>/', views.GetProductView.as_view(),name='get'),
]