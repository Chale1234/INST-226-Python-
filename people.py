import re

""" This will be writing a script that 
    takes a text file and parse the text in each row in the text.
    
    Driver: Enchalew Abebe
    Navigator: Enchalew Abebe
    Assignment: exercise7 INST326
    Date: 12_09_23
Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    
    """
def parse_name(text):
    """ The function that contain one parameter called text

    Args:
        text (string): a string representing a single line of the file

    Returns:
        tuple: Return the first and last name as strings
    """
    match = re.match(r'(\w+)\s(\w+)', text)
    if match:
        return match.group(1), match.group(2)
    else:
        None, None

def parse_address(text):
    """ The function will contains one parameter 
    a string representing a single line
    

    Args:
        text (String): String representing a single line of the file

    Returns:
        _text_: return the street, city and state
    """
    #match = re.match(r'(\d+ \w+), (\w+), (\w+)', text)
    #match = re.match('\s(\d+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(w+)', text)
    #match = re.match(r'(\d+ [^ ]+) ([^,]) ([^,]+)\s', text)
    
    match = re.match(r'^.*?(\d+ [^ ]+) ([^,]+) ([^,]+)\s', text)
    if match:
        return Address(match.group(1), match.group(2), match.group(3))
    else:
        return None


def parse_email(text):
    """The function will contains one parameter, text, 
    a string representing a single line of the file 

    Args:
        text (string): A string representing a single line of the file

    Returns:
        _text_: Return the email identified
    """
    match = re.search(r'([\w\.-]+@[a-zA-Z\d\.-]+)', text)
    if match:
        return match.group(1)
    else:
        None
    
class Address:
    def __init__(self, street, city, state):
        """The class that have three parameters

        Args:
            street (string): The name of street
            city (string): The name of the city
            state (string): The name of the state
        """
        self.street = street
        self.city = city
        self.state = state
        
class Employee:
    def __init__(self, row):
        """The function that have four attributes 
        and created by passing in the row of th file 

        Args:
        (string): The name of employee information
        """
        self.first_name, self.last_name= parse_name(row) 
        self.address = parse_address(row)
        self.email = parse_email(row)


def main(path):
    """ A function that have one parameter , path, and 
        and It prints First name, last Name, email, and address
    

    Args:
        path (_string_): The path to the file that is being parsed

    Returns:
        _type_: _description_
    """
    employee_list = []
    
    with open(path, 'r') as file:
        for line in file:
            employee = Employee(line.strip())
            employee_list.append(employee)
            
            print(f"Full Name: {employee.first_name} {employee.last_name}")
            print(f"Address: {employee.address.street} {employee.address.city} {employee.address.state} ")
            print(f"Email: {employee.email} \n")
                
    return employee_list

if __name__ == '__main__':
    person_info = main("people.txt")
    #print(person_info) # it print out the memory location of the out put

    
    

    