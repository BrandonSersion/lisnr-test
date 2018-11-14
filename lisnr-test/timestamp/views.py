from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from datetime import datetime


@api_view(['GET'])
def timestamp(request):
    current_time = datetime.utcnow().isoformat()
    return Response({"timestamp": current_time})