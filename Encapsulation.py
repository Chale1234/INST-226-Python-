"""
Encapsulation is help us to restrict access either in the class or in the method
Private Variable : access using method or calling in the method , if you are trying to call in the l
the class the calling calls may trace back an error, we have to call inside the method
Private Method : when calling private method you have to call 
from another method to access its method, and we have to call inside the method 

lets create a class name called Enchalew that have private variable called __FirstName 
and a public
variable called LastName
the class Enchalew are going to have a method called firstname and Last Name 
    """
class Enchalew:
    __FirstName =" Enchalew " # private variable nama called __FirstName
    LastName= " Abebe" # Public Variable called LastName can't access by class name
    def FirstName(self):
        print(self.__FirstName)
    
    def astName(self):
        print(self.LastName)
    def __greatFather(self):
        print(" my great father name is Bize")
        
        
    def callGreatFather(self):
        self.__greatFather()
        """
        The different between __ str__ and __reps__ 
        both of them are a kind of formal and informal
        to access the method or the variable it better to use the
        data ub encapsulation  is using setter and getter method 
        
        
        __str__ and __repr__ these are two specual ethod used to define how an object should reoresebted a 
        string when t us printed or converted to as string
        
        when called __ str__  we are calling the string
        
        """
        
    class Test:
        def __init__(self):
            self.fool= "fool"
            self._bar = "bar" # this is a private variable that can not access to the outside the method
            self.__baz = "baz"
        def get_bar(self):
            return self._bar
        def set_bar (self,bar):
            self,_bar = bar 
        
        
    test1 = Test()
    print(test1)
    print(dir(test1))
    print(test1.get_bar())
    print(test1.set_bar())
    
    
    class Person :
        def __inti__(self, f_name, LastName, age, occupation ):
            """_summary_

            Args:
                f_name (_type_): _description_
                LastName (_type_): _description_
            """
            self._f_name = f_name
            self._lastName = LastName
            self._age = age
            self._occupation = occupation
        def add_year(self, x):
            self.add_year +x
        def set_f_name(self,f_name):
            self._f_name = f_name 
        def get_f_name(self):
            return self._f_name
            
        
            ## when you do your exercise the the default value is always at the end
            
        # after that ywe have to use setter and getter method to access the first nam, last name and age.
        
    #print(test1_bar)# this does not work because the instance does not an access the variable bar
        
    
    
    
    
    
Name = Enchalew() 
Name.FirstName()
Name.astName()
Name.callGreatFather()
#print(type(Enchalew.__FirstName))
#print(Name.LastName)