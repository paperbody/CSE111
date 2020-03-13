SELECT COUNT(*)
FROM customer, nation, orders
WHERE n_nationkey = c_nationkey AND n_name = "BRAZIL" AND o_orderpriority = "1-URGENT" AND o_custkey = c_custkey AND o_orderdate >= "1994-01-01" AND o_orderdate <= "1997-12-31";

