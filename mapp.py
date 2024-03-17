# import folium package
import folium
import geocoder

g = geocoder.ip('me')
print(g.latlng)
print(g.latlng[0])
print(g.latlng[1])

my_map3 = folium.Map(location = [g.latlng[0], g.latlng[1]],
                                            zoom_start = 15)
    
    # Pass a string in popup parameter
folium.Marker([g.latlng[0], g.latlng[1]],
                popup = ' Geeksforgeeks.org ').add_to(my_map3)
    
my_map2 = folium.Map(location = [g.latlng[0], g.latlng[1]],
                                         zoom_start = 12)
 
# CircleMarker with radius
folium.CircleMarker(location = [g.latlng[0], g.latlng[1]],
                    radius = 50, popup = ' FRI ').add_to(my_map2)

my_map3.save(" my_map3.html ")
my_map2.save(" my_map2.html ")

