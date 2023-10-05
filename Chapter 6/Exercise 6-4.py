"""
Chapter 6, Exercise 4: Deli
"""
# Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
# As each sandwich is made,move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders=["chicken sandwich","egg sandwich","grilled cheese sandwich","ham and cheese sandwich"]
finished_sandwiches=[]

while sandwich_orders:
    orders=sandwich_orders.pop()
    print("\nYour sandwich,", orders+", is being made. Please wait a few more minutes.")
    finished_sandwiches.append(orders)
for sandwich in finished_sandwiches:
    print("\nYour order,", orders+", is finished, please collect at the counter.")
    
# The difference in using a comma and plus when printing a string concatenation is that a comma will automatically add a space while a plus will not have a space.