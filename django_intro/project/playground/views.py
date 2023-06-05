from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def test_api(request):
    return HttpResponse("First API")


# JSON message
def test_json_api(request):
    data = {
        "name" : "First Json API",
        "framework" : "Python-Django",
        "university": "Silicon Institute of Technology"
    }
    return JsonResponse(data)


# HTML Template
def test_html_page(request):
    my_dict = {
        "name" : "Sambit",
        "framework2024" : "Python-Django",
        "framework2023" : "Java Springboot",
        "university": "Silicon Institute of Technology"
    }
    return render(request, "index.html",context=my_dict)