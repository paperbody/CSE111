SELECT COUNT(DISTINCT(c_name))
FROM customer, lineitem, orders
WHERE c_custkey = o_custkey AND l_orderkey = o_orderkey AND l_discount >= 0.04

