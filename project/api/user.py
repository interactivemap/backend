from django.contrib.auth import authenticate


def jwt_get_username_from_payload_handler(payload):
    """Handle for JWT authetication in settings.py."""
    username = payload.get("sub").replace("|", ".")
    authenticate(remote_user=username)
    return username
