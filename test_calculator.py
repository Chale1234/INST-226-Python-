from  calculator import Calculator as calculate
import math

"""Creating test_calculate function to test Calculator class. 
    It covers various scenarios
    Name : Enchalew Abebe
    Course : INST 326
    Instructor: Professor Bill Farmer
    Submitted On : 11/ 05 / 2023
    exercise6

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """


def test_add():
    """Testify both normal and edge cases by adding x and y with various value and scenario.
    """

    assert calculate.add(3, 10, 15) == 25
    assert calculate.add(3, -5, -5) ==-10
    assert calculate.add(3, -5, 0) == -5
    assert calculate.add(3, 5, 0) == 5
    assert calculate.add(3, -8, 3) == -5
    assert calculate.add(3, 9, -5) == 4
    assert math.isclose(calculate.add(3, 3.24, 3.4), 6.64)
    assert calculate.add(3, 1200, 560000) == 561200
    assert calculate.add(3, -1000000, -10000000) == -11000000
    
    
def test_subtract():
    """
    
    Testify both normal and edge cases by subtracting y from x with different value and scenario.
    """
    assert calculate.subtract(3, -5, -5) == 0
    assert calculate.subtract(3, -5, 8) == -13
    assert calculate.subtract(3, 20000000, 3) == 19999997
    assert calculate.subtract(3, 9, -5) == 14
    assert calculate.subtract(3, 1958674, 0) == 1958674
    assert calculate.subtract(3, 0,   17584) == -17584
    assert math.isclose(4.6, calculate.subtract(3, 15.3, 10.7))
    
def test_multiply():
    """ Testify both normal and edge cases by multiply x by y with various scenario.
    """
    assert calculate.multiply(3, 100, 100) == 10000
    assert calculate.multiply(3, -5, -5) == 25
    assert calculate.multiply(3, -5, 8) == -40
    assert calculate.multiply(3, 100, -2) ==-200
    assert calculate.multiply(3, 0, 1000000000) == 0
    assert calculate.multiply(3, 5, 0) == 0
    assert calculate.multiply(3, 1000000, 1000000) == 1000000000000
    assert calculate.multiply(3, 3.4, 3.5) == 11.9

    
    
    
def test_division_by_zero():
    """It handles division by zero gracefully and 
    if the value of y is equal 
    to zero then it raise zero division error
    """
    try:
        x = 0
        y = 0
        x / y
        #calculate.divide(5, 0)
    except ZeroDivisionError as e:
        f"{str(e)}: Can not divide by zero"
def test_divide():
    """ Testify both normal and edge cases by dividing x by y 
    
    
    """
    assert calculate.divide(3, 4, 10) == 0.4
    assert calculate.divide(3, -5, -5) == 1
    assert calculate.divide(3, -50, 10) == -5
    assert calculate.divide(3, 15, -5) == -3
    assert calculate.divide(3, 0, 3) == 0
    assert calculate.divide(3, 1000000, 10) == 100000
    assert math.isclose( 2.5, calculate.divide(3, 5.0, 2))
    assert calculate.divide(3, 5, 0) !=0

    

