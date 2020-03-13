SELECT DISTINCT(n_name)
FROM customer, orders, nation
WHERE c_nationkey =  n_nationkey AND o_orderdate LIKE "1996-12-__" AND c_custkey = o_custkey;
