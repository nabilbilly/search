from django.urls import path
from .views import *


urlpatterns =[
    path("search/",SearchResultsViews.as_view(), name="searchresult"),
    path("",HomePage.as_view(), name="Home page"),
]