from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Motorcycle
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
  washing_form= WashingForm()
  return render(request, 'motorcycles/detail.html', { 'motorcycle': motorcycle, 'washing_form': washing_form })

def add_washing(request, motorcycle_id):
  form = WashingForm(request.POST)
  if form.is_valid():
    new_washing = form.save(commit=False)
    new_washing.motorcycle_id = motorcycle_id
    new_washing.save()
  return redirect('detail', motorcycle_id=motorcycle_id)

class MotorcycleCreate(CreateView):
  model = Motorcycle
  fields = '__all__'
  success_url = '/motorcycles/'

class MotorcycleUpdate(UpdateView):
  model = Motorcycle
  fields = '__all__'

class MotorcycleDelete(DeleteView):
  model = Motorcycle
  success_url = '/motorcycles/'