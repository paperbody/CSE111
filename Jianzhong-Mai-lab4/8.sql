select n_name, count(distinct(o_orderkey))
from region, nation, orders, lineitem, supplier
where r_regionkey = n_regionkey and 
s_suppkey = l_suppkey and
o_orderkey = l_orderkey and
 r_name = "AMERICA" and 
 o_orderstatus = "F" and 
 o_orderdate like "1995%" and
 n_nationkey = s_nationkey
group by n_name
