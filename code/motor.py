import shift

DATA1, CLOCK1, SHIFT1 = 4, 5, 6
number_of_shift = 3
s = shift.ShiftRegister(DATA1, CLOCK1, SHIFT1, number_of_shift)

class Motor:
    def __init__(self, enb, dire, pul):
        self.enb = enb[0]*8 + enb[1]
        self.dir = dire[0]*8 + dire[1]
        self.pul = pul[0]*8 + pul[1]
        return

    def enable(self):
        data = s.string_data(self.enb)
        s.send_data(data)
        return

    def direction(self):
        data = s.string_data(self.dir)
        s.send_data(data)
        return

    def pulse(self):
        data = s.string_data(self.pul)
        s.send_data(data)
        return


