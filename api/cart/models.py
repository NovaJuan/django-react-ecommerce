from products.models import Product,ProductSerializer

class Cart:
    _model = Product
    _serializer = ProductSerializer
    totalItems = 0
    items = {}

    def __init__(self,oldCart = {}):
        if type(oldCart) is dict:
            self.totalItems = oldCart.get('totalItems') or 0 
            self.items = oldCart.get('items') or {} 

    def addToCart(self,id,qty = 1):
        id = str(id)
        if id in self.items:
            self.items[id] = {
                'quantity': self.items[id]['quantity'] + qty
            }
        else:
            self.items[id] = {
                'quantity':qty
            }

        self.totalItems += qty

    def getCart(self):
        items = []
        totalPrice = 0

        for id,data in self.items.items():
            try:
                product = self._model.objects.get(pk=id)
            except self._model.DoesNotExist:
                continue
            items.append({
                'product': self._serializer(product).data,
                'totalPrice':product.price * data['quantity'],
                'totalItems':data['quantity']
            })
            totalPrice += product.price * data['quantity']

        return {
            'items':items,
            'totalItems':self.totalItems,
            'totalPrice':totalPrice
        }

    def getRoot(self):
        return {
            'items':self.items,
            'totalItems':self.totalItems,
        }


