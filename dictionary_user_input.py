"""responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("which mountain would you like to climb someday? ")

    responses[name] = response
    repeat = input("would you like to let another person respond? (yes/ no)")
    if repeat == "no":
        polling_active = False

print("\n---Poll Result---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")"""

responses = {}
polling_active = True

while polling_active:
    name = input("\n What is your name? : ")
    response = input("which mountain would you like to climb somebody?: ")
    responses[name] = response
    repeat = input("would you like to let another person respond? (yes/ no)")
    if repeat == "no":
        polling_active = False
print("\n-----poking result")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
