from django.core.management import BaseCommand
from django.db import models
from django.db.models import Count, Sum, F, Prefetch
from django.db.models.functions import Length

from shop_app.models import Category, Order, OrderProduct, UserModel


class Command(BaseCommand):
    help = "Show examples"

    def show_all_categories(self):
        for category in Category.objects.all():
            self.stdout.write(category.name)

    def create_categories(self):
        new_names = ("meat", "vegetables", "drinks", "sparkling water")
        new_categories = [Category(name=new_name) for new_name in new_names]
        Category.objects.bulk_create(new_categories)

        self.stdout.write(f"New categories: {new_categories}")

    def simple_filters_examples(self):

        op_qs = OrderProduct.objects.filter(quantity__gt=1).select_related("product")
        for op in op_qs:
            self.stdout.write(
                f"{op.pk} order #{op.order_id} {op.quantity} {op.product.title}"
            )

        categories_count = Category.objects.count()
        self.stdout.write(f"Categories count: {categories_count}")

    def simple_annotation_examples(self):

        categories_qs = (
            Category.objects.annotate(
                name_length=Length("name"),
            )
            .filter(
                name_length__lt=5,
            )
            .all()
        )
        short_categories_count = categories_qs.count()
        self.stdout.write(f"Short categories count: {short_categories_count}")

        for category in categories_qs:
            self.stdout.write(
                f"Category {category.name!r} of length {category.name_length}"
            )

    def show_order_with_op(self):
        orders_qs = Order.objects.prefetch_related("order_products").all()
        for order in orders_qs:
            self.stdout.write(
                f"Order {order.pk} to address {order.address!r} status is {order.status}"
            )
            for op in order.order_products.all():
                self.stdout.write(
                    f"OP {op.pk} quantity: {op.quantity}, price(1): {op.price}"
                )

    def show_order_with_op_details(self):
        op_qs = OrderProduct.objects.annotate(
            total_price=F("quantity") * F("price"),
        )
        orders_qs = (
            Order.objects.prefetch_related(
                Prefetch("order_products", queryset=op_qs),
            )
            .defer("created_at", "updated_at")
            .all()
        )
        for order in orders_qs:
            self.stdout.write(
                f"Order {order.pk} to address {order.address!r} status is {order.status}"
            )
            for op in order.order_products.all():
                self.stdout.write(
                    f"OP {op.pk} quantity: {op.quantity}, price(1): {op.price}, "
                    f"total pos price = {op.total_price}"
                )

    def show_order_with_total_price_details(self):
        orders_qs = (
            Order.objects.annotate(
                total_sum=Sum(
                    F("order_products__quantity") * F("order_products__price"),
                    output_field=models.DecimalField(),
                ),
            )
            .defer("created_at", "updated_at")
            .all()
        )
        for order in orders_qs:
            self.stdout.write(
                f"Order {order.pk} to address {order.address!r} status is {order.status}"
            )
            self.stdout.write(f"  total order sum = {order.total_sum}")

    def show_order_with_op_totals(self):
        orders_qs = (
            Order.objects.annotate(
                op_count=Count("order_products__pk"),
                total_quantity=Sum("order_products__quantity"),
            )
            .defer("created_at", "updated_at")
            .all()
        )
        for order in orders_qs:
            self.stdout.write(
                f"Order {order.pk} to address {order.address!r} status is {order.status}, "
                f"op count: {order.op_count}, "
                f"quantity: {order.total_quantity}"
            )

    def show_users_total_orders_counts(self):
        counts = UserModel.objects.aggregate(
            orders_count=Count("orders"),
        )
        self.stdout.write(f"Counts: {counts}")

    def show_users_with_orders_counts(self):
        users = UserModel.objects.annotate(
            orders_count=Count("orders"),
        ).values("pk", "username", "orders_count")
        self.stdout.write(f"Users products info:")
        for user in users:
            self.stdout.write(
                f"{user['pk']} {user['username']} orders: {user['orders_count']}"
            )

    def check_user_exists(self, username: str):
        exists = UserModel.objects.filter(username=username).exists()
        self.stdout.write(f"User {username} exists: {exists}")
        return exists

    def handle(self, *args, **options):
        self.stdout.write("Start show examples")

        self.show_all_categories()
        self.create_categories()
        self.simple_filters_examples()
        self.simple_annotation_examples()
        self.show_order_with_op()
        self.show_order_with_op_totals()
        self.show_order_with_op_details()
        self.show_order_with_total_price_details()
        self.show_users_total_orders_counts()
        self.show_users_with_orders_counts()
        self.check_user_exists("john")
        self.check_user_exists("bob")

        category: Category = Category.objects.filter(name="milk").get()
        category.description = "Whole milk."
        category.save(update_fields=["description"])

        # self.stdout.write(self.style.ERROR("ERROR example"))
        # self.stdout.write(self.style.WARNING("WARNING example"))
        self.stdout.write(self.style.SUCCESS("Finished"))
