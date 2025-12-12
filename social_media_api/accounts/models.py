from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # other fields you may already have...
    following = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followers",
        blank=True,
        help_text="Users this user is following"
    )

    def follow(self, other_user):
        self.following.add(other_user)

    def unfollow(self, other_user):
        self.following.remove(other_user)

    def is_following(self, other_user):
        return self.following.filter(pk=other_user.pk).exists()

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    
    # followers: users following me
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username

