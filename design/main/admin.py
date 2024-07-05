from django.contrib import admin
from .models import (
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
    Connection,
)


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    pass


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('price', 'description', 'rate')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'rate')


@admin.register(WhyWeAre)
class WhyWeAreAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(ReasonsWhyWeAre)
class ReasonsWhyWeAreAdmin(admin.ModelAdmin):
    list_display = ('text', 'picture_url', 'why_we_are')


@admin.register(OurProject)
class OurProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'footage', 'price')


@admin.register(ProjectPicture)
class ProjectPictureAdmin(admin.ModelAdmin):
    list_display = ('picture_url', 'description', 'our_project')


@admin.register(OurWorksVideo)
class OurWorksVideoAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(OneReview)
class OneReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'photo_url',
                    'title', 'text', 'email', 'review')


@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ('address', 'office_hours', 'phone', 'email')
