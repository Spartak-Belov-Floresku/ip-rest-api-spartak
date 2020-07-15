from rest_framework import serializers, viewsets
from . import models

class CIDRSerializerAll(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CIDR
        fields = ('id', 'url', 'address', 'status')
        read_only_fields = ('id', 'url', 'address' )

class CIDRViewSetAll(viewsets.ModelViewSet):
    queryset = models.CIDR.lists.all()
    serializer_class =  CIDRSerializerAll
    filter_fields = ('address',)
