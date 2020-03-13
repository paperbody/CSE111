select s_name, p_size, min(ps_supplycost)
from nation, region, part, supplier, partsupp 
where n_regionkey = r_regionkey and
s_nationkey = n_nationkey and
s_suppkey = ps_suppkey and
ps_partkey = p_partkey and
r_name = "AMERICA"  and
p_type like "%steel"
group by p_size
order by s_name
