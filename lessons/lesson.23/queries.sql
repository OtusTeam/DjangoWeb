SELECT "shop_app_order"."id",
       "shop_app_order"."user_id",
       "shop_app_order"."status",
       "shop_app_order"."address",
       "shop_app_order"."created_at",
       "shop_app_order"."updated_at",
       COUNT("shop_app_orderproduct"."id")     AS "op_count",
       SUM("shop_app_orderproduct"."quantity") AS "total_quantity"
FROM "shop_app_order"
         LEFT OUTER JOIN "shop_app_orderproduct" ON ("shop_app_order"."id" = "shop_app_orderproduct"."order_id")
GROUP BY "shop_app_order"."id", "shop_app_order"."user_id", "shop_app_order"."status", "shop_app_order"."address",
         "shop_app_order"."created_at", "shop_app_order"."updated_at";


SELECT "shop_app_order"."id",
       "shop_app_order"."user_id",
       "shop_app_order"."status",
       "shop_app_order"."address",
       COUNT("shop_app_orderproduct"."id")     AS "op_count",
       SUM("shop_app_orderproduct"."quantity") AS "total_quantity"
FROM "shop_app_order"
         LEFT OUTER JOIN "shop_app_orderproduct" ON ("shop_app_order"."id" = "shop_app_orderproduct"."order_id")
GROUP BY "shop_app_order"."id", "shop_app_order"."user_id", "shop_app_order"."status", "shop_app_order"."address";

--

SELECT "shop_app_order"."id"
     , "shop_app_order"."user_id"
     , "shop_app_order"."status"
     , "shop_app_order"."address"
FROM "shop_app_order"
ORDER BY "shop_app_order"."id" ASC;

SELECT "shop_app_orderproduct"."id",
       "shop_app_orderproduct"."product_id",
       "shop_app_orderproduct"."order_id",
       "shop_app_orderproduct"."quantity",
       "shop_app_orderproduct"."price",
       (
           CAST(
                   (
                       "shop_app_orderproduct"."quantity" * "shop_app_orderproduct"."price"
                       ) AS NUMERIC
           )
           ) AS "total_price"
FROM "shop_app_orderproduct"
WHERE "shop_app_orderproduct"."order_id" IN (1, 2, 3)
ORDER BY "shop_app_orderproduct"."id" ASC;

--

SELECT "shop_app_order"."id"
     , "shop_app_order"."user_id"
     , "shop_app_order"."status"
     , "shop_app_order"."address"
     , (
    CAST(
            SUM(
                    (
                        CAST(
                                (
                                    "shop_app_orderproduct"."quantity" * "shop_app_orderproduct"."price"
                                    ) AS NUMERIC
                        )
                        )
            ) AS NUMERIC
    )
    ) AS "total_sum"
FROM "shop_app_order"
         LEFT OUTER JOIN "shop_app_orderproduct"
                         ON (
                             "shop_app_order"."id" = "shop_app_orderproduct"."order_id"
                             )
GROUP BY "shop_app_order"."id"
       , "shop_app_order"."user_id"
       , "shop_app_order"."status"
       , "shop_app_order"."address";

--
SELECT "auth_user"."id"
     , "auth_user"."username"
     , COUNT("shop_app_order"."id") AS "orders_count"
FROM "auth_user"
         LEFT OUTER JOIN "shop_app_order" ON ("auth_user"."id" = "shop_app_order"."user_id")
GROUP BY "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser",
         "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email",
         "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined";