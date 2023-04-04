from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductUnitSerializer
from .models import ProductUnit


class ProductUnitProductView(APIView):
    def get(self, request, id):
        s = ProductUnit.objects.filter(product_id=id)
        return Response(ProductUnitSerializer(s, many=True).data)


class ProductUnitProductMainView(APIView):
    def get(self, request, id):
        s = ProductUnit.objects.filter(product_id=id)
        data = ProductUnitSerializer(s, many=True).data
        ans = dict()
        ans['brand'] = data[0]['product']['brand']
        ans['name'] = data[0]['product']['name']
        ans['bucket_link'] = data[0]['product']['bucket_link']

        min_price = data[0]["unit_bundle"]["final_price"]
        for d in data:
            min_price = min(min_price, d["unit_bundle"]["final_price"])

        ans['min_price'] = min_price
        return Response(ans)
# Create your views here.
