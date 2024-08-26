from django.apps import AppConfig


class ShopAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "shop_app"
    verbose_name = "Shop App"

    def ready(self):
        from shop_app import signals

        print("Inited signals for shop_app:", signals.__name__)
