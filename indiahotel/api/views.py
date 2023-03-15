from django.shortcuts import render
from .models import menu_items
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class DishList(APIView):
    def get(self,request,*args,**kwargs):
        allitems=menu_items
        if 'category' in request.query_params:
            cat=request.query_params.get("category")
            allitems=[i for i in menu_items if i['category']==cat]
        if 'limit' in request.query_params:
            lmt=int(request.query_params.get("limit"))
            allitems=menu_items[0:lmt]
            return Response(data=allitems)
        return Response(data=menu_items)
    def post(self,request,*args,**kwargs):
        data=request.data
        menu_items.append(data=menu_items)

    
class SpecificDish(APIView):
    def get(self,req,*args,**kwargs):
        did=kwargs.get("did")
        dish=[i for i in menu_items if i['id']==did].pop()
        return Response(data=dish)
    def delete(self,request,*args,**kwargs):
        did=kwargs.get("did")
        dish=[i for i in menu_items if i['id']==did].pop()
        menu_items.remove(dish)
        return Response(data=menu_items)
    def put(self,request,*args,**kwargs):
        did=kwargs.get("did")
        data=request.data
        dish=[i for i in menu_items if i['id']==did].pop()
        dish.update(data)
        return Response(data=dish)
  