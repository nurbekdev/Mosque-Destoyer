import pygame
import time
import random
from settings import *
from background import Background
from hand import Hand
from hand_tracking import HandTracking
from mosquito import Mosquito
from bee import Bee
import cv2
import ui

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()

        # Kamerani ochadi
        self.cap = cv2.VideoCapture(0)

        self.sounds = {}
        self.sounds["slap"] = pygame.mixer.Sound(f"Assets/Sounds/slap.wav")
        self.sounds["slap"].set_volume(SOUNDS_VOLUME)
        self.sounds["screaming"] = pygame.mixer.Sound(f"Assets/Sounds/screaming.wav")
        self.sounds["screaming"].set_volume(SOUNDS_VOLUME)


    def reset(self): # barcha kerakli o'zgaruvchilarni qayta o'rnating
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.insects = []
        self.insects_spawn_timer = 0
        self.score = 0
        self.game_start_time = time.time()


    def spawn_insects(self):
        t = time.time()
        if t > self.insects_spawn_timer:
            self.insects_spawn_timer = t + MOSQUITOS_SPAWN_TIME

            # vaqt o'tishi bilan hasharotning asalari bo'lish ehtimolini oshiring
            nb = (GAME_DURATION-self.time_left)/GAME_DURATION * 100  / 2  #butun o'yin davomida 0 dan 50 gacha oshirish (chiziqli)
            if random.randint(0, 100) < nb:
                self.insects.append(Bee())
            else:
                self.insects.append(Mosquito())

            #o'yinning yarmidan keyin boshqa chivin yaratiladi
            if self.time_left < GAME_DURATION/2:
                self.insects.append(Mosquito())

    def load_camera(self):
        _, self.frame = self.cap.read()


    def set_hand_position(self):
        self.frame = self.hand_tracking.scan_hands(self.frame)
        (x, y) = self.hand_tracking.get_hand_center()
        self.hand.rect.center = (x, y)

    def draw(self):
        # orqa fonni chizish
        self.background.draw(self.surface)
        # hasharotlarni chizish
        for insect in self.insects:
            insect.draw(self.surface)
        # qo'lni chizish
        self.hand.draw(self.surface)
        # hisobni chizish
        ui.draw_text(self.surface, f"Ball : {self.score}", (5, 5), COLORS["score"], font=FONTS["medium"],
                    shadow=True, shadow_color=(255,255,255))
        # qolgan vaqtni yozish
        timer_text_color = (160, 40, 0) if self.time_left < 5 else COLORS["timer"] # change the text color if less than 5 s left
        ui.draw_text(self.surface, f"Qolgan Vaqt : {self.time_left}", (SCREEN_WIDTH//2, 5),  timer_text_color, font=FONTS["medium"],
                    shadow=True, shadow_color=(255,255,255))


    def game_time_update(self):
        self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0)



    def update(self):

        self.load_camera()
        self.set_hand_position()
        self.game_time_update()

        self.draw()

        if self.time_left > 0:
            self.spawn_insects()
            (x, y) = self.hand_tracking.get_hand_center()
            self.hand.rect.center = (x, y)
            self.hand.left_click = self.hand_tracking.hand_closed
            print("Hand closed", self.hand.left_click)
            if self.hand.left_click:
                self.hand.image = self.hand.image_smaller.copy()
            else:
                self.hand.image = self.hand.orig_image.copy()
            self.score = self.hand.kill_insects(self.insects, self.score, self.sounds)
            for insect in self.insects:
                insect.move()

        else: # Game over bo'lganda
            if ui.button(self.surface, 540, "Davom etish", click_sound=self.sounds["slap"]):
                return "menu"


        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)
