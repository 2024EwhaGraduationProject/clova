from rest_framework import serializers
from .models import Notice, PointShop

class NoticeSerializer(serializers.ModelSerializer):
    noticeid = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Notice
        fields= ['noticeid', 'title', 'noticeDate', 'contents']

class NoticeListSerializer(serializers.ModelSerializer):
    noticeid = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Notice
        fields= ['noticeid', 'title', 'noticeDate']

class PointShopSerializer(serializers.ModelSerializer):
    stuffid = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = PointShop
        fields = ['stuffid', 'stuff', 'price', 'soldout']

class PointShopDetailSerializer(serializers.ModelSerializer):
    stuffid = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = PointShop
        fields = ['stuffid', 'stuff', 'price', 'shop']

'''
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']
'''