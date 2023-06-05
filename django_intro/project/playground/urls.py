from django.urls import path
from playground import views

urlpatterns = [
    # path("route-name",views,name="name of the route")
    # name is used for redirection purpose
    path("",views.test_api,name="test_api"),
    path("test-json-api/",views.test_json_api,name="json_test_api"),
    path("test-html-page/",views.test_html_page,name="test-html-page")
]
