'''
This homework is a fulfillment of the Class lecture. showing how to use this to 
resolve the usage of car/plane for noting the service management period based on define service time
'''
#using the random dll to assist in randomising checks for car/plane usage
import random 

class Vehicle():
    # define mandatory values make, model, year & weight 
    def __init__(self, make, model , year, weight, needsMaintenance = False, tripsSinceMaintenance = 0):
        self.sMake(make)
        self.sModel(model)
        self.sYear(year)
        self.sWeight(weight)
        self.sneedsMaintenance(needsMaintenance)
        self.stripsSinceMaintenance(tripsSinceMaintenance)

    # define getters
    def gMake(self):
        return self.make

    def gModel(self):
        return self.model

    def gYear(self):
        return self.year

    def gWeight(self):
        return self.weight

    def isneedsMaintenance(self):
        return self.needsMaintenance

    def gtripsSinceMaintenanance(self):
        return self.tripsSinceMaintenance

    # define setters
    def sMake(self, make):
        self.make = make

    def sModel(self, model):
        self.model = model
    
    def sYear(self, year):
        self.year = year

    def sWeight(self, weight):
        self.weight = weight

    def sneedsMaintenance(self, needsMaintenance):
        self.needsMaintenance = needsMaintenance

    def stripsSinceMaintenance(self, tripsSinceMaintenance):
        self.tripsSinceMaintenance = tripsSinceMaintenance 
    
    def rtripsSinceMaintenance(self):
        self.stripsSinceMaintenance(0)

    def __str__(self):
        return 'Car Make : ' + self.gMake() + '\nCar Model: ' + self.gModel() + '\nManufacture Year: ' + str(self.gYear()) + '\n Car Weight: ' + str(self.gWeight()) + 'Kg\nRequires Maintenance?: ' + str(self.isneedsMaintenance()) + '\nLast trip since maintenance: ' + str(self.gtripsSinceMaintenanance())
    
    # define method for trip counting
    def tripsCounter(self):
        exitingTrips = self.gtripsSinceMaintenanance()
        exitingTrips += 1
        self.stripsSinceMaintenance(exitingTrips)
    
    

class Car(Vehicle):

    def __init__(self, make, model, year, weight, isDriving=False, maxtripsb4Maintenance=100):
        Vehicle.__init__(self, make, model, year, weight)
        self.sDriving(isDriving)
        self.stripsb4Maintenance(maxtripsb4Maintenance)

    def __str__(self):
        return 'Car: \n' + Vehicle.__str__(self)
    

    # define setters
    def sDriving(self, isDriving):
        self.isDriving = isDriving

    def stripsb4Maintenance(self, maxtripsb4Maintenance):
        self.maxtripsb4Maintenance = maxtripsb4Maintenance

      # define getters
    def isDrivingCurrently(self):
        return self.isDriving

    def gmaxTripsb4Maintenance(self):
        return self.maxtripsb4Maintenance


    # define Car Operations
    
    def drive(self):
        if self.isDrivingCurrently() == False:
            # show the car is driving
            self.sDriving(True)
            
        
    def stop(self):
        if self.isDrivingCurrently() == True:
            # show car stopped
            self.sDriving(False)
            # increment trips counter
            self.tripsCounter()
            # check if car requires maintenance by this trip
            self.needsMaintenanceStatus()

    def needsMaintenanceStatus(self):
        if self.gtripsSinceMaintenanance() >= self.gmaxTripsb4Maintenance():
            self.sneedsMaintenance(True)

    def repair(self):
        # reset the service maintenance value
        self.rtripsSinceMaintenance()
        # set the needsMaintenance value to False
        self.sneedsMaintenance(False)


class Plane(Vehicle):
    def __init__(self, make, model, year, weight, isFlying = False, maxtripsb4Maintenance = 100 ):
        Vehicle.__init__(self, make, model, year, weight)
        self.sFlying(isFlying)
        self.stripsb4Maintenance(maxtripsb4Maintenance)

    def __str__(self):
        return 'Plane:\n' + Vehicle.__str__(self)

    # define getters
    def isFlyingCurrently(self):
        return self.isFlying
    
    def gmaxTripsb4Maintenance(self):
        return self.maxtripsb4Maintenance

    # define setters
    def sFlying(self, isFlying):
        self.isFlying = isFlying

    def stripsb4Maintenance(self, maxtripsb4Maintenance):
        self.maxtripsb4Maintenance = maxtripsb4Maintenance


    # define Plane Operations
    def needsMaintenanceStatus(self):
        if self.gtripsSinceMaintenanance >= self.gmaxTripsb4Maintenance():
            self.sneedsMaintenance(True)

    def repair(self):
        if self.isneedsMaintenance():
            self.rtripsSinceMaintenance() 
            self.sneedsMaintenance(False)

    def ableToFly(self):
        if self.isneedsMaintenance() == True:
            return False
        return True

    def fly(self):
        if self.ableToFly() == True and self.isFlyingCurrently() == False:
            self.sFlying(True)
    
    def land(self):
        if self.isFlyingCurrently() == True:
            self.sFlying(False)
            self.tripsCounter()
            # check if this plane requires maintenance
            if self.gtripsSinceMaintenanance() >= self.gmaxTripsb4Maintenance():
                self.sneedsMaintenance(True)



# Vehicle Simulation

# Define Car Simulation Flow
def simulateCars(carTrips = 100, limitb4Maintenance = 50):
    print('='*20 + '\nCar Test\n' + '='*20)
    Innoson = Car(make = 'Innoson', model = 'Fox', year = 2014, weight = 1090, isDriving=False, maxtripsb4Maintenance=limitb4Maintenance)
    Volkswagen = Car(make = 'Volkswagen', model = 'Tiguan', year = 2014, weight = 2135, isDriving=False, maxtripsb4Maintenance=limitb4Maintenance)
    Tesla = Car(make = 'Tesla', model = 'Model X', year = 2013, weight = 2455, isDriving=False, maxtripsb4Maintenance=limitb4Maintenance)

    # print car list
    print(Innoson)
    print(Volkswagen)
    print(Tesla)
       
    # define an array of the car list
    cars = [Innoson, Volkswagen, Tesla]
    
    for trips in range(carTrips):
        r = random.randint(0,len(cars) -1) 
        # change selected car state 
        print('CAR TEST: ' + cars[r].gModel() + ' Seleted')
        if cars[r].isDrivingCurrently() == True:
            cars[r].stop()
            print('CAR TEST: ' + cars[r].gModel() + ' Stopped, Trips since last maintenance: ' + str(cars[r].gtripsSinceMaintenanance()))
        else:
            print('CAR TEST: ' + cars[r].gModel() + ' Started')
            cars[r].drive()

    # print car current state after simulation
    print(Innoson)
    print(Volkswagen)
    print(Tesla)

# Define Planes Simulation Flow
def simulatePlanes(flightTrips = 100, maxflightTripsb4Maintenance = 50):
    print('='*20 + '\nPlane Test\n' + '='*20)
    # list planes and features
    boeing = Plane('Boeing', '787', 2009, 215000, False, maxflightTripsb4Maintenance)
    airbus = Plane('Air Bus', 'AirBus380', 2005, 183500, False, maxflightTripsb4Maintenance)
    bombardier = Plane('Bombardier Aerospace', 'CRJ900', 1999, 84500, False, maxflightTripsb4Maintenance)

    # print plane list
    print(boeing)
    print(airbus)
    print(bombardier)

    # define plane array list
    planes = [boeing, airbus, bombardier]
    
    for trips in range(flightTrips):
        p = random.randint(0, len(planes) -1) 
        print('PLANE TEST: selected plane' + planes[p].gModel())
        if planes[p].isFlyingCurrently() == False:
            # Start flight simulation flow as well as checking if maintenance is needed..
            print('PLANE TEST: ' + planes[p].gModel() + ' Commencing takeoff...')
            if planes[p].isneedsMaintenance() == True:
                print('PLANE TEST: Ensure ' + planes[p].gModel() + ' before commencing operations')
                planes[p].repair()
            planes[p].fly()
            print('PLANE TEST: ' + planes[p].gModel() + ' has taken off...')
        else:
            planes[p].land()
            print('PLANE TEST: ' + planes[p].gModel() + ' has landed, this plane has made ' + str(planes[p].gtripsSinceMaintenanance()) + ' trips since last maintenance job')

    print(boeing)
    print(airbus)
    print(bombardier)    

# initiate simulation run.
simulateCars(carTrips=100, limitb4Maintenance=10)
simulatePlanes(flightTrips=100, maxflightTripsb4Maintenance=10)