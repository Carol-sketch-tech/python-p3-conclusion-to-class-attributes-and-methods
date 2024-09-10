# Conclusion to Class Attributes and Class methods.


# how do i recognize a class attribute
'''
class attributes belong to the class itself rather than to any particular instance of the class.
they are shared across all instances of the class.

these is how you can know it is a class attribute:
     1. Declaration -> they are declared directly inside the class body, outside of any instance methods or constructors
     __init__ methods.they are usually defined at the top of the class, before any methods.

     2.Access -> class attributes can be accessed both from the class itself,and from instance of the class.
     accessing them from the class is straightforward, while access them from an instance can be done as well but it less common.

     3. usage - > class attributes are suseful for values that should be shared among all isntaces, such as constants, configuration valies or shared data.

     class method can access and modify the class attribute  by using the cls parameter of the class method.
'''

#how do i know when to define class methods.
'''
to know when to define class methods need one to understand the specifi roles for class methods, instance methods and static methods.
 # when to use a Class method.
 classmethods are defined using the @classmethod decorator and take cls as their first parameter, which represents the class itself.
 not an isntance of the class.

 Here's when you can decide to Access or modify Class Method:
    1. when you need to access or modify Class state: use a class method if you need to work with class-level attributes or state rather than 
    instance-specific data.

    2. when you need to provide alternative constructors: class methods are useful for defining alternative ways to create intances of a class.
    for instance you want to create instances from different types of input data.

    3. when you need to access other class methods or class variables -> if your method needs to call other methods or access 
    class level variables, it should be a class method.
'''

# explanation for point two in how do i know when to use the class method.
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_str):
        # plit the string by '-' and convert each part to an interger 
        day, month, year = map(int, date_str.split('-'))
        # create an instance using the class and return it 
        return cls(day, month, year)
 
my_date = Date(12, 23, 3234)
date2 = Date.from_string('12-12-1234')

#  in the code above we have provided an example of a class method usd to create instances of a class from a string representation of the date.


# Understandint he concept of remembrance in object oriented programming.
'''
 the concept of object oriented programming refers to the ability of an object to maintain its state and behaviour across different interactions or mthods calls.
 it means that the object remembers its state or data between different invocations and maintains consistency as its methods are called.

 # Key Aspects of Object Remembrance.
    1. State persistence.
        a) instance varibales-> objects maintain their state using isntance variables(attributes). once an obejct is created and its attributes are set,
        those attributes hold their values unitl explicityly changed or until the object is destroyed.
    2. Encapsulation.
        a) objects encapsulate their state and behaviour, meaning that their internal data is hidden from the outside world.
        only methods(fucntions) defined within the object can access or modify its state. This helps in managing complexity and protectiong data integrity.
    3. Behavour Consistency.
        a) Methods calls ->  objects can performa ctions via their methods, and they remember their state between method calls.
        this consistency ensures thet the methods operate in the most surrent state of the object.

    4. Lifecycle Management.
        a) Objects are created , used and eventually destroyed. teh state of an object is maintained thorughout its lifecycle.
        proper management of this lifecycle ensures that the object behaves correclty thoroughout its existence.

Object remembrance in obeject orientated programming is about maintaining an objeact's state and behaviour across interactions.
it is achieved through intance variables and methods that ensure that objects retain their data and behave consistently over their lifecycle.
This concept is central to obejct oriented programming principleas like encapsulation, data hiding and state management.
'''