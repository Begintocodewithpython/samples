# EG8-22 Tables of sales data

mon_sales=[50,54,29,33,22,100,45,54,89,75]
tue_sales=[80,98,40,43,43,80,50,60,79,30]
wed_sales=[10,7,80,43,48,82,33,55,83,80]
thu_sales=[15,20,38,10,36,50,20,26,45,20]
fri_sales=[20,25,47,18,56,70,30,36,65,28]
sat_sales=[122,140,245,128,156,163,90,140,150,128]
sun_sales=[100,130,234,114,138,156,107,132,134,148]

week_sales=[mon_sales,tue_sales,wed_sales,thu_sales,fri_sales,sat_sales,sun_sales]

total_sales=0
for day_sales in week_sales:
    for sales_value in day_sales:
        total_sales=total_sales+sales_value

print('Total sales for the week are',total_sales)




