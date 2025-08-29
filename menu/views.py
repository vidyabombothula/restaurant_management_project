from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DishSerializer
from django.shortcuts import render
import requests

def home(request):
    try:

        response=requests.get()
        menu_items=response.json()
    except Execption as e:
        menu_items=[]
        print("Error fetching menu: {e}")

    return render(request, 'menu/home.html', {'menu_items':menu_items})

class MenuAPIView(APIView):
    def get(self,request):

        menu= [
             {

                "name":"Pizza",
                "price":50
             },

             {
                "name" : "Burger",
                "price": 30
             },

             {
                "name":"Cheese cake",
                "price":50
             }


        ]

        serializer=DishSerializer(menu,many=True)
        return Response(serializer.data)