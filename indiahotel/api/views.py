from django.shortcuts import render
from .models import menu_items
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class DishList(APIView):
    def get(self,req,*args,**kwargs):
        return Response(data=menu_items)
    
class SpecificDish(APIView):
    def get(self,req,*args,**kwargs):
        did=kwargs.get("did")
        dish=[i for i in menu_items if i['id']==id].pop()
        return Response(data=dish)