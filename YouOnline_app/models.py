from django.contrib.auth.models import User
from django.db import models


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


class youonline(SoftDeleteModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    text_post = models.TextField(blank=True, null=True)
    photo = models.ImageField('images/')

