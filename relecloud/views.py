from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from . import models
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return HttpResponse("Contact Us")

def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'destinations.html', { 'destinations': all_destinations})

class DestinationDetailView(generic.DetailView):
    template_name = 'destination_detail.html'
    model = models.Destination
    context_object_name = 'destination'


class DestinationCreate(SuccessMessageMixin, generic.CreateView):
    template_name = 'destination_form.html'
    model = models.Destination
    fields = ['name', 'description']
    #success_url = reverse_lazy('index')
    #success_message = 'Thank you, %(name)s! Your destination has been added!'


class DestinationUpdate(SuccessMessageMixin, generic.UpdateView):
    template_name = 'destination_form.html'
    model = models.Destination
    fields = ['name', 'description']
    #success_url = reverse_lazy('index')
    #success_message = 'Thank you, %(name)s! Your destination has been updated!'

class DestinationDelete(SuccessMessageMixin, generic.DeleteView):
    template_name = 'destination_confirm_delete.html'
    model = models.Destination
    success_url = reverse_lazy('destinations')
    


class CruiseDetailView(generic.DetailView):
    template_name = 'cruise_detail.html'
    model = models.Cruise
    context_object_name = 'cruise'


class InfoRequestCreate(SuccessMessageMixin, generic.CreateView):
    template_name = 'info_request_create.html'
    model = models.InfoRequest
    fields = ['name', 'email', 'cruise', 'notes']
    success_url = reverse_lazy('index')
    success_message = 'Thank you, %(name)s! We will email you when we have more information about %(cruise)s!'