from django.core.mail import send_mail
from django.conf import settings


def update_stock(order_data):
    from .models import ProductIngredient  # NOQA: F401

    product_ingredients = ProductIngredient.objects.filter(product=order_data.product)
    for pi in product_ingredients:
        pi.ingredient.stock -= pi.amount * order_data.quantity
        pi.ingredient.save()
        if (
            pi.ingredient.stock
            <= pi.ingredient.initial_stock * settings.STOCK_THRESHOLD / 100
            and not pi.ingredient.low_stock_alert_sent
        ):
            send_low_stock_alert(pi.ingredient)


def send_low_stock_alert(ingredient):
    send_mail(
        "Low Stock Alert",
        f"The stock for {ingredient.name} has fallen below {settings.STOCK_THRESHOLD}%. Please restock.",
        settings.DEFAULT_FROM_EMAIL,
        [settings.ADMIN_EMAIL],
    )
    ingredient.low_stock_alert_sent = True
    ingredient.save()
