from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Project, Profile
from .forms import ProfileForm, ProjectForm
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    
    return render(request, 'index.html')
    