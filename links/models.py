from django.db import models
from django.conf import settings


class Link(models.Model):
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='link_like', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    ADVANCED = 'A'
    INTERMEDIATE = 'I'
    BEGINNER = 'B'
    LEVEL_CHOICES = [
        (ADVANCED, 'Advanced'),
        (INTERMEDIATE, 'Intermediate'),
        (BEGINNER, 'Beginner')
    ]
    level = models.CharField(
        max_length=2,
        choices=LEVEL_CHOICES,
        blank=False
    )

    PODCAST = "PO"
    YOUTUBE = "YT"
    COURSE = "CO"
    ARTICLE = "AR"
    BOOK = "BO"
    OTHER = "OT"
    TYPE_CHOICES = [
        (PODCAST, 'Podcast'),
        (YOUTUBE, 'YouTube / Video'),
        (COURSE, 'Online course (eg: Coursera)'),
        (ARTICLE, 'Article, Text or Blog'),
        (BOOK, 'Book'),
        (OTHER, 'Other')
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        blank=False,
        default=OTHER
    )

    url = models.URLField(max_length=300, blank=False)
    description = models.TextField(max_length=500, blank=False)
    name = models.TextField(max_length=100, blank=False)
    tags = models.ManyToManyField(
        to='links.Tag',
        related_name='links',
        blank=True
    )

    def __str__(self):
        return self.name

    def number_of_likes(self):
        return self.likes.count()


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

