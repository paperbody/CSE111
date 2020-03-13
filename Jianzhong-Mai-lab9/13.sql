select count(distinct(o_orderkey))
from 
(select o_orderkey
from Q1, orders
where c_custkey = o_custkey and c_nation = "CANADA"
intersect
select distinct(o_orderkey)
from Q2, lineitem, orders
where s_suppkey = l_suppkey and o_orderkey = l_orderkey and s_region = "EUROPE"
);

