def area_of_circle(pi, radius):
    return pi * (radius ** 2)

def total_due(money, tax_rate_percent):
    return money + (money * tax_rate_percent) / 100

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print("Area of Circle Calculation")
radius = int(input("Enter radius: "))
pi = 3.1416
area = area_of_circle(pi, radius)
print("Area of the circle:", area)

print("\nTotal Due Calculation")
money = int(input("Enter money amount: "))
tax_rate = int(input("Enter tax rate as whole number: "))
total = total_due(money, tax_rate)
print("Total due:", total)

print("\nFahrenheit to Celsius Conversion")
fahrenheit = int(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print("Temperature in Celsius:", celsius)