import cherrypy
class UriReverser():
    """docstring for Reverser"""

    exposed = True

    def __init__(self):
        pass


    def GET(self, *uri):

        if len(uri)>0:
            uri = [x[::-1] for x in uri][::-1]
            return ','.join(uri)
        else:
            # you can define a simple http error message
            raise cherrypy.HTTPError(400, 'No URI given, you need to provide at least one uri')

   

if __name__ == '__main__':
    conf = {
        '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tools.sessions.on': True,
        }
    }


    #cherrypy.config.update({'server.socket_host': '192.168.1.176'})
    cherrypy.tree.mount(UriReverser(), '/rev', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
