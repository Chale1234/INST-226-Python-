""" A python deliverable script
Driver: Enchalew Abebe
Navigator: Enchalew Abebe
Assignment: exercise2 INST326
Date: 9_24_23
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""
# It creates a Vehicle class
class Vehicle :
    
    """ It builds a Vehicle class and the vehicle will have five (5) attributes:
        the class will accept five (5) parameters into 
        the initialization method. The x and y parameters will have
        default values of zero (0).
    Args: 
    make(str)- the make of the car.
    model(str)- the model of the car.
    year(int)- the year of the car.
    x_pos(int)- the x position of the vehicle
    y_pos(int- the y position of the vehicle.
    
    
    
    """
    
    
    def __init__(self, make, model, year, x_pos= 0, y_pos = 0):
    
        """ It Initialize the instance object when the class is called
        
        Args: 
        make (str) - the make of the vehicle.
        Model(Str)- the model of the vehicle
        year(int)- the Year of the vehicle
        x_pos (int) - the x position of the vehicle.
        y_pos(int)_ the y Position of the vehicle.
        """
        
        
        self.make = make
        self.model = model
        self.year = year
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    
    def move_x(self, move_x):
        """ Modify the instance attribute x_pos by
            adding the parameter value to it
        Args: 
        move_x(int)- the number of x positions to move

        """
        
        self.x_pos = self.x_pos + move_x
        
    
    def move_y(self, move_y):
        """ Modify the instance attribute x_pos by 
        adding the parameter value to it

        Args:
            move_y (int)- the number of y position to move
        """
        self.y_pos = self.y_pos + move_y
    
    
    def vehicle_info(self):
        """ No parameter
        Returns:A string that contains the year + make + model with
            a single space between year & make and a single
            space between make & model:
        """
        
        return f'{self.year} {self.make} {self.model}'
    
    
    def vehicle_position(self):
        """ No parameter
        Returns:A string that contains the x_pos + y_pos 
        """
        return f'x_pos: {self.x_pos} y_pos: {self.y_pos }'
    
    
def main():
    vehicle1 = Vehicle("Toyota","RAV4",2022)
    vehicle2 = Vehicle("Honda","CR-V",2020)

    print(vehicle1.vehicle_info() )
    print(vehicle1.vehicle_position() )
    vehicle1.move_x(2)
    vehicle1.move_y(3)
    print(vehicle1.vehicle_position() )


    print(vehicle2.vehicle_info() )
    print(vehicle2.vehicle_position() )
    vehicle2.move_x(5)
    vehicle2.move_y(8)
    print(vehicle2.vehicle_position() )
if __name__ == "__main__":
    main()


