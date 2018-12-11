__author__ = 'Administrator'
from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.simple_tag
def get_language(language,submission):

    print(type(language))
    print(language)
    print(type(submission))
    # print(submission)
    # print(type(language[submission['language']]))
    # print(language[submission['language']])

    return language[submission.language]