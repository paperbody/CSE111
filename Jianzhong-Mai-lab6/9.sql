select distinct p_name
from part, customer, orders, lineitem, nation,region
where p_partkey = l_partkey and
l_orderkey = o_orderkey and
c_custkey = o_custkey and
n_nationkey = c_nationkey and
n_regionkey = r_regionkey and
r_name = "AMERICA" and
p_name in (
select distinct p_name
from nation, region, part, supplier, partsupp
where p_partkey = ps_partkey and
s_suppkey = ps_suppkey and
n_nationkey = s_nationkey and
r_regionkey = n_regionkey and
r_name = "ASIA"
group by p_name
having count(distinct s_suppkey) = 4)
order by p_name;
