import pygame
import os
import sys
import random


def game():
    print("You are a helecopter pilot. One day you are assigned a mission to attack a russian base")
    print("You are in a helicopter and you have to land on the base.")
    # open a window with a size of 800x600
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    # set the title of the window
    pygame.display.set_caption("Copoilet")
    # set icon to python logo
    pygame.display.set_icon(pygame.image.load("python.png"))
    # show base.jpg
    base = pygame.image.load("base.jpg")
    # load spikes.png
    spikes = pygame.image.load("spikes.png")
    # create 10 variables for x and y coordinates of the spikes
    x_spikes = [random.randint(0, 800) for i in range(10)]
    y_spikes = [random.randint(0, 600) for i in range(10)]
    # create window loop
    playerx = 100
    playery = 100
    while True:
        # fill the screen with a color white
        screen.fill((255, 255, 255))
        # show spikes.png in random places
        for i in range(0, 5):
            screen.blit(spikes, (x_spikes[i], y_spikes[i]))
        # draw base.jpg on the screen
        screen.blit(base, (600, 400))
        # if touching base print "You win"
        if playerx > 600 and playery > 400:
            os.system("cls")
            pygame.quit()
            input("You win\n")
            sys.exit()
        # if touching spikes print "You lose"
        for i in range(0, 5):
            if playerx > x_spikes[i] and playerx < x_spikes[i] + 100 and playery > y_spikes[i] and playery < y_spikes[i] + 100:
                os.system("cls")
                pygame.quit()
                input("You lose\n")
                sys.exit()
        # draw a rectangle as for the player
        pygame.draw.rect(screen, (0, 255, 0), (playerx, playery, 50, 50))
        # update the window
        pygame.display.update()
        
        for event in pygame.event.get():
            
            # implement a movment system

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    playery -= 5
                if event.key == pygame.K_s:
                    playery += 5
                if event.key == pygame.K_a:
                    playerx -= 5
                if event.key == pygame.K_d:
                    playerx += 5
                if event.key == pygame.K_k:
                    playery -= 20
                if event.key == pygame.K_j:
                    playery += 20
                if event.key == pygame.K_h:
                    playerx -= 20
                if event.key == pygame.K_l:
                    playerx += 20
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


print("Welcome to Copoilet!")
play = input("Do you want to play?[y/n]: ")
if play.lower() == "y":
    game()
else:
    print("Bye!")