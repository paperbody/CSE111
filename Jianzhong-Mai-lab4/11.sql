select r_name, s_name
from nation, region, supplier
where 
n_nationkey = s_nationkey and
r_regionkey = n_regionkey
group by r_name
having Max(s_acctbal);
