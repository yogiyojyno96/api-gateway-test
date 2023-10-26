from nameko.web.handlers import http
import requests
from werkzeug.wrappers import Response

Service1_URL = "http://127.0.0.1:8001"
Service2_URL = "http://127.0.0.1:8002"
Service3_URL = "http://127.0.0.1:8003"

class GatewayService:
    name = "gateway_service"

    @http('GET', '/service1')
    def get_service1(self, request):
        return requests.get(Service1_URL).json()

    @http('GET', '/service2')
    def get_service2(self, request):
        return requests.get(Service2_URL).json()

    @http('GET', '/service3/<path:path>')
    def get_service3(self, request, path):
        response = requests.get(f"{Service3_URL}/{path}")
        return Response(response.content, response.status_code, response.headers.items())
    
    @http('GET', '/service4')
    def get_service4(self, request):
        response = requests.get(f"{Service1_URL}")
        print(response)
        response = requests.get(f"{Service2_URL}")
        print(response)
        response = requests.get(f"{Service3_URL}")
        print(response)
        return Response(response.content, response.status_code, response.headers.items())