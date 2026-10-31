a=True
j=0
while a==True:

        def add(num1, num2):
            return num1 + num2

        def multiply(num1, num2):
            return num1 * num2

        def divide(num1, num2):
            return num1 / num2

        def subtract(num1, num2):
            return num1 - num2




        if j>0:
            h = input("Type y for old and n for new").lower()
            if h=="y":
                n1 = output
                n2 = int(input("Enter the number 2:"))

            else:
                n1 = int(input("Enter the number 1:"))
                n2 = int(input("Enter the number 2:"))


        else:
            n1 = int(input("Enter the number 1:"))
            n2 = int(input("Enter the number 2:"))
            j+=1

        k = input("""Enter the operation you want to perform
        '+'
        '/'
        '*'
        '-'""")
        if k == "+":
            output = add(num1=n1, num2=n2)
            print(output)
        elif k == "*":
            output = multiply(num1=n1, num2=n2)
            print(output)
        elif k == "/":
            output = divide(num1=n1, num2=n2)
            print(output)
        elif k == "-":
            output = subtract(num1=n1, num2=n2)
            print(output)
