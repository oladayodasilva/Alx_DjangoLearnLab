# Security Measures in Bookshelf App

This app implements Django security best practices:

## Settings Security
- `DEBUG = False` for production.
- `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE` ensure cookies are only sent via HTTPS.
- Browser protections enabled:
  - `SECURE_BROWSER_XSS_FILTER`
  - `SECURE_CONTENT_TYPE_NOSNIFF`
  - `X_FRAME_OPTIONS = "DENY"`

## CSRF Protection
All form templates include `{% csrf_token %}`.

## Secure Views
- User inputs are validated using Django forms.
- ORM filters are used to prevent SQL injection.
- No raw SQL queries are used.

## Content Security Policy
The CSP middleware restricts loading of scripts/styles to trusted sources only.


