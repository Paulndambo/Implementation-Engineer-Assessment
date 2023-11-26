from django.urls import path

from searchapp.views import search_and_results

urlpatterns = [
    path("", search_and_results, name="search"),
]