#from PIL.ImageColor import colormap
import PIL
from numpy import asarray
from pygame import *
from PIL import Image
import numpy as np
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
import cv2


imageColor = Image.open('C1W.png')
colorMap = asarray(imageColor)

imageHeight = Image.open('D1.png')
colorHeight = asarray(imageHeight)
rgb_im = imageColor.convert('RGB')
rgb_im2 = imageHeight.convert('RGB')

#colors = imageHeight.getpixel((0,0))
def colorRet(x,y):
    r, g, b = rgb_im.getpixel((x, y))
    return (r,g,b)
print(colorRet(100,100))
# def Render(p, height, horizon, scale_height, distance, screen_width, screen_height):
#     # Draw from back to the front (high z coordinate to low z coordinate)
#     for z in range(distance, 1, -1):
#         # Find line on map. This calculation corresponds to a field of view of 90°
#         pleft  = Point(-z + p.x, -z + p.y)
#         pright = Point( z + p.x, -z + p.y)
#         # segment the line
#         dx = (pright.x - pleft.x) / screen_width
#         # Raster line and draw a vertical line for each segment
#         for i in range(0, screen_width):
#             height_on_screen = (height - colorHeight[pleft.x, pleft.y]) / z * scale_height.y + horizon
#             DrawVerticalLine(i, height_on_screen, screen_height, colorMap[pleft.x, pleft.y] )#colormap[pleft.x, pleft.y]
#             pleft.x += dx
#
#
def heightRet(x,y):
    r, g, b = rgb_im2.getpixel((x, y))
    #mix= rgb/3
    mix=int((r+b+g)/3)
    maxHeght=800

    #map 255 is 50
    x=int((50*mix)/255)
    """return a single value that maps to height"""
    return x

import pygame
pygame.init()

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
White = (255, 255, 255)

def colorpicker(BLACK,BLUE,i):
    if i%2==0:
        return BLACK
    return BLUE
size = [600, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Voxel")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
distance=100
p=Point(300,300)
screen_width,screen_height=800,800
height, horizon, scale_height= 50, 120, 120

def drawIt():
    for z in range(distance, 1, -1):
        print(z)
        # Find line on map. This calculation corresponds to a field of view of 90°
        pleft  = Point(-z + p.x, -z + p.y)
        pright = Point( z + p.x, -z + p.y)
        # segment the line
        dx = int((pright.x - pleft.x) / screen_width)
        # Raster line and draw a vertical line for each segment
        for i in range(0, screen_width):
            height_on_screen = int((int(height) - int(heightRet(pleft.x, pleft.y) )) / z * scale_height + horizon)
            #print(height_on_screen)
            #print(i,colorHeight[pleft.x, pleft.y])
            #DrawVerticalLine(i, height_on_screen, screen_height, colorMap[pleft.x, pleft.y] )#colormap[pleft.x, pleft.y]
            pygame.draw.lines(screen, colorRet(pleft.x,pleft.y), False, [[i, 800], [i, height_on_screen]], 5)
            pleft.x += 0.9 #dx



while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    #clock.tick(10)

    # for event in pygame.event.get():  # User did something
    #     if event.type == pygame.QUIT:  # If user clicked close
    #         done = True  # Flag that we are done so we exit this loop
    # events = pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p.x -= 1
            if event.key == pygame.K_RIGHT:
                print("Right")
                p.x += 1
            if event.key == pygame.K_UP:
                p.y -= 1
            if event.key == pygame.K_DOWN:
                p.y += 1
    # Clear the screen and set the screen background
    screen.fill(White)
    #pygame.draw.lines(screen, BLACK, False, [[200, 300], [400, 400],[300, 200], [200, 300]], 5)


    # Draw a circle
    #pygame.draw.circle(screen, BLUE, [300, 300], 40)
    #def Render(p, height, horizon, scale_height, distance, screen_width, screen_height):
    #Render( Point(0, 0), 50, 120, 120, 300, 800, 600 )
    print(p.x,p.y)
    # for z in range(distance, 1, -1):
    #     # Find line on map. This calculation corresponds to a field of view of 90°
    #     pleft  = Point(-z + p.x, -z + p.y)
    #     pright = Point( z + p.x, -z + p.y)
    #     # segment the line
    #     dx = int((pright.x - pleft.x) / screen_width)
    #     # Raster line and draw a vertical line for each segment
    #     for i in range(0, screen_width):
    #         height_on_screen = int((int(height) - int(heightRet(pleft.x, pleft.y) )) / z * scale_height + horizon)
    #         print(height_on_screen)
    #         #print(i,colorHeight[pleft.x, pleft.y])
    #         #DrawVerticalLine(i, height_on_screen, screen_height, colorMap[pleft.x, pleft.y] )#colormap[pleft.x, pleft.y]
    #         pygame.draw.lines(screen, colorRet(pleft.x,pleft.y), False, [[i, 800], [i, height_on_screen]], 5)
    #         pleft.x += dx
    drawIt()






    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()




# Call the render function with the camera parameters:
# position, height, horizon line position,
# scaling factor for the height, the largest distance,
# screen width and the screen height parameter
#Render( Point(0, 0), 50, 120, 120, 300, 800, 600 )


