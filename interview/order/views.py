from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponseNotAllowed
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from datetime import datetime


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

class ListOrdersInDateRangeAPIView(APIView):

    def get(self, request, format=None):
        start_date = request.query_params.get('start_date')
        embargo_date = request.query_params.get('embargo_date')

        if not start_date or not embargo_date:
            return Response({'error': 'Both start_date and embargo_date are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            embargo_date = datetime.strptime(embargo_date, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        orders = Order.objects.filter(start_date__gte=start_date, embargo_date__lte=embargo_date)
        orders_data = [{'id': order.id, 'inventory': order.inventory.name, 'start_date': order.start_date, 'embargo_date': order.embargo_date} for order in orders]
        return Response({'orders': orders_data})
