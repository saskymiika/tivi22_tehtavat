"""
Tehtävä 13.1
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""


def main():
    def isValid(num):
        return (num >= 1) and (num % 2 == 0)

    valid = False
    while not valid:
        try:
            x = int(input("Enter an odd positive number: "))
            if isValid(x):
                raise ValueError('Number is not positive or an odd number.')
            else:
                valid = True

        except ValueError as except_object:
            print("{}".format(except_object))

    print("{:d} was accepted".format(x))


if __name__ == "__main__":
    main()