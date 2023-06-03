import pygame

WINDOW_NAME = "Musque Destoyer"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

FPS = 90
DRAW_FPS = True

# o'lchamlar
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80)
MOSQUITOS_SIZES = (50, 38)
MOSQUITO_SIZE_RANDOMIZE = (1,2) # Har bir chivin uchun chivinlar o'lchami random tarzda tanlanadi
BEE_SIZES = (50, 50)
BEE_SIZE_RANDOMIZE = (1.2, 1.5)

# Chizish
DRAW_HITBOX = False # Barcha obyektlar uchun to'rtburchaklar chizish

# animatsiya
ANIMATION_SPEED = 0.08 # hasharotlarning ramkasi har X soniyada o'zgaradi

# O'yining qiyinchiligi
GAME_DURATION = 60 # o'yin X soniya davom etadi
MOSQUITOS_SPAWN_TIME = 1
MOSQUITOS_MOVE_SPEED = {"min": 1, "max": 5}
BEE_PENALITY = 1 # o'yinchining X ballini olib tashlaydi (agar u ari o'ldirsa)

# raanglar
COLORS = {"title": (38, 61, 39), "score": (38, 61, 39), "timer": (38, 61, 39),
            "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (46, 54, 163)}} # second is the color when the mouse is on the button

# musiqa / ovozlar
MUSIC_VOLUME = 0.16 # 0 dan 1 gacha bo'lgan qiymat
SOUNDS_VOLUME = 1

# shriftlar va fonlar
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)
