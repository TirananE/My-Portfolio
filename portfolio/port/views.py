from django.http import HttpResponse
from django.template import loader,RequestContext
from django.shortcuts import render
from .models import Contact
from port.forms import ContactForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
  form = ContactForm()
  return render(request, 'port/blog.html', {'form': form})
@csrf_exempt
def add_contact(request):
  form = ContactForm()
  one= request.POST['name']
  two=request.POST['email']
  three =request.POST['message']
  Contact.objects.create(name=one,email=two,message=three)
  return render(request, 'port/blog.html', {'form': form})
