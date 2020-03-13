SELECT n_name, SUBSTR(o_orderdate,1,4), COUNT(o_orderdate)
FROM nation, supplier, orders,lineitem
WHERE s_nationkey = n_nationkey AND l_suppkey = s_suppkey AND l_orderkey = o_orderkey AND o_orderpriority = "3-MEDIUM"
GROUP BY n_name, SUBSTR(o_orderdate,1,4);
