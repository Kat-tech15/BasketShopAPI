import uuid
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.permissions import IsOwnerOrReadOnly
from .serializers import OrderSerializer
from .models import Order,Payment

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permissiom_class = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

class MockPaymentAPIView(APIView):
    def post(self, request, *args, **kwargs):
        order_id = request.data.get('order')
        amount = request.data.get('amount')
        payment = Payment.objects.create(
            order_id=order_id,
            amount=amount,
            status='success',
            transaction_id=str(uuid.uuid4())
        )
        return Response({
            'message': 'Payment successful!',
            'transaction_id': payment.transaction_id,
            'status': payment.status
        })    