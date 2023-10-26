"""
Chapter 3, Exercise 6: Shrinking Guest List
"""
# Task: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
# Start with your program from Exercise 3-5. 
# Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. 
# Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. 
# Print your list to make sure you actually have an empty list at the end of your program.  
# Print your list to make sure you actually have an empty list at the end of your program.

guest_list=["Taylor Swift","Elizabeth Schuyler","Annalise Keating","Amy March"]

# A variable named guest_list is given a list of guests.

print("Invitations:")
print("\tGood evening! "+guest_list[0]+", please join us over dinner soon.")
print("\tGood evening! "+guest_list[1]+", please join us over dinner soon.")
print("\tGood evening! "+guest_list[2]+", please join us over dinner soon.")
print("\tGood evening! "+guest_list[3]+", please join us over dinner soon.")

# Each person, through the list index, is then printed with a message inviting them for dinner.

print('\n"Hello! This is '+guest_list[2]+'. Unfortunately, I will not be able to join you for dinner as I am very busy as of the moment."')
del(guest_list[2])

guest_list.insert(2,"Florence Pugh")
print("\nFortunately, "+guest_list[2]+" said that she is available to come for dinner any time.")

# By using the delete function, one person from the guest list is removed.
# By using insert, the guest who is unable to come is replaced by a new guest.

print("\nInvitations:")
print("\tHello, "+guest_list[0]+". It would be a pleasure to have you over for dinner soon.")
print("\tHello, "+guest_list[1]+". It would be a pleasure to have you over for dinner soon.")
print("\tHello, "+guest_list[2]+". It would be a pleasure to have you over for dinner soon.")
print("\tHello, "+guest_list[3]+". It would be a pleasure to have you over for dinner soon.")
# Current guest list: Taylor Swift, Elizabeth Schuyler, Florence Pugh, Amy March

print("\nIt seems that you only have space for two guests.")

guest_list.pop(-2)
message=("\n\tHi! Sorry Florence, but we can only have two people over for dinner at this time. Join us next time!")
print(message)

guest_list.pop(1)
message=("\tHi! Sorry Elizabeth, but we can only have two people over for dinner at this time. Join us next time!")
print(message)

# By using the pop function, two guests are removed from the guest list.

print("\n\tHello, "+guest_list[0]+". Just wanted to inform you that you are still invited for dinner. See you soon!")
print("\tHello, "+guest_list[1]+". Just wanted to inform you that you are still invited for dinner. See you soon!")  

del(guest_list[0])
del(guest_list[-1])

# Del function is used to delete the remaining names on the guest list.

print(guest_list)