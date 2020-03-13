select n_name, o_orderstatus, count(distinct(o_orderkey))
from region, nation, customer, orders, lineitem
where r_regionkey = n_regionkey and n_nationkey = c_nationkey and c_custkey = o_custkey and o_orderkey = l_orderkey and r_name = "ASIA"
group by n_name, o_orderstatus
