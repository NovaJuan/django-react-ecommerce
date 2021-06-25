from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Product
from .models import Cart

class AddToCartView(APIView):
    def post(self,request):
        item = request.data.get('item')

        if item is None:
            return Response({
                'success':False,
                'error':'Item object is required'
            })

        productId = item.get('productId')

        try:
            Product.objects.get(pk=productId)
        except Product.DoesNotExist:
            return Response({
                'success':False,
                'error':'Product does not exists.'
            })

        root = request.data.get('root')
        quantity = item.get('quantity') or 1

        cart = Cart(root or {})
        cart.addToCart(productId,quantity)


        return Response({
            'success':True,
            'root':cart.getRoot()
        })
