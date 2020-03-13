select count(*) 
from (
	select s_name
	from nation, lineitem, customer, supplier, orders
	where o_custkey = c_custkey and
	n_nationkey = c_nationkey and
	s_suppkey = l_suppkey and
	o_orderkey = l_orderkey and
	(n_name = "GERMANY" or
	n_name = "FRANCE")
	group by s_name
	having count(distinct(o_orderkey)) <30
);
