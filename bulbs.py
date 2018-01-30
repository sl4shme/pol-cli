import yeelight


class Bulbs():
    def __init__(self):
        self.bulbs = [yeelight.Bulb(i['ip'])
                      for i in yeelight.discover_bulbs()]

    def turn_on(self):
        for bulb in self.bulbs:
            bulb.turn_on()

    def turn_off(self):
        for bulb in self.bulbs:
            bulb.turn_off()

    def set_color_temp(self, temp):
        for bulb in self.bulbs:
            bulb.set_color_temp(temp)

    def set_default(self):
        for bulb in self.bulbs:
            bulb.set_default()

    def set_brightness(self, bright):
        for bulb in self.bulbs:
            bulb.set_brightness(bright)
