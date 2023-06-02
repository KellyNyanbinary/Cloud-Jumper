# -*- coding: utf-8 -*-

import pygame
import random
import math
import sys
import os
import time

# ------------------------------------------------ Functions Block --------------------------------------------------- #


def generate_platform(w, h, generate, pixel_width):            # This function generates the platforms.
    platforms_out = [[0 for x in range(w)] for y in range(h)]      # Creates a matrix filled with 0s.

    for x in range(0, h - 1):                                  # Generates random 1s in the matrix, leaves out last line
        for y in range(0, w - 3):
            if random.randint(0, generate) == generate:        # The probability a 1 appears(1/generate).
                random_int = random.randint(1, 12)
                if random_int == 1 or random_int == 2 or random_int == 3 or random_int == 4 or random_int == 5 or random_int == 6:
                    platforms_out[x][y] = 1
                if random_int == 7 or random_int == 8 or random_int == 9 or random_int == 10:
                    platforms_out[x][y] = 1
                    platforms_out[x][y + 1] = 1
                if random_int == 11 or random_int == 12:
                    platforms_out[x][y] = 1
                    platforms_out[x][y + 1] = 1
                    platforms_out[x][y + 2] = 1

    platforms_out[h - 2][int(screen_width / 2 / pixel_width) - 1] = 1   # Creates spawn platform
    platforms_out[h - 2][int(screen_width / 2 / pixel_width)] = 1
    platforms_out[h - 2][int(screen_width / 2 / pixel_width) + 1] = 1

    for z in range(3, h - 1):
        platforms_out[h - z][int(screen_width / 2 / pixel_width) - 1] = 0   # Deletes block above spawn platform
        platforms_out[h - z][int(screen_width / 2 / pixel_width)] = 0
        platforms_out[h - z][int(screen_width / 2 / pixel_width) + 1] = 0

    # for y in range(0, h):
    #     print(platforms[y])                                    # Prints it so we can check!

    return platforms_out


def generate_pixels(pixel_width, x, y, r, g, b, x_slide):
    pygame.draw.rect(screen, (r, g, b), (x * pixel_width + x_slide, y * pixel_width, pixel_width, pixel_width), 0)
    # Draws the pixels.


def generate_individual_pixel_info(pixel_width, pixel_matrix, r, g, b, x_slide):
    for x in range(0, len(pixel_matrix[0])):
        for y in range(0, len(pixel_matrix)):
            if pixel_matrix[y][x] == 1:
                generate_pixels(pixel_width, x, y, r, g, b, x_slide)  # "Compiles" the list, then calls generate_pixels


def generate_player(pixel_width, x, y, r, g, b):
    pygame.draw.rect(screen, (r, g, b), (x - 0.5 * pixel_width, y - 0.5 * pixel_width, pixel_width, pixel_width), 0)
    # Draws the player

# ----------------------------------------------- Initialize Block --------------------------------------------------- #

menu = []
menu.append([0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
menu.append([0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0])
menu.append([0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
menu.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


level = 0
screen_height = 900
screen_width = int(screen_height * 1.5) + 1
platforms_template_width = 128
platforms_actual_width = 0
platforms_height = 32
pixel_w_menu = int(screen_height / len(menu))
pixel_w = int(screen_height / platforms_height)
player_x = 0
player_y = screen_height / 2
if player_x % pixel_w > int(0.5 * pixel_w):                             # Detects player actual on screen location
    player_actual_x = int(int(screen_width / pixel_w / 2) - player_x / pixel_w)
else:
    player_actual_x = int(int(screen_width / pixel_w / 2 + 1) - player_x / pixel_w)
player_actual_y = int((player_y - 0.5 * pixel_w) / pixel_w)
player_xv = 0
player_yv = 0
template_gen_rate = 12
bottom_contact = False
upper_contact = False
left_contact = False
right_contact = False
clock = pygame.time.Clock()
rise_v = 0
alive = False
text = ''
bounce = True
clipped = False
bump = False
bumped = False
jump = False
completed = 0
re_gen = False
muted = False
paused = False
percentage_bar = []
mouse_pos = [0, 0]
i = 0
c = 0
x = 0

cloudWhite = (235, 235, 235,)
cloudWhite_r = cloudWhite[0]
cloudWhite_g = cloudWhite[1]
cloudWhite_b = cloudWhite[2]
skyBlue = (125, 196, 240)
skyBlue_r = skyBlue[0]
skyBlue_g = skyBlue[1]
skyBlue_b = skyBlue[2]
playerGrey = (195, 195, 195)
playerGrey_r = playerGrey[0]
playerGrey_g = playerGrey[1]
playerGrey_b = playerGrey[2]
scrollRed = (255, 0, 0)
scrollRed_r = scrollRed[0]
scrollRed_g = scrollRed[1]
scrollRed_b = scrollRed[2]
scrollGreen = (0, 255, 0)
scrollGreen_r = scrollGreen[0]
scrollGreen_g = scrollGreen[1]
scrollGreen_b = scrollGreen[2]
loadingGreen = (50, 222, 50)
loadingGreen_r = loadingGreen[0]
loadingGreen_g = loadingGreen[1]
loadingGreen_b = loadingGreen[2]
loadingRed = (222, 50, 50)
loadingRed_r = loadingRed[0]
loadingRed_g = loadingRed[1]
loadingRed_b = loadingRed[2]
loadingYellow = (222, 222, 50)
loadingYellow_r = loadingYellow[0]
loadingYellow_g = loadingYellow[1]
loadingYellow_b = loadingYellow[2]

dir_path = os.path.dirname(os.path.realpath(__file__))
audio_path = dir_path + '\\audio'
img_path = dir_path + '\\image'
background_music = audio_path + '\\background.wav'
jump_sound = audio_path + '\\jump.wav'
bump_sound = audio_path + '\\bump.aiff'
death_sound = audio_path + '\\death.wav'
victory_sound = audio_path + '\\victory.aiff'
icon = img_path + '\\icon.PNG'

pygame.init()
icon = pygame.image.load(icon)
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.Surface(screen.get_size())

pygame.mixer.init(channels=8)

pygame.mixer.music.load(background_music)
pygame.mixer.music.play(-1, 0.0)

platforms_actual_width = int(platforms_template_width + (platforms_template_width / 8) * level)
gen_rate = int(platforms_actual_width / template_gen_rate)
platforms = generate_platform(platforms_actual_width, platforms_height, gen_rate, pixel_w)

# -------------------------------------------------- Menu Block ------------------------------------------------------ #

while True:
    text = 'Welcome to Cloud Jumper, click the arrow or press space to begin level ' + str(level)
    pygame.display.set_caption(text)

    while not alive:                                                        # Runs menu
        screen.fill((skyBlue_r, skyBlue_g, skyBlue_b))
        generate_individual_pixel_info(pixel_w_menu, menu, cloudWhite_r, cloudWhite_g, cloudWhite_b, 0)
        for event in pygame.event.get():                                    # Keyboard input for menu
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 12 * pixel_w_menu <= mouse_pos[0] <= 22 * pixel_w_menu and 12 * pixel_w_menu <= mouse_pos[1] <= 21 * pixel_w_menu:
                    alive = True
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.get_pressed()
                if key_pressed[pygame.K_SPACE]:
                    alive = True
                if key_pressed[pygame.K_m]:
                    if muted:
                        muted = False
                    else:
                        muted = True

        if muted:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

        pygame.display.flip()
        pygame.display.update()
        clock.tick(72)

    screen.fill((loadingGreen_r, loadingGreen_g, loadingGreen_b))                                                  # The percentage bar
    for w in range(0, 10):
        for y in range(0, 10):
            if y < w:
                generate_pixels(pixel_w, int(screen_width / pixel_w / 2) - 5 + y, 1, 0, 255, 0, 0)
            if y >= w:
                generate_pixels(pixel_w, int(screen_width / pixel_w / 2) - 5 + y, 1, 255, 0, 0, 0)
            pygame.display.flip()
            pygame.display.update()
        y = 0
        pygame.display.flip()
        pygame.display.update()
        clock.tick(72)
    w = 0
    screen.fill((loadingGreen_r, loadingGreen_g, loadingGreen_b))
    pygame.display.flip()
    pygame.display.update()

    player_x = 0
    player_y = screen_height / 2
    if player_x % pixel_w > int(0.5 * pixel_w):  # Detects player actual on screen location
        player_actual_x = int(int(screen_width / pixel_w / 2) - player_x / pixel_w)
    else:
        player_actual_x = int(int(screen_width / pixel_w / 2 + 1) - player_x / pixel_w)
    player_actual_y = int((player_y - 0.5 * pixel_w) / pixel_w)
    player_xv = 0
    player_yv = 0

    text = 'Cloud Jumper level ' + str(level)
    pygame.display.set_caption(text)

# ------------------------------------------------- In Game Block ---------------------------------------------------- #

    while alive:

        if platforms[player_actual_y + 1][player_actual_x] == 1:                   # Detects collision(contact)
            bottom_contact = True
            if not bumped:
                bump = True
            if player_y >= player_actual_y * pixel_w + 0.55 * pixel_w:
                clipped = True
            else:
                clipped = False
        else:
            bottom_contact = False
            clipped = False

        if platforms[player_actual_y][player_actual_x] == 1 or player_actual_y <= -1:
            upper_contact = True
            bump = True
        else:
            upper_contact = False

        if platforms[player_actual_y][player_actual_x - 1] == 1 and player_xv > 0:
            right_contact = True
            if not bumped:
                bump = True
        else:
            right_contact = False

        if platforms[player_actual_y][player_actual_x + 1] == 1 and player_xv < 0:
            left_contact = True
            if not bumped:
                bump = True
        else:
            left_contact = False

        for event in pygame.event.get():                                        # Keyboard input
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.get_pressed()
                if bottom_contact or right_contact or left_contact:
                    if key_pressed[pygame.K_UP]:
                        rise_v = -0.8
                        jump = True
                if key_pressed[pygame.K_RIGHT]:
                    player_xv += -0.5
                if key_pressed[pygame.K_LEFT]:
                    player_xv += 0.5
                if key_pressed[pygame.K_SPACE]:
                    re_gen = True
                if key_pressed[pygame.K_m]:
                    if muted:
                        muted = False
                    else:
                        muted = True
                if key_pressed[pygame.K_p]:
                    if paused:
                        paused = False
                    else:
                        paused = True

        if bottom_contact:                                                        # Controls x axis velocity
            if player_xv > 0.01:
                player_xv += -0.02
            elif player_xv < -0.01:
                player_xv += 0.02
            else:
                player_xv = 0
        else:
            if player_xv > 0.005:
                player_xv += -0.005
            elif player_xv < -0.005:
                player_xv += 0.005
            else:
                player_xv = 0
        if right_contact or left_contact:
            if player_xv < -0.05 or player_xv > 0.05:
                player_xv *= -0.1
            else:
                if right_contact:
                    player_xv += -0.5
                if left_contact:
                    player_xv += 0.5

        if bottom_contact:                                                    # Controls y axis velocity
            if player_yv > 0.05:
                player_yv *= -0.25
            else:
                player_yv = 0
            if clipped:
                player_yv += -0.2
        else:
            player_yv += 0.01
        if upper_contact:
            player_yv *= -0.5
            player_yv += 0.1
        if rise_v != 0:
            if i > rise_v:
                player_yv += rise_v
                i += -1
                rise_v += 1
            else:
                i = 0
                rise_v = 0

        if muted:                                                            # Sound effects
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
            if jump:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound(jump_sound))
                jump = False
            if bump:
                pygame.mixer.Channel(2).play(pygame.mixer.Sound(bump_sound))
                bump = False
            if bottom_contact:
                bumped = True
            else:
                bumped = False

        player_x += player_xv * (pixel_w / 5)                                 # Sets location
        player_y += player_yv * (pixel_w / 5)

        if player_x % pixel_w > int(0.5 * pixel_w):                           # Detects player actual on screen location
            player_actual_x = int(int(screen_width / pixel_w / 2) - player_x / pixel_w)
        else:
            player_actual_x = int(int(screen_width / pixel_w / 2 + 1) - player_x / pixel_w)
        player_actual_y = int((player_y - 0.5 * pixel_w) / pixel_w)

        completed = int(player_actual_x / platforms_actual_width * 100)         # Gives out percentage of completion

        percentage_bar = []                                                     # Generates the percentage bar list
        for c in range(0, int(completed / 10)):
            percentage_bar.append(1)
        for c in range(int(completed / 10), 10):
            percentage_bar.append(0)

        if player_actual_y >= platforms_height - 2:                             # Detects if the player is dead or not
            alive = False
            text = 'You died!'
            screen.fill((loadingRed_r, loadingRed_g, loadingRed_b))
            pygame.display.set_caption(text)
            pygame.mixer.Channel(3).play(pygame.mixer.Sound(death_sound))
            pygame.display.flip()
            pygame.display.update()
            for w in range(0, 10):
                for y in range(0, 10):
                    if y < w:
                        generate_pixels(pixel_w, int(screen_width / pixel_w / 2) - 5 + y, 1, scrollGreen_r, scrollGreen_g, scrollGreen_b, 0)
                    if y >= w:
                        generate_pixels(pixel_w, int(screen_width / pixel_w / 2) - 5 + y, 1, scrollRed_r, scrollRed_g, scrollRed_b, 0)
                    pygame.display.flip()
                    pygame.display.update()
                y = 0
                pygame.display.flip()
                pygame.display.update()
                clock.tick(10)
            w = 0
            screen.fill((loadingRed_r, loadingRed_g, loadingRed_b))

        if player_actual_x >= platforms_actual_width - 2:                       # Detects if the player passed the level
            alive = False
            text = 'You passed level ' + str(level)
            pygame.display.set_caption(text)
            level += 1
            pygame.mixer.Channel(3).play(pygame.mixer.Sound(victory_sound))

            platforms_actual_width = int(platforms_template_width + (platforms_template_width / 8) * level)
            gen_rate = int(platforms_actual_width / template_gen_rate)
            platforms = generate_platform(platforms_actual_width, platforms_height, gen_rate, pixel_w)

            screen.fill((loadingGreen_r, loadingGreen_g, loadingGreen_b))
            for w in range(0, 10):
                for y in range(0, 10):
                    if y < w:
                        generate_pixels(pixel_w, int(screen_width / pixel_w / 2) - 5 + y, 1, scrollGreen_r, scrollGreen_g, scrollGreen_b, 0)
                    if y >= w:
                        generate_pixels(pixel_w, int(screen_width / pixel_w / 2) - 5 + y, 1, scrollRed_r, scrollRed_g, scrollRed_b, 0)
                    pygame.display.flip()
                    pygame.display.update()
                y = 0
                pygame.display.flip()
                pygame.display.update()
                clock.tick(2)
            w = 0
            screen.fill((loadingGreen_r, loadingGreen_g, loadingGreen_b))

        if re_gen:                                                          # Detects if re-render the level
            re_gen = False
            alive = False
            text = 'Regenerating level'
            screen.fill((loadingYellow_r, loadingYellow_g, loadingYellow_b))
            pygame.display.set_caption(text)

            platforms_actual_width = int(platforms_template_width + (platforms_template_width / 8) * level)
            gen_rate = int(platforms_actual_width / template_gen_rate)
            platforms = generate_platform(platforms_actual_width, platforms_height, gen_rate, pixel_w)

            for w in range(0, 10):
                for y in range(0, 10):
                    if y < w:
                        generate_pixels(pixel_w, int(screen_width / pixel_w / 2) - 5 + y, 1, scrollGreen_r, scrollGreen_g, scrollGreen_b, 0)
                    if y >= w:
                        generate_pixels(pixel_w, int(screen_width / pixel_w / 2) - 5 + y, 1, scrollRed_r, scrollRed_g, scrollRed_b, 0)
                    pygame.display.flip()
                    pygame.display.update()
                y = 0
                pygame.display.flip()
                pygame.display.update()
                clock.tick(30)
            w = 0
            screen.fill((loadingYellow_r, loadingYellow_g, loadingYellow_b))

        # print(player_x, player_actual_x, player_xv, player_y, player_actual_y, player_yv, rise_v, i, bottom_contact, upper_contact, clipped, gen_rate, completed, pixel_w, platforms_actual_width)

        while paused:                                                           # Runs if paused
            for event in pygame.event.get():                                    # Keyboard input
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    key_pressed = pygame.key.get_pressed()
                    if key_pressed[pygame.K_p]:
                        if paused:
                            paused = False
                        else:
                            paused = True
                    if key_pressed[pygame.K_m]:
                        if muted:
                            muted = False
                        else:
                            muted = True
            if muted:                                                           # Sound effects
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()

        screen.fill((skyBlue_r, skyBlue_g, skyBlue_b))                                                            # Draws all stuff
        generate_individual_pixel_info(pixel_w, platforms, cloudWhite_r, cloudWhite_g, cloudWhite_b, player_x)
        generate_player(pixel_w, int((int(screen_width / pixel_w / 2) + 0.5) * pixel_w), player_y, playerGrey_r, playerGrey_g, playerGrey_b)
        for x in range(0, 10):
            if percentage_bar[x] == 1:
                generate_pixels(pixel_w, int(screen_width / pixel_w / 2) - 5 + x, 1, scrollGreen_r, scrollGreen_g, scrollGreen_b, 0)
            if percentage_bar[x] == 0:
                generate_pixels(pixel_w, int(screen_width / pixel_w / 2) - 5 + x, 1, scrollRed_r, scrollRed_g, scrollRed_b, 0)
        x = 0

        pygame.display.flip()
        pygame.display.update()
        clock.tick(72)
