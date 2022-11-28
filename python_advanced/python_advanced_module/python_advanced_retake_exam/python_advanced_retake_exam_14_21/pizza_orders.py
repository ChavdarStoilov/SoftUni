from collections import deque

pizza_orders = deque([int(order) for order in input().split(', ')])
emp_capacities = [int(emp) for emp in input().split(', ')]

pizza_made = 0

while pizza_orders and emp_capacities:

    current_order = pizza_orders[0]
    current_emp = emp_capacities[-1]

    if current_order > 10:
        pizza_orders.popleft()
        continue
    elif 0 >= current_order:
        pizza_orders.popleft()
        continue

    else:

        if current_emp >= current_order:
            pizza_made += pizza_orders.popleft()
            emp_capacities.pop()
        elif current_order > current_emp:
            pizza_made += emp_capacities[-1]
            pizza_orders[0] -= emp_capacities.pop()

if pizza_orders and not emp_capacities:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join([str(orders) for orders in pizza_orders])}')

else:
    print(f'All orders are successfully completed!\nTotal pizzas made: {pizza_made}')
    print(f'Employees: {", ".join([str(employee) for employee in emp_capacities])}')