from django.utils.translation import gettext_lazy
from . import __version__

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")




class PluginApp(PluginConfig):
    name = "pretix_es_mail"
    verbose_name = "Simple Mail Templates"

    class PretixPluginMeta:
        name = gettext_lazy("Simple Mail Templates")
        author = "Electroservices Team"
        description = gettext_lazy("Simple E-mail Templates")
        visible = True
        restricted = False 
        version = __version__
        category = "CUSTOMIZATION"
        

    def ready(self):
        from . import signals  # NOQA


default_app_config = "pretix_es_mail.PluginApp"
