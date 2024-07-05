from rest_framework import serializers
from .models import (
    OurWorksVideoDetail,
    Rate,
    Price,
    Service,
    WhyWeAre,
    ReasonsWhyWeAre,
    OurProject,
    ProjectPicture,
    OurWorksVideo,
    Review,
    OneReview,
    Connection
)


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        read_only_fields = ('id', 'title')


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        read_only_fields = ('id', 'price', 'description')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        read_only_fields = ('id', 'title')


class WhyWeAreSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyWeAre
        read_only_fields = ('id', 'title')


class ReasonsWhyWeAreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReasonsWhyWeAre
        read_only_fields = ('id', 'text', 'picture_url')


class OurProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurProject
        read_only_fields = ('id', 'title', 'footage')


class ProjectPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPicture
        read_only_fields = ('id', 'picture_url', 'description')


class OurWorksVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurWorksVideo
        read_only_fields = ('id', 'title')


class OurWorksVideoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurWorksVideoDetail
        read_only_fields = ('id', 'url')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        read_only_fields = ('id', 'title')


class OneReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneReview
        read_only_fields = ('id', 'name', 'surname', 'photo_url',
                            'title', 'text', 'email')


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        read_only_fields = ('address', 'office_hours',
                            'phone', 'email')
