import posixpath
from django import template
from django.templatetags.static import static as original_static
from ..utils import compile_static, get_supported_extensions

register = template.Library()


# PATCH: Replacement of default static tag
@register.simple_tag
def static_mod(path):
    '''
    Temporary tag for replacing 'static-preprocessors' with modified 'static-precompilers'
    '''
    new_path = path
    basename, ext = posixpath.splitext(path)
    supported_extensions = get_supported_extensions()
    if ext in supported_extensions:
         new_path = compile_static(path)
    return original_static(new_path)
