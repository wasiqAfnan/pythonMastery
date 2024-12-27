'''
Polymorphism in Python refers to the ability of different objects to respond differently to
the same method or operation. It enables a single interface to represent different underlying
forms (data types or classes). Polymorphism is a key concept in object-oriented programming
that promotes flexibility and reusability.
'''

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

# Polymorphism
def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()

make_sound(dog)  # Output: Bark
make_sound(cat)  # Output: Meow

# explaination
'''
The function make_sound(animal) is defined to take an object (animal) as an argument.
Inside the function, it calls the method animal.sound().
This means that whatever object is passed to make_sound, 
it must have a sound() method. If not, Python will raise an AttributeError.
'''