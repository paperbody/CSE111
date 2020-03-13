select s_region, c_region, cast(sum(l_extendedprice)as int)
from lineitem, Q1, Q2, orders
where l_suppkey = s_suppkey and
o_orderkey = l_orderkey and
c_custkey = o_custkey
group by s_region, c_region
