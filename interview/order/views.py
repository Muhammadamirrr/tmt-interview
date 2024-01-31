from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404


from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer

class DeactivateOrderView(APIView):
    def post(self, request, *args, **kwargs):
        order_id = kwargs.get('order_id')
        if not order_id:
            return JsonResponse({'error': 'Missing order ID'}, status=400)

        order = get_object_or_404(Order, pk=order_id)
        order.is_active = False
        order.save()

        return JsonResponse({'message': 'Order deactivated successfully'})
