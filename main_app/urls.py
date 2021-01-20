from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('widgets/<int:pk>/delete/',
         views.WidgetDelete.as_view(), name='widget_delete')

]
