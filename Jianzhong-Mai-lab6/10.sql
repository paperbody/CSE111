select r_name
from customer, lineitem, nation, supplier, orders, region
where c_custkey = o_custkey and
n_regionkey = r_regionkey and
n_nationkey = s_nationkey and
c_nationkey = s_nationkey and
l_suppkey = s_suppkey and
l_orderkey = o_orderkey
group by r_name
order by sum(l_extendedprice) desc
limit 1
