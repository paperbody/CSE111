select s_nation, count(distinct(o_orderkey))
from Q2, Q5, lineitem
where  s_suppkey = l_suppkey and
o_orderkey = l_orderkey and
 s_region = "AMERICA" and 
 o_orderstatus = "F" and 
 o_orderyear = "1995" 
group by s_nation
