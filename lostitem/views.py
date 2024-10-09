from django.shortcuts import render, get_object_or_404
from rest_framework import views, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from .models import Lost
from .serializers import LostSerializer, LostlistSerializer

from .GPT_desc import register
from .GPT_find import *

import os

# Create your views here.
class LostlistView(views.APIView):
    def get(self, request, *args, **kwargs):
        lostitems = Lost.objects.all()
        serializer = LostlistSerializer(lostitems, many=True)

        return Response({'message': 'lostitem get 성공', 'data': serializer.data})

class LostDetailView(views.APIView):
    def get(self, request, lostid):
        lost = get_object_or_404(Lost, id=lostid)
        serializer = LostSerializer(lost)

        return Response({'message': 'lostdetail get 성공', 'data': serializer.data})


def imageSave(image):
    import os
    from django.conf import settings
    from urllib.parse import urljoin

    save_path = os.path.join(settings.MEDIA_ROOT, 'uploaded_img')
    os.makedirs(save_path, exist_ok=True)

    file_name = image.name
    file_path = os.path.join(save_path, file_name)

    with open(file_path, 'wb') as f:
        for chunk in image.chunks():
            f.write(chunk)

    image_url = urljoin(settings.MEDIA_URL, 'uploaded_img/' + file_name)
    return image_url


class LostImageUploadView(views.APIView):
    def post(self, request, *args, **kwargs):
        image = request.data.get('image')
        image_url = imageSave(image)

        if not image:
            return Response({"error": "잘못된 이미지"}, status=status.HTTP_400_BAD_REQUEST)

        imagefile = os.path.abspath('.' + image_url)

        try:
            losttime = datetime.now().strftime('%H')
            lostdate = datetime.now().strftime('%Y-%m-%d')
            cat, desc, title = register(imagefile)

            return Response({
                "category": cat, "description": desc, "title": title, 
                "losttime": losttime, "lostdate": lostdate
                }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e), "image":imagefile}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LostUploadView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwars):
        serializer=LostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(userget=request.user)
            return Response({'message':'Lostitem Upload 성공', 'data':serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message':'Lostitem Upload 실패', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class LostSearchView(views.APIView):
    #permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwars):
        import pandas as pd

        lostdate = request.data.get('lostdate')
        losttime1 = request.data.get('losttime1')
        losttime2 = request.data.get('losttime2')
        getwhere = request.data.get('getwhere')
        description = request.data.get('description')

        lostitems = Lost.objects.all()

        if getwhere:
            lostitems = lostitems.filter(getwhere__icontains=getwhere)

        if losttime1 and losttime2:
            lostitems = lostitems.filter(losttime__range=[losttime1, losttime2])

        if lostdate:
            lostitems = lostitems.filter(lostdate=lostdate)

        if not lostitems.exists():
            return Response({'message': '검색결과가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

        lostitemSerializers = LostSerializer(lostitems, many=True)
        #df = pd.DataFrame(lostitemSerializers.data)
        #df = df[['lostid', 'description', "category"]]
        #idx = find(df, description)
        filtered_data = [ { 'lostid': item['lostid'], 'description': item['description'], 'category': item['category'] } for item in lostitemSerializers.data]
        idx = find(filtered_data, description)
        

        lostitems = lostitems.filter(id__in=idx)
        lostitemsOrdered = sorted(lostitems, key=lambda x: idx.index(x.id))
        lostitemSerializers = LostlistSerializer(lostitemsOrdered, many=True)

        return Response({'message': 'Lostitem 검색 성공', 'data': lostitemSerializers.data}, status=status.HTTP_200_OK)