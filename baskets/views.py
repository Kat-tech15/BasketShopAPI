from rest_framework import mixins, generics, permissions
from rest_framework.response import Response
from .serializers import BasketSerializer
from .models import Basket

class BasketList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return Response({'message': 'Item posted successfully!'})

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

class BasketDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)
        return Response({'message': 'Item updated successfully.'})
    
    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response({'message': 'Item deleted successfully.'})
