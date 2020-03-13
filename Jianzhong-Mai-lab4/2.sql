select n_name, count(s_name)
from nation, region, supplier
where n_regionkey = r_regionkey and n_nationkey = s_nationkey
group by n_name
