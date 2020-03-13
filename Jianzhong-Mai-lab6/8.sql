select count(distinct(o_custkey)) 
from orders , customer
where o_custkey = c_custkey and
o_orderkey not in (
	select  (o_orderkey)
	from nation, region,lineitem, supplier, orders
	where s_suppkey = l_suppkey and
	o_orderkey = l_orderkey and
	n_regionkey = r_regionkey and
	n_nationkey = s_nationkey and
	r_name not in ("ASIA") 
	group by o_orderkey

);
