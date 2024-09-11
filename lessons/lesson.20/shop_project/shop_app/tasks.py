from django.core.mail import send_mail
from celery import shared_task

from shop_app.models import Order


@shared_task
def notify_user_order_created(
    order_id: int,
) -> None:
    order: Order = Order.objects.select_related("user").get(id=order_id)
    print("Send user email about order", order)
    # sleep(10)

    subject = f"Order #{order.pk} created successfully"
    message_text = f"Thank you for your order! Order #{order.pk} created successfully!"
    from_email = "megashop-care@example.com"
    recipient = f"{order.user.username}@example.com"
    send_mail(
        subject,
        message_text,
        from_email,
        [recipient],
        fail_silently=False,
    )
    print("Successfully sent email about order", order)
