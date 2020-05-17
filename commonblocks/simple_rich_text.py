from django.utils.safestring import mark_safe

try:
    from wagtail.core.rich_text import RichText, expand_db_html
except:
    from wagtail.wagtailcore.rich_text import RichText, expand_db_html


class SimpleRichText(RichText):
    """
    A custom simple RichText to avoid the <div class='richtext'></div>
    """

    def __str__(self):
        return mark_safe(expand_db_html(self.source))
