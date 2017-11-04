from django.shortcuts import render
from django.http import HttpResponse


def mapping(request):
   makeMap(request)
   return render(request, "map.html")
	
	
   
def makeMap(request):
   import gmplot

   gmap = gmplot.GoogleMapPlotter.from_geocode("San Francisco")

   #gmap.plot(37.779, -122.398, 'cornflowerblue', edge_width=10)
   #gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
   #gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
   #gmap.heatmap(heat_lats, heat_lngs)

   gmap.draw("map.html")
   return render(request, "index.html")

def landing(request):
	return render(request, "index.html")

