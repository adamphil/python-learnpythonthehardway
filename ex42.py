## Animal is-a object (yes, sort of confusing)
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog (as self) has-a name
		self.name = name

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat (self) has-a name
		self.name = name

## Person is-a Object
class Person(object):

	def __init__(self,name):
		## Person has-a Name
		self.name = name

		## Person has-a Pet of some sort
		self.pet = None

## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		##
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass

## is-a animal: Dog, has-a name: Rover
rover = Dog("Rover")

## is-a animal: Cat, has-a name: Satan
satan = Cat("Satan")

## is-a object: Person, has-a name: Mary
mary = Person("Mary")

## mary has-a pet, satan
mary.pet = satan

## is-a Person: Employee, has-a name: Frank, has-a salary: 120000
frank = Employee("Frank", 120000)

## frank has-a pet, rover
frank.pet = rover

# flipper is-a object: Fish
flipper = Fish()

# crouse is-a Fish: Salmon
crouse = Salmon()

# harry is-a Fish: Halibut
harry = Halibut()

