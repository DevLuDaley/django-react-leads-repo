from rest_framework import serializers
from leads.models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'email', 'message')  # mapping specifi fields
        # mapping all fields
        # #fields = '__all__'
