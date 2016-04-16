from pprint import pprint
import json

from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from web import serializers

from dockerutils import dclient

class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class ListAll(APIView):
    """Lists all the containers."""

    def get(self, request, format=None):
        return Response(dclient.list_all(), status=status.HTTP_200_OK)


class Stop(APIView):
    """Stop container"""

    # def get(self, request, image, *args, **kwargs):
    #     if image_status:
    #         image.stop()
    #         serializer = serializers.OwtfContainerSerializer(image)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #     else:
    #         return HttpResponse('Failed!')


class Execute(APIView):
    """Get a command and the pass it on to the associated container"""

    def get(self, request, image, *args, **kwargs):


        return Response(json.dumps({"msg":"hello"}), status=status.HTTP_200_OK)


    def post(self, request, image, *args, **kwargs):

        request_data = serializers.CommandSerializer(data=request.data)
        if request_data.is_valid():
            data_obj = request_data.data
            dclient.execute(data_obj['container'], data_obj['code'],
                            data_obj['target'])
            return Response(data_obj, status=status.HTTP_200_OK)

        pprint(request_data.errors)
        return HttpResponse('Command is not valid!')


class Results(APIView):
    """Poll the workers for results and let them go"""
    def get(self, request):
        json_results = dclient.check_results()
        pprint(json_results)
        return Response(json.dumps(json_results),
                        status=status.HTTP_200_OK)