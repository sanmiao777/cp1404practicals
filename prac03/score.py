import random
def main():
    number = int(input("Enter the number of scores: "))
    input_file = open("results.txt", "w")


    for score in range(number):
        score = random.randint(0, 101)
        result = get_result(score)
        input_file.write(str(score))
        input_file.write(' is ')
        input_file.write(result+'\n')

        print("{} is {}".format(score,result))



def get_result(score):
    if score <= 50:
        return"Bad"
    elif score < 90:
        return"Passable"
    else:
        return"Excellent"
main()
