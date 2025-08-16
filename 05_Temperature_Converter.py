#Temperature converter (Using return function)

#Step-1: Define conversion functions
def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32
def celcius_to_kelvin(celcius):
    return celcius + 273.15
def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15
def kelvin_to_celcius(kelvin):
    return kelvin - 273.15
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

#Step-2: Display the menu
def show_menu():
    print("\n---Temperature converter menu---")
    print("1.Celcius to fahrenheit and kelvin")
    print("2.Fahrenheit to celcius and kelvin")
    print("3.Kelvin to celcius and fahrenheit")
    print("4.Exit")

#Step-3: Main program loop

while True:
    show_menu()
    choice = input("Enter your choice(1/2/3/4):")

    if choice == "1":
        celcius = float(input("Enter temperature in celcius :"))
        print(f"Fahrenheit: {celcius_to_fahrenheit(celcius):.2f} F")
        print(f"Kelvin: {celcius_to_kelvin(celcius):.2f} K")
    elif choice == "2":
        fahrenheit = float(input("Enter the temperature in Fahrenheit :"))   
        print(f"Celcius: {fahrenheit_to_celcius(fahrenheit): .2f} C")
        print(f"Kelvin: {fahrenheit_to_kelvin(fahrenheit):.2f} K")
    elif choice == "3":
        kelvin = float(input("Enter the temperature in kelvin :"))   
        print(f"Celcius: {kelvin_to_celcius(kelvin):.2f} C")
        print(f"Fahrenheit: {kelvin_to_fahrenheit(kelvin):.2f} F")
    elif choice == "4":
        print("Exiting the program. Thank you!")
    else :
        print("Invalid choice entered please enter a valid choice.")              
