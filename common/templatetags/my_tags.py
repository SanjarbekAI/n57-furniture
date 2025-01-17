from django import template

register = template.Library()


@register.simple_tag
def get_lang_url(request, lang):
    url = request.path
    url = url.split('/')
    url[1] = lang
    res = '/'.join(url)
    return res

@register.simple_tag
def get_lang_flag(lang):
    if lang == "uz":
        return "🇺🇿"
    return "🇺🇸"

