########################
# Assignment expressions
########################

###############################
# ## Statements and expressions
###############################

###############################
# ## Using the walrus operator
###############################
# normal way to assign a value to a variable and use that variable:
value = 10
modulus = 3
remainder = value % modulus
if remainder:
    print(f"Not divisible! The remainder is {remainder}")

# using assignment expression:
if remainder := value % modulus:
    print(f"Not divisible! The remainder is {remainder}")

# allow customers to choose a flavor:
flavors = ['pistachio', 'malaga', 'vanilla', 'chocolate', 'strawberry']
prompt = 'Choose your flavor: '
print(flavors)
while True:
    choice = input(prompt)
    if choice in flavors:
        break
    print(f"Sorry, '{choice}' is not a valid option.")
print(f"You chose '{choice}'.")

# using an assignment expression:
while (choice := input(prompt)) not in flavors:
    print(f"Sorry, '{choice}' is not a valid option.")
print(f"You chose '{choice}'")

###############################
# ## A word of warning
###############################
