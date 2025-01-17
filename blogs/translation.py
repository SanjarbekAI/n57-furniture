from modeltranslation.translator import register, TranslationOptions

from blogs import models


@register(models.BlogCategoryModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(models.BlogTagModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(models.BlogAuthorModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name',)


@register(models.BlogModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
