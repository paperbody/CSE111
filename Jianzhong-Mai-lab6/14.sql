select name1,(exts - ext) 
from (select n_name as name1, sum(l_extendedprice) as ext
from customer, orders, lineitem, supplier, nation			  
where c_custkey = o_custkey and 
l_orderkey = o_orderkey and
l_suppkey = s_suppkey and
c_nationkey = n_nationkey and 
s_nationkey != n_nationkey and 
l_shipdate LIKE "1996%"
group by n_name),(select n_name as name2, sum(l_extendedprice) as exts
from customer, orders, lineitem, supplier, nation			  
where c_custkey = o_custkey and 
l_orderkey = o_orderkey and
l_suppkey = s_suppkey and
c_nationkey != n_nationkey and 
s_nationkey = n_nationkey and 
l_shipdate LIKE "1996%"
group by n_name)
where name1 = name2;

