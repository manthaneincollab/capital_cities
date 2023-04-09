from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Capital


class NewCapitalView(CreateView):
    template_name = "capital_new.html"
    model = Capital
    fields = ["city", "country"]
