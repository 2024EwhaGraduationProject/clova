from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Lost
from accounts.serializers import UserSerializer

class LostSerializer(serializers.ModelSerializer):
    lostid = serializers.IntegerField(source='id', read_only=True)
    #lostdate = serializers.DateField(input_formats=['%Y-%m-%d'], format='%Y-%m-%d', required=False)
    #losttime = serializers.TimeField(input_formats=['%H'], format='%H', required=False)
    userget = UserSerializer(source='user.nickname', read_only=True)

    class Meta:
        model = Lost
        fields = ['lostid', 'image', 'lostdate', 'losttime', 'description', 
                  'title', 'moredesc', 'founded', 
                  'userget', 'category', 'getwhere', 'nowwhere']

class LostlistSerializer(serializers.ModelSerializer):
    lostid = serializers.IntegerField(source='id', read_only=True)
    #lostdate = serializers.DateField(input_formats=['%Y-%m-%d'], format='%Y-%m-%d', required=False)

    class Meta:
        model = Lost
        fields = ['lostid', 'image', 'title', 'category', 'getwhere', 'nowwhere', 'lostdate', 'losttime']

# class LostImageUploadSerializer(serializers.ModelSerializer):
#     # image = serializers.ImageField()
#     lostdate = serializers.DateField(input_formats=['%Y-%m-%d'], format='%Y-%m-%d', required=False)
#     losttime = serializers.TimeField(input_formats=['%H'], format='%H', required=False)

#     class Meta:
#         model = Lost
#         fields = ['lostid', 'lostdate', 'losttime']