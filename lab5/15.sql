
select sum(l_extendedprice * (1 - l_discount)) / 
(select sum(l_extendedprice * (1 - l_discount))
from lineitem, supplier, customer,  region, orders, nation n1, nation n2
where c_nationkey == n1.n_nationkey and
r_regionkey= n1.n_regionkey and
s_nationkey = n2.n_nationkey and
r_name = 'EUROPE' and
c_custkey = o_custkey and
o_orderkey = l_orderkey and
l_suppkey = s_suppkey and
l_shipdate >= "1996-01-01" and
l_shipdate <='1996-12-31')
from lineitem, supplier, customer,  region, orders, nation n1, nation n2
where c_nationkey = n1.n_nationkey and
n1.n_regionkey = r_regionkey and
s_nationkey = n2.n_nationkey and
n2.n_name = 'UNITED STATES' and
r_name = 'EUROPE' and
c_custkey = o_custkey and
o_orderkey = l_orderkey and
l_suppkey = s_suppkey and
l_shipdate >= '1996-01-01' and
l_shipdate <=  '1996-12-31'
