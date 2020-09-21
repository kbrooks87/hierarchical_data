from django.shortcuts import render

from .models import Tree_Model

# Create your views here.
def index(request):
  return render(request, 'index.html', {'branch_files': Tree_Model.objects.all()})
