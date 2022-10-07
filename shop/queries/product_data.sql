SELECT
    shop_product.id,
    shop_product.name,
    shop_product.initial_amount - ifnull(purchase_count.purchased, 0)
        AS amount_left,
    CAST(
        CASE
            WHEN
                ifnull(purchase_count.purchased, 0)
                    > shop_product.initial_amount / 2
            THEN
                shop_product.price * 1.2
            ELSE
                shop_product.price
        END AS int
    ) AS price
FROM
    shop_product
LEFT JOIN
    (
        SELECT
            product_id,
            count(*) AS purchased
        FROM
            shop_purchase
        GROUP BY
            product_id
    ) AS purchase_count
ON
    shop_product.id = purchase_count.product_id;
