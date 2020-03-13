select s_region, s_name
from Q2
group by s_region
having Max(s_acctbal);

