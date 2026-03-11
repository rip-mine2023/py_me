import pygame
from PIL import Image, ImageSequence
from py_me import os_me
import time
import events
from typing import Callable

class animation:
    idd = 1
    LAGANIMATION = 1073742108
    SAFEANIMATION = 1073742109
    NEGATIVEROLL = 1073742110
    POSITIVEROLL = 1073742111
    GIFEXECUTED = 1073742112
    NEWMENU = 1073742114
    SELECTUP = 1073742115
    SELECTDOWN = 1073742116
    SELECTCONFIRM = 1073742117
    def __init__(self):
        import pyga_me
        self.pyga_me = pyga_me
        os_me.details.enable_rich_traceback = False
        os_me.details.silent_FileHunter = True
        self.frame_timer = 0
        self.frame_index = 0
        self.roll = 0
        self._play = True
        self.stop = False
        self._start = None
        self._nunber_of_executions = 0
        self.id = animation.idd
        animation.idd += 1

    def extract_frames_gif(self, path_gif, size):
            gif = Image.open(path_gif)
            frames = []
            for frame in ImageSequence.Iterator(gif):
                fr = frame.convert("RGBA").resize(size)
                surf = pygame.image.fromstring(fr.tobytes(), fr.size, fr.mode).convert_alpha()
                frames.append(surf)
            return frames

    def animation(self, frames: list, screen, auto_fill: bool = True, Clok_value: int  = None, coordinates: tuple[int] = (0,0)):
        self._nunber_of_executions += 1
        events.events_inmoment.append(events.event(animation.GIFEXECUTED, self._nunber_of_executions))
        if self._play:
            self._start = time.time()
            self._play = False
        if auto_fill:
            screen.fill((0,0,0))
        self.frame_timer += 1
        if self.frame_timer >= 10:
            self.frame_index = (self.frame_index + 1) % len(frames)
            stop = time.time()
            lag = stop - self._start
            #calcula o lag e envia o evento apropriado de acordo com o valor do Clock passado pelo usuario, se for None, considera 60 FPS (16.67ms por frame) como referência
            if Clok_value is not None:
                frame_time = 1000.0 / Clok_value  # tempo ideal por frame em milissegundos
                if lag > frame_time:
                    events.events_inmoment.append(events.event(animation.LAGANIMATION, lag))
            elif lag > 0.01667:  # considerando 60 FPS como referência
                events.events_inmoment.append(events.event(animation.LAGANIMATION, lag))
            else:
                events.events_inmoment.append(events.event(animation.SAFEANIMATION, lag))
            self.frame_timer= 0
            self._play = True
        screen.blit(frames[self.frame_index], coordinates)

    def scrolling_text(self, text: list, font: pygame.font.Font, screen, space: int, roll: int = 10):
        for i, texto in enumerate(text):
            render = font.render(texto, True, (0, 0, 250))
            x = screen.get_width() // 2 - render.get_width() // 2
            y = space + i  * 60 + self.roll
            screen.blit(render, (x, y))
            keys = pygame.key.get_pressed()
            if not self.stop:
                if keys[pygame.K_UP]:
                    self.roll -= roll
                elif keys[pygame.K_DOWN]:
                    self.roll += roll
            if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                self.stop = False
            if self.roll > 0:
                events.events_inmoment.append(events.event(animation.POSITIVEROLL, [self, self.roll]))
            if self.roll < 0:
                events.events_inmoment.append(events.event(animation.NEGATIVEROLL, [self, self.roll * -1]))
    
    class menu:
        def __init__(self):
            self.x = 0
            self.y = 0
            self.selected = 0
        def menu_config(self, screen, options: list[str], font: pygame.font.Font, evento=None):
            events.events_inmoment.append(events.event(animation.NEWMENU, self))
            menu_ativo = True
            self.x = screen.get_width()
            self.y = screen.get_height()
            
            if evento:
                if evento.type == pygame.QUIT:
                    menu_ativo = False
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(options)
                        events.events_inmoment.append(events.event(animation.SELECTUP, self.selected))
                    elif evento.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(options)
                        events.events_inmoment.append(events.event(animation.SELECTDOWN, self.selected))
                    elif evento.key == pygame.K_RETURN:
                        events.events_inmoment.append(events.event(animation.SELECTCONFIRM, self.selected))
                        return menu_ativo
            return menu_ativo
                        
        def menu_draw_basic(self, screen, options: list[str], font: pygame.font.Font, select: int, auto_fill: bool = True):
            if auto_fill:
                screen.fill((0,0,0))
            for i, option in enumerate(options):
                color = (255, 0, 0) if i == select else (255, 255, 255)
                text_surface = font.render(option, True, color)
                x = self.x // 2 - text_surface.get_width() // 2
                y = self.y // 2 - len(options) * 30 + i * 60
                screen.blit(text_surface, (x, y))

        def menu_draw_advanced(self, screen, options: list[str], font: pygame.font.Font, select: int, auto_fill: bool = True, color_selected: tuple = (255, 0, 0), color_unselected: tuple = (255, 255, 255), roll_mode: bool = False, roll_config: int = 0):
            if auto_fill:
                screen.fill((0,0,0))
            for i, option in enumerate(options):
                color = color_selected if i == select else color_unselected
                text_surface = font.render(option, True, color)
                x = self.x // 2 - text_surface.get_width() // 2
                y = self.y // 2 - len(options) * 30 + i * 60
                if roll_mode:
                    y += roll_config
                screen.blit(text_surface, (x, y))