
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderTagsAPIView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('<int:order_id>/tags/', OrderTagsAPIView.as_view(), name='api-order-tags'),
]