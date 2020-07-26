from django.urls import path

from .views import vistaClass

urlpatterns = [
    path('', vistaClass.as_view())
]
