import pygame, sys, os
from subprocess import call

# initializing the constructor
pygame.init()


font = "/home/surya/Documents/PyGameProject - Copy/font.otf"
debug_font = "/home/surya/Documents/PyGameProject - Copy/debug_font.otf"
conflict_font = "/home/surya/Documents/PyGameProject - Copy/conflict_font.ttf"
clock = pygame.time.Clock()


# screen resolution
res = (1366,768)
width = 1366
height = 768

# opens up a window
screen = pygame.display.set_mode(res)

# background
bg_img = pygame.image.load("/home/surya/Documents/PyGameProject - Copy/bg.jpg")
bg_img = pygame.transform.scale(bg_img,(1366,768))
bg2 = pygame.image.load("/home/surya/Documents/PyGameProject - Copy/bg2.jpg")
bg2 = pygame.transform.scale(bg2,(1366,768))
death = pygame.image.load("/home/surya/Documents/PyGameProject - Copy/screenshot.png")
death = pygame.transform.scale(death,(1366,768))

# define the RGB value for white,
# green, yellow, orange colour
color = (255,255,255)
white=(255, 255, 255)
yellow=(255, 255, 0)
green=(0, 255, 255)
orange=(255, 100, 0)
black = (0,0,0)
done = False

menu_font = pygame.font.Font(font, 132)
small_menu_font = pygame.font.Font(font, 100)
back_button_font = pygame.font.Font(font, 50)
button_font = pygame.font.Font(debug_font, 80)
death_font = pygame.font.Font(conflict_font, 80)

 
class Button():
    #prepares and renders the button in the specified place
	def __init__(button, image, pos, text_input, font, base_color, hovering_color):
		button.image = image
		button.x_pos = pos[0]
		button.y_pos = pos[1]
		button.font = font
		button.base_color, button.hovering_color = base_color, hovering_color
		button.text_input = text_input
		button.text = button.font.render(button.text_input, True, button.base_color)
        #if we don't set an image as the bg, this will cause the text to be standalone
		if button.image is None:
			button.image = button.text
		button.rect = button.image.get_rect(center=(button.x_pos, button.y_pos))
		button.text_rect = button.text.get_rect(center=(button.x_pos, button.y_pos))

	def update(button, screen):
		if button.image is not None:
			screen.blit(button.image, button.rect)
		screen.blit(button.text, button.text_rect)
    
    #checks to see if the position of your mouse is in the x and y range of the button
	def checkForInput(button, position):
		if position[0] in range(button.rect.left, button.rect.right) and position[1] in range(button.rect.top, button.rect.bottom):
			return True
		return False
    
    #if the position if your mouse is over the button, it will change the colour
	def changeColor(button, position):
		if position[0] in range(button.rect.left, button.rect.right) and position[1] in range(button.rect.top, button.rect.bottom):
			button.text = button.font.render(button.text_input, True, button.hovering_color)
		else:
			button.text = button.font.render(button.text_input, True, button.base_color)

"""# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()"""


def main_menu():
    while True:
        screen.blit(bg_img, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = menu_font.render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(700, 100))

        LESSON_BUTTON = Button(image=pygame.image.load("/home/surya/Documents/PyGameProject - Copy/Large_Rect.png"), pos=(700, 250), text_input="Lesson", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
        PLAY_BUTTON = Button(image=pygame.image.load("/home/surya/Documents/PyGameProject - Copy/Small_Rect.png"), pos=(700, 400), text_input="Play", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
        QUIZ_BUTTON = Button(image=pygame.image.load("/home/surya/Documents/PyGameProject - Copy/Small_Rect.png"), pos=(700, 550), text_input="Quiz", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
        RESULTS_BUTTON = Button(image=pygame.image.load("/home/surya/Documents/PyGameProject - Copy/Large_Rect.png"), pos=(400, 700), text_input="Results", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("/home/surya/Documents/PyGameProject - Copy/Quit_Rect.png"), pos=(1000, 700), text_input="EXIT", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [LESSON_BUTTON, PLAY_BUTTON, QUIZ_BUTTON, RESULTS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LESSON_BUTTON.checkForInput(MENU_MOUSE_POS):
                    lesson()
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIZ_BUTTON.checkForInput(MENU_MOUSE_POS):
                    quiz()
                if RESULTS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    results()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()



def lesson():
    #call(["python", "C:/Users/Surya/Documents/PyGameProject/test_video.py"])
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        PLAY_TEXT = menu_font.render('Lesson Goes Here', True, white)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(690, 260))
        screen.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_BACK = Button(image=None, pos=(1200, 700), text_input="BACK", font=back_button_font, base_color="White", hovering_color="Green")
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                main_menu()

        pygame.display.update()

def play():
    #call(["python", "C:/Users/Surya/Documents/PyGameProject/lore_video.py"])
    while True:
        screen.blit(bg2, (0,0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()


        PLAY_TEXT = small_menu_font.render('what  will  you  do', True, white)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(690, 100))
        screen.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_WALK = Button(image=None, pos=(700, 400), text_input="Keep Walking", font=button_font, base_color="#d7fcd4", hovering_color="white")
        PLAY_MOMENT = Button(image=None, pos=(700, 600), text_input="Take a Moment to Collect your Thoughts", font=button_font, base_color="#d7fcd4", hovering_color="white")

        
        PLAY_WALK.changeColor(PLAY_MOUSE_POS)
        PLAY_WALK.update(screen)
        PLAY_MOMENT.changeColor(PLAY_MOUSE_POS)
        PLAY_MOMENT.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if PLAY_WALK.checkForInput(PLAY_MOUSE_POS):
                walking1()
              if PLAY_MOMENT.checkForInput(PLAY_MOUSE_POS):
                main_menu()

        pygame.display.update()

def walking1():
      while True:
        screen.blit(bg2, (0,0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()


        PLAY_TEXT = small_menu_font.render('choose   wisely', True, white)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(690, 100))
        screen.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_CAVE = Button(image=None, pos=(700, 400), text_input="Take Shelter in a Nearby Cave", font=button_font, base_color="#d7fcd4", hovering_color="white")
        PLAY_WALK = Button(image=None, pos=(700, 600), text_input="Try to Find your Way Back", font=button_font, base_color="#d7fcd4", hovering_color="white")

        
        PLAY_CAVE.changeColor(PLAY_MOUSE_POS)
        PLAY_CAVE.update(screen)
        PLAY_WALK.changeColor(PLAY_MOUSE_POS)
        PLAY_WALK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if PLAY_CAVE.checkForInput(PLAY_MOUSE_POS):
                death_spider()
              if PLAY_WALK.checkForInput(PLAY_MOUSE_POS):
                death_tiger()

        pygame.display.update()


    
def death_spider():
  #call(["python", "C:/Users/Surya/Documents/PyGameProject/test_video.py"])
      while True:
        screen.blit(death, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()


        TEXT = death_font.render('YOU WERE BITTEN BY A DEADLY SPIDER', True, white)
        RECT = TEXT.get_rect(center=(690, 100))
        screen.blit(TEXT, RECT)
        DEATH_MENU = Button(image=None, pos=(700, 400), text_input="Main Menu", font=button_font, base_color="green", hovering_color="white")
        
        DEATH_MENU.changeColor(MOUSE_POS)
        DEATH_MENU.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if DEATH_MENU.checkForInput(MOUSE_POS):
                main_menu()

        pygame.display.update()

def death_tiger():
  #call(["python", "C:/Users/Surya/Documents/PyGameProject/test_video.py"])
      while True:
        screen.blit(death, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()


        TEXT = death_font.render('YOU WERE KILLED BY A TIGER', True, white)
        RECT = TEXT.get_rect(center=(690, 100))
        screen.blit(TEXT, RECT)
        DEATH_MENU = Button(image=None, pos=(700, 400), text_input="Main Menu", font=button_font, base_color="green", hovering_color="white")
        
        DEATH_MENU.changeColor(MOUSE_POS)
        DEATH_MENU.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if DEATH_MENU.checkForInput(MOUSE_POS):
                main_menu()

        pygame.display.update()

def death_tiger():
  #call(["python", "C:/Users/Surya/Documents/PyGameProject/test_video.py"])
      while True:
        screen.blit(death, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()


        TEXT = death_font.render('YOU WERE KILLED BY A TIGER', True, white)
        RECT = TEXT.get_rect(center=(690, 100))
        screen.blit(TEXT, RECT)
        DEATH_MENU = Button(image=None, pos=(700, 400), text_input="Main Menu", font=button_font, base_color="green", hovering_color="white")
        
        DEATH_MENU.changeColor(MOUSE_POS)
        DEATH_MENU.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if DEATH_MENU.checkForInput(MOUSE_POS):
                main_menu()

        pygame.display.update()


def quiz():
    #call(["python", "C:/Users/Surya/Documents/PyGameProject/test_video.py"])
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        PLAY_TEXT = menu_font.render('Quiz', True, white)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(690, 260))
        screen.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_BACK = Button(image=None, pos=(1200, 700), text_input="BACK", font=back_button_font, base_color="White", hovering_color="Green")
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                main_menu()

        pygame.display.update()

def results():
    #call(["python", "C:/Users/Surya/Documents/PyGameProject/test_video.py"])
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        PLAY_TEXT = menu_font.render('Results go Here', True, white)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(690, 260))
        screen.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_BACK = Button(image=None, pos=(1200, 700), text_input="BACK", font=back_button_font, base_color="White", hovering_color="Green")
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                main_menu()

        pygame.display.update()



main_menu()

