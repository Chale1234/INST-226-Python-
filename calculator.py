import sys
import argparse
"""Creating Calculator class to make basic operations
    Name : Enchalew Abebe
    Course : INST 326
    Instructor: Professor Bill Farmer
    Submitted On : 11 / 05/ 2023
    exercise6

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

class Calculator():
    def add (self, x, y):
        """ adding the two given number 

        Args:
            x (_int_): x value
            y (_int_): y value

        Returns:
            _int _: return their sum
        """
        return x + y
    def subtract(self, x, y):
        """ Subtracting the two given values

        Args:
            x (_int_): The X value
            y (_int_): The y value

        Returns:
            _int_: The result of subtracting y from x 
        """
        
        return x - y

    def multiply(self, x, y):
        """ Product of the two values

        Args:
            x (_int_): The X value 
            y (_int_): The y value

        Returns:
            _int_: Return the result of x multiply by 
        """
        return x * y
    def divide( self, x, y ):
        """ Divide the two number

        Args:
            x ( int ): The x value
            y ( int): The y value

        Returns:
            int : return the result of x divided by y 
            if the y value if zero , then it raise exception and print invalid
        """
        try :
            return ( x / y)
        
        except ZeroDivisionError:
            print ("Can not divide by zero")
            

#def main():
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Accept 3 parameter from the command line")
    parser.add_argument("method", choices=["add", "subtract", "multiply", "divide"], help="Choose an operation")
    parser.add_argument("x", type = float, help = "first operand" )
    parser.add_argument("y", type = float, help = "second operand ")
    args = parser.parse_args()
    

    calculate = Calculator()
    if args.method == "add":
        value = args.x +  args.y
    elif args.method == "subtract":
        value = args.x - args.y
    elif args.method == "multiply":
        value = args.x * args.y
    elif args.method == "divide":
        try:
            value = args.x / args.y
        except ZeroDivisionError as e:
            value = f"{str(e)}: Can not be divide by zero"
        
    print(value)
    








