cost_price = int(input())
repair_cost = int(input())
selling_price = int(input())

total_cost = cost_price + repair_cost
gain = selling_price - total_cost
gain_percentage = (gain / total_cost) * 100

print("{:.2f}".format(gain_percentage))