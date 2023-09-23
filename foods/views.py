from django.shortcuts import render, HttpResponse
# import the View Class
from django.views import View
# import JsonResponse
from django.http import JsonResponse

# Create your views here.

##Function view, (function that returns a response)
def foods(request):
    if request.method == "GET":
        return HttpResponse("Hello World")
    if request.method == "POST":
        return HttpResponse("This Was a POST Request")
    
## Class Based Views: A Class whose method returns a response
class foods_class_views(View):
    def get(self, request):
        return JsonResponse({"message": "Hello World!"})
    def post(self, request):
        return JsonResponse({"message": "This was a POST Request"}) 