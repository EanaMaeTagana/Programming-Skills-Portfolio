"""
Chapter 5, Exercise 5: Pets
"""
# Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. 
# Next, loop through your list and as you do, print everything you know about each pet.

pets=[]

pet={
    "Kind of Animal": "Cat",
    "Owner Name": "Taylor",
    "Pet Name": "Meredith",
}
pets.append(pet)

pet={
    "Kind of Animal": "Dog",
    "Owner Name": "Joe",
    "Pet Name": "Benjamin",
}
pets.append(pet)

pet={
    "Kind of Animal": "Mouse",
    "Owner Name": "Tim",
    "Pet Name": "Mary",
}
pets.append(pet)

for pet in pets:
    print(f"\nThis information is what has been gathered about {pet['Pet Name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")