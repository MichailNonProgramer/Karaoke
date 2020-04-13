import pygame
import time, sys
import ParceText
import Karaoke



class Player:
    def __init__(self, text, punkts=None):
        self.text = text
        if punkts is None:
            punkts = [120, 140, u'Punkts', (0, 250, 120), (250, 30, 250)]
        self.punkts = punkts

    def render(self, screen, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                screen.blit(font.render(i[2],1,i[4]), (i[0], i[1]))
            else: screen.blit(font.render(i[2],1,i[3]), (i[0], i[1]))

    def Play(self, music):
        pygame.mixer.init()  # Start song at 0 and don't loop
        pygame.init()
        scr = pygame.Surface((800,100))
        Karaoke.screen.blit(Karaoke.background_play, Karaoke.background_play_rect)
        go_back = False

        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        start_timer = time.time()
        ParceText.init_dict(self.text)
        font = pygame.font.Font(None, 40)

        swap1, swap2, swap3, swap4 = True, True, True, True
        dict = ParceText.init_dict(self.text)
        actual_time = time.time() - start_timer
        game_start = False
        str1, time_str1, color_str1 = ParceText.knife_text(dict, actual_time, actual_time, game_start)
        actual_time_str2 = actual_time + time_str1
        str2, time_str2, color_str2 = ParceText.knife_text(dict, actual_time_str2, actual_time, game_start)
        actual_time_str3 = time_str2 + actual_time_str2
        str3, time_str3, color_str3 = ParceText.knife_text(dict, actual_time_str3, actual_time, game_start)
        actual_time_str4 = time_str3 + actual_time_str3
        str4, time_str4, color_str4 = ParceText.knife_text(dict, actual_time_str4, actual_time,game_start)

        font_menu = pygame.font.SysFont('arial', 50)
        punkt = 0
        volume = 1

        while pygame.mixer.music.get_busy():
            actual_time = time.time() - start_timer
            mp = pygame.mouse.get_pos()
            scr.blit(Karaoke.background_play, Karaoke.background_play.get_rect(bottomright=(800, 100)))

            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < int(i[0]) + 155 and mp[1]  > i[1] + 500 and mp[1]  < int(i[1]) + 550:
                    punkt = i[5]
                self.render(scr, font_menu, punkt)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.stop()
                        go_back = True
                    if event.key == pygame.K_LEFT:
                        if punkt > 0:
                            punkt -=1
                    if event.key == pygame.K_RIGHT:
                        if punkt < len(self.punkts) -1:
                            punkt +=1
                if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.K_RETURN)  and event.button == 1:
                    if punkt == 0:
                        volume += 0.1
                        pygame.mixer.music.set_volume(volume)
                    elif punkt == 1:
                        volume -= 0.1
                        pygame.mixer.music.set_volume(volume)
                    elif punkt == 2:
                        pygame.mixer.music.stop()
                        go_back = True



            if swap1:
                str1, time_str1, color_str1 = ParceText.knife_text(dict, actual_time, actual_time,game_start)
                actual_time_str2 = actual_time + time_str1
                swap1 = False

            if swap2:
                str2, time_str2, color_str2 = ParceText.knife_text(dict, actual_time_str2, actual_time,game_start)
                actual_time_str3 = time_str2 + actual_time_str2
                swap2 = False
            if swap3:
                str3, time_str3, color_str3 = ParceText.knife_text(dict, actual_time_str3, actual_time, game_start)
                actual_time_str4 = time_str3 + actual_time_str3
                swap3 = False
            if swap4:
                str4, time_str4, color_str4 = ParceText.knife_text(dict, actual_time_str4, actual_time, game_start)
                swap4 = False


            if actual_time > ParceText.game_state(self.text):
                game_start = True

            # print_words = {}
            # for index in dict:
            #     state_dict = dict[index]
            #     for ind in state_dict:



            print(str1,str2,str3,str4)


            if round(actual_time) == round(actual_time_str2):
                swap2 = True
            if round(actual_time) == round(actual_time_str3):
                swap3 = True
            if round(actual_time) == round(actual_time_str4):
                swap4 = True
            if round(time_str4 + actual_time_str4) == round(actual_time):
                swap1, swap2, swap3, swap4 = True, True, True, True


            string1 = font.render(str1, 1, color_str1)
            string2 = font.render(str2, 1, color_str2)
            string3 = font.render(str3, 1, color_str3)
            string4 = font.render(str4, 1, color_str4)

            Karaoke.screen.blit(Karaoke.background_play, Karaoke.background_play_rect)
            """открисовка"""
            Karaoke.clock.tick(Karaoke.FPS)
            Karaoke.main_window.blit(Karaoke.screen, (0, 0))
            Karaoke.main_window.blit(scr, (0, 500))
            Karaoke.main_window.blit(string1, (150, 150))
            Karaoke.main_window.blit(string2, (350, 250))
            Karaoke.main_window.blit(string3, (150, 350))
            Karaoke.main_window.blit(string4, (350, 450))
            pygame.display.update()

        if(go_back):
            Karaoke.init_musics()

        Karaoke.init_musics()

