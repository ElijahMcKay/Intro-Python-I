# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
# class Robot:
#     def __init__(self, name, color, weight): # constructor function syntax in python.  We still need the "self" arg, 
#         self.name = name
#         self.color = color
#         self.weight = weight
#     def introduce_self(self): # method of a class, we have to add self as an arg to methods
#         print("My name is " + self.name, self.color, self.weight) # like "this" in Java/Javascript

# r1 = Robot() # default constructor to instantion a new object of a class
# r1.name = "Tom" # this is how to set attributes for each object
# r1.color = "red"
#r1.weight = 30
# This is not an optimal way to set attributes, it's easy to make mistakes
# r1 = Robot("Elijah", "Purple", 200)
# r1.introduce_self()


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
        # print(self)
    def __str__(self):
        return 'the location is {self.name} and the coordinates are {self.lat} by {self.lon}'.format(self = self)


wp = Waypoint("Hello", 100, 200)

print(wp.lat, wp.name, wp.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?


class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        return 'the location is {self.name}, the size is {self.size} and the coordinates are {self.lat} by {self.lon}'.format(self = self)

geocache = Geocache("Richard", "hard", 135, 1, 2409)

# print(geo.lat, geo.lon, geo.name, geo.difficulty)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

waypoint = Waypoint('Catacombs', 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

geocache = Geocache(44.052137, 121.41556, "Newberry Views", 1.5, 2)
# Print it--also make this print more nicely
print(geocache)










# example from Youtube
# class Tweet: # the class is like a "factory" that provides default behavior
#     pass # most basic class

# a = Tweet() # calling a class, a is known as an instance object (convention is to start with lowercase letters)

# a.message = "140 characters" # one way of assigning attributes to a class.  These stay and die with the instance

# # print(Tweet.message) # this won't print anything, because we have not instantiated an instance object of this class yet
# #print(a.message) # this will, because we've instantiated the instance object "a"

# b = Tweet() # this is entirely different from a

# b.message = "different message"

# print(b.message)

# redefining the Tweet class to include a dunder init method, aka a constructor method

# class Tweet:
#     def __init__(self, message):
#         self.x = message

# a = Tweet('something here')

# #print(a) # "__init__() takes 0 positional arguments but 1 was given" error even though none was provided

# # WHEN A CLASS IS CALLED, THE INSTANCE IS ALWAYS PASSED AS THE FIRST ARGUMENT

# # Now that self is added, this will work
# print(a.x)

# b = Tweet("another instanct")

# print(b.x)