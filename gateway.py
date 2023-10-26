from nameko.web.handlers import http
import requests


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

    @http('GET', '/service3')
    def get_service3(self, request):
        return requests.get(Service3_URL).json()