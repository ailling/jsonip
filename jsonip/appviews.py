
import json
from django.http import HttpResponse
from decorators import json_response

def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


@json_response
def homepage(request):
    data = {"ip": get_client_ip(request),
            "request_meta": {
                "http_referer": request.META.get("HTTP_REFERER"),
                "content_length": request.META.get("CONTENT_LENGTH"),
                "content_type": request.META.get("CONTENT_TYPE"),
                "http_accept_encoding": request.META.get("HTTP_ACCEPT_ENCODING"),
                "http_accept_language": request.META.get("HTTP_ACCEPT_LANGUAGE"),
                "method": request.method,
            },
            "pages": {
                "home": "/",
                "about": "/about",
            }
    }

    if request.method == "GET":
        data["params"] = json.dumps(request.GET)
    if request.method == "POST":
        data["params"] = json.dumps(request.POST)
    return data

@json_response
def about(request):
    data = {"description": "A simple network and development tool to inspect HTTP requests and initiating clients",
            "developer": "Alan Illing",
            "developer-website": "http://alanilling.com",
            "developer-github": "https://github.com/ailling",
            "source": "https://github.com/ailling/jsonip"
    }
    return data

@json_response
def error404(request):
    return {"error": "404", "description": "Not found"}

@json_response
def error500(request):
    return {"error": "500", "description": "Server error"}

@json_response
def error403(request):
    return {"error": "403", "description": "Forbidden"}

