from django.db import models

# Create your models here.


class Thread(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)


class Comment(models.Model):
    thread = models.ForeignKey(Thread,
                               on_delete=models.CASCADE,
                               related_name="comments")
    parent = models.ForeignKey("self",
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name="children")
    username = models.CharField(max_length=50)
    email = models.EmailField()
    url = models.URLField(null=True, blank=True)
    text = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user_ip = models.GenericIPAddressField()
    useragent = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Comment'

    def __str__(self):
        return f"{self.username}/{self.email}/{self.created}"
