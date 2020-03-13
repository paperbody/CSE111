select count(distinct(o_clerk))
from  nation, lineitem, orders, supplier
where  s_suppkey = l_suppkey and
o_orderkey = l_orderkey and
n_nationkey = s_nationkey and
 n_name = 'RUSSIA'
group by n_name
