# bookshelf/signals.py
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    if sender.name == 'bookshelf':  # Only run for bookshelf app
        # Define groups
        groups_permissions = {
            "Editors": ["can_create", "can_edit"],
            "Viewers": ["can_view"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        Book = apps.get_model('bookshelf', 'Book')

        for group_name, perms in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_name in perms:
                permission = Permission.objects.get(
                    codename=perm_name,
                    content_type__app_label='bookshelf',
                    content_type__model='book'
                )
                group.permissions.add(permission)

