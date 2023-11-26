from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from searchapp.cities_data import load_cities_data
from searchapp.models import City


# Create your views here.
def search_and_results(request):

    cities_count = City.objects.first()

    if not cities_count:
        try:
            load_cities_data()
        except Exception as e:
            raise e

    cities = City.objects.all()
    if request.method == "POST":
        search_value = request.POST.get("search")

        cities = City.objects.filter(
            Q(name__icontains=search_value) | 
            Q(country__icontains=search_value)
        )
    paginator = Paginator(cities, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "cities": cities,
        "page_obj": page_obj
    }

    return render(request, "search_and_results.html", context)