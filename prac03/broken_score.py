
def main():
    score = int(input("Enter the score: "))
    result = get_result(score)
    print("{} is {}".format(score,result))

def get_result(score):
    if score <= 50:
        return"Bad"
    elif score < 90:
        return"Passable"
    else:
        return"Excellent"
main()

