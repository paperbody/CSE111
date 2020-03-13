select distinct(s_name), c_name
from supplier, customer, lineitem, orders 
where c_custkey = o_custkey and
l_orderkey = o_orderkey and
c_custkey = o_custkey and
s_suppkey = l_suppkey and 
o_orderstatus  = "F" and 
o_totalprice = 
(select max(o_totalprice) 
	from orders
	where o_orderstatus  = "F"
);
