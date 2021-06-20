from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="shop home"),
    path("about/",views.about,name="abous us"),
    path("contact/",views.contact,name="contact"),
    path("tracker/",views.tracker,name="tracker"),
    path("search/",views.search,name="search"),
    path("products/<int:myid>",views.products,name="productview"),
    path("checkout/",views.checkout,name="checkout"),
]