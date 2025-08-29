from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DishSerializer

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