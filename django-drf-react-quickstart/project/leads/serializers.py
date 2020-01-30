from rest_framework import serializers
from leads.models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'email', 'message')  # mapping specific fields
        # mapping all fields
        # #fields = '__all__'
# python manage.py loaddata leads
