select n_name
from  nation,customer
where c_nationkey = n_nationkey
group by n_name 
having count(*) =(select max(cnt) 
from (select count(c_name) as cnt
from customer, nation
where c_nationkey = n_nationkey
group by n_name
));
