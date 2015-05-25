import pygame
import random
import sys
from time import sleep, time


#Object classes
class Square(pygame.sprite.Sprite):
    def __init__(self, color = pygame.Color(0, 0, 0), width = 16, height = 16, color_num = 0):
        super(Square, self).__init__()
        self.color = color
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.color_num = color_num
        self.light = False
        self.sound = None


    def is_pressed(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            return True

    def light_up(self):
        #light up
        if self.light == True:
            ticks = pygame.time.get_ticks()
            delta = ticks - board.start_time
            self.image.fill(self.find_color())
            if delta > 350:
                self.image.fill(self.color)
                self.light = False
                board.next_round = True

    def find_color(self):
        if self.color_num == 1:
            return (153, 255, 153)

        if self.color_num == 2:
            return (255, 153, 153)

        if self.color_num == 3:
            return (255, 255, 153)

        if self.color_num == 4:
            return (153, 153, 255)
        



class Board():

    def __init__(self):
        self.mode = "menu"
        self.index = None
        self.start_time = None
        self.pattern = []
        self.next_round = False
        self.clicked = False
        self.button_pressed = None
        self.score = 0
        self.highscore = 0
        self.sound = False
        
    

    def start_round(self):
        self.mode = "remember"
        self.index = 0

        self.start_time = pygame.time.get_ticks()
        for square in color_list:
            if square.color_num == self.pattern[self.index]:
                square.image.fill(square.find_color())
                
        
    def draw_board(self):
        global end_score, highscore
        
        if self.mode == "remember":
            ticks = pygame.time.get_ticks()
            delta = ticks - self.start_time

            if self.sound == True:
                if delta < 100:
                    for square in color_list:
                        if square.color_num == self.pattern[self.index]:         
                            pygame.mixer.Sound.play(square.sound, maxtime = 900)
                
                
            if delta > 1500:
                for square in color_list:
                    if square.color_num == self.pattern[self.index]:                            
                        square.image.fill(square.color)
                        

                self.index += 1

                if self.index + 1 > len(self.pattern):
                    for square in color_list:
                        square.image.fill(square.color)
                        self.index = 0
                        self.mode = "guess"
                        

                else:
                    for square in color_list:
                        if square.color_num == self.pattern[self.index]:
                            square.image.fill(square.find_color())


                    self.start_time = pygame.time.get_ticks()

            if delta < 1500 and delta > 800:
                for square in color_list:
                    if square.color_num == self.pattern[self.index]:                            
                        square.image.fill(square.color)

                
        if self.mode == "guess":

            if self.next_round == True:
                if self.index + 1 > len(self.pattern):
                    self.score += 1
                    self.mode = "between"


            if self.clicked == True:

                if self.button_pressed[0] == self.pattern[self.index]:
                    for square in color_list:
                        if square.color_num == self.pattern[self.index]:
                            if self.sound == True:
                                pygame.mixer.Sound.play(square.sound, maxtime = 900)
                            
                    self.index += 1
                    self.button_pressed[1].light = True
                    self.start_time = pygame.time.get_ticks()
                    self.button_pressed = None
                    self.clicked = False
                    
                    

                else:
                    if self.sound == True:
                        pygame.mixer.Sound.play(game_over_sound)
                    self.start_time = pygame.time.get_ticks()
                    self.clicked = False
                    self.button_pressed = None
                    score_text = "Score: " + str(self.score)
                    end_score = font.render(score_text, True, black)
                    if self.score > self.highscore:
                        self.highscore = self.score
                        highscore_text = "Highscore: " + str(self.highscore)
                        highscore = font.render(highscore_text, True, black)
                    self.mode = "menu"      



def manage_game():
    if board.mode == "between":
        start_the_round = True
        for color in color_list:
            if color.light == True:
                start_the_round = False
        
        if start_the_round == True:
            board.next_round = False
            ticks = pygame.time.get_ticks()
            delta = ticks - board.start_time
            if delta > 2000:
                board.pattern.append(random.randint(1, 4))
                board.start_round()

                


    
    

def make_squares():
    
    square_green = Square(color = pygame.Color(63, 255, 63), width = window_width/2, height = window_height/2)
    square_green.rect.x = 0
    square_green.rect.y = 0
    group_squares.add(square_green)
    color_list.append(square_green)
    square_green.color_num = 1
    square_green.sound = green_sound

    square_red = Square(color = pygame.Color(255, 71, 71), width = window_width/2, height = window_height/2)
    square_red.rect.x = window_width/2
    square_red.rect.y = 0
    group_squares.add(square_red)
    color_list.append(square_red)
    square_red.color_num = 2
    square_red.sound = red_sound

    square_yellow = Square(color = pygame.Color(255, 255, 68), width = window_width/2, height = window_height/2)
    square_yellow.rect.x = 0
    square_yellow.rect.y = window_width/2
    group_squares.add(square_yellow)
    color_list.append(square_yellow)
    square_yellow.color_num = 3
    square_yellow.sound = yellow_sound

    square_blue = Square(color = pygame.Color(81, 81, 255), width = window_width/2, height = window_height/2)
    square_blue.rect.x = window_width/2
    square_blue.rect.y = window_width/2
    group_squares.add(square_blue)
    color_list.append(square_blue)
    square_blue.color_num = 4
    square_blue.sound = blue_sound
    
    

#before running
if (__name__ == "__main__"):
    pygame.init()

    #create monitor info object
    info_object = pygame.display.Info()

    #set window
    window_size = window_width, window_height = info_object.current_h - 80, info_object.current_h - 80
    window = pygame.display.set_mode(window_size)

    
    #Colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    #font
    font = pygame.font.Font("Quicksand-Regular.ttf", 60)
    title_font = pygame.font.Font("Quicksand-Regular.ttf", 200)
    ingame_score_font = pygame.font.Font("Quicksand-Bold.ttf", 60)

    score = ingame_score_font.render("0", True, black)
    end_score = font.render("Score: 0", True, black)
    highscore = font.render("Highscore: 0", True, black)
    title = title_font.render("Simon", True, black)

    #set window color
    window.fill(white)

    #images
    play_button_image = pygame.image.load("play_button.png")
    play_button_image = pygame.transform.scale(play_button_image, (200, 200))

    sound_button_image_on = pygame.image.load("sound_on.png")
    sound_button_image_on = pygame.transform.scale(sound_button_image_on, (50, 50))

    sound_button_image_off = pygame.image.load("sound_off.png")
    sound_button_image_off = pygame.transform.scale(sound_button_image_off, (50, 50))


    #sounds
    green_sound = pygame.mixer.Sound("green.wav")
    red_sound = pygame.mixer.Sound("red.wav")
    yellow_sound = pygame.mixer.Sound("yellow.wav")
    blue_sound = pygame.mixer.Sound("blue.wav")
    game_over_sound = pygame.mixer.Sound("game_over.wav")

    
    #set fps
    clock = pygame.time.Clock()
    frames_per_second = 30

    #create group
    group_squares = pygame.sprite.Group()

    #make squares
    color_list = []
    make_squares()

    #pattern
    board = Board()

    #circle pos and triangle pos
    circle_width = round(window_width / 2 - play_button_image.get_rect().width/2)
    circle_height = round(window_height / 4 + window_height / 2 - play_button_image.get_rect().height/3)

    button_play = pygame.Rect(circle_width, circle_height, 200, 200)

    button_sound = pygame.Rect(window_width / 100, window_height / 100, 50, 50)
    
    

    #while running
    running = True
    while running:
        clock.tick(frames_per_second)

    
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and
                event.key == pygame.K_ESCAPE):
                
                running = False
                

            if (event.type == pygame.MOUSEBUTTONUP):
                mouse_pos = pygame.mouse.get_pos()
                if board.mode == "guess":
                    for color in color_list:
                        if color.is_pressed(mouse_pos) == True:
                            board.button_pressed = (color.color_num, color)
                            board.clicked = True
                            

            if board.mode == "menu":
                mouse_pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if button_play.collidepoint(mouse_x, mouse_y):
                    if (event.type == pygame.MOUSEBUTTONUP):
                        board.mode = "between"
                        board.pattern = []
                        board.score = 0
                        board.start_time = pygame.time.get_ticks()


                if button_sound.collidepoint(mouse_x, mouse_y):
                    if (event.type == pygame.MOUSEBUTTONUP):
                        if board.sound == False:
                           board.sound = True
                        elif board.sound == True:
                            board.sound = False
                

                    



        clock.tick(frames_per_second)
        window.fill(white)
        board.draw_board()
        manage_game()
        for color in color_list:
            color.light_up()

        
        

        #draws the sprites
        if board.mode != "menu":
            group_squares.draw(window)
            score = ingame_score_font.render(str(board.score), True, black)
            window.blit(score, (window_width/2 - score.get_rect().width/2, window_height/2 - score.get_rect().height/2))
        else:
            window.blit(play_button_image, button_play)
            if board.sound == False:
                window.blit(sound_button_image_off, button_sound)
            else:
                window.blit(sound_button_image_on, button_sound)

            window.blit(title, (window_width/2 - title.get_rect().width/2, window_height/10 - 75))
            window.blit(highscore, (window_width/2 - highscore.get_rect().width/2, window_height/2))
            window.blit(end_score, (window_width/2 - end_score.get_rect().width/2, window_height/2 - 60))

            
        pygame.display.update()
    pygame.quit()
