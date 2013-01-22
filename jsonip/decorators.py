from django.http import HttpResponse
import json
import mimes

def json_response(func):
    """
    A decorator thats takes a view response and turns it
    into json. If a callback is added through GET or POST
    the response is JSONP.
    """
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        if isinstance(objects, HttpResponse):
            return objects
        try:
            data = json.dumps(objects)
            if 'callback' in request.REQUEST:
                "jsonp"
                data = '%s(%s);' % (request.REQUEST['callback'], data)
                return HttpResponse(data, mimes.JSONP)
        except:
            data = json.dumps(str(objects))

        return HttpResponse(data, mimes.JSON)
    return decorator
