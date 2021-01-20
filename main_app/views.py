from django.shortcuts import render
from .models import Widget
from django.views.generic.edit import CreateView, DeleteView
from .forms import WidgetForm

from django.db.models import Sum


# Create your views here.

def home(request):
    widgets = Widget.objects.all()
    form = WidgetForm()
    total_quantity = Widget.objects.all().aggregate(Sum('quantity'))
    return render(request, 'index.html', {'widgets': widgets, 'form': form, 'total_quantity': total_quantity})


class WidgetCreate(CreateView):
    model = Widget
    success_url = '/'


class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'
