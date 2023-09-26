"""
Chapter 3, Exercise 7: Seeing the World
"""
# Think of at least five places in the world you’d like to visit. 
# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order.

destinations=["Indonesia","Thailand","South Korea","Italy","Switzerland"]
print("My dream destinations that I want to visit are:")
print(destinations)

# Use sorted() to print your list in alphabetical order without modifying the actual list.

print("\nSorted order without modifications:")
print(sorted(destinations))

# Show that your list is still in its original order by printing it.

print("\nOriginal order:")
print(destinations)

# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

print("\nReverse sorted without modifications:")
print(sorted(destinations, reverse=True))

# Show that your list is still in its original order by printing it again.

print("\nOriginal order:")
print(destinations)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.

print("\nReverse order with modifications:")
destinations.reverse()
print(destinations)

# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

print("\nOriginal order:")
destinations.reverse()
print(destinations)

# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

print("\nSorted order with modifications:")
destinations.sort()
print(destinations)

# Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

print("\nReverse sorted with modifications:")
destinations.sort(reverse=True)
print(destinations)
