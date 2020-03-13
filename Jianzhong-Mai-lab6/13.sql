SELECT n_name
FROM lineitem, (SELECT n_name, sum(l_extendedprice) 
FROM nation,supplier,lineitem
WHERE s_suppkey = l_suppkey and
n_nationkey = s_nationkey)
WHERE l_shipdate LIKE "1996%"
GROUP BY n_name;
