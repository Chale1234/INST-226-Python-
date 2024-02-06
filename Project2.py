""" This program write battery, motor, robot, and servicerobot class.

Author: Enchalew Abebe
Assignment: Homework #2 INST326
Due Date: 11/ 14/2023

I pledge on my honor that I have not given or 
received any unauthorized assistance on this assignment. 

    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
from abc import ABC, abstractmethod
import random
import string
import argparse
import sys
class Battery():
    battery_rules = {"nuclear":10000,"lithium_ion":200,"lithium_polymer":175,"nickel_hydride":150,"lead_acid":100}
    def __init__(self, battery_id, battery_type):
        """ Initialization parameters
        Args: 
        battery_id(str) : A unique indicator for the battery
        battery_type(str): battery type
        battery_level(float):the level of the battery
        """

        self._battery_id = battery_id
        if battery_type in self.battery_rules: #["nuclear", "lithium_ion", "lithium_polymer", "nickel_hydride", "lead_acid"]:
            self._battery_type = battery_type    
        else:
                self._battery_type =None
                self._max_battery_level = None
        self._battery_level = 0.0
        if self._battery_type == 'lithium_ion':
            self._battery_level = min(self._battery_level, 200.0)
        elif self._battery_type == 'nickel_hydride':
            self._battery_level = min(self._battery_level, 150.0)
        elif self._battery_type == 'lithium_polymer':
            self._battery_level = min(self._battery_level, 175.0)
        elif self._battery_type == 'nuclear':
            self._battery_level = min(self._battery_level, 10000.0)
        elif self._battery_type =="lead Acid":
            self._battery_level= min(self._battery_level, 100.0)
        else :
            None
        
    
    @property
    def battery_id(self):
        """Get the battery id

        Returns:
            _Str_: The id number of the battery
        """
        return self._battery_id
    @battery_id.setter
    def battery_id(self, battery_id):
        """Set the id of the battery

        Args:
            battery_id (_str_): The id number of the battery
        """
        self._battery_id = battery_id
        
    @property
    def battery_type(self):
        """Get the battery type of the vehicle

        Returns:
            _str_: The battery type of the car
        """
        return self._battery_type
    @battery_type.setter
    def battery_type(self, battery_type):
        """ set The battery type of the car 

        Args:
            battery_type (_str_): The battery type of the car 
        """
        self._battery_type = battery_type
        
    @property
    def battery_level(self):
        """Get the battery level of the car

        Returns:
            _float_: The batter level of the car 
        """
        return self._battery_level
    @battery_level.setter
    def battery_level(self, battery_level):
        """Set the battery level of the car 

        Args:
            battery_level (_float_): The battery level of the car
        """
        self._battery_level = battery_level
        
    def charge_battery(self, amount):
        """Create method named charge battery that takes one parameter 

        Args:
            amount (_float_): The amount of that battery charge
        """
        if self._battery_type == "lithium_ion":
            self._battery_level = min(self._battery_level + amount, 200)
        elif self._battery_type == "lithium_polymer":
            self._battery_level = min(self._battery_level + amount, 175)
        elif self._battery_type == "nickel_hydride":
            self._battery_level = min(self._battery_level + amount, 150)
        elif self._battery_type == "lead_acid":
            self._battery_level = min(self._battery_level + amount, 100)
        elif self._battery_type == "nuclear":
            self._battery_level = min(self._battery_level + amount, 10000)
        else:
            self._battery_level = None
        #self._battery_level = min(self._battery_level + amount, self._max_battery_level)
        
    def consume_battery(self, amount):
        """Create a consume battery method that takes one parameter 

        Args:
            amount (_float _): The amount the battery consumed 
        """
        if(self._battery_level - amount) <= 0:
            self._battery_level = 0
        else:
            self._battery_level -= amount
    
    
    def __str__(self):
        return f"battery_id ( {self._battery_id} ) battery_type ( {self._battery_type} ) battery_level ( {self._battery_level} )"
        
class Motor:
    motor_types = ["dc_motor", "stepper_motor", "servo_motor"]
    def __init__(self, motor_id, motor_type, current_rating, speed):
        """Initialization parameters for motor class

        Args:
            motor_id (_str_): a unique indicator for the motor
            motor_type (_str_): The motor type of the car
            current_rating (_float_): Rating value of the car 
            speed (_int_): The speed of the car 
        """
        
        self._motor_id = motor_id
            
        if motor_type in self.motor_types:
            self._motor_type = motor_type #"""if motor_type in("dc_motor","stepper_motor","servo_motor")"""
        else:
            None
        self._current_rating = current_rating if current_rating > 0 and current_rating <=5 else None
        self._speed = speed if speed > 0 and speed <=5 else None
        self._state = 0
        
    @property
    def motor_id(self):
        """Get the motor id

        Returns:
            _str_: The Motor id of the car
        """
        return self._motor_id
    @motor_id.setter
    def motor_id( self, motor_id):
        """Set the motor id of the car

        Args:
            motor_id (_str_): The motor id of the car 
        """
        self._motor_id = motor_id
    
    @property
    def motor_type(self):
        """Get the motor type of the car 

        Returns:
            _str_: The motor type of the car 
        """
        return self._motor_type
    @motor_type.setter
    def motor_type( self, motor_type):
        """Set the motor type of the car 

        Args:
            motor_type (_str_): The motor type of the car 
        """
        self._motor_type = motor_type
        
    @property
    def current_rating(self):
        """Get the current rate 

        Returns:
            _float_: The current rate of the car 
        """
        return self._current_rating
    @current_rating.setter
    def current_rating( self, current_rating):
        """Set the current rate of the car 

        Args:
            current_rating (_float_): The current rate of the car
        """
        self._current_rating = current_rating
        
    @property
    def speed(self):
        """Get the speed of the car 

        Returns:
            _int_: The speed of the car 
        """
        return self._speed
    @speed.setter
    def speed( self, speed):
        """Set the speed of the car

        Args:
            speed (_int_): The speed of the car 
        """
        self._speed= speed
        
    @property
    def state(self):
        """Get the state of the car 

        Returns:
            _int_: The state of the car 
        """
        return self._state
    @state.setter
    def state( self, state):
        """Set the state of the car 

        Args:
            state (_int_): The state of the car 
        """
        self._state= state
        
    def start_motor(self):
        """Set the stat of the motor to one
        """
        self._state = 1
    def stop_motor(self):
        """Set the state odf the motor to one
        """
        self._state = 0
    def step_consumption_cost(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        match self._motor_type:
            case "dc_motor":
                return 3
            case "stepper_motor":
                return 2
            case "servo_motor":
                return 1
            case _:
                print("No motor type set!")
                return 0
    def __str__(self):
        return f"motor_id ( {self._motor_id} ) motor_type ( {self._motor_type} ) current_rating ( {self._current_rating} ) speed ( {self._speed} ) state ( {self._state})"
        
        
class Item:
    item_types =  ["cube","cylinder","cone","sphere","pyramid"]
    def __init__(self, item_type, color):
        """initialization parameter for the item class 

        Args:
            item_type (_str_): The item type 
            color (_type_): color value
        """
        if item_type in self.item_types: #["cube","cylinder","cone","sphere","pyramid"]
            self._item_type = item_type 
        else:
            None
        self._color = color
    
    @property
    def item_type(self):
        """Get the value of item type

        Returns:
            _str _: the item type 
        """
        return self._item_type
    
    @item_type.setter
    def item_type(self, item_type):
        """Set the item type 

        Args:
            item_type (_str_): The item type 
        """
        self._item_type = item_type
        
    @property
    def color(self):
        """Get  the color of the robot

        Returns:
            _str_: The color of the robot
        """
        return self._color
    @color.setter
    def color(self, color):
        """Set the color of the robot

        Args:
            color (_str_): The color of the robot
        """
        self._color = color


class Robot(ABC):
    def __init__(self, robot_id, battery, motor, x_pos=0, y_pos=0):
        """ Initialize a Robot object

        Args:
            robot_id (str): Identifier of the Robot
            battery (str): The Battery of the Robot
            motor (str): The Motor of the robot must be either brushless_dc or Brushed_dc 
            x_pos (int): The X position of the robot. Defaults to 0.
            y_pos (int): The Yposition of the robot. Defaults to 0.
        """
        self._robot_id = robot_id
        self._battery = battery #if battery in ['lithium_ion', 'lithium_polymer', 'nickel_metal_hydride', 'nuclear'] else None
        self._motor = motor #motor = 'brushed_dc' or 'brushless_dc': 
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._items = []
            
            
    @property        
    def robot_id(self):
        return self._robot_id
        """ Return the robot_id
        
        """
    @robot_id.setter
    def robot_id(self, robot_id):
        """ set the Robot_id

        Args:
            robot_id (str): identifier for the robot
        """
        self._robot_id = robot_id
    @property
    def battery(self):
        """ Get the type of battery

        Returns:
            str: return the type of battery
        """
        return self._battery
    @battery.setter
    def battery(self, new_battery):
        """ Set the type of battery

        Args:
            battery (str): set the type of the battery
        """
        self._battery = new_battery
        
    @property
    def motor(self):
        """Get the motor 

        Returns:
            _str_: Returns motor
        """
        return self._motor
    @motor.setter
    def motor(self, new_motor):
        """Set the motor

        Args:
            motor (str): set the value of motor
        """
        self._motor = new_motor
        
    @property
    def x_pos(self):
        """ Get the x_position

        Returns:
            _int_: return the x_position 
        """
        return self._x_pos
    @x_pos.setter
    def x_pos(self, x_pos):
        """Set the x position

        Args:
            x_pos (_int_): set the value of the x position
        """
        self._x_pos = x_pos
        
    @property
    def y_pos(self):
        """Get the y position

        Returns:
            _int_: return the x_position 
        """
        return self._y_pos
    
    @y_pos.setter
    def y_pos(self, y_pos):
        """Set the y-Position

        Args:
            y_pos (_int_): set the value of the y-position
        """
        self._y_pos = y_pos
    @property  
    def items(self):
        """Get the item

        Returns:
            _dict_: contain the items that are collected and the
number of each.
        """
        return self._items
    @items.setter
    def set_items(self, new_items):
        """Set items in the dictionary

        Args:
            items (_dict_): set items that are collected each time
        """
        self._items = new_items
    @property
    def get_battery_level(self):
        
        """Get the battery_level 

        Returns:
            _float_: Return the _battery_level
        """
        return self._battery_level
    
    def get_battery_level(self, battery_level):
        
        """Set battery_level to battery_level
        
        Args:
            battery_level(float): Set the battery_level of the robot
        """
        self._battery_level = battery_level
    
    def set_battery_level(self):
        """Parameters: None

        Returns:
            _int_: Return the battery level
        """
        return self._battery.battery_level
    
    
    def move_forward(self, amount):
        """Move the robot forward
        Args:
        amount <int>:  the amount moved 
        If battery_level > 0
        Decrease battery level by motor.step_consumption_cost
        Add 1 to y_pos
        """
        #for move in range(0, move):
            
                #self.y_pos += 1
                #self._engine.consume_fuel(1)
            
        for moves in range(0, amount):
            if self.get_battery_level() > 0:
                self._battery.consume_battery(self._motor.step_consumption_cost())
                self._y_pos += 1
            #  self._battery.consume_battery(1.0)
            #self._battery.battery_level -= 1
            #self.motor.step_consumption_cost
        
        
            
        
        
        #if self._battery.battery_level > 0:
        #self._battery.battery_level -= 1
        #  self._y_pos += 1

    def move_backward(self, amount):
        """Move the robot backward
        Args:
        amount <int>:  The amount moved 
        If battery_level > 0
        Decrease battery level by motor.step_consumption_cost
        Subtract 1 from y_pos
        """
        for moves in range(0, amount):
            if self.get_battery_level() > 0:
                self._battery.consume_battery(self._motor.step_consumption_cost())
                #self._battery.battery_level -= 1
                self._y_pos -= 1
                #self._battery.consume_battery(1.0)
            
            #self._battery.consume_battery(self._motor.step_consumption_cost())
            
        
        #if self._battery.battery_level > 0:
        #   
        #   self._y_pos -= 1

    def move_right(self, amount):
        
        """Move the robot right
        Args: 
        amount < int> : The amount moved 
            If battery_level > 0
            Decrease battery level by motor.step_consumption_cost
            Add 1 to x_pos
        """
        for moves in range(0, amount):
            
            if self.get_battery_level() > 0:
                self._battery.consume_battery(self._motor.step_consumption_cost())
                #self._battery.battery_level -= 1
                self._x_pos += 1
                #self._battery.consume_battery(1.0)
            
            #self._motor.step_consumption_cost()
            #self._battery.consume_battery(self._motor.step_consumption_cost())
        
            
            
        #if self._battery.battery_level > 0:
        #    self._battery.battery_level -= 1
        #    self._x_pos += 1
            

    def move_left(self, amount):
        
        """Move the robot right
        Args: 
        amount <int > The amount moved   
            If battery_level > 0
            Decrease battery level by motor step_consumption _cost
            Subtract 1 from x_pos
        """
        for moves in range(0, amount):
            
            if self.get_battery_level() > 0:
                self._battery.consume_battery(self._motor.step_consumption_cost())
                #self._battery.battery_level -= 1
                self._x_pos -= 1
                #self._battery.consume_battery(1.0)
            
            
        #if self._battery.battery_level > 0:
        
        #    self._x_pos -= 1
        #if self._motor.step_consumption_cost() <= self._battery.battery_level:
            #    self._battery.consume_battery(self._motor.step_consumption_cost())
            #return self._battery_level - self._motor.step_consumption_cost()
            
    @abstractmethod
    def collect_item(self, item):
        """ Check if item in items dictionary

        Args:
            item (_str_): If item is already in dictionary then add items to items in the
                        dictionary and increment the counter in the dictionary
                        If item is not in dictionary then add it to the dictionary
        """
    
        """if item in self._items:
            self._items[item] += 1
        else:
            self._items[item] = 1"""
        pass
            
    @abstractmethod
    def drop_item(self, item):
        """ check to see if item already
            exists prior to removing it.

        Args:
            item (str): Remove one item from dictionary at a time
        """
    
        """if  item in self._items:
            if self._items[item] > 1:
                self._items[item] -= 1
        else:
            del self._items[item]"""
        pass
            
    
    
    @abstractmethod
    def print_items(self):
        """Print all of the items that the robot currently has
        for item, count in self._items.items():
            print(f"{count} {item}")"""
        pass

    def charge_battery(self, amount):
        """ Add amount to battery_level

        Args:
            amount (_float_): Add Amount to battery_level 
            after checking that the battery level does not 
            exceed the maximum for the battery type
        """
        
        self._battery.charge_battery(amount)
        
        #if self._battery == 'lithium_ion':
        #   self._battery_level = min(self._battery_level, 100.0)
        #elif self._battery == 'nickel_metal_hydride':
        #self._battery_level = min(self._battery_level, 100.0)
        #elif self._battery == 'lithium_polymer':
        #    self._battery_level = min(self._battery_level, 100.0)
        #elif self._battery == 'nuclear':
        #    self._battery_level = min(self._battery_level, 10000.0)
            
            
    def get_battery_level(self):
        """Parameters: None

        Returns:
            _int_: Return the battery level
        """
        return self._battery.battery_level

    def get_position(self):
        """Parameters: None


        Returns:
            _int_: Return a tuple of x and y positions in that order
        """
    
        return (self._x_pos, self._y_pos)

    def reset_position(self):
        """Parameters: None
            Set x_pos and y_pos to Zero (0
        """

        self._x_pos = 0
        self._y_pos = 0

    def __str__(self):
        return f"Robot_id: {self._robot_id} \n\tbattery: {self._battery} \n\tmotor: {self._motor}" \
        f" \n\tx_pos: {self._x_pos} y_pos: {self._y_pos}"

    def __repr__(self):
        return f"Robot_id: {self._robot_id} battery: {self._battery} motor: {self._motor}" \
        f" x_pos: {self._x_pos} y_pos: {self._y_pos}" 
        
class ServiceRobot(Robot):
    def __init__(self, robot_id, battery, motor, x_pos =0, y_pos =0):
        super().__init__(robot_id, battery, motor, x_pos, y_pos)
        """initialization parameter 
        Args:
        robot_id--str_
        battery_ The battery of the service robot
        motor_ The motor of the service robot
        x_pos- default to zero
        y_pos- default to zero
        
        """
    
        self._items = []
        
    def collect_item(self, item):
        """ create a method that override the abstract method

        Args:
            item <item> _ item object in the item list
        """
        self._items.append(item)
        
    def drop_item(self, color, item_type):
        """Create the a method that override 

        Args:
            color (_str_): color
            item_type (_str_): item type
        """
        ""
        #self._items = [item for item in self._items if item['color'] != color or item['type'] != item_type]
        for i, item in enumerate(self._items):
            if item.color == color and item.item_type == item_type:
                del self._items[i]
            
    def print_items(self):
        """Create a method that print out the color 
            and item type that the robot has  
        """
        
        item_counts = {}
        for item in self._items:
            key = (item.color, item.item_type)
            item_counts[key] = item_counts.get(key, 0) + 1

        for (color, item_type), count in item_counts.items():
            print(f"{count} {color} {item_type}")
    
    def __str__(self):
        
        return f"ServiceRobot {super().__str__()} battery_level ({self.get_battery_level()})"
        #return f"Robot_id: {self._robot_id} \n\tbattery: {self._battery} \n\tmotor: {self._motor}" \
        #f" \n\tx_pos: {self._x_pos} y_pos: {self._y_pos}"      
    #def __str__(self):
    #   return f"{self._color} {self._item_type}"
def parse_args(args_list):
    parser = argparse.ArgumentParser(description = "  ")
    parser.add_argument("numservicerobots", type = int,)
    args = parser.parse_args(args_list)
    if args.numservicerobots <= 0:
        raise ValueError("numservicerobots must be greater than 0")
    return args
def main(numservicerobots):
# Note, the following is not what I have in the unit tests. I have different

# This code should cover most of the cases that you are required to test;

# you may see a few additional test cases.
    battery1 = Battery("1234abyz","lithium_ion")
    motor1 = Motor("M1A2B","servo_motor",3,4)
    servicerobot1 = ServiceRobot("123ABX", battery1, motor1,0,0)
    print(servicerobot1)
    print(repr(servicerobot1))
    item1 = Item("cylinder","blue")
    servicerobot1.collect_item(item1)
    print("----********----")
    random.seed(5)
    
    
    myrobotlist = []
    for x in range(0, numservicerobots):
        #
        batteryrulekeys = list(Battery.battery_rules.keys())
        rbatindex = random.randint(0,(len(batteryrulekeys)-1))
        print("----rbatindex----",rbatindex)
        batterytype1 = batteryrulekeys[rbatindex]
        print("----batterytype1----",batterytype1)
            
            
        randlet1 = random.choice(string.ascii_letters)
        randlet2 = random.choice(string.ascii_letters)
        randnum1 = random.randint(0,9)
        randnum2 = random.randint(0,9)
        batteryid1 = randlet1 + randlet2 + str(randnum1) + str(randnum2)
            
            
        battery1 = Battery(batteryid1,batterytype1)
            
        randlet1 = random.choice(string.ascii_letters)
        randlet2 = random.choice(string.ascii_letters)
        randlet3 = random.choice(string.ascii_letters)
        randnum1 = random.randint(0,9)
        randnum2 = random.randint(0,9)
        randnum3 = random.randint(0,9)
        motorid1 = randlet1 + randlet2 + str(randnum1) + str(randnum2) + randlet3 + str(randnum3)
        mtypeindex = random.randint(0,(len(Motor.motor_types)-1))
        motortype = Motor.motor_types[mtypeindex]
            
            
        motor1 = Motor(motorid1,motortype,3,4)
            
        randlet1 = random.choice(string.ascii_letters)
        randlet2 = random.choice(string.ascii_letters)
        randlet3 = random.choice(string.ascii_letters)
        randlet4 = random.choice(string.ascii_letters)
        randnum1 = random.randint(0,9)
        randnum2 = random.randint(0,9)
        randnum3 = random.randint(0,9)
        randnum4 = random.randint(0,9)
        robotid1 = randlet1 + randlet2 + str(randnum1) + str(randnum2) + randlet3 + str(randnum3)+ randlet4 + str(randnum4)
        service_robot = ServiceRobot(robotid1, battery1, motor1,0,0)
        myrobotlist.append(service_robot)
        print(service_robot)
        
    print("----LENGTH OF THE ROBOT LIST----")
    print(len(myrobotlist))
        
    item1 = Item("cone","blue")
    item2 = Item("cone","blue")
    item3 = Item("cube","green")
        
    myrobotlist[0].collect_item(item1)
    myrobotlist[0].collect_item(item2)
    myrobotlist[0].collect_item(item3)
        
    print(myrobotlist[0])
    print(myrobotlist[0].print_items())
    myrobotlist[0].drop_item("blue","cone")
    myrobotlist[0].drop_item("yellow","cone")
        
    myrobotlist[0].move_forward(100)
            # Should not have moved because we did not charge it yet
    assert myrobotlist[0].x_pos== 0.0, ("Robot moved but we did not charge it yet")
        
    myrobotlist[0].charge_battery(100)
        
    myrobotlist[0].move_forward(5)
    myrobotlist[0].move_right(4)
    myrobotlist[0].move_backward(2)
    myrobotlist[0].move_left(2)
        
    print(myrobotlist[0])
        
    myrobotlist[0].move_forward(500)
    print(myrobotlist[0])
if __name__ == "__main__":
    try:
        arguments = parse_args(sys.argv[1:])
        main(arguments.numservicerobots)
    except ValueError as e:
        main(2)

        
        
        
