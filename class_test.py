#!/usr/bin/env python3
# tmp file to practice writing classes


class Cars:
    def __init__(self, color, price):
        self.color = color
        self.price = price

    def __repr__(self):
        return f'{self.color}, {self.price}'

    def oil_change(self):
        print('Change your oil every 4K miles!')

    def new_tire(self):
        print('Time for some new tires!')

    def tune_up(self):
        print('Get a tune-up before its too late!')


class Ford(Cars):
    pass


if __name__ == '__main__':
    mustang = Cars('blue', 34000)
    print(mustang)
    mustang.oil_change()



