"""
Chapter 3, Exercise 5: Change Guest List
"""
# Task: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4.
# Add a print() call at the end of your program stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

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

# The invitations are printed again individually, now with the new guest added.
