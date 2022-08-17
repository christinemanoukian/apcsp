lovely_loveseat_description = 'This is a wonderful loveseat with vegan stuffing and a nice vegan leather. It is brown.'
lovely_loveseat_price = 572

lovely_armchair_description = 'This is a nice small armchair fir for studio apartments. It is blue.'
lovely_armchair_price = 30

lovely_table_description = 'This is a nice table made of oak and walnut. It seats 6.'
lovely_table_price = 300

sales_tax = .0825

customer_total = 0
customer_itemization = '' 

item = input('Do you want a loveseat, an armchair, or a table? ')
if item == 'loveseat':
    customer_total += lovely_loveseat_price
    customer_itemization += lovely_loveseat_description
if item == 'armchair':
    customer_total += lovely_armchair_price
    customer_itemization += lovely_armchair_description
if item == 'table':
    customer_total += lovely_table_price
    customer_itemization += lovely_table_description

customer_total += customer_total*sales_tax

print('Your total is ' + str(customer_total))
print('Here is the breakdown: ' + customer_itemization)
