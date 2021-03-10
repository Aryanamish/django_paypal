from django.shortcuts import render, HttpResponse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.ipn.views import ipn
from paypal.standard.ipn.models import PayPalIPN
from django.urls import reverse
import random
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


'''

client_id
currency
debug
intent = [capture, authorize, subscription, tokenize]
valut = True for subscription
date= date_of_launch

'''


def make_payment_custom(request):
    try:
        paypal = settings.PAYMENT_GATEWAY['paypal']
    except KeyError:
        raise KeyError("Check Your Settings.PAYMENT_GATEWAY")
    amount = 10
    currency = 'USD'
    paypal_data = {
        'currency': currency,
        'client-id': paypal.get('client_id'),
        # "notify-url": request.build_absolute_uri(reverse('payment:confirm')),
    }
    last_keys = list(paypal_data.keys())[-1]
    paypal_data = {i: paypal_data[i] + '&' if i != last_keys else paypal_data[i] for i in paypal_data}
    return render(request, 'payment/custom.html', {
        'paypal_data': paypal_data,
        'amount': amount,

    })


def make_payment_lib(request):
    # for all parameter
    # https://developer.paypal.com/docs/paypal-payments-standard/integration-guide/Appx-websitestandard-htmlvariables/
    paypal_dict = {
        "business": "merchant@gmail.com",
        "amount": "10.00",
        "currency_code": 'USD',
        "item_name": "name of the item",
        "invoice": random.randint(0, 1000),
        "notify_url": request.build_absolute_uri(reverse('payment:confirm')),
        "return": request.build_absolute_uri(reverse('payment:return')),
        "cancel_return": request.build_absolute_uri(reverse('payment:cancel')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment/lib.html", context)


# this is just wrapper function to call the paypal ipn function this is called by paypal after successful transaction
@csrf_exempt
def confirm(request):
    # before saving the transaction data
    rv = ipn(request)
    # after saving the data
    return rv


def confirm_payment(request):
    response = {
        'status': ''
    }
    return HttpResponse({}, content_type="application/json")


# when user returns back to the website after transaction
def return_payment(request):
    # check if payment was successful or not using PayerID
    return HttpResponse(f"<h1>Return Back to Merchant site payerId:<u>{request.GET.get('PayerID')}</u></h1>")


def cancel_payment(request):
    # when payment was canceled
    return HttpResponse("<h1>The Payment was Canceled</h1>")