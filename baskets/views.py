from rest_framework import mixins, generics
from rest_framework.response import Response
from .serializers import BasketSerializer
from .models import Basket

class BasketList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

class BasketDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(sel, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
