from rest_framework import serializers
from .models import IFSC


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = IFSC
        fields = ('ifsc','bank_id','branch','address','city','district','state','bank_name')
