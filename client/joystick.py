import pygame
import numpy as np

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    

def getAngle(y, x):
    angle = np.arctan2(x, y)
    if (angle <= 0):
        angle = (2*np.pi+angle)
    return angle*360/(2*np.pi) - 275

pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

pygame.joystick.init()
    
textPrint = TextPrint()

while done == False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
            
    screen.fill(WHITE)
    textPrint.reset()

    joystick_count = pygame.joystick.get_count()

    textPrint.print(screen, "Number of joysticks: {}".format(joystick_count) )
    textPrint.indent()
    
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
        textPrint.print(screen, "Joystick {}".format(i) )
        textPrint.indent()
    
        name = joystick.get_name()
        textPrint.print(screen, "Joystick name: {}".format(name) )

        axes = joystick.get_numaxes()
        textPrint.print(screen, "Number of axes: {}".format(axes) )
        textPrint.indent()
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
        textPrint.unindent()
            
        buttons = joystick.get_numbuttons()
        textPrint.print(screen, "Number of buttons: {}".format(buttons) )
        textPrint.indent()

        for i in range( buttons ):
            button = joystick.get_button( i )
            textPrint.print(screen, "Button {:>2} value: {}".format(i,button) )
        textPrint.unindent()

        hats = joystick.get_numhats()
        textPrint.print(screen, "Number of hats: {}".format(hats) )
        textPrint.indent()

        for i in range( hats ):
            hat = joystick.get_hat( i )
            textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)) )

        linearKey = joystick.get_axis(2)
        stopKey = joystick.get_button(0)
        exitKey = joystick.get_button(1)
        axisX = joystick.get_axis(0)
        axisY = joystick.get_axis(1)
        turnAngle = getAngle(axisX, axisY)

        if (linearKey < -0.001):
            print("Forward")
            #ws.send("forward")
        elif (linearKey > 0.001):
            print("Backward")
            #ws.send("backward")

        if (stopKey > 0):
            print("Stop")
            #ws.send("stop")

        if (exitKey > 0):
            print("Exit")
            done = True
        if (abs(axisX) > 0.001 and abs(axisY) > 0.001):
            if (0 < turnAngle < 90):
                print("Turn Left with Angle:", turnAngle)
            elif (-90 < turnAngle < 0):
                print("Turn Right with Angle:", turnAngle)

        textPrint.unindent()
        
        textPrint.unindent()

    pygame.display.flip()

    clock.tick(20)

pygame.quit ()