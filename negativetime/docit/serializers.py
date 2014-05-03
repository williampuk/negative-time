from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'user', 'name', 'summary')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class SectionSerializer(serializers.Serializer):
    name = serializers.CharField()
    content = serializers.CharField()

    def to_native(self, value):
        # hack to support recursive field serialization
        if 'children' not in self.fields:
            self.fields['children'] = SectionSerializer(many=True)

        return super().to_native(value)
