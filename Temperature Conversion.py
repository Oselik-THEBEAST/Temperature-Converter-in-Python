print("Welcome to the temperature conversion tool")

system_from = input("Enter the system you want to convert from (C,F,K): ")

if system_from == "C":
    system_to = input("Enter which system you want to convert to (F/K): ")
    if system_to == "F":
        temperature = float(input("Enter the temperature in Celsius: "))
        print(f'{temperature} in Celsius = {((temperature * 2) + 30):.2f} in Fahrenheit')
    elif system_to == "K":
        temperature = float(input("Enter the temperature in Celsius: "))
        print(f'{temperature} in Celsius = {(temperature + 273.15):.2f} in Kelvin')
    else:
        print("Invalid Information. Choose from F or K")
elif system_from == "F":
    system_to = input("Enter which system you want to convert to (C/K): ")
    if system_to == "C":
        temperature = float(input("Enter the temperature in Fahrenheit: "))
        print(f'{temperature} in Fahrenheit = {((temperature - 30) / 2):.2f} in Celsius')
    elif system_to == "K":
        temperature = float(input("Enter the temperature in Fahrenheit: "))
        print(f'{temperature} in Fahrenheit = {((temperature - 32) / 1.8 + 273.15):.2f} in Kelvin')
    else:
        print("Invalid Information. Choose from C or K")
elif system_from == "K":
    system_to = input("Enter which system you want to convert to (C/F): ")
    if system_to == "C":
        temperature = float(input("Enter the temperature in Kelvin: "))
        print(f'{temperature} in Kelvin = {(temperature - 273.15):.2f} in Celsius')
    elif system_to == "F":
        temperature = float(input("Enter the temperature in Celsius: "))
        print(f'{temperature} in Kelvin = {((temperature - 273.15) * 1.8 + 32):.2f} in Fahrenheit')
    else:
        print("Invalid Information. Choose from C or F")
else:
    print("Invalid Information. Please choose from C , F or K")