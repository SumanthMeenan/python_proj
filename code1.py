location = {("24.4539", "54.3773"):"abudabhi",("43.0828", "79.0742"):"niagara", ("1.3521","103.8198"):"singapore"} 
latitude = [] 
longitude = [] 
places = [] 
for city in location: 
    latitude.append(city[0]) 
    longitude.append(city[1]) 
    places.append(location[city[0], city[1]]) 