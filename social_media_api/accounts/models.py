from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    following = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followers",
        blank=True,
        help_text="Users this user is following"
    )
    pass

    def follow(self, other_user):
        self.following.add(other_user)

    def unfollow(self, other_user):
        self.following.remove(other_user)

    def is_following(self, other_user):
        return self.following.filter(pk=other_user.pk).exists()


