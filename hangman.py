# This is my first time making a GUI, following a video tutorial

import sys
import math
import pygame
from pygame.locals import QUIT
import random

# This sets the basic gui window
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nelson's Hangman")

#button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65 #this is the corresponding number for the letter A.  Then we can add to the for loop, so 65+i each loop
for i in range(26):
  x = startx + GAP * 2 + ((RADIUS *2 + GAP) * (i %13)) #simulates having two rows
  y = starty + ((i //13) * (GAP + RADIUS * 2))
  letters.append([x, y, chr(A + i), True]) #chr = convert to character
  
#Fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 40)
WORD_FONT = pygame.font.SysFont("comicsans", 60)

# load images
images = []
for i in range(7): #this will happen 7 times, and i will +1 each time
  image = pygame.image.load("hangman" + str(i) + ".png") #standard naming is good.
  images.append(image)

# game variables
hangman_status = 0
words = ["SALOON", "PONY", "WESTERN", "ARIZONA", "MEXICO", "CALIFORNIA", "BONANZA", "TAHOE", "TEXAS", "WHISKEY", "GOLD", "SILVER"]
word = random.choice(words)
guessed = []

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# This sets the basics of the back end of the game
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
  win.fill(WHITE)

  #draw word
  display_word = ""
  for letter in word:
    if letter in guessed:
      display_word += letter + " "
    else:
      display_word += " _ "

  text = WORD_FONT.render(display_word, 1, BLACK)  
  win.blit(text, (400, 200))
  #draw buttons
  for letter in letters:
    x, y, ltr, visible = letter #split the values
    if visible:
      pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
      text = LETTER_FONT.render(ltr, 1, BLACK)
      win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    
  win.blit(images[hangman_status], (150, 100))
  pygame.display.update()  

def display_message(message):
    pygame.time.delay(2000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

#main while loop.
while run:
  clock.tick(FPS)
  
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        m_x, m_y = pygame.mouse.get_pos()
        for letter in letters:
          x, y, ltr, visible = letter
          if visible:
            dis = math.sqrt((x - m_x)**2 + (y - m_y)**2) #distance btw mouse position and button
            if dis < RADIUS:
              letter[3] = False
              guessed.append(ltr)
              if ltr not in word:
                hangman_status += 1

  draw()

  won = True
  for letter in word:
    if letter not in guessed:
      won = False
      break

  if won:
    display_message("You WON!")
    break

  if hangman_status == 6:
    display_message("You LOST!")
    break

pygame.quit()