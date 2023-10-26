"""
Chapter 6, Exercise 5: No Pastrami
"""
# Task: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders=["chicken sandwich","pastrami sandwich","pastrami sandwich","egg sandwich","grilled cheese sandwich","pastrami sandwich","ham and cheese sandwich"]
finished_sandwiches=[]

# A list is created to include all the sandwich ordersm including three pastrami sandiwches.
# Another list, one that is empty, is created to include sandwich orders which are finished.

print("Attention all valued customers, unfortunately, the deli has run out of pastrami sandwiches. Thank you for your cooperation.")

while "pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("pastrami sandwich") # The remove function will now remove all pastrami sandwich orders from the list.
    
while sandwich_orders:
    orders=sandwich_orders.pop() # The pop function will remove the sandwich that is being made, removing it from the list.
    print("\nYour sandwich,", orders+", is being made. Please wait a few more minutes.")
    finished_sandwiches.append(orders) # The function append will add the ordered sandwich to the finished sandwiches list.
for sandwich in finished_sandwiches:
    print("\nYour order,", orders+", is finished, please collect at the counter.") # By using the for loop, each sandwich will be printed alongside a message that states that the sandwich is finished.
    
print("\nThe finished sandwiches include:", finished_sandwiches) # To ensure that no pastrami sandwiches are in the finished sandwiches list.
    