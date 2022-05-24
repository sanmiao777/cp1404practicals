def main():
    temperature = float(input("Enter the  temperature : "))
    print("Temperature in 'Celsius' or 'Fahrenheit'")
    choose = input("C or F:").upper()
    if choose == "C":

        fahrenheit = c_to_f(temperature)
        print(fahrenheit)
    elif choose =="F":
        celsius = f_to_c(temperature)
        print(celsius)
    else:
        print("Invalid command")



def c_to_f(temperature):
    return temperature * 9.0 / 5 + 32

def f_to_c(temperature):
    return 5.0 * (temperature - 32) / 9
main()