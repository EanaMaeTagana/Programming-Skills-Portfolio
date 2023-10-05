"""
Chapter 6, Exercise 5: No Pastrami
"""
# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders=["chicken sandwich","pastrami sandwich","pastrami sandwich","egg sandwich","grilled cheese sandwich","pastrami sandwich","ham and cheese sandwich"]
finished_sandwiches=[]

print("Attention all valued customers, unfortunately, the deli has run out of pastrami sandwiches. Thank you for your cooperation.")

while "pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("pastrami sandwich")
    
while sandwich_orders:
    orders=sandwich_orders.pop()
    print("\nYour sandwich,", orders+", is being made. Please wait a few more minutes.")
    finished_sandwiches.append(orders)
for sandwich in finished_sandwiches:
    print("\nYour order,", orders+", is finished, please collect at the counter.")
    