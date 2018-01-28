error = "I don't understand."

print("Welcome to Westworld!")

answer = input("Do you watch it or do something better with your time? watch/live \n")
if answer == "watch":
    print("Baaad choice...")
elif answer == "live":
    print("Good idea. Do something better with your time.")
else:
    print(error)
