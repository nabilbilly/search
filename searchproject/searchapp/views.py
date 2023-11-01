from typing import Any
from django.db.models.query import QuerySet,Q
from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView,ListView
# Create your views here.

class HomePage(TemplateView):
    template_name ='home.html'

class SearchResultsViews(ListView):
    model = City

    template_name = 'searchresult.html'
   # queryset = City.objects.filter(state__icontains="Texas")   make use of quaryset and filter to narrow or quary all state with the name Texas and it worked

    # def get_queryset(self):
    #     return City.objects.filter(state__icontains="a")    # another way using the get_quaryset  || built-in QuerySet methods of filter(), all(), get(), or exclude() 
    
    # def get_queryset(self):
    #     return City.objects.filter( Q(state__icontains="Texas") | Q(state__icontains="new york") )  # using the Q object , Q works with the logical  statement to filter object in the database, logical operatro Use by Q object "OR" "AND"
    
    def get_queryset(self) :
        query = self.request.GET.get("q")
        object_list = City.objects.filter( 
            Q( name__icontains=query) | Q(state__icontains=query)
        )
        return object_list
    
    # it worked  refer to this  if any problem    https://learndjango.com/tutorials/django-search-tutorial


