class Car:
    def __init__(self, registration):
        self.registration = registration
        self.acceleration = 10
        self.velosity = 0
        self.in_motion = False

    def drive(self):
         self.in_motion = True

    def accelerate(self):
        self.velosity += self.acceleration

    def accelerate_n_times(self, times):
        for i in range(times):
            self.accelerate()

    def stop(self):
        self.velosity = 0
        self.in_motion = False

if __name__ == '__main__':
    car_1 = Car('DX XYT')
    print(f'Registration: {car_1.registration}')
    print(f'Car in motion : {car_1.in_motion}')
    car_1.drive()
    print(f'Car in motion : {car_1.in_motion}')
    car_1.accelerate()
    car_1.accelerate()
    print(f'Car velosity : {car_1.velosity}')

    car_1.stop()
    print(f'Car velosity : {car_1.velosity}')
    print(f'Car in motion : {car_1.in_motion}')

