SELECT 
    SUM(p.amount * er.exchange_rate_to_eur) AS "SUM(AMOUNT_EUR)",
    p.transaction_date
FROM 
    payments p
JOIN 
    currencies c ON p.currency = c.currency_id
JOIN 
    exchange_rates er ON c.currency_id = er.currency_id
LEFT JOIN 
    blacklist b ON p.user_id_sender = b.user_id
WHERE 
    c.end_date IS NULL
    AND b.user_id IS NULL
GROUP BY 
    p.transaction_date;
