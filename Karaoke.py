import pygame
import sys
import Player


pygame.init()
pygame.font.init()

FPS = 60
pygame.init()
pygame.font.init()
pygame.mixer.init()
main_window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Karaoke club")
Les_Text = 'music/text/les.txt'
Les_Music = 'music/les.mp3'

clock = pygame.time.Clock()


screen = pygame.Surface((800,600))





background_play = pygame.image.load('image/play.bmp')
background_play_rect = background_play.get_rect(bottomright=(800, 600))

background_menu = pygame.image.load('image/menu.bmp')
background_menu_rect = background_menu.get_rect(bottomright = (800,600))



class Musics:
    def __init__(self, punkts=None):
        if punkts is None:
            punkts = [120, 140, u'Punkts', (0, 250, 120), (250, 30, 250)]
        self.punkts = punkts
    def render(self, screen, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                screen.blit(font.render(i[2],1,i[4]), (i[0], i[1]))
            else: screen.blit(font.render(i[2],1,i[3]), (i[0], i[1]))
    def mus_list(self):
        done = True
        font_menu = pygame.font.SysFont('arial', 50)
        punkt = 0
        go_play_les = False
        go_play_2 = False
        go_back = False
        while done:
            screen.fill((0,100,10))
            screen.blit(background_menu, background_menu_rect)

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0]<int(i[0])+155 and mp[1]>i[1] and mp[1]<int(i[1])+50:
                    punkt = i[5]
                self.render(screen, font_menu, punkt)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = False
                        go_back = True

                    if event.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -=1
                    if event.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) -1:
                            punkt +=1
                if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.K_RETURN) and event.button == 1:
                    if punkt == 0:
                        done = False
                        go_play_les = True
                    elif punkt == 1:
                        done = False
                        go_play_2 = True
                    elif punkt == 2:
                        done = False
                        init_menu()


            main_window.blit(screen, (0,0))
            pygame.display.update()

        if (go_back):
            init_menu()
        if (go_play_les):
            init_play(Les_Text, Les_Music)




class Menu:
    def __init__(self, punkts=None):
        if punkts is None:
            punkts = [120, 140, u'Punkts', (0, 250, 120), (250, 30, 250)]
        self.punkts = punkts
    def render(self, screen, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                screen.blit(font.render(i[2],1,i[4]), (i[0], i[1]))
            else: screen.blit(font.render(i[2],1,i[3]), (i[0], i[1]))
    def menu(self):
        pygame.mixer.music.load('music/UNO.mp3')
        pygame.mixer.music.play(-1)
        done = True
        font_menu = pygame.font.SysFont('arial', 50)
        punkt = 0
        volume = 1
        go_bus_list = False
        while done:
            screen.fill((0,100,10))
            screen.blit(background_menu, background_menu_rect)

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0]<int(i[0])+155 and mp[1]>i[1] and mp[1]<int(i[1])+50:
                    punkt = i[5]
                self.render(screen, font_menu, punkt)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -=1
                    if event.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) -1:
                            punkt +=1
                if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.K_RETURN) and event.button == 1:
                    if punkt == 0:
                        pygame.mixer.music.stop()
                        done = False
                        go_bus_list = True
                    elif punkt == 1:
                        sys.exit()
                    elif punkt == 2:
                        volume += 0.1
                        pygame.mixer.music.set_volume(volume)
                    elif punkt == 3:
                        volume -= 0.1
                        pygame.mixer.music.set_volume(volume)
            main_window.blit(screen, (0,0))
            pygame.display.update()
        if (go_bus_list):
            init_musics()


def init_musics():
    punkts = [(280, 140, u'Лесник КИШы', (0, 0, 120), (250, 30, 250), 0),
          (280, 190, u'2', (0, 0, 120), (250, 30, 250), 1),
          (500, 350, u'Back', (0, 0, 120), (250, 30, 250), 2)]
    mus = Musics(punkts)
    mus.mus_list()


def init_play(text, music):
    punkts = [(20, 50, u'Sound UP', (0, 0, 120), (250, 30, 250), 0),
              (280, 50, u'Sound Down', (0, 0, 120), (250, 30, 250), 1),
              (650, 50, u'Back', (0, 0, 120), (250, 30, 250), 2)]
    player = Player.Player(text, punkts)
    player.Play(music)

def init_menu():
    punkts = [(280, 140, u'GAME', (0, 0, 120), (250, 30, 250), 0),
          (293, 280, u'QUIT', (0, 0, 120), (250, 30, 250), 1),
          (50, 500, u'Sound UP', (0, 0, 120), (250, 30, 250), 2),
          (500, 500, u'Sound Down', (0, 0, 120), (250, 30, 250), 3)]
    game = Menu(punkts)
    game.menu()

def main():
    init_menu()


if __name__ == '__main__':
    main()
