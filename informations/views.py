from django.shortcuts import render, get_object_or_404
from rest_framework import views, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notice, PointShop
from .serializers import NoticeSerializer, NoticeListSerializer, PointShopSerializer, PointShopDetailSerializer

from lostitem.serializers import LostlistSerializer
from lostitem.models import Lost

# Create your views here.

class NoticeView(views.APIView):
    def get(self, request, *args, **kwargs):
        notices = Notice.objects.all()
        serializer = NoticeListSerializer(notices, many=True)

        return Response({'message': 'announcements get 성공', 'data': serializer.data})
    
    def post(self, request):
        serializer=NoticeSerializer(data=request.data)

        if serializer.is_valid():
            return Response({"message":'공지사항 추가 성공',"data":serializer.validated_data}, status=status.HTTP_200_OK)
        return Response({"message":'공지사항 추가 실패',"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class NoticeDetailView(views.APIView):
    def get(self, request, noticeid):
        notice = get_object_or_404(Notice, id=noticeid)
        serializer = NoticeSerializer(notice)

        return Response({'message': 'Notice Detail get 성공', 'data': serializer.data})

class PointShopView(views.APIView):
    def get(self, request, *args, **kwargs):
        query = PointShop.objects.filter(soldout=False)
        shop = request.query_params.get('shop')
        if shop:
            query = query.filter(shop=shop)
            
        serializer = PointShopSerializer(query, many=True)
        return Response({'message': 'PointShop stuff list get 성공', 'data': serializer.data})

class PointShopDetailView(views.APIView):
    def get(self, request, stuffid):
        stuff = get_object_or_404(PointShop, id=stuffid)
        serializer = PointShopDetailSerializer(stuff)

        return Response({'message': 'PointShop Detail get 성공', 'data': serializer.data})

class LostMylistView(views.APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        lostitems = Lost.objects.filter(userget=user)
        serializer = LostlistSerializer(lostitems, many=True)

        return Response({'message': 'mylostitem get 성공', 'data': serializer.data})