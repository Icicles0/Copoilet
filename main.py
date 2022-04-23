import pygame
import os
import sys

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
    # create window loop
    playerx = 100
    playery = 100
    while True:
        # fill the screen with a color red
        screen.fill((255, 0, 0))
        # draw base.jpg on the screen
        screen.blit(base, (600, 400))
        # if touching base print "You win"
        if playerx > 600 and playery > 400:
            os.system("cls")
            pygame.quit()
            input("You win\n")
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
                    playery -= 5
                if event.key == pygame.K_j:
                    playery += 5
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