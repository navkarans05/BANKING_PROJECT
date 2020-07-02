from rest_framework import serializers
from .models import detail


class detailSerializer(serializers.ModelSerializer):
    class Meta:
       model=detail
       fields=['bank_id','branch','address','city','bank_name']

class ifscSerializer(serializers.ModelSerializer):
    class Meta:
       model=detail
       fields=['ifsc','bank_id','branch','address','city','district','state','bank_name']
