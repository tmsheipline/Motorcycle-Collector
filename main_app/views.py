from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Motorcycle, Helmet
from .forms import WashingForm

# Create your views here.
def home(request):
    return HttpResponse('<h1>Motorcycle Collector</h1>')

def about(request):
  return render(request, 'about.html')

def motorcycles_index(request):
  motorcycles = Motorcycle.objects.all()
  return render(request, 'motorcycles/index.html', { 'motorcycles': motorcycles })

def motorcycles_detail(request, motorcycle_id):
  motorcycle = Motorcycle.objects.get(id=motorcycle_id)
  id_list = motorcycle.helmets.all().values_list('id')
  helmets_motorcycle_doesnt_have = Helmet.objects.exclude(id__in=id_list)
  washing_form= WashingForm()
  return render(request, 'motorcycles/detail.html', { 'motorcycle': motorcycle, 'washing_form': washing_form, 'helmets': helmets_motorcycle_doesnt_have })

def add_washing(request, motorcycle_id):
  form = WashingForm(request.POST)
  if form.is_valid():
    new_washing = form.save(commit=False)
    new_washing.motorcycle_id = motorcycle_id
    new_washing.save()
  return redirect('detail', motorcycle_id=motorcycle_id)

class MotorcycleCreate(CreateView):
  model = Motorcycle
  fields = ['make','model','color','year']
  success_url = '/motorcycles/'

class MotorcycleUpdate(UpdateView):
  model = Motorcycle
  fields = '__all__'

class MotorcycleDelete(DeleteView):
  model = Motorcycle
  success_url = '/motorcycles/'


class HelmetList(ListView):
    model = Helmet


class HelmetDetail(DetailView):
    model = Helmet


class HelmetCreate(CreateView):
    model = Helmet
    fields = '__all__'


class HelmetUpdate(UpdateView):
    model = Helmet
    fields = ['type', 'color']


class HelmetDelete(DeleteView):
    model = Helmet
    success_url = '/helmets/'


def assoc_helmet(request, motorcycle_id, helmet_id):
    Motorcycle.objects.get(id=motorcycle_id).helmets.add(helmet_id)
    return redirect('detail', motorcycle_id=motorcycle_id)