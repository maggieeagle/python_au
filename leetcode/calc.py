import sys

def calculate(num1, num2, operation):
    calc = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2,
    }
    return cals(operation)

def main(num1, num2, operation):
    print(calculate(num1, num2, operation)

if __name__ == '__main__':
    params = sys.argv
    main(float(params[1]), float(params[2]), params[3])