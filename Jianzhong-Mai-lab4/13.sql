select count(distinct(o_orderkey))
from 
(select o_orderkey
from customer, nation, orders
where c_nationkey = n_nationkey and c_custkey = o_custkey and n_name = "CANADA"
intersect
select distinct(o_orderkey)
from supplier, nation, region, lineitem, orders
where s_nationkey = n_nationkey and r_regionkey = n_regionkey and s_suppkey = l_suppkey and o_orderkey = l_orderkey and r_name = "EUROPE"
);
