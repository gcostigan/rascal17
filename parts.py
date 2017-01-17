import wiringpi

class trencher:
    def tilt(self, servo, amount):
        self.servo = servo
        self.amount = amount
        return

    def spin(self, servo, amount):
        self.servo = servo
        self.amount = amount
        return

    def origin(self):
        return

    def manual(self):
        # Loop to be called when the operator needs manual overdrive
        return


class ice_extracter:
    def heat(self, amount):
        self.amount = amount
        return

    def move_z(self, amount):
        self.amount = amount
        return


class railing:
    def move_x(self, amount):
        self.amount = amount
        return

    def move_y(self, amount):
        self.amount = amount
        return
