select max((l_extendedprice * (1 - l_discount)))
from lineitem
where julianday(1994-10-02) <l_shipdate 
