## APP (relcloud) urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('destinations/', views.destinations, name='destinations'),
    path('destination/<int:pk>', views.DestinationDetailView.as_view(), name='destination_detail'),
    path('destination/add', views.DestinationCreate.as_view(), name='destination_form'),
    path('destination/<int:pk>/update', views.DestinationUpdate.as_view(), name='destination_update'),
    path('destination/<int:pk>/delete', views.DestinationDelete.as_view(), name='destination_delete'),
    path('cruise/<int:pk>', views.CruiseDetailView.as_view(), name='cruise_detail'),
    path('info_request', views.InfoRequestCreate.as_view(), name='info_request'),
]
