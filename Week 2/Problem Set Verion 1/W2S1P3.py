"""
A dictionary ticket_sales is used to map ticket type to number of tickets sold. 
Return the total number of tickets of all types sold.

def total_sales(ticket_sales):
    pass
    
Example Usage:
ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))

Example Output:
4500

UNDERSTAND:
input: dictionary
output: int (sum of the values)

PLAN:
1. initialize an integer total as 0
1.1 loop through the dictionary's values 
    1.2 update the sum by adding the value
2. return sum    

"""
#IMPLEMENT

def total_sales(ticket_sales):
    total = 0
    for sales in ticket_sales.values():
        total += sales
    return total    


ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
print(total_sales(ticket_sales))