""" This program write a Robot class to create robot objects.

Author: Enchalew Abebe
Assignment: Homework #1 INST326
Due Date: 10/ 10/2023

I pledge on my honor that I have not given or 
received any unauthorized assistance on this assignment. 

    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """


class Robot:
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
        self._battery = battery if battery in ['lithium_ion', 'lithium_polymer', 'nickel_metal_hydride', 'nuclear'] else None
        self._motor = motor #motor = 'brushed_dc' or 'brushless_dc': 
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._items = {} 
        
        if battery == 'lithium_ion':
            self._battery_level = 100.0
        elif battery == 'nickel_metal_hydride':
            self._battery_level = 100.0
        elif battery == 'lithium_polymer':
            self._battery_level = 100.0
        elif battery == 'nuclear':
            self._battery_level = 10000.0
        else:
            battery ='none'
            self._battery_level = 0.0
            
            
            
    def get_robot_id(self):
        return self._robot_id
        """ Return the robot_id
        
        """
    
    def set_robot_id(self, robot_id):
        """ set the Robot_id

        Args:
            robot_id (str): identifier for the robot
        """
        self._robot_id = robot_id
    
    def get_battery(self):
        """ Get the type of battery

        Returns:
            str: return the type of battery
        """
        return self._battery
    def set_battery(self, battery):
        """ Set the type of battery

        Args:
            battery (str): set the type of the battery
        """
        self._battery = battery
    
    def get_motor(self):
        """Get the motor 

        Returns:
            _str_: Returns motor
        """
        return self._motor
    def set_motor(self, motor):
        """set the motor

        Args:
            motor (str): set the value of motor
        """
        self._motor = motor
        
    def get_x_pos(self):
        """ Get the x_position

        Returns:
            _int_: return the x_position 
        """
        return self._x_pos
    def set_x_pos(self, x_pos):
        """ Set the x position

        Args:
            x_pos (_int_): set the value of the x position
        """
        self._x_pos = x_pos
    
    def get_y_pos(self):
        """ Get the y position

        Returns:
            _int_: return the x_position 
        """
        return self._y_pos
    def set_y_pos(self, y_pos):
        """Set the y-Position

        Args:
            y_pos (_int_): set the value of the y-position
        """
        self._y_pos = y_pos
        
    def get_items(self):
        """ Get the item

        Returns:
            _dict_: contain the items that are collected and the
number of each.
        """
        return self._items
    
    def set_items(self, items):
        """set items in the dictionary

        Args:
            items (_dict_): set items that are collected each time
        """
        self._items = items
    
    def get_battery_level(self):
        
        """ get the battery_level 

        Returns:
            _float_: Return the _battery_level
        """
        return self._battery_level
    
    def set_battery_level(self, battery_level):
        
        """Set battery_level to battery_level
        
        Args:
            battery_level(float): Set the battery_level of the robot
        """
        self._battery_level = battery_level
    
    
    def move_forward(self):
        """Parameters: none
        If battery_level > 0
        Decrease battery level by 1
        Add 1 to y_pos
        """
        
        if self._battery_level > 0:
            self._battery_level -= 1
            self._y_pos += 1

    def move_backward(self):
        """Parameters: None
        If battery_level > 0
        Decrease battery level by 1
        Subtract 1 from y_pos
        """
        
        if self._battery_level > 0:
            self._battery_level -= 1
            self._y_pos -= 1

    def move_right(self):
        
        """Parameters: None
            If battery_level > 0
            Decrease battery level by 1
            Add 1 to x_pos
        """
        
        if self._battery_level > 0:
            self._battery_level -= 1
            self._x_pos += 1

    def move_left(self):
        """Parameters: None
            If battery_level > 0
            Decrease battery level by 1
            Subtract 1 from x_pos
        """
        
        if self._battery_level > 0:
            self._battery_level -= 1
            self._x_pos -= 1

    def collect_item(self, item):
        """ Check if item in items dictionary

        Args:
            item (_str_): If item is already in dictionary then add items to items in the
                        dictionary and increment the counter in the dictionary
                        If item is not in dictionary then add it to the dictionary
        """
    
        if item in self._items:
            self._items[item] += 1
        else:
            self._items[item] = 1

    def drop_item(self, item):
        """ check to see if item already
            exists prior to removing it.

        Args:
            item (str): Remove one item from dictionary at a time
        """
    
        if  item in self._items:
            if self._items[item] > 1:
                self._items[item] -= 1
        else:
            del self._items[item]

    def print_items(self):
        """Print all of the items that the robot currently has
        """
    
        for item, count in self._items.items():
            print(f"{count} {item}")

    def charge_battery(self, amount):
        """ Add amount to battery_level

        Args:
            amount (_float_): Add Amount to battery_level 
            after checking that the battery level does not 
            exceed the maximum for the battery type
        """
        
        self._battery_level += amount
        
        if self._battery == 'lithium_ion':
            self._battery_level = min(self._battery_level, 100.0)
        elif self._battery == 'nickel_metal_hydride':
            self._battery_level = min(self._battery_level, 100.0)
        elif self._battery == 'lithium_polymer':
            self._battery_level = min(self._battery_level, 100.0)
        elif self._battery == 'nuclear':
            self._battery_level = min(self._battery_level, 10000.0)
            
            
    def get_battery_level(self):
        """Parameters: None

        Returns:
            _int_: Return the battery level
        """
        return self._battery_level

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
        return f"Robot_id: {self._robot_id} charge level: {self._battery_level}"

    def __repr__(self):
        return f"Robot_id: {self._robot_id} battery: {self._battery} battery level: {self._battery_level} motor: {self._motor} x_pos: {self._x_pos} y_pos: {self._y_pos}"

def main():
# Note, the following is not what I have in the unit tests.
# This code should cover most of the cases that you are required to test.
    robot1 = Robot("123ABX", "lithium_ion", "brushless_dc",0,0)
    print(robot1)
    print(repr(robot1))
    robot1.collect_item("green block")
    robot1.collect_item("green block")
    robot1.collect_item("red block")
    robot1.collect_item("red block")
    robot1.collect_item("red block")
    robot1.print_items()
    robot1.drop_item("green block")
    print("---------")
    robot1.print_items()
    robot1.move_forward()
    robot1.move_left()
    robot1.move_left()
    robot1.move_left()
    robot1.move_forward()
    print(robot1)
    robot1.charge_battery(5)
    for i in range(0,50):
        robot1.move_forward()
    print(repr(robot1))
    robot1.charge_battery(7)
    print(repr(robot1))
    robot1.reset_position()
    print(repr(robot1))
    robot1.charge_battery(50)
    print(repr(robot1))
if __name__ == "__main__":
    main()





    