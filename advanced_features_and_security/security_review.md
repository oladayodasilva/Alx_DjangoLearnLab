# Security Review — HTTPS & Secure Redirects

## Implemented Measures

### 1. Enforced HTTPS
- Enabled `SECURE_SSL_REDIRECT=True` so all HTTP traffic is redirected to HTTPS.
- Added HSTS settings (`SECURE_HSTS_SECONDS`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`, 
`SECURE_HSTS_PRELOAD`) to force browsers to use HTTPS.

### 2. Secure Cookies
- `SESSION_COOKIE_SECURE=True`
- `CSRF_COOKIE_SECURE=True`
These ensure cookies are only transmitted over HTTPS.

### 3. Secure Browser Headers
- `X_FRAME_OPTIONS="DENY"` — prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF=True` — prevents content-type sniffing attacks.
- `SECURE_BROWSER_XSS_FILTER=True` — activates browser XSS protection.

### 4. Input & Output Protection
- All forms use `{% csrf_token %}`.
- ORM queries used to avoid SQL injection.

## Areas for Improvement
- Add CSP (Content Security Policy) using django-csp for deeper XSS protection.
- Add SSL certificate rotation automation.
- Enable HTTP/2 on the deployment server.

