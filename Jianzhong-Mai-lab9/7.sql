select c_nation, o_orderstatus, count(distinct(o_orderkey))
from Q1, Q5, lineitem
where c_custkey = o_custkey and o_orderkey = l_orderkey and c_region = "ASIA"
group by c_nation, o_orderstatus

