from rest_framework import serializers
from django import forms
from .models import Status


# class CustomSerializer(serializers.Serializer):
#
#     text_field = serializers.CharField()
#     email = serializers.EmailField()


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

    # def validate_content(self, attrs):
    #     if len(attrs) > 10000:
    #         raise serializers.ValidationError("Content is too long")

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required")
        return data


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]
