# temperature_converter.py
# This program converts temperature in Celsius to Fahrenheit.
# It asked for a number, checks if it is valid, 
# then converts it to Fahrenheit.
# Formula: F = (C * 9/5) + 32


while True:  # asks until the user types a valid number
    text = input("Enter the temperature in Celsius: ").strip()
 
    # check if the user typed something
    if len(text) == 0:
        print("You must type something. Try again.")
    else:
        # If the user typed a number with a "C" at the end, remove it
        if text.upper().endswith("C"):
            text = text.upper().replace("C", "")
 
        try:
            celsius = float(text)  # fails if the text is not a number
            if celsius < -273.15:
                print("That is below absolute zero. Try again.")
            else:
                break
        except ValueError:
            # runs when it can't convert the text to a number
            print("That wasn't a number. Try again.")

# formula for conversion  
fahrenheit = (celsius * 9 / 5) + 32
 
# show the result to the user
unit_c = "c"
unit_f = "f"
print(str(celsius) + " C = " + str(round(fahrenheit, 1)) + " F")