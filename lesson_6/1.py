import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def __init__(self, r = 'red', y='yellow', g='green'):
        self.__r = 'red'; self.__y='yellow'; self.__g='green'

    def running(self):
        i = 0
        while i < 5:
            for el in TrafficLight.__color:
                if el == 'red':
                    print(el)
                    time.sleep(7)
                elif el == 'yellow':
                    print(el)
                    time.sleep(2)
                elif el == 'green':
                    print(el)
                    time.sleep(5)
            i += 1


traffic = TrafficLight()
traffic.running()
