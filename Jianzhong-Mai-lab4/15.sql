select count(distinct(o_orderkey))
from orders, supplier, customer, lineitem
where s_suppkey = l_suppkey and
c_custkey = o_custkey and
o_orderkey = l_orderkey and
 c_acctbal < 0 and
 s_acctbal > 0

