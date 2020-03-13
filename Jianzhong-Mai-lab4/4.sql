select s_name, count(p_size)
from nation, region, part, supplier, partsupp
where n_regionkey = r_regionkey  and s_suppkey = ps_suppkey and p_partkey = ps_partkey and n_nationkey = s_nationkey and n_name = "BRAZIL" and p_size < 20 
group by s_name;

