from django.db.models.signals import post_save
from django.dispatch import receiver
from shop_app.models import Order
from shop_app.tasks import notify_user_order_created


@receiver(post_save, sender=Order)
def handle_order_saved(instance: Order, created: bool, **kwargs):
    if not created:
        print("Just updated order:", instance)
    # notify_user_order_created(instance.pk)
    result = notify_user_order_created.delay(order_id=instance.pk)
    print("Notify user order task created:", result)
