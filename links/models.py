from django.db import models
from django.conf import settings
from django.db.models import Count
from django.contrib.auth.models import User


class LinkQuerySet(models.QuerySet):
    def search(self, **kwargs):
        if len(kwargs['tags']) != 0:
            qs = self
            qs = qs.filter(approved=True)
            if kwargs.get('level', []):
                if "AN" not in kwargs['level']:
                    qs = qs.filter(level__in=[kwargs['level'], "AN"])
            if kwargs.get('type', []) and len(kwargs['type']) != 0:
                qs = qs.filter(type__in=kwargs['type'])
            if kwargs.get('tags', []):
                qs = qs.filter(tags__in=kwargs['tags'])
            qs = qs.annotate(q_count=Count('likes')).order_by('-q_count')
            return qs.distinct()
        else:
            return Link.objects.none()


class Link(models.Model):

    approved = models.BooleanField(default=False, blank=False, null=False)
    objects = LinkQuerySet.as_manager()

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='link_like', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    ADVANCED = 'AD'
    INTERMEDIATE = 'IN'
    BEGINNER = 'BE'
    ANY = "AN"
    LEVEL_CHOICES = [
        (ANY, 'Any level'),
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced')
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
    tagline = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100, blank=False)
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


class Comment(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=500)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment in {} by {}'.format(self.link.name, self.user.username)