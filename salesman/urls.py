from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^main$', views.displayOrderList, name='salespersonmain'),
    url(r'^createorder$', views.createOrder, name='createorder'),
    url(r'^view/invoice/(?P<order_id>[0-9]+)$', views.displayOrderDetail, name='orderdetail'),
]
