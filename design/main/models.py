from django.db import models


class Rate(models.Model):
    title = models.CharField(max_length=255, default='Default Title')

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'


class Price(models.Model):
    price = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    rate = models.ForeignKey(
        Rate, on_delete=models.CASCADE, related_name='prices')

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return self.price


class Service(models.Model):
    title = models.CharField(max_length=255)
    rate = models.ForeignKey(
        Rate, on_delete=models.CASCADE, related_name='services')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title


class WhyWeAre(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Почему мы?'
        verbose_name_plural = 'Почему мы?'

    def __str__(self):
        return self.title


class ReasonsWhyWeAre(models.Model):
    text = models.TextField()
    picture_url = models.URLField()
    why_we_are = models.ForeignKey(
        WhyWeAre, on_delete=models.CASCADE, related_name='reasons')

    class Meta:
        verbose_name = 'Причины почему мы'
        verbose_name_plural = 'Причины почему мы'

    def __str__(self):
        return self.text[:20]


class OurProject(models.Model):
    title = models.CharField(max_length=255)
    footage = models.FloatField()
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Наш проект'
        verbose_name_plural = 'Наши проекты'

    def __str__(self):
        return self.title


class ProjectPicture(models.Model):
    picture_url = models.URLField()
    description = models.TextField()
    our_project = models.ForeignKey(
        OurProject, on_delete=models.CASCADE, related_name='project_pictures')

    class Meta:
        verbose_name = 'Картинки наших проектов'
        verbose_name_plural = 'Картинки наших проектов'


class OurWorksVideo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')

    class Meta:
        verbose_name = 'Видео наших работ'
        verbose_name_plural = 'Видео наших работ'


class OurWorksVideoDetail(models.Model):
    url = models.URLField()
    our_works_video = models.ForeignKey(
        OurWorksVideo, on_delete=models.CASCADE, related_name='video_urls')

    class Meta:
        verbose_name = 'Отдельное видео наших работ'
        verbose_name_plural = 'Отдельные видео наших работ'


class Review(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.title


class OneReview(models.Model):
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    photo_url = models.URLField()
    title = models.CharField(max_length=80)
    text = models.TextField()
    email = models.EmailField()
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='one_reviews')

    class Meta:
        verbose_name = 'Конкретный отзыв'
        verbose_name_plural = 'Конкретные отзывы'

    def __str__(self):
        return self.title


class Connection(models.Model):
    address = models.CharField(max_length=255)
    office_hours = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Связаться'
        verbose_name_plural = 'Связаться'

    def __str__(self):
        return self.address
