"""
更多温度 创建一个名为的文本文件temps_input.txt，并用至少 15 个介于 -200 和 +200 之间的任何值的浮点数填充它。你从哪里得到这些数字？
当然，编写一个 Python 脚本来创建文本文件！
现在编写一个程序 ，convert_temps.py它使用您创建的函数来转换温度。
将值读取temps_input.txt为华氏值，并将转换后的摄氏值写入temps_output.txt
"""
import random
def main():
    creat_input_file(16)
    temps_input = open("temps_input.txt", "r")
    temps_output = open("temps_output.txt", "w")
    for line in temps_input:
        value = c_f(float(line))
        print(value,file=temps_output)
    temps_input.close()
    temps_output.close()


def creat_input_file(number):
    temps_file = open("temps_input.txt", "w")
    temps_c = random.uniform(-200, 200)
    i = 0
    """不能用 for i in range (number) 否则随机数将会相同"""
    while i < number:
        print(temps_c, file=temps_file)
        i += 1
        temps_c = random.uniform(-200, 200)
    temps_file.close()
def c_f(c):
    return c * 9.0 / 5 + 32
main()