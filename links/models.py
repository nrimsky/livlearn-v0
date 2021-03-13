from django.db import models
from django.conf import settings
from django.db.models import Count

class LinkQuerySet(models.QuerySet):
    def search(self, **kwargs):
        qs = self
        qs = qs.order_by('-created_at')
        if kwargs.get('q', ''):
            qs = qs.filter(models.Q(name__icontains=kwargs['q']) | models.Q(description__icontains=kwargs['q']) | models.Q(tags__name__icontains=kwargs['q']))
        if kwargs.get('level', []):
            if "AN" not in kwargs['level'] and len(kwargs['level']) != 0:
                levels = kwargs['level']
                levels.append("AN")
                qs = qs.filter(level__in=levels)
        if kwargs.get('type', []) and len(kwargs['type']) != 0:
            qs = qs.filter(type__in=kwargs['type'])
        if kwargs.get('tags', []) and len(kwargs['tags']) != 0:
            qs = qs.filter(tags__in=kwargs['tags'])
        return qs.distinct()


class Link(models.Model):

    objects = LinkQuerySet.as_manager()

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='link_like', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    ADVANCED = 'AD'
    INTERMEDIATE = 'IN'
    BEGINNER = 'BE'
    ANY = "AN"
    LEVEL_CHOICES = [
        (ADVANCED, 'Advanced'),
        (INTERMEDIATE, 'Intermediate'),
        (BEGINNER, 'Beginner'),
        (ANY, 'Any level')
    ]
    level = models.CharField(
        max_length=2,
        choices=LEVEL_CHOICES,
        blank=False,
        default=ANY
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

