from pretix.base.email import TemplateBasedMailRenderer
from django.template.loader import get_template

class SimpleMailRenderer(TemplateBasedMailRenderer):
    verbose_name = "Simple E-mail Template"
    identifier = "es-simple"
    thumbnail_filename = "pretix_es_mail/simple.png"
    template_name = "pretix_es_mail/simple.html"

