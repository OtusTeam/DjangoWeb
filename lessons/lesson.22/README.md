```
➜ python manage.py debugsqlshell
Python 3.12.3 (main, May  9 2024, 20:16:14) [Clang 14.0.3 (clang-1403.0.22.14.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from shop_app.models import Order
>>> orders = Order.objects.select_related("user").all()
>>> for order in orders:
...   print(order)
... 
SELECT "shop_app_order"."id",
       "shop_app_order"."user_id",
       "shop_app_order"."status",
       "shop_app_order"."address",
       "shop_app_order"."created_at",
       "shop_app_order"."updated_at",
       "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
FROM "shop_app_order"
INNER JOIN "auth_user" ON ("shop_app_order"."user_id" = "auth_user"."id")
ORDER BY "shop_app_order"."id" ASC [0.72ms]
viewer - NEW - qwerty
sam - PENDING - ul Pushkina
john - SHIPPED - qwertgqwerqwer
>>> orders = Order.objects.select_related("user").prefetch_related("order_products__product__categories").all()
>>> for order in orders:
...   for product in products
KeyboardInterrupt
>>> orders = Order.objects.select_related("user").prefetch_related("products__categories").all()
>>> for order in orders:
...   for product in order.products.all():
... 
KeyboardInterrupt
>>> for order in orders:
...   print(order)
...   for product in order.products.all():
...     print(product)
...     for category in product.categories.all():
...       print("-", category)
... 
SELECT "shop_app_order"."id",
       "shop_app_order"."user_id",
       "shop_app_order"."status",
       "shop_app_order"."address",
       "shop_app_order"."created_at",
       "shop_app_order"."updated_at",
       "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
FROM "shop_app_order"
INNER JOIN "auth_user" ON ("shop_app_order"."user_id" = "auth_user"."id")
ORDER BY "shop_app_order"."id" ASC [1.05ms]
SELECT ("shop_app_orderproduct"."order_id") AS "_prefetch_related_val_order_id",
       "shop_app_product"."id",
       "shop_app_product"."title",
       "shop_app_product"."description",
       "shop_app_product"."price",
       "shop_app_product"."archived"
FROM "shop_app_product"
INNER JOIN "shop_app_orderproduct" ON ("shop_app_product"."id" = "shop_app_orderproduct"."product_id")
WHERE "shop_app_orderproduct"."order_id" IN (1,
                                             2,
                                             3)
ORDER BY "shop_app_product"."id" ASC [0.27ms]
SELECT ("shop_app_product_categories"."product_id") AS "_prefetch_related_val_product_id",
       "shop_app_category"."id",
       "shop_app_category"."name",
       "shop_app_category"."description"
FROM "shop_app_category"
INNER JOIN "shop_app_product_categories" ON ("shop_app_category"."id" = "shop_app_product_categories"."category_id")
WHERE "shop_app_product_categories"."product_id" IN (1,
                                                     2,
                                                     3,
                                                     4,
                                                     5,
                                                     6,
                                                     7)
ORDER BY "shop_app_category"."id" ASC [0.17ms]
viewer - NEW - qwerty
Bread
- food
- wheat
plastic bag
- bags
Milk
- food
- milk
sam - PENDING - ul Pushkina
Полезная Рыба
- food
- fish
Dorado
- food
- fish
john - SHIPPED - qwertgqwerqwer
Gaming Chair
- furniture
gaming keyboard
- Keyboards
>>> from django.db.models import Q
>>> Order.objects.filter(Q(products__title__startswith='B'))
SELECT "shop_app_order"."id",
       "shop_app_order"."user_id",
       "shop_app_order"."status",
       "shop_app_order"."address",
       "shop_app_order"."created_at",
       "shop_app_order"."updated_at"
FROM "shop_app_order"
INNER JOIN "shop_app_orderproduct" ON ("shop_app_order"."id" = "shop_app_orderproduct"."order_id")
INNER JOIN "shop_app_product" ON ("shop_app_orderproduct"."product_id" = "shop_app_product"."id")
WHERE "shop_app_product"."title" LIKE 'B%' ESCAPE '\'
ORDER BY "shop_app_order"."id" ASC
LIMIT 21 [2.46ms]
SELECT "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 2
LIMIT 21 [0.11ms]
<QuerySet [<Order: viewer - NEW - qwerty>]>
>>> Order.objects.filter(Q(products__title__startswith='B') | ~Q(products__categories__name__startswith="foo"))
SELECT "shop_app_order"."id",
       "shop_app_order"."user_id",
       "shop_app_order"."status",
       "shop_app_order"."address",
       "shop_app_order"."created_at",
       "shop_app_order"."updated_at"
FROM "shop_app_order"
LEFT OUTER JOIN "shop_app_orderproduct" ON ("shop_app_order"."id" = "shop_app_orderproduct"."order_id")
LEFT OUTER JOIN "shop_app_product" ON ("shop_app_orderproduct"."product_id" = "shop_app_product"."id")
WHERE ("shop_app_product"."title" LIKE 'B%' ESCAPE '\' OR NOT (EXISTS(SELECT 1 AS "a" FROM "shop_app_orderproduct" U1 INNER JOIN "shop_app_product" U2 ON (U1."product_id" = U2."id") INNER JOIN "shop_app_product_categories" U3 ON (U2."id" = U3."product_id") INNER JOIN "shop_app_category" U4 ON (U3."category_id" = U4."id") WHERE (U4."name" LIKE 'foo%' ESCAPE '\'
       AND U1."id" = ("shop_app_orderproduct"."id"))
LIMIT 1)))
ORDER BY "shop_app_order"."id" ASC
LIMIT 21 [1.30ms]
SELECT "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 2
LIMIT 21 [0.06ms]
SELECT "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 2
LIMIT 21 [0.06ms]
SELECT "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 4
LIMIT 21 [0.09ms]
SELECT "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 4
LIMIT 21 [0.05ms]
<QuerySet [<Order: viewer - NEW - qwerty>, <Order: viewer - NEW - qwerty>, <Order: john - SHIPPED - qwertgqwerqwer>, <Order: john - SHIPPED - qwertgqwerqwer>]>
>>> Order.objects.filter(Q(products__title__startswith='B') | ~Q(products__categories__name__startswith="foo"))
KeyboardInterrupt
>>> Q() & Q()
<Q: (AND: )>
>>> Q(foo="bar") & Q(spam="eggs")
<Q: (AND: ('foo', 'bar'), ('spam', 'eggs'))>
>>> Q(foo="bar") | Q(spam="eggs")
<Q: (OR: ('foo', 'bar'), ('spam', 'eggs'))>
>>> Q(foo="bar") ^ Q(spam="eggs")
<Q: (XOR: ('foo', 'bar'), ('spam', 'eggs'))>
>>> Q(foo="bar") & ~Q(spam="eggs")
<Q: (AND: ('foo', 'bar'), (NOT (AND: ('spam', 'eggs'))))>
>>> Q(foo="bar") & ~Q(Q(), spam="eggs")
<Q: (AND: ('foo', 'bar'), (NOT (AND: (AND: ), ('spam', 'eggs'))))>
>>> 
```