"""A python exercise4 script deliverable for INST326.
Driver: Enchalew Abebe
Navigator: Enchalew Abebe
Assignment: exercise5 INST326
Date: 10_27_23
Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""


from abc import ABC, abstractmethod
import math
import json

class Vehicle(ABC):
    """ we are going to build our abstract vehicle class. 
    declare @abstract method and our attributes to ‘private’. 
    We will create setters and getters for all of our variables using Decorator. 
    We will also add a __str__ and __repr__ methods
    """
    def __init__(self, make, model, year, x_pos=0, y_pos=0):
        """_summary_

        Args:
            make (str) - the make of the vehicle.
            model (str)- the model of the vehicle.
            year (int)- the year of the vehicle.
            x_pos (int, optional)- the x position of the vehicle. Defaults to 0
            y_pos (int, optional)- the y position of the vehicle.. Defaults to 0.
        """
        self._make = make
        self._model = model
        self._year = year
        self._x_pos = x_pos
        self._y_pos = y_pos
    @abstractmethod
    def move_x(self, move_x):
        """ Modify the instance attribute x_pos by
            adding the parameter value to it
        Args: 
        move_x(int)- the number of x positions to move

        """
        pass
        
        #self._x_pos += move_x
    @abstractmethod
    def move_y(self, move_y):
        """ Modify the instance attribute y_pos by 
        adding the parameter value to it

        Args:
            move_y (int)- the number of y position to move
        """
        pass
        #self._y_pos += move_y

    def vehicle_info(self):
        """ No parameter
        
        Returns: A string that contains the year + make + model with
            a single space between year & make and a single
            space between make & model:
        """
        return f"{self._year} {self._make} {self._model}"

    def vehicle_position(self):
        """ No parameter
        
        Returns:A string that contains the x_pos + y_pos 
        """
        return f"x_pos: {self._x_pos} y_pos: {self._y_pos}"

    # Setters and getters for all attributes
    @property
    def make(self):
        """  The make method returns the value of the "_make".

        Returns:
            str: The make of the vehicle
        """
        return self._make
    @make.setter
    def make(self, make):
        """ Set the make of the vehicle

        Args:
            make (str): The make of the vehicle
        """
        self._make = make
    @property
    def model(self):
        """ Get the model of the vehicle

        Returns:
            str: The model of the vehicle
        """
        return self._model
    @model.setter
    def model(self, model):
        """ Set the model of the vehicle

        Args:
            model (str): The model of the vehicle
        """
        self._model = model
    @property
    def year(self):
        """ Get the year of the vehicle

        Returns:
            int: The year of the vehicle
        """
        
        return self._year
    @year.setter
    def year(self, year):
        """ Set the year of the car

        Args:
            year (int): The year of the vehicle
        """
        self._year = year
        
    @property
    def x_pos(self):
        """ Get the x position of the vehicle

        Returns:
            int : The x position of the vehicle
        """
        return self._x_pos
    @x_pos.setter
    def x_pos(self, x_pos):
        """ Set the x Position of the vehicle


        Args:
            x_pos (int): The x position of the vehicle
        """
    
        self._x_pos = x_pos
    @property
    def y_pos(self):
        """ Get the y_position of the vehicle

        Returns:
            int : The x position of the vehicle
        """
        return self._y_pos
    @y_pos.setter
    def y_pos(self, y_pos):
        """ Set the y position of the vehicle


        Args:
            y_pos (int): The y position of the vehicle
        """
        self._y_pos = y_pos
    def __str__(self):
        """ The __str__ method to customize the string 
        representation of an instance of a class.

        Returns:
            str: The year, make, and model of the car
        """
        return f"Year: {self._year} Make: {self._make} Model: {self._model}"

    def __repr__(self):
        """ The __repr__ () method returns a string that can 
        be executed and yield the same value as the object.

        Returns:
            str: It returns the year, make, and model of the vehicle.
        """
        return f"Vehicle(Year: {self._year} Make: {self._make} Model: {self._model})"

class Bicycle(Vehicle):
    
    def __init__(self, make, model, year, bicycle_type, frame_material, gears, x_pos = 0, y_pos = 0):
        """ Create a bicycle class that inherit from  Vehicle class

        Args:
            make (_str_): The make of the vehicle
            model (_str_): The model of the vehicle_
            year (_int_): The year of the vehicle_
            bicycle_type (_str_): The type oof the bicycle
            frame_material (_str_): The frame material of the bicycle
            gears (_int_): The gears of the bicycle
            x_pos (int): The x position of the bicycle. Defaults to 0.
            y_pos (int): The y position of the bicycle. Defaults to 0.
        """
        super().__init__(make, model, year, x_pos , y_pos)
        self._bicycle_type = bicycle_type #if bicycle_type in ["road","mountain","hybrid"] else 'none'
        self._frame_material = frame_material #if frame_material in ["carbon","steel","aluminum","titanium"] else 'none'
        self._gears = gears
        self._current_gears = 1
    
    # create setters and getters using property decorators 
    def move_x( self, move_x):
        """ The number of x positions to move
                Modify the instance attribute x_pos by
                adding the parameter value to it

        Args:
            move_x (_int_): The Number of x positions to move
        """
        self._x_pos +=move_x
    def move_y( self, move_y):
        """ The number of y positions to move
                Modify the instance attribute y_pos by
                adding the parameter value to it

        Args:
            move_y (_int_): The Number of y positions to move
        """
        self._x_pos +=move_y
        
        
    @property
    def bicycle_type(self):
        """ Get the bicycle type

        Returns:
            _str_:  The type of bicycle
        """
        return self._bicycle_type
    @bicycle_type.setter
    def bicycle_type(self,bicycle_type):
        """ Set the bicycle type

        Args:
            bicycle_type (_str_): Sets the bicycle type
        """
        self._bicycle_type = bicycle_type
    
    @property
    def frame_material(self):
        
        """ Get frame material of the bicycle

        Returns:
            _str_:  The frame material of the bicycle
        """
        return self._frame_material
    
    @frame_material.setter
    def frame_material(self,frame_material):
        """ Set the frame material of the bicycle

        Args:
            frame_material (_str_):  The frame material of the bicycle
        """
        self._frame_material = frame_material
    
    @property
    def gears(self):
        """ Get the gear of the bicycle 

        Returns:
            _int _:  The gear of the bicycle 
        """
        return self._gears 
    
    @gears.setter
    def gears(self,gears):
        """Set the gears of the bicycle

        Args:
            gears (_int_):  The gears of the bicycle
        """
        self._gears = gears 
    
    @property
    def current_gear( self):
        
        """ Get the current gear of the bicycle

        Returns:
            _int _: The current gears of the bicycle
        """
        return self._current_gear 

    @current_gear.setter
    def current_gears(self,current_gear):
        """ Set the current gear of the bicycle

        Args:
            current_gears (_int_): The current gear of the bicycle
        """
        self._current_gears = current_gear
        
        
        
    def pedal(self, move_x):
        """
            Modify the instance attribute x_pos by
            adding the parameter value to it

        Args:
            move_x (_int_): The number of x positions to move
        """
        self._x_pos += move_x
        
    def brake(self): # it does nothing
        pass
    def change_gears(self, gear):
        
        """
            Modify the current_gear to this value.
            Verify the gear value is between 1-30.
            
        Args:
            gear(int): The gear to set the bike 
        """
        
        if gear in range(1,31):
            self._current_gear = gear
            
    def __str__(self):
        return f"Year: {self._year} Make: {self._make} Model: {self._model} BicycleType: {self._bicycle_type} FrameMaterial: {self._frame_material} Gears: {self._gears}"
    def __repr__(self):
        return f"Class(Year: {self._year} Make: {self._make} Model: {self._model})"       
            
class Engine:
    def __init__(self, cylinder_count, displacement,horsepower,fuel_type):
        """_summary_

        Args:
            cylinder_count (_int_): The cylinder of the car
            displacement (_float_): The car displacement
            horsepower (_int_): The Horsepower of the car 
            fuel_type (_float_): The fuel type of the car
        """
        self.cylinder_count = cylinder_count if cylinder_count > 0 and cylinder_count <=12 else None
        self.displacement = displacement if displacement >0 and displacement < 6 else None
        self.horsepower = horsepower  if horsepower > 0 and horsepower <=1000 else None
        self.fuel_type = fuel_type if fuel_type in ["gasoline", "diesel", "hybrid", "electric"] else None
        self.fuel_level = 0.0
        
    # create a setter and getter method using @property decorator
    @property
    def cylinder_count(self):
        """ Get the cylinder count

        Returns:
            _int_: _description_
        """
        return self._cylinder_count
    @cylinder_count.setter
    def cylinder_count(self, cylinder_count):
        """Set the cylinder count

        Args:
            cylinder_count (_int_): _description_
        """
        self._cylinder_count = cylinder_count 
        
    @property
    def displacement(self):
        """ Get the displacement

        Returns:
            _float_: It returns the value of displacement
        """
        return self._displacement
    @displacement.setter
    def displacement(self, displacement):
        """Set displacement

        Args:
            displacement (_float_): The engine displacement
        """
        self._displacement = displacement 
        
    @property
    def horsepower(self):
        """Get the horse power of the car 

        Returns:
            _int_: The horsepower of the car 
        """
        return self._horsepower
    @horsepower.setter
    def horsepower(self, horsepower):
        """Set the horsepower of the car 

        Args:
            horsepower (_int_): The horse power of the car 
        """
        self._horsepower = horsepower 
    
    @property
    def fuel_type(self):
        """Get the fuel type of the car 

        Returns:
            _str_: The fuel type of the car 
        """
        return self._fuel_type
    @fuel_type.setter
    def fuel_type(self, fuel_type):
        """Set the fuel type of the car 

        Args:
            fuel_type (_str_): The fuel type of the car 
        """
        self._fuel_type = fuel_type 
    
    @property
    def fuel_level(self):
        """Get the fuel level of the car 

        Returns:
            _float_: The fuel level of the car 
        """
        return (round(self._fuel_level, 1))
    @fuel_level.setter
    def fuel_level(self, fuel_level):
        """Set the fuel level of the car 

        Args:
            fuel_level (_float_): The fuel level of the car 
        """
        self._fuel_level = fuel_level 
    
    def consume_fuel(self, amount_moved):
        """_summary_

        Args:
            amount_moved (_type_): _description_
        """
        fuel_used = amount_moved * (self._displacement/5.0) # Not real calculation
        self._fuel_level -= fuel_used
        if self._fuel_level < 0:
            self._fuel_level = 0
            
    def fill_tank(self, amount):
        """_summary_

        Args:
            amount (_type_): _description_
        """
        if self._fuel_level > 100 or self._fuel_level + amount >= 100: #TODO hard coded
            self._fuel_level = 100
        else:
            self._fuel_level += amount
        
        
    def __str__(self):
            return f"Cylinder count: {self.cylinder_count}, Displacement: {self.displacement}, Horsepower: {self.horsepower}, Fuel Type: {self.fuel_type}, Fuel Level: {self.fuel_level}"
        
            
class Car(Vehicle):
    def __init__(self, make, model, year, car_type, number_doors, engine, x_pos =0, y_pos = 0):
        """ Create the class car that inherit from Vehicle class

        Args:
            make (_str_): The make of the vehicle
            model (_str_): The model of the vehicle
            year (_int_): The year of the vehicle
            type (_str_): The type of the car
            number_doors (_int_): The car door number  
            engine (_str_): The engine type of the car 
            x_pos (int): The x position of the vehicle. Defaults to 0.
            y_pos (int): The y position of the vehicle. Defaults to 0.
        """
        
        
        super().__init__(make, model, year, x_pos, y_pos)
        self._car_type = car_type # if type in ["sedan", "sport", "hatchBack", "convertible"] else 'none'
        self._number_doors =  number_doors #if number_doors in range(1,5) else 'none'
        self._engine = engine  # if engine in ["i4","v6","v8"] else "Not Specified"
        self.engine_state = 0
        
    # create setters and getters using property decorators
    @property
    def car_type(self):
        """ Get the type of the car

        Returns:
            str: The type of the car
        """
        return self._car_type

    @car_type.setter
    def type(self, car_type):
        """Set the type of the car

        Args:
            type (int): The type of the car
        """
        self._car_type =car_type
    
    @property
    def number_doors(self):
        """ Get the number of doors 

        Returns:
            int: The number of the doors
        """
        return self._number_doors

    @number_doors.setter
    def number_doors(self,number_doors):
        """ Set the number of doors

        Args:
            number_doors (int):  The number of doors
        """
        self._number_doors = number_doors
    
    @property
    def engine(self):
        """Get the engine type of the car

        Returns:
            str: The engine of the car
        """
        return self._engine

    @engine.setter
    def engine(self,engine):
        """ Set the engine of the car

        Args:
            engine (_str_): The engine of the car
        """
        self._engine = engine
        
    @property
    def engine_state(self):
        """ Get the engine state of the car

        Returns:
            int: The engine state of the car
        """
        return self._engine_state

    @engine_state.setter
    def engine_state(self,engine_state):
        """ Set the engine state of the car

        Args:
            engine_state (_int_): The engine state of the car
        """
        self._engine_state = engine_state
        
        
    def honk(self):
        """

        Returns:
            str: It return the string "Honk!"
        """
        return "Honk!"

    def start(self):
        """
        Set engine state to one
        """
        self._engine_state = 1
        
        
    def stop(self):
        """
        Set engine state to zero
        """
        self._engine_state = 0
        
    def move_x(self, move_x):
        """verify that the fuel level in the Engine object in your Car
            object is greater than 0 (zero). If the fuel level is greater
            than 0 (zero) then move the x direction and then call
            the consume_fuel method on the Engine object within your
            Car object.

        Args:
            move_x (_init_): The number of x position to move
        """
        for move in range(0, move_x): 
            if self._engine.fuel_level > 0:
                self.x_pos += 1
                self._engine.consume_fuel(1)
        
            
    def move_y (self, move_y):
        """ verify that the fuel level in the Engine object in your Car
            object is greater than 0 (zero). If the fuel level is greater
            than 0 (zero) then move the y direction and then call
            the consume_fuel method on the Engine object within your
            Car object.

        Args:
            move_y (_int_): The number of y position to move
        """
        for move in range(0,move_y):
            if self._engine.fuel_level > 0 :
                self.y_pos += 1
                self._engine.consume_fuel(1)
        
    def __str__(self):
        """ The __str__ method to customize the string representation of an instance of a class.

        Returns:
            str: The year, make, and model of the car
        """
        return f"Year: {str(self._year)} Make: {self._make} Model: {self._model} CarType: {self._car_type} Doors: {self._number_doors} Engine: {self._engine} X_Pos: {self._x_pos} Y_pos: {self._y_pos}"
    
    
def main():
# Uncomment this attempt to instantiate a Vechicle objectto test.
# It should fail with a "Can't instantiated abstract class Vehicle with
#abstract methods move_x, move_y"
# add the comment back in to run the rest of the code, or just remove this
#line.
#vehicle1 = Vehicle("Toyota","Tundra",2022)
    bicycle1 = Bicycle("Specialized","Allez", 2023,"road","carbon",12) # you should
    #test wth x and y positions as well
    print(bicycle1)
    bicycle1.make = "Huffy"
    bicycle1.model = "Model II"
    bicycle1.gears = 20
    bicycle1.pedal(3) # x_pos should equal 3 after pedalling. We will change this
    #behavior in subsequent exercises
    bicycle1.brake() # doesn't do anything currently
    bicycle1.change_gears(5) # bicylce.current_gear should equal 5, originally it
    #was 1.
    print(f"Bicycle: {bicycle1}")
    #cylinder_count, displacement, horsepower, fuel_type
    engine1 = Engine(4, 3.7, 120, "hybrid")
    car1 = Car("Toyota","RAV4",2021,"sedan",4,engine1) # you should test wth x and
    #y positions as well
    car1.engine.fill_tank(10)
    print(car1)
    print(f"Engine state a: {car1.engine_state}") # should equal 0
    car1.start()
    print(f"Engine state b: {car1.engine_state}") # should equal 0
    car1.stop()
    print(f"Engine state c: {car1.engine_state}") # should equal 0
    car1.start()
    print(car1.honk()) # should equal "Honk!"
    car1.move_x(1)
    car1.move_y(4)
    car1.move_y(5)
    car1.move_x(3)
    car1.move_x(4)
    car1.move_x(4)
    print(car1)
'''
The last print statement prints the following:
Year: 2021 Make: Toyota Model: RAV4 CarType: sedan Doors: 4 Engine:
Cylinder count: 4, Displacement: 3.7, Horsepower: 120, Fuel Type: hybrid, Fuel
Level: 0 X_Pos: 8 Y_pos: 9
'''
if __name__ == "__main__":
    main()
