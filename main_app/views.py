from django.shortcuts import render
from django.http import HttpResponse


# Add the Cat class & list and view function below the imports
class Motorcycle:  # Note that parens are optional if not inheriting from another class
  def __init__(self, make, model, year, color):
    self.make = make
    self.model = model
    self.year = year
    self.color = color

motorcycles = [
  Motorcycle('Indian', 'Scout', 2017, 'Cream'),
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Motorcycle Collector</h1>')

def about(request):
  return render(request, 'about.html')

def motorcycles_index(request):
  return render(request, 'motorcycles/index.html', { 'motorcycles': motorcycles })