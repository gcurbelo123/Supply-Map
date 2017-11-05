from django.shortcuts import render
from django.http import HttpResponse
import map.screenshot


def mapping(request):
   makeMap(request)
   return render(request, "map.html")
	
def save(request):
   map.screenshot.main()
   return render(request, "map.html")
   
def makeMap(request):
   
   return render(request, "index.html")

def staticMap(request):
   return render(request, "staticmap.html")
   

def landing(request):
	return render(request, "index.html")

