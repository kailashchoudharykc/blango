from django import template
from django.contrib.auth import get_user_model
from django.utils.html import format_html

user_model = get_user_model()

register = template.Library()

@register.filter
def author_details(author):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = format_html(f"{author.first_name} {author.last_name}")
    else:
        name = format_html(f"{author.username}")

    if author.email:
        email = format_html(author.email)
        prefix = f'<a href="mailto:{email}">'
        suffix = "</a>"
    else:
        prefix = ""
        suffix = ""

    return format_html(f"{prefix}{name}{suffix}")