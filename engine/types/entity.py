import math

class GameEntity():
    def __init__(self, id):
        self.id = id
        self.anim = 'still'
        self.xp = 0.0
        self.yp = 0.0
        self.zp = 0.0
        self.xa = 0.0
        self.ya = 0.0
        self.za = 0.0
        self.xt = 0.0
        self.yt = 0.0
        self.zt = 0.0
        self.xr = 0.0
        self.yr = 0.0
        self.zr = 0.0

    def animate(self):
        if self.anim == 'still':
            self.xt = 0.0
            self.yt = 0.0
            self.zt = 0.0
            self.xr = 0.0
            self.yr = 0.0
            self.zr = 0.0

        elif self.anim == 'forward':
            self.xt = 0.0
            self.yt = -math.sin(self.xa)
            self.zt = math.cos(self.xa)
            self.xr = 0.0
            self.yr = 0.0
            self.zr = 0.0

        elif self.anim == 'backward':
            self.xt = 0.0
            self.yt = math.sin(self.xa)
            self.zt = -math.cos(self.xa)
            self.xr = 0.0
            self.yr = 0.0
            self.zr = 0.0

        self.xp += self.xt
        self.yp +=  self.yt
        self.zp +=  self.zt
        print(self.zp)
