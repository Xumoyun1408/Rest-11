
from .models import All_Xarajat

from rest_framework import serializers


class All_XarajatSerializer(serializers.ModelSerializer):
    class Meta:
        model = All_Xarajat
        fields = '__all__'
