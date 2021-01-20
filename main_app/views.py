from django.shortcuts import render
from .models import Widget
from django.views.generic.edit import CreateView, DeleteView
from .forms import WidgetForm


# Create your views here.


def home(request):
    widgets = Widget.objects.all()
    form = WidgetForm()
    return render(request, 'index.html', {'widgets': widgets, 'form': form})


class WidgetCreate(CreateView):
    model = Widget
    success_url = '/'


class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'
