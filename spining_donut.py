import pygame
import os
from math import cos,sin

WHITE = (255,255,255)
BLACK = (0,0,0)

RESOLUTION = W_HEIGHT,W_WIDTH = 300,300
FPS = 60

#screen settings
pixel_h= pixel_w = 7
screen_h = int(W_WIDTH/pixel_w)
screen_w = int(W_HEIGHT/pixel_h)
screen_size = screen_h*screen_w
x_pixel=y_pixel = 0

#rotation init
A,B=0,0

#lumination init
chars = ".,-~:;=!*#$@"

#Donut init
theta_spacing = 7
phi_spacing = 2
R1 = 10
R2 = 20
K2 = 50
K1 = screen_h * K2*3/(8*(R1+R2))
print(K1)

pygame.init()

window = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
pygame.display.set_caption("Spinning donut by ZiM0u")
font = pygame.font.SysFont("Arial",15)

def text(value, x, y):
    txt = font.render(str(value),True,WHITE)
    #center the text
    text_rect = txt.get_rect(center=(x,y))
    window.blit(txt,text_rect)

print(screen_w,screen_h,screen_size)

k = 0 #char selector
continuer= 1
while continuer:
    clock.tick(FPS)
    window.fill(BLACK)

    output = [' ']*(screen_size)
    zbuffer =[0]*(screen_size)

    #drawin donut
    for theta in range(0,628,theta_spacing):
        for phi in range (0,628,phi_spacing):

            cosA = cos(A)
            sinA = sin(A)
            cosB = cos(B)
            sinB = sin(B)


            
            costheta = cos(theta)
            sintheta = sin(theta)
            cosphi = cos(phi)
            sinphi = sin(phi)

            #x and y coordinates before revolving
            circlex = R2 +R1*costheta
            circley = R1*sintheta

            #3D x,y,z coordinates after rotation (matrice multiplication)
           # x = circlex*cosphi
            #y = circley
            #z = K2 + circlex*sinphi
            #ooz = 1/z # one over z

            x = circlex*(cosB*cosphi+sinA*sinB*sinphi)-circley*cosA*sinB
            y = circlex*(sinB*cosphi-sinA*cosB*sinphi)+circley*cosA*cosB
            z = K2+cosA*circley*sinphi+circley*sinA
            ooz = 1/z

            #camera projection (x and y projection)
            xp = int(screen_w/2+K1*ooz*x)
            yp = int(screen_h/2-K1*ooz*y)

            position = xp+screen_w*yp

            output[position]='*'

            #luminance
            L = cosphi * costheta * sinB - cosA * costheta * sinphi - sinA * sintheta + cosB *(cosA * sintheta - costheta * sinA * sinphi)

            if ooz >zbuffer[position]:
                zbuffer[position] = ooz#larger ooz means the pixel is closer to the viewer than what's already plotted
                luminance_index = int(L*8) #by 8 to get luminance_index range 0 to 11 (8*sqrt(2) =11)
                output[position] = chars[luminance_index if luminance_index >0 else 0]
    
    for y in range(1,screen_h+1):
        for x in range(1,screen_w+1):
            text(output[k],(x*pixel_w)-pixel_w//2,(y*pixel_h)-pixel_h//2)
            
            k+=1
    k=0
    A+=0.2
    B+=0.1

    pygame.display.update() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuer = 0
            
            
    
pygame.quit()
