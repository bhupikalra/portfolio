from django.shortcuts import render
from .models import Project

# Create your views here.
def project_index(request):
    projects = Project.objects.all()

    data ={
        'projects': projects,
    }
    return render(request, 'project_index.html', data)

def project_detail(request, id):
    project = Project.objects.get(pk = id)

    data ={
        'project': project,
    }
    return render(request, 'project_detail.html', data)