select count(distinct(o_clerk))
from  Q2, lineitem, Q5
where  s_suppkey = l_suppkey and
o_orderkey = l_orderkey and
 s_nation = 'RUSSIA'
group by s_nation

