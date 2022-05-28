import pygame
import os
import sys
import random

def lose():
    pygame.quit()
    input("You lose\n")
    sys.exit()

def game():
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
    # if a spike is on the spawn point, move it to a random position
    for i in range(10):
        if x_spikes[i] == 400 and y_spikes[i] == 300:
            x_spikes[i] = random.randint(0, 800)
            y_spikes[i] = random.randint(0, 600)
    # if the spikes are right next to each other, move them to a random position
    for i in range(10):
        for j in range(10):
            if i != j:
                if x_spikes[i] == x_spikes[j] and y_spikes[i] == y_spikes[j]:
                    x_spikes[i] = random.randint(0, 800)
                    y_spikes[i] = random.randint(0, 600)
    # create window loop
    playerx = 100
    playery = 100
    # make varible for player health
    health = 3
    print('Health:' , str(health))

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
                if health == 1:
                    print('Health: 0')
                    lose()
                else:
                    health -= 1
                    print('Health:' , str(health))
                    playerx = 100
                    playery = 100

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


if __name__ == "__main__":
    game()