# coding:utf-8
from __future__ import print_function
from __future__ import division
 

 
import requests
 
# URLs antiguas
tmp_url = "https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom=17&size=400x400&maptype=satellite&markers=color:green|label:|{lat},{lon}"
 
def crea_url(datos):
    return tmp_url.format(**datos)
 
def save_imagen(datos):
    url = crea_url(datos)
    r = sesion.get(url)
    f=open('%s.png' % datos["nombre"],'wb')
    f.write(r.content)
    f.close()
 
proxy = ""  # In case you need a proxy
proxies = {"http": proxy, "https": proxy}
sesion = requests.Session()
sesion.proxies = proxies
 
# Aqui se modifican los datos
datos = {"lat":  36.6529220, "lon":  -121.7981630, "nombre": "mapimage"}
 
save_imagen(datos)