import urllib.request, requests
from bs4 import BeautifulSoup


def location_lookup():
    site = urllib.request.Request('https://geoiptool.com/', \
                              headers = {'User-Agent': 'Mozilla/5.0'})
    html_content = urllib.request.urlopen(site).read().decode('utf-8')
    site = BeautifulSoup(html_content, 'html.parser')

    long = str(longitude(site)) # makes string so it's sliceable 
    long = long[6:14]
    
    lat = str(latitude(site)) 
    lat = lat[6:13]

    coordinate = (long, lat)
    
    #20 is longitude
    #17 is latitude
    
    return(coordinate)

def longitude(site):
    i = 0
    for div_class in site.findAll('div', {'class':'data-item'}):
        for part in div_class.findAll('span'):
            i += 1
            if i == 20:
                return(part)

def latitude(site):
    i = 0
    for div_class in site.findAll('div', {'class':'data-item'}):
        for part in div_class.findAll('span'):
            i += 1
            if i == 18:
                return(part)
            
def main():
    print(location_lookup())
main()
