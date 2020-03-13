select count(ps_supplycost * ps_availqty)
from partsupp, supplier, nation
where s_nationkey = n_nationkey and
s_suppkey = ps_suppkey and
n_name = "CANADA" and 
ps_supplycost * ps_availqty in
(
select ps_supplycost * ps_availqty
from partsupp 
order by ps_supplycost * ps_availqty DESC 
LIMIT 
(select count(*) *0.03
from partsupp)
) 
