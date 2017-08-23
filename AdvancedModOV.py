# Collections overview and practice

from collections import Counter, defaultdict, OrderedDict, namedtuple
import datetime

# counter a subclass that helps count hashable objects

l = [1, 1, 1, 5, 2, 66, 5, 8, 5, 5, 1321, 654, 1, 5]

print(Counter(l))

ph = "This is a sentence that acts as a test subject so we can count count count count the number of words as follows"

C = Counter(ph.split())
print(C)

print(C.most_common(3))

"""
Usual patterns when using the Counter object
sum(C.values())         C.clear()
list(C)                 set(C)
dict(C)                 C.items()
Counter(dict(pair_list()))          C.most_common() takes a number as argument indicating how many logs to return, arg can be negative to return the least common instead of most
C += Counter()                                      removing zero and negative counts if any
"""

D1 = defaultdict(lambda: 0)

D1['A']
D1['B'] = 1

D2 = defaultdict(lambda: 0)

D2['B'] = 1
D2['A']

OD1 = OrderedDict()
OD1['C'] = 3
OD1['A'] = 1
OD1['B'] = 2

if D1 == D2:
    print("Dictionaries equal")
else:
    print("Dictionaries not equal")

OD = OrderedDict()
OD['A'] = 1
OD['B'] = 2
OD['C'] = 3

for k, v in OD.items():
    print(k, v)

OD1 = OrderedDict()
OD1['C'] = 3
OD1['A'] = 1
OD1['B'] = 2

if OD == OD1:
    print("Ordered Dictionaries equal")
else:
    print("Ordered Dictionaries not equal")

"""
The named tuples perform similar to objects, however they ARE tuples, althoough everything in Python is an object anyway
Named tuples, work better than normal tuples where they are much easier than normal ones in terms of keeping track of 
values
"""

Person = namedtuple("Person", "Name Age City Job")

Anderson = Person(Name="Anderson", Age=27, City="Chicago", Job="Physician")
Rey = Person(Name="Ret", Age=25, City="New York", Job="Software Engineer")

print(Anderson.Name, Anderson.Job, " In ", Anderson.City)
print(Rey.Name, Rey.Job, " In ", Rey.City)

# Date and time

Ti = datetime.time(10, 2, 55)
print(Ti)

Ti.hour
Ti.second
Ti.minute

# .....etc

print(datetime.time.min,
      datetime.time.max,
      datetime.time.resolution)

thisDay = datetime.date.today()
print(thisDay)

thisDay.timetuple()
# thisDay.day ....etc there is also the ability to replace
thisDay.replace(year=1992)



