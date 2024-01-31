
from django.urls import path
from interview.order.views import (
    OrderListCreateView,
    OrderTagListCreateView,
    DeactivateOrderView,
    ListOrdersInDateRangeAPIView,
)


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('<int:order_id>/deactivate/', DeactivateOrderView.as_view(), name='deactivate-order'),
    path('date-range/', ListOrdersInDateRangeAPIView.as_view(), name='api-list-orders-date-range'),
]
