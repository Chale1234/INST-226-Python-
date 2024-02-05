"""A python exercise3 script deliverable for INST326.
Driver: Enchalew Abebe
Navigator: Enchalew Abebe
Assignment: exercise3 INST326
Date: 9_30_23
Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""




class Vehicle:
    """ we are going to build onto our vehicle class from the last exercise. 
we change our attributes to ‘private’ and add an additional attributes engine which we will
do parameter validation. 
We will create setters and getters for all of our variables. 
We will also add a __str__ and __repr__ methods
    """
    def __init__(self, make, model, year, engine, x_pos=0, y_pos=0):
        """_summary_

        Args:
            make (str) - the make of the vehicle.
            model (str)- the model of the vehicle.
            year (int)- the year of the vehicle.
            engine (str)- the engine type of the vehicle with some validation
            x_pos (int, optional)- the x position of the vehicle. Defaults to 0
            y_pos (int, optional)- the y position of the vehicle.. Defaults to 0.
        """
        self._make = make
        self._model = model
        self._year = year
        self._engine = engine if engine in ["v6", "v8"] else "Not Specified"
        self._x_pos = x_pos
        self._y_pos = y_pos

    def move_x(self, move_x):
        """ Modify the instance attribute x_pos by
            adding the parameter value to it
        Args: 
        move_x(int)- the number of x positions to move

        """
        
        self._x_pos += move_x

    def move_y(self, move_y):
        """ Modify the instance attribute x_pos by 
        adding the parameter value to it

        Args:
            move_y (int)- the number of y position to move
        """
        self._y_pos += move_y

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

    def get_make(self):
        """  The get_make method returns the value of the "_make".

        Returns:
            str: The make of the vehicle
        """
        return self._make

    def set_make(self, make):
        """ The set_make method takes a "make" parameter  and assigns it to the make variable.

        Args:
            make (str): The make of the vehicle
        """
        self._make = make

    def get_model(self):
        """ The get_model method returns the value of the "_model"

        Returns:
            str: The model of the vehicle
        """
        return self._model

    def set_model(self, model):
        """ The se_model takes a "Model" parameter and assigns it to the model variable

        Args:
            model (str): The model of the vehicle
        """
        self._model = model

    def get_year(self):
        """ The get_model method returns the value of the "_model"

        Returns:
            int: The year of the vehicle
        """
        
        return self._year

    def set_year(self, year):
        """ The set_year takes a " year" parameter and assigns it to the year variable

        Args:
            year (int): The year of the vehicle
        """
        self._year = year

    def get_engine(self):
        """ The get_engine method returns the value of the "_engine"

        Returns:
            str: The engine of the vehicle 
        """
        return self._engine

    def set_engine(self, engine):
        """ The set_engine method takes an "engine" parameter and assigns it to the year variable, 
        and validate if the engine is in range between [v6,v8], it returns the engine type, and
        if the engine is outside the given range, it will returns " Not Specified"

        Args:
            engine (str): The engine of the vehicle
        """
        if engine in ["v6", "v8"]:
            self._engine = engine
        else:
            self._engine = "Not Specified"

    def get_x_pos(self):
        """ The get_x_pos method returns the value of the "x_pos"

        Returns:
            int : The x position of the vehicle
        """
        return self._x_pos

    def set_x_pos(self, x_pos):
        """ The set_x_pos takes a " x_pos" parameter and assigns it to the x_pos variable


        Args:
            x_pos (int): The x position of the vehicle
        """
    
        self._x_pos = x_pos

    def get_y_pos(self):
        """ The get_y_pos method returns the value of the "_engine"

        Returns:
            int : The x position of the vehicle
        """
        return self._y_pos

    def set_y_pos(self, y_pos):
        """ The set_y_pos takes a " y_pos" parameter and assigns it to the y_pos variable


        Args:
            y_pos (int): The y position of the vehicle
        """
        self._y_pos = y_pos

    def __str__(self):
        """ The __str__ method to customize the string representation of an instance of a class.

        Returns:
            str: The year, make, model, and the engine of the vehicle
        """
        return f"Year: {self._year} Make: {self._make} Model: {self._model} Engine: {self._engine}"

    def __repr__(self):
        """ The __repr__ () method returns a string that can be executed and yield the same value as the object.

        Returns:
            str: It returns the year, make, model,and engine of the vehicle
        """
        return f"Class(Year: {self._year} Make: {self._make} Model: {self._model} Engine: {self._engine})"


def main():
    """ It displays the vehicle information 
    """
    vehicle1 = Vehicle("Toyota","Tundra",2022,"v8")
    vehicle2 = Vehicle("BMW","328d",2014,"v6",5,10)
    vehicle3 = Vehicle("Nissan","Pathfinder",2015,"v6",5,10)
    vehicle4 = Vehicle("Toyota","Prius",2011,"i4",5,10)
    str(vehicle1)
    print(vehicle1.vehicle_position() )
    vehicle1.move_x(2)
    vehicle1.move_y(3)
    print(vehicle1.vehicle_position() )
    str(vehicle2)
    print(vehicle2.vehicle_position() )
    vehicle2.move_x(2)
    vehicle2.move_y(3)
    print(vehicle2.vehicle_position() )
    print(vehicle1)
    print(repr(vehicle1))
    print(vehicle2)
    print(repr(vehicle2))
    print(vehicle3)
    print(repr(vehicle3))
    print(vehicle4)
    print(repr(vehicle4))
    vehicle4.set_make("Mazda")
    vehicle4.set_model("CX5")
    vehicle4.set_year("2021")
    vehicle4.set_x_pos(11)
    vehicle4.set_y_pos(33)
    vehicle4.set_engine("v6")
    print(vehicle4)
    print(repr(vehicle4))
if __name__ == "__main__":
    main()


