# EG8-01 Finding the largest sales

from BTCInput import *

sales1=read_int('Enter the sales for stand 1: ')
sales2=read_int('Enter the sales for stand 2: ')
sales3=read_int('Enter the sales for stand 3: ')
sales4=read_int('Enter the sales for stand 4: ')
sales5=read_int('Enter the sales for stand 5: ')
sales6=read_int('Enter the sales for stand 6: ')
sales7=read_int('Enter the sales for stand 7: ')
sales8=read_int('Enter the sales for stand 8: ')
sales9=read_int('Enter the sales for stand 9: ')
sales10=read_int('Enter the sales for stand 10: ')

if sales1>sales2 and sales1>sales3 and sales1>sales4 \
   and sales1>sales5 and sales1>sales6 and sales1>sales7 \
   and sales1>sales8 and sales1>sales9 and sales1>sales10:
   print('Stand 1 had the best sales')
