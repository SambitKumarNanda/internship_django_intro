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
        "university": "KIIT"
    }
    return render(request, "playground/index.html",context=my_dict)

# Hello , {{name}}
def test_hello_name(request,name):
    return HttpResponse(f"Hello,{name}")

# for loop
def test_html_for_loop(request):
    context={
        "data":[{
            "name": "SIT",
            "framework": "Django"
        },
                {
                    "name": "SIT",
                    "framework": "Mern"
                }]
    }
    return render(request,"playground/hello.html",context=context)

def home_page(request):
    return render(request,"playground/main.html")

def about_page(request):
    print(request.GET)
    return render(request,"playground/about.html")