from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
from django.utils.text import slugify

from categories.models import Category


class Post(models.Model):
    title = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75, blank=True)
    content = models.TextField()
    category = models.ForeignKey(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, blank=True)

    class Meta:
        ordering = ('-created',)
        get_latest_by = 'created'

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('post_detail', [self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)
