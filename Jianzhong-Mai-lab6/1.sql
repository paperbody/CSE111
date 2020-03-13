select strftime('%m', l_shipdate) as month, avg(l_quantity)
from lineitem
where l_shipdate >= "1996-01-01" and
l_shipdate <= "1996-12-31"
group by strftime('%m', l_shipdate);
