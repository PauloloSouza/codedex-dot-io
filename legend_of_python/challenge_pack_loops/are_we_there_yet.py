#Are We There Yet?

answer = input("Are we there yet? ").upper() #Not exercise requirement
while answer != "YES":
    answer = input("Are we there yet? ").upper() #.upper() added to accept upper and lower case letters
    if answer == "YES":
        print("WE MADE IT!")
