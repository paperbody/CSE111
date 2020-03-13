select count(cnt)
from(select count(p_partkey) as cnt
from partsupp, part, nation, supplier
where s_suppkey = ps_suppkey and
p_partkey = ps_partkey and
s_nationkey = n_nationkey and
n_name = "CANADA" 
group by p_partkey
having count(p_partkey) > 1);

