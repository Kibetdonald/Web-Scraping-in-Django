from django.db.models import fields
from rest_framework import serializers
from web_scraper.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


def get_image_url(self, obj):
    return obj.image.url
