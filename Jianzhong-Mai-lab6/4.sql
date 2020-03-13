select count(cnt)
from(select count(s_suppkey) as cnt
from partsupp, part, nation, supplier
where s_suppkey = ps_suppkey and
p_partkey = ps_partkey and
s_nationkey = n_nationkey and
n_name = "CANADA" 
group by s_suppkey
having count(distinct(p_partkey)) > 3)

