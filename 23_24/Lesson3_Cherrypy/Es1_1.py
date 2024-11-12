import cherrypy
import json

# Return the reverted parameters as JSON formatted string
class ParamsReverser(object):
    """docstring for Reverser"""
    exposed = True

    def __init__(self):
        pass

    def GET(self, *uri, **params):
        if len(uri) == 0:
            reverse = {}
            for key in params.keys():
                reverse[key] = params[key][::-1]
            return json.dumps(reverse)
        else:
            raise cherrypy.HTTPError(400, 'No URI given, you need to provide at least one uri')



# Return the reverted parameters a proper JSON, you can see the difference in the browser
class ParamsReverserJSON(object):
    """docstring for Reverser"""
    exposed = True

    def __init__(self):
        pass
    # we can use this linee before the method to return the output as a proper json
    # in this case we do not need to use json.dumps()
    @cherrypy.tools.json_out()
    def GET(self, *uri, **params):
        if len(uri) == 0:
            if params!={}:
                reverse = {}
                for key in params.keys():
                    reverse[key] = params[key][::-1]
                # no need to use json.dumps()
                return reverse
            else:
                raise cherrypy.HTTPError(400, 'No parameters given, you need to provide at least one parameter')
        else:
            raise cherrypy.HTTPError(400, 'No URI given, you need to provide at least one uri')


if __name__ == '__main__':
    conf = {
        '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tools.sessions.on': True
        }
    }
    cherrypy.tree.mount(ParamsReverser(), '/simple', conf)
    cherrypy.tree.mount(ParamsReverserJSON(), '/fancy', conf)
    # this is needed if you want to have the custom error page
    # cherrypy.config.update({'error_page.400': error_page_400})
    cherrypy.engine.start()
    cherrypy.engine.block()

