from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
# from .serializers import PostSerializer

@api_view(['GET'])
def index(request):

    return Response({"Success": "The setup was successful"})