##Forwards and Backwards
##Create a program that is able to detect if an input is the same as the
##reverse of the same input – i.e. a Palindrome

def palindrome(arg):
    if arg == arg[::-1]:
        print('Yes it\'s a palindrome')
    else:
        print('No it\'s not a palindrome')


####0 Year Addition Create a program that accepts a year in the format ####,
##e.g. 2015. The program then adds each digit of the year together and
##outputs the answer. E.g. 2015 becomes the output 8. Extension: 1.
##Develop this so that the user can guess an integer value. If the MOD
##division is “0” they score a point, if it isn’t they can guess again, up
##to 3 attempts in total
##


def add_year(year):
    """Output the sum of each digit in year)"""
    year = str(year)
    sum_of_year = 0
    for y in year:
        sum_of_year += int(y)
    return sum_of_year

##Word Subtraction Create a program that takes two strings/words. Then
##then converts this to an ASCII value and subtracts the values from each
##other.
##
##Extension: 1. Also add a function that removes any characters in
##the second word that occur in the first word. E.g. Fish and Tin, would
##return “Fsh” and “Tn”

def word_subtraction(one, two):
    
    ascii_value = ord(one) - ord(two)
    return ascii_value

def removeone_fromtwo(one, two):
    for l in two:
        if l in one:
            one = one.replace(l, '')
            two = two.replace(l, '')
    print(f'"{one}" and "{two}"')

#####CLASS

class WordSubtraction:
    """ A program that takes two strings/words.

       Then converts this to an ASCII value
       and subtracts the values from each
       other.


    """

    def __init__(self, one, two):
        self.one = one
        self.two = two

    def wordascii_subtraction(self):
        output = ord(self.one) - ord(self.two)
        
        print(output)
         
    def removetwo_fromone(self):
        for l in self.two:
            if l in self.one:
                self.one = self.one.replace(l, '')
                self.two = self.two.replace(l, '')
        print(self.one, self.two)
    
    
wordtoascii1 = WordSubtraction("brain", "strain")
wordtoascii = WordSubtraction("z", "d")
print(f"Word To Ascii OnE1.: {wordtoascii.one}\nWord To Ascii TwO2.: {wordtoascii.two}")
wordtoascii.wordascii_subtraction()
wordtoascii1.removetwo_fromone()
##
##Averages Make a program that asks the user for a series of numbers until
##they either want to output the average or quit the program. Extensions:

##1. Expand the program to print the median and mode averages also

##2.
##Include options so that if the user wants to, they can save their list
##of numbers to a text file and read them back out later on.

def Averages(*nums):
    import math
    print('Enter "O" to save output ina file and "Q" to quit')
    options = input()
    if options.lower() == 'o':
        import statistics
        filename = 'average.txt'
        with open('filename', 'w') as f_obj:
            f_obj.write(f"\nThe 'mean / average' of list: {sum(nums) / len(nums)}\n"
                f"The Median of input list: {len(nums) / 2}.\n")
            f_obj.close()
    return sum(nums) / len(nums),  len(nums) / 2
    
    


