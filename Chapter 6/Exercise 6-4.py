"""
Chapter 6, Exercise 4: Deli
"""
# Task: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
# As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders=["chicken sandwich","egg sandwich","grilled cheese sandwich","ham and cheese sandwich"]
finished_sandwiches=[]

# A list is created to include all the sandwich orders.
# Another list, one that is empty, is created to include sandwich orders which are finished.

while sandwich_orders:
    orders=sandwich_orders.pop() # The pop function will remove the sandwich that is being made, removing it from the list.
    print("\nYour sandwich,", orders+", is being made. Please wait a few more minutes.")
    finished_sandwiches.append(orders) # The function append will add the ordered sandwich to the finished sandwiches list.
for sandwich in finished_sandwiches:
    print("\nYour order,", orders+", is finished, please collect at the counter.") # By using the for loop, each sandwich will be printed alongside a message that states that the sandwich is finished.
    
# The difference in using a comma and plus when printing a string concatenation is that a comma will automatically add a space while a plus will not have a space.