# get two integer parameters
# return sum
def plus(x, y):
    return x+y

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit, 1: plus")
        check = int(input())
        if check == 1:
            print("0: add, 1: minus, 2: multiply, 3: divide")
            num = int(input())
            if num == 0:
                print("First Number")
                a = int(input())
                print("Second Number")
                b = int(input())
                print("answer : ", plus(a,b))
            elif num == 1:
                print("First Number")
                a = int(input())
                print("Second Number")
                b = int(input())
                print("answer : ", a-b)
            elif num == 2:
                print("First Number")
                a = int(input())
                print("Second Number")
                b = int(input())
                print("answer : ", a*b)
            elif num == 3:
                print("First Number")
                a = int(input())
                print("Second Number")
                b = int(input())
                print("answer : ", a/b)
            elif num > 4:
                print("Unsupported")
        elif check > 1:
            print("Unsupported")
        else:
            print("Thank you")

if __name__ == "__main__":
    main()
