from django.shortcuts import render
from django.http import JsonResponse
from product.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    function API request
    """
    app_product = (
        Product.objects.all().order_by("?").first()
    )  # this gets the random  of products
    data = {}
    if app_product:
        data = model_to_dict(app_product, fields=["name", "description", "price"])
    return Response(data)
