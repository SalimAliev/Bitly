from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect

from .models import Url
from .serializers import UrlSerializer

import random
import string


def generate_shor_url_key():
    letters = string.ascii_lowercase + string.digits
    key_length = 10
    short_url = ''.join([random.choice(letters) for _ in range(key_length)])
    while Url.objects.filter(short_url=short_url).exists():
        short_url = short_url
    return short_url


class UrlsListView(APIView):
    def get(self, request, url_id=None):
        if url_id:
            serializer = UrlSerializer(get_object_or_404(Url, pk=url_id))
        else:
            serializer = UrlSerializer(Url.objects.all(), many=True)
        return Response({'urls': serializer.data})

    def post(self, request):
        request.data['short_url'] = generate_shor_url_key()
        serializer = UrlSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'url': serializer.data})


class UrlRedirectView(APIView):
    def get(self, request, short_url):
        url = get_object_or_404(Url, short_url=short_url)
        if url.is_active:
            url.requests_count += 1
            url.save()
            return redirect(url.long_url)
        else:
            return Response({'error': 'Url is no longer available'}, status=status.HTTP_404_NOT_FOUND)