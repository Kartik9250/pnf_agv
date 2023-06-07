#!/usr/bin/env python3

class BitManipulation:
    def __init__(self):
        self.hex1 = 0
        self.hex2 = 0
        self.dec1 = 0
        self.dec2 = 0
        self.p = 0
        self.bc = 0
        self.b1 = 0
        self.b2 = 0
        self.l1 = []
        self.bl = []
        self.y_hex1 = 0
        self.y_hex2 = 0
        self.x_hex1 = 0
        self.x_hex2 = 0
        self.y_dec1 = 0
        self.y_dec2 = 0
        self.xp = 0
        self.angvalue = 0
        self.yp = 0
        self.angvalue = 0
        self.finalbl = 0
    def rightS(self, hexi):
        self.hex1 = hexi[0:2]
        self.hex2 = hexi[2:4]
        self.dec1 = int(self.hex1, 16)
        self.dec2 = int(self.hex2, 16)

        self.bc = bin(int(hexi, 16))[2:]

        self.b1 = bin(self.dec1)[2:]
        self.b2 = bin(self.dec2)[2:]

        self.l1 = [*self.b1]
        self.bl = [*self.bc]

        for i in range(len(self.bc)):
            try:
                if i == 0:
                    self.bl[i] = 0
                else:
                    self.p = self.l1[i - 1]
                    self.bl[i] = self.p
            except:
                break

        self.finalbl = ''.join(map(str, self.bl))
        self.anglevalue = int(self.finalbl, 2)
        return self.anglevalue
    def x_pos(self, x_hex):
        if x_hex[0:2] == "00" and x_hex[4:6] != "00":
            return self.rightS(x_hex[4:])/10

        elif x_hex[0:2] != "07":
            return int(str(x_hex)[6:], 16)/10

        else:
            self.x_hex1 = int(str(x_hex)[2:4], 16)
            self.x_hex2 = int(str(x_hex)[6:8], 16)
            self.xp = -self.x_hex1 + self.x_hex2
            return self.xp/10

    def y_pos(self, y_hex):
        self.y_hex1 = str(y_hex)[0:2]
        self.y_hex2 = str(y_hex)[2:4]
        self.y_dec1 = int(str(self.y_hex1), 16)
        self.y_dec2 = int(str(self.y_hex2), 16)
        if self.y_dec1 < self.y_dec2:
            return self.y_dec2/10
        elif self.y_dec1 > self.y_dec2:
            self.yp = self.y_dec2 - self.y_dec1
            return self.yp/10

    def angle_value(self, angle_hex):
        return self.rightS(angle_hex)

    def angle_degree(self, angle_hex):
        return self.rightS(angle_hex)/10

    def tag_data(self, tag_hex):
        if str(tag_hex) == "40":
            return True
        else:
            return False














