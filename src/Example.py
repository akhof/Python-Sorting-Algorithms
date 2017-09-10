from PySortAlgos import *

def example_1():
    persons = {"Thomas":21, "Ursula":58, "Mike":19, "Max":30, "Tina":21}
    
    person_sortedKeysByAge1 = BubbleSort(key=lambda p: persons[p]).sort(persons.keys())
    person_sortedKeysByAge2 = QuickSort(key=lambda p: persons[p]).sort(persons.keys())
    
    print("Sorted with BubbleSort (stable):")
    for key in person_sortedKeysByAge1:
        print("{} ({})".format(key, persons[key]))
    
    print("\nSorted with QuickSort (not so stable):")
    for key in person_sortedKeysByAge2:
        print("{} ({})".format(key, persons[key]))

def example_2():
    class Person(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __str__(self, *args, **kwargs):
            return "{} ({})".format(self.name, self.age)
    
    persons = [Person("Thomas", 21), Person("Ursula", 58), Person("Mike", 19), Person("Max", 30), Person("Tina", 21)]
    
    persons_sortedByName = BubbleSort(compare=lambda x,y: 0 if x==y else (-1 if x<y else 1), key=lambda p: p.name.upper()).sort(persons)
    persons_sortedByAge = BubbleSort(key=lambda p: p.age).sort(persons)
    
    
    print("Index\tpre sorted\tsorted by age\tsorted by name")
    for i in range(len(persons)):
        print("{}\t{}\t{}\t{}".format(i, persons[i], persons_sortedByAge[i], persons_sortedByName[i]))


if __name__ == "__main__":
    example_1()
    example_2()