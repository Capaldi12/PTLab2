SELECT
    shop_product.id,
    shop_product.name,
    shop_product.price,
    shop_product.initial_amount - ifnull(purchase_count.purchased, 0)
        AS amount_left
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
