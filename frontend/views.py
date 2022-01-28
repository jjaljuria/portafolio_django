from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
	skills = [
		{'name': 'Bring the Coffee', 'percentage': 70, 'color': '#0d6efd'},
		{'name': 'Sleep', 'percentage': 40, 'color': '#198759'},
		{'name': 'Eat', 'percentage': 50, 'color': '#dc3545'},
	]

	projects = Project.objects.all()
	return render(request, 'home.html', {'skills': skills, 'projects': projects})
