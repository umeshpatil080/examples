#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pumesh
#
# Created:     08/10/2017
# Copyright:   (c) pumesh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Celsius:
    def __init__(self, temperature = 0):
        #self.temperature = temperature
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Get temprature")
        return self.__temperature

    def set_temperature(self, value):
        if(value < -273):
            raise ValueError("Temprature below -273 is not possible")
        print("Setting temprature")
        self.__temperature = value

    temperature = property(get_temperature, set_temperature)




def main():
    c = Celsius(32)


if __name__ == '__main__':
    main()
