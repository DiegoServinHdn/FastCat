from django.db.models import fields
from rest_framework import serializers
from .models import Workspace

class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ('id', 'code', 'host', 'guest_can_edit', 'created_at')
