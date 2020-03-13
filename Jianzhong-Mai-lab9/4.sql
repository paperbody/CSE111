select s_name, count(p_size)
from  part, Q2, partsupp
where s_suppkey = ps_suppkey and p_partkey = ps_partkey and  s_nation = "BRAZIL" and p_size < 20 
group by s_name;


