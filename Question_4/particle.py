class Particle:
    def __init__(self):
        # should randomize position x from 0 to width
        self.pos_x = random(0, width)
        # position y from 0 to height
        self.pos_y = random(0, height)
        # velocity x from -5 to 5
        self.speed_x = random(-5, 5)
        # velocity y from -5 to 5
        self.speed_y = random(-5, 5)


    def move(self):
        # Should move the particle according to its velocity.
        self.pos_x = self.pos_x + self.speed_x
        self.pos_y = self.pos_y + self.speed_y
        #Should wrap around the screen if off limits.
        if self.pos_x < 0:
            self.pos_x = width
        if self.pos_x > width:
            self.pos_x = 0
        if self.pos_y < 0:
            self.pos_y = height
        if self.pos_y > height:
            self.pos_y = 0 
             
           
    def draw(self):
        # Should draw a circle where the particle is.
        circle(self.pos_x, self.pos_y, 15)
