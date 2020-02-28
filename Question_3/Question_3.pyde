import random
import particle


def setup():
    global Balls
    Balls = []
    for i in range (10): 
        Ball = particle.Particle()
        Balls.append(Ball)
        
       
    size(400,400)
    background(0)
     
  
def draw():
    background(0)
    stroke(255) 
    global Balls
    for i in range(len(Balls)):
        Ball = Balls[i]
        Ball.draw()
        Ball.move()
        
        
        
