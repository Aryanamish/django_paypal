from django.urls import path, include
from . import views
from .apps import PaymentConfig

app_name = PaymentConfig.name

urlpatterns = [
    path('paypal/custom', views.make_payment_custom, name='make_payment_custom'),
    path('paypal/lib', views.make_payment_lib, name='make_payment_lib'),
    path('paypal/confirm', views.confirm, name='confirm'),
    path('paypal/return', views.return_payment, name='return'),
    path('paypal/cancel', views.cancel_payment, name='cancel'),
]