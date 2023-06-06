from django.urls import path
from playground import views

urlpatterns = [
    # path("route-name",views,name="name of the route")
    # name is used for redirection purpose
    path("test_api/", views.test_api, name="test_api"),
    path("test-json-api/", views.test_json_api, name="json_test_api"),
    path("test-html-page/", views.test_html_page, name="test-html-page"),
    path("test-hello-name/<name>", views.test_hello_name, name="test-hello-name"),
    path("test-html-for-loop", views.test_html_for_loop, name="test-html-for-loop"),
    path("home-page/", views.home_page, name="home-page"),
    path("about-page/", views.about_page, name="about-page")
]
