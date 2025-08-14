from django.shortcuts import render
from django.conf import settings


 def homepage(request):
    context={
        "restaurant_name":"Tasty Bites",
        "phone_number": "1234567"
    }

    return render(request, "index.html", context)

