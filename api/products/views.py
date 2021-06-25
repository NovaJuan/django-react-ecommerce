from django.http.response import HttpResponse
from django.views import View
from django.http import JsonResponse
from .models import Product,ProductSerializer

class IndexView(View):
    model = Product
    serializer = ProductSerializer
    def get(self,request):
        return JsonResponse(
            {
                'success':True,
                'data':[self.serializer(product).data for product in self.model.objects.all()]
            }
        )

class GetProductView(View):
    model = Product
    serializer = ProductSerializer
    def get(self,request,id):
        return JsonResponse(
            {
                'success':True,
                'data':self.serializer(self.model.objects.get(pk=id)).data
            }
        )
