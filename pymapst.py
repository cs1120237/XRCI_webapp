import pygmaps
import webbrowser
mymap = pygmaps.maps(25.6, 85.2, 16)
# mymap.setgrids(37.42, 37.43, 0.001, -122.15, -122.14, 0.001)
# mymap.addpoint(37.427, -122.145, "#0000FF")
# mymap.addradpoint(37.429, -122.145, 95, "#FF0000")
# path = [(37.429, -122.145),(37.428, -122.145),(37.427, -122.145),(37.427, -122.146),(37.427, -122.146)]
# mymap.addpath(path,"#00FF00")
# mymap.draw('./mymap.draw.html')
mymap.draw('./mymap.html')
