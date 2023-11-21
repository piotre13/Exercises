
import cherrypy

class HelloWorld(object):
    exposed=True


    def GET(self,*uri,**params):
        #Standard output
        output="Hello World"
        #Check the uri in the requests
        #<br> is just used to append the content in a new line 
        #(<br> is the \n for HTML)
       
        if len(uri)!=0:
            output+='<br>uri: '+', '.join(uri)
        #Check the parameters in the request
        #<br> is just used to append the content in a new line 
        #(<br> is the \n for HTML)
        if params!={}:
            output+='<br>params: '+str(params)
   
        return output

if __name__=="__main__":
    #Standard configuration to serve the url "localhost:8080"
    conf={
        '/':{
                'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
                'tools.sessions.on':True
        }
    }
    cherrypy.quickstart(HelloWorld(),'/',conf)