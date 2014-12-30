import web, pygmaps 

#just a comment

urls = (
    '/', 'index'
)
mymap = pygmaps.maps(37.428, -122.145, 16)

class index:
    def GET(self):
        return "Hello world! Hello Universe"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
    print mymap

