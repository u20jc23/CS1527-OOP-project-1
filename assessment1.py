
#  The following is a template of the design.
#  you will need to complete the definition of each class, including class attributes,
# instance attributes, and instance methods. However, please do not change the class 
# names provided below.

# IMPORTANT: In order to get your program pass the test, make sure your class constructors 
# use exactly the same parameter names as in the test examples provided at the end of this template. 

# ================Your codes start here=============
class Boat:
  
  __doc__ = 'Boat Class'

  all_boats = [] #keeps track of all boats

  #initialises the a boat object
  def __init__(self, co: str, br: str, yr: int, **kwargs):
    super().__init__(**kwargs)
    self.__colour = co
    self.__brand = br
    self.__year = yr
    Boat.all_boats.append(self) #adds newly created boats to all_boats

  #returns age of boat by calculating difference between current year and year
  def get_boat_age(self, cur_year: int) -> int:
    return cur_year - self.__year

  def __str__(self) -> str:
    return 'This Boat is of colour: {}, of the brand: {}, and of the year: {}'.format(self.__colour, self.__brand, self.__year)
#  pass


class Engine: 
  
  __doc__ = 'Engine Class For Boats'

  #initialises engine, assigning speed to engine depending on tech
  def __init__(self, tech: str, **kwargs):
    super().__init__(**kwargs)
    self.__tech = tech
    if tech == 'gas':
      self.__engine_speed = 80  
    elif tech == 'electric':
      self.__engine_speed = 20 

  #returns the speed of the engine
  def get_engine_speed(self) -> float :
    return self.__engine_speed

  def __str__(self) -> str:
    return "This Engine is of {} technology making it's maximum speed {} mph".format(self.__tech, self.__engine_speed)
# pass  


class Motorboat(Boat, Engine):
  
  __doc__ = 'Motorboat Class'

  #initialises a motorboat object, inheriting from boat and engine
  def __init__(self, fl: float, fe: float, **kwargs):
    super().__init__(tech = 'gas', **kwargs)
    self.__fuel_level = fl
    self.__fuel_efficiency = fe

  #returns the maximum speed
  def get_max_speed(self):
    return super().get_engine_speed()

  #returns the shortest time it takes to travel a distance d, if there isn't enough gas it returns the remaining distance
  def cal_travel_time(self, d: float) -> float:
    max_distance = self.__fuel_level * self.__fuel_efficiency
    if max_distance >= d:
      return d / self.get_max_speed()
    else:
      remaining_distance = d - max_distance
      print("This motorboat runs out of fuel {} miles away from the destination.".format(remaining_distance))
      return max_distance / self.get_max_speed()

  def __str__(self) -> str:
        return "This is a motorboat of the brand: {}, colour: {}, year: {}, technology: {}, maximum speed: {} mph, fuel level: {} gallons and fuel efficiency: {} mpg".format(
          self._Boat__brand, self._Boat__colour, self._Boat__year, self._Engine__tech, self.get_max_speed(), self.__fuel_level, self.__fuel_efficiency)
# pass


class Pedalboat(Boat):
  
  __doc__ = 'Pedalboat Class'

  #initialises pedalboat inheriting from boat
  def __init__(self, ps: float, **kwargs):
    super().__init__(**kwargs)
    self.__pedal_speed = ps

  #returns time it takes to cover a distance d 
  def cal_travel_time(self, d: float) -> float:
    return d / self.get_pedal_speed()

  #checks if the speed assigned to the pedalboat is correct and returns True if so as well as rounding up or down the value if not
  def check_speed(self) -> bool:
    if self.__pedal_speed < 10:
      self.__pedal_speed = 10
    elif self.__pedal_speed > 20:
      self.__pedal_speed = 20
    return 10 <= self.__pedal_speed <= 20

  #returns the pedal speed, if the pedal speed was not correct, it corrects the speed and returns that
  def get_pedal_speed(self) -> float:
    if self.__pedal_speed < 10:
      return 10
    elif self.__pedal_speed > 20:
      return 20
    return self.__pedal_speed

  def __str__(self) -> str:
    return "This is a pedalboat of the brand: {}, colour: {}, year: {} and pedal speed: {} mph".format(
        self._Boat__brand, self._Boat__colour, self._Boat__year, self.get_pedal_speed())
#  pass


class Eboat(Pedalboat, Engine):
  
  __doc__ = 'Eboat Class'

  #initialises eboat inheriting from pedalboat and engine
  def __init__(self, bt: float, **kwargs):
    super().__init__(tech = 'electric',**kwargs)
    self.__battery_time = bt

  #returns the maximum speed being pedaling and using the engine at the same time
  def get_max_speed(self):
    return super().get_pedal_speed() + super().get_engine_speed()

  #returns the travel time for a distance d by breaking down into two scenarios
  def cal_travel_time(self, d: float) -> float:
    distance_cov_engine = self.__battery_time * self.get_max_speed()
    #this is where the distance can be covered at the maximum speed
    if distance_cov_engine >= d:
      return d/self.get_max_speed()
    #if the distnace cannot be covered at max speed, it calculates the time covered at max and adds to that the remaing time to cover the distance
    else:
      return self.__battery_time + ((d-distance_cov_engine)/super().get_pedal_speed())

  def __str__(self) -> str:
    return "This is a boat of the brand: {}, colour: {}, year: {}, technology: {}, maximum speed: {} mph, battery time: {} hours".format(
        self._Boat__brand, self._Boat__colour, self._Boat__year, self._Engine__tech, self.get_max_speed(), self.__battery_time)
 # pass

# ============ End of your codes here ==================





# ============No modification beyond here =============
# the following is a list of test instances, please do not  modify them
if __name__ == '__main__':
  # arguments: co - colour, br - brand, yr - year, tech - technology used in engine
  boat1=Boat(co='Black', br='Trek', yr=2012)
  engine1=Engine(tech='gas')
  print(engine1.get_engine_speed())

  # arguments: co - colour, br - brand, yr - year, ps - pedal speed
  pedalboat1=Pedalboat(co='Red', br='GIANT', yr=2015, ps=15)
  pedalboat2=Pedalboat(co='Red', br='GIANT', yr=2015, ps=30)
  print(pedalboat1.get_pedal_speed())
  print(pedalboat2.get_pedal_speed())
  print(pedalboat1.cal_travel_time(300))

  # arguments: co - colour, br - brand, yr - year, ps - pedal speed, bt - battery time 
  eboat1=Eboat(co='Blue', br='Basis', yr=2018, ps=15, bt=10)
  print(eboat1.get_max_speed())
  print(eboat1.cal_travel_time(350))
  print(eboat1.cal_travel_time(650))

  # arguments: co - colour, br - brand, yr - year, fl - fuel level, fe - fuel efficiency
  motorboat1=Motorboat(co='Silver', br='YAMAHA', yr=2013, fl=40, fe=12)
  print(motorboat1.get_max_speed())
  print(motorboat1.cal_travel_time(300))
  print(motorboat1.cal_travel_time(600))

  # get the age of all bikes created
  for b in Boat.all_boats:
    print(b.get_boat_age(2023))
