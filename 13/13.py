print('Task 1')

class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population
    
    def add(self, other):
        name = self.name + ' ' + other.name
        population = self.population  + other.population
        return Country(name, population)

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)


print('Task 2')


class Country:
    # adding custom attributes
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def __add__(self, other):
        return Country(self.name + ' ' + other.name, self.population + other.population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina

print(bosnia_herzegovina.name)
print(bosnia_herzegovina.population)


print('Task 3')


class Car():
    def __init__(self, brand: str, model: str, year: int, speed: int):
        self.brand = brand
        self.model = model
        self.year = year 
        self.speed = speed
    
    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def display_speed(self):
        return print(self.speed)
    
porsche = Car('Porsche', '911 Carrera', 1989, 15)
porsche.display_speed()
porsche.accelerate()
porsche.display_speed()
porsche.brake()
porsche.display_speed()
porsche.brake()
porsche.display_speed()
porsche.brake()
porsche.display_speed()
porsche.brake()
porsche.display_speed()


print('Task 4')


class Robot():
    def __init__(self, orientation : str, position_x: int, position_y: int,):
        self.orientation = orientation # (left, right, up, down)
        self.position_x = position_x
        self.position_y = position_y 


    def move(self, steps: int):
        try:
            if self.orientation == 'left':
                self.position_x -= steps
            elif self.orientation == 'right':
                self.position_x += steps 
            elif self.orientation == 'up':
                self.position_y += steps 
            else:
                self.position_y -= steps                            
        except Exception:
            print(f'Please use an int')
    
    def display_position(self):
        print(f'The orientation is {self.orientation}, position_x is {self.position_x}, position_x is {self.position_y},')

    def turn(self, turn_to: str):
        try:
            list_dir = ['right', 'down', 'left', 'up']
            orientation_n = list_dir.index(self.orientation)
            print(orientation_n)
            if turn_to == 'right' and orientation_n != 3:
                self.orientation = list_dir[orientation_n + 1]
            elif turn_to == 'right' and orientation_n == 3:
                self.orientation = 'right'                
            elif turn_to == 'left' and orientation_n != 0:
                self.orientation = list_dir[orientation_n - 1]
            else:
                self.orientation = 'up'         
        except Exception:
            print(f'Please use left or right')        


robot = Robot('up', 2, 5)
robot.move(5)
robot.display_position()
robot.turn('left')
robot.display_position()
robot.move(1)
robot.display_position()
robot.turn('right')

