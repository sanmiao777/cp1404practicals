import random
def main():
    input_file = open("temps_input.txt","w")
    output_file = open("temps_output.txt","w")
    for fahrenheit in range(15):
        fahrenheit = random.uniform(-200,200)
        input_file.write(str(fahrenheit)+'\n')
        celsius = f_to_c(fahrenheit)
        output_file.write(str(celsius)+'\n')
    input_file.close()
    output_file.close()
def f_to_c(fahrenheit):
    return 5.0 * (fahrenheit - 32) / 9
main()
