from binary import *

class Chain:
    def __init__(self,Abin, Bbin):
        self.A = Abin
        self.B = Bbin

    def apply2(self,pic, x,y):
        matches = self.A.apply(pic, x,y)
        if len(matches) == 0:
            return 0
        for match in matches:
            res = self.B.apply2(pic, match.x, match.y)
            return res
