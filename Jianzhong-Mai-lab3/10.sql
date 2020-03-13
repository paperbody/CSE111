SELECT SUM(o_totalprice)
FROM customer, nation, region, orders
WHERE c_nationkey = n_nationkey AND n_regionkey = r_regionkey AND r_name = "EUROPE" AND c_custkey = o_custkey AND o_orderdate LIKE "1996-__-__";

