def tempertaure_converter():
    print("\n Temperature Converter")
    print("Enter your choice which temperature you want to calculate : ")
    print("1. Celsius to Fahrenheit")
    print("2. Farhenheit to Celsius ")
    print("3. Celsius to Kelvin ")
    print("4. Kelvin to Celsius ")
    print("5. Kelvin to Fahrenheit ")
    print("6. Fahrenheit to Kelvin")

    choice = int(input("Enter your choice : "))


    if choice == 1:
        celsius = float(input("Enter temperature in Celsius : "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}C = {fahrenheit}F")

    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit : "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}F = {celsius}C")
    
    elif choice == 3:
        celsius = float(input("Enter temperature in Celsius : "))
        kelvin = celsius + 273.15
        print(f"{celsius}C = {kelvin}K")

    elif choice == 4:
        kelvin = float(input("Enter temperature in Kelvin : "))
        celsius = kelvin - 273.15   
        print(f"{kelvin}K = {celsius}C")

    elif choice == 5:
        kelvin = float(input("Enter temperature in Kelvin : "))
        fahrenheit = (kelvin * 9/5) - 459.67
        print(f"{kelvin}K = {fahrenheit}F")

    elif choice == 6:
        fahrenheit = float(input("Enter temperature in Fahrenheit : "))
        kelvin = (fahrenheit  + 459.67) * 5/9
        print(f"{fahrenheit}F = {kelvin}K")
    else :
        print("Invalid use choice! ")

tempertaure_converter()
