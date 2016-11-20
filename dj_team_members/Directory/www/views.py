from django.shortcuts import render
from .models import Person
# Create your views here.
def index(request):
    #get all the piipl
    people = Person.objects.all()
    return render(request,'index.html', {'people':people});