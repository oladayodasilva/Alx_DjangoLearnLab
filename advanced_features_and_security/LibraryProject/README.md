# Bookshelf App Permissions Setup

This app uses Django groups and custom permissions to control access.

## Custom Permissions on Book Model
- `can_view` → view books
- `can_create` → add books
- `can_edit` → edit books
- `can_delete` → delete books

## Groups
- **Viewers** → can_view
- **Editors** → can_create, can_edit
- **Admins** → all permissions

## Notes
- Views are protected using `@permission_required`.
- Groups and permissions can be managed in Django Admin.
- Alternatively, `signals.py` auto-creates groups with the correct permissions after migrations.

