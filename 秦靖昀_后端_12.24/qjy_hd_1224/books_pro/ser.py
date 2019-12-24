from rest_framework import serializers
from .models import books1


# 序列化
class creSerializer(serializers.ModelSerializer):
    class Meta:
        model = books1
        fields = '__all__'
