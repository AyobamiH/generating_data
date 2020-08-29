# # Problem 9-1:

# Make a class called Shirt.

# The constructor for this class should store two attributes, size and color.

# Create a method on your class that, when called, prints the two attributes on the class out.

# Create an instance of your Shirt class.

# Print each attribute of the class out individually.

# Then, call the method on the class that you wrote to print out the attributes.

# Then, create a new instance of the Shirt class. Print each attribute of the class out individually. Then, call the method on the class that you wrote to print out the attributes.

class Shirt():
    ''' This is a shirt class.'''
    def __init__(self, color,size):
        '''Initialising class attributes.'''
        self.color = color
        self.size = size

    def shirtdescription(self):
        ''' Describes the shirt instance'''
        print('The color of the shirt:', self.color)
        print('Shirt size:', self.size)


# Making an instance of a blue colored shirt.
blueshirt = Shirt('blue', 16)

# Print each attribute of shirt individually.
print('The color of the shirt created:', blueshirt.color)
print('The size of the shirt created is:', blueshirt.size)

# Describing shirt made.
blueshirt.shirtdescription()

# Creating an instance of a Grey  colored shirt.
greyshirt = Shirt('Grey', 15.5)

# Print each attribute of shirt individually.
print('The color of the shirt created:', greyshirt.color)
print('The size of the shirt created is:', greyshirt.size)

# Describing shirt.
greyshirt.shirtdescription()


# Problem 9-2:

# Modify your Shirt class (give it a new name) that adds an attribute called quantity that is set to a default value of 1.

# Create two new methods on the class, one to increase the quantity attribute and one to decrease it. The increase function will add a passed number to the value of the quantity attribute. The decrease function will work in the reverse - passed numbers will be subtracted from the current value of the quantity attribute.

# Create an instance of the new class and call the increase method three different times, using a different number each time. After calling the method, print out the value of the quantity attribute. Then, call the decrease function twice, using a different variable each time. After calling the method, you will again print out the value of the quantity attribute.

class MakeShirt():
    ''' This is a shirt class.'''

    def __init__(self, color, size):
        '''Initialising class attributes.'''
        self.color = color
        self.size = size
        self.quantity = 1

    def describeshirt(self):
        ''' Describes the shirt.'''
        print('The color of the shirt:', self.color)
        print('Shirt size:', self.size)

    def increasequantity(self, integer):
        ''' Increase quantity of shirts. '''
        self.quantity += integer

    def decreasequantity(self, integer):
        ''' Decrease quantity of shirts.'''
        self.quantity -= integer

# Making instance on the Makeshirt class.
# Calling the increase method three different times.
# using a different number each time.
shirtmaking = MakeShirt('Red', 'XXL')

print('Quantity values after calling increase method.')
# Increase quantity by 23.
shirtmaking.increasequantity(23)
print('Value of quantity attribute:', shirtmaking.quantity)

# Increase quantity by 9.
shirtmaking.increasequantity(9)
print('Value of quantity attribute:', shirtmaking.quantity)

# Increase quantity by 12.
shirtmaking.increasequantity(12)
print('Value of quantity attribute:', shirtmaking.quantity)

# Calling shirtmaking with the decrease quantity function.
# Using two different variables named less_shirt and lesser_shirt.
print('Quantity values after calling decrease method twice.')
# Decrease quantity by 9.
less_shirt = shirtmaking.decreasequantity(5)
print('Value of quantity attribute:', shirtmaking.quantity)

# Decrease quantity by 10.
lesser_shirt = shirtmaking.decreasequantity(10)
print('Value of quantity attribute:', shirtmaking.quantity)


# Problem 9-3:

# Re-write the shirt class you created in problem 9-2 to be called "Clothing" instead.
# Create a new class called "ShirtInherit" that adds type information(short or long sleeves) as well as a printed message.
# Add a method to print out the current message on the shirt.

# Create an instance of this and call the increase method with a number of your choosing. Print out the current value of the quantity attribute. Then, call the method you created to print out the message on the shirt.




class Clothing():
    ''' This is a class representation of clothing.'''

    def __init__(self, color, size):
        '''Initialising class attributes.'''
        self.color = color
        self.size = size
        self.quantity = 1

    def describeshirt(self):
        ''' Describes the shirt.'''
        print('The color of the shirt:', self.color)
        print('Shirt size:', self.size)

    def increasequantity(self, integer):
        ''' Increase quantity of shirts. '''
        self.quantity += integer

    def decreasequantity(self, integer):
        ''' Decrease quantity of shirts.'''
        self.quantity -= integer


class ShirtInherit(Clothing):
    ''' A class representation of customised shirtmaking.'''

    def __init__(self, color, size, typeofsleeve, message):
        '''Initialising attrs for ShirtInherit class.'''

        super().__init__(color, size)
        self.typeofsleeve = typeofsleeve
        self.message = message

    def print_message(self):
        print('Message info:', self.message)


# Create an instance of ShirtInherit & call
# The increase quantity method with a number of your choosing.
make_clothings = ShirtInherit('Green', 3, 'Long', 'Make hay while the sun shines.')

# Calling The increase quantity method.
make_clothings.increasequantity(19)

# Print out the current value of the quantity attribute from clothing class.
print('Current Value of quantity attribute(Clothing class).:', make_clothings.quantity)

# Calling print_message method on the instance of ShirtInherit class.
# printing print_message() method of the ShirtInherit class
make_clothings.print_message()


class Pants(Clothing):
    ''' Initialise attrs of clothing specific to pants.'''

    def __init__(self, color, size, fabric, style):
        ''' Initialising attrs for base class.
            Then add fabric type and style type to the base class.
            '''
        super().__init__(color, size)
        self.fabric = fabric
        self.style = style
