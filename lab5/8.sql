select count(distinct (s_name))
from supplier, partsupp, part
where p_type like "%MEDIUM POLISHED%" and
(p_size  = 3 or
p_size = 23 or
p_size = 26 or
p_size = 49) and
s_suppkey = ps_suppkey and
ps_partkey = p_partkey
