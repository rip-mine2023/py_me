import pygame
from typing import Callable
from collections import deque

P2DCREATED = 1073742124
P2DUPDATE = 1073742125
P2DRMOVE = 1073742126
P2DLMOVE = 1073742127
P2DJUMP = 1073742128
P2DLANDED = 1073742129
P2DSPECIALKEYPRESSED = 1073742130
P2DDEAD =1073742131
RPGCREATED = 1073742132
RPGUPDATE = 1073742133
RPGMOVE = 1073742134
RPGSPECIALKEYPRESSED = 1073742135
RPGDEAD = 1073742136
USEREVENT = 1073742137

class Player2D:
    from pyga_me import pyga_me
    events = pyga_me.events
    def __init__(self, size: tuple[int], right_frames_stop: list[pygame.Surface]| str , left_frames_stop: list[pygame.Surface]| str, right_frames_walking: list[pygame.Surface]| str, left_frames_walking: list[pygame.Surface]| str, gravity: int, vel:int, jump_limit: int, screen):
        Player2D.events.events_inmoment.append(Player2D.events.event(P2DCREATED, self))
        self.size = size
        self.r_frames = right_frames_stop
        self.l_frames = left_frames_stop
        self.r_frames_walking = right_frames_walking
        self.l_frames_walking = left_frames_walking
        self.gravity = gravity
        self.pos_x = 500
        self.pos_y = 500
        self.vel = vel
        self.lock_x_L = False
        self.lock_x_R = False
        self.lock_y_UP = False
        self.lock_y_D = False
        self.jump_control = 0
        self.jump_limit = jump_limit
        self.x, self.y = screen.get_size()
        self.direction = "left"
        self.state = "stop"
        self.player = Player2D.pyga_me.Animation()
        self.frames = []
        self.frames_control = True
        if isinstance(right_frames_stop, str) and isinstance(left_frames_stop, str) and isinstance(right_frames_walking, str) and isinstance(left_frames_walking, str):
            self.frames_cache = {
                "1": self.player.extract_frames_gif(right_frames_walking, (self.size[0], self.size[1])),
                "2": self.player.extract_frames_gif(right_frames_stop, (self.size[0], self.size[1])),
                "3": self.player.extract_frames_gif(left_frames_walking, (self.size[0], self.size[1])),
                "4": self.player.extract_frames_gif(left_frames_stop, (self.size[0], self.size[1])),
            }
        elif isinstance(right_frames_stop, list) and isinstance(left_frames_stop, list) and isinstance(right_frames_walking, list) and isinstance(left_frames_walking, list):
            self.frames_cache = {
                "1": self.r_frames_walking,
                "2": self.r_frames,
                "3": self.l_frames_walking,
                "4": self.l_frames,
            }
        else:
            #depois que eu fizer a classe de exeção eu irei colocar o raise aqui, por enquanto só vou colocar um pass para não dar erro de sintaxe
            pass
        self.alive = True
        self._eventsinmoment: deque[pygame.event.Event] = deque()

    def colect_events(self, event: pygame.event.Event):
        self._eventsinmoment.append(event)
    
    def _get_colect_events(self):
        events = []
        try:
            ev: pygame.event.Event = self._eventsinmoment.popleft()
            events.append(ev)
        except:
            pass
        return events
        
    def update(self, special_keys: int | list[int], consequences: Callable | list[Callable], AltoXYBarrier: bool = True, screen = None):
        if not self.alive:
            self.events.events_inmoment.append(Player2D.events.event(P2DDEAD, self))
            return 
        Player2D.events.events_inmoment.append(Player2D.events.event(P2DUPDATE, self))
        self.x, self.y = screen.get_size()
        keys = pygame.key.get_pressed()
        if AltoXYBarrier:
            ma0 = max(self.y, self.pos_y)
            #fazer que o pulo recarregue mesmo sem o travamento direto do usuario quando AltoXYBarrier estiver ativo
            if ma0 == self.pos_y or self.lock_y_D:
                self.jump_control = 0
        else:
            if self.lock_y_D:
                self.jump_control = 0
            
        if AltoXYBarrier:
            ma = max(self.y, self.pos_y)
            if not self.lock_y_D and not ma == self.pos_y:
                 self.pos_y += self.gravity
                 Player2D.events.events_inmoment.append(Player2D.events.event(P2DLANDED, [self, self.pos_y]))
        else:
            if not self.lock_y_D:
                self.pos_y += self.gravity
        if keys[pygame.K_RIGHT]:
            if AltoXYBarrier:
                ma2 = max(self.x, self.pos_x)
                if not self.lock_x_R and not ma2 == self.pos_x:
                    self.state = "walking"
                    self.pos_x += self.vel
                    self.direction = "right"
                    Player2D.events.events_inmoment.append(Player2D.events.event(P2DRMOVE, [self, self.pos_x]))
            else:
                if not self.lock_x_R:
                    self.state = "walking"
                    self.pos_x += self.vel
                    self.direction = "right"
                    Player2D.events.events_inmoment.append(Player2D.events.event(P2DRMOVE, [self, self.pos_x]))
        elif keys[pygame.K_LEFT]:
            if AltoXYBarrier:
                mim = min(0, self.pos_x)
                if not self.lock_x_L and mim == 0:
                    self.state = "walking"
                    self.pos_x -= self.vel
                    self.direction = "left"
                    Player2D.events.events_inmoment.append(Player2D.events.event(P2DLMOVE, [self, self.pos_x]))
            else:
                if not self.lock_x_L:
                    self.state = "walking"
                    self.pos_x -= self.vel
                    self.direction = "left"
                    Player2D.events.events_inmoment.append(Player2D.events.event(P2DLMOVE, [self, self.pos_x]))
        if not keys[pygame.K_RIGHT] or not keys[pygame.K_LEFT]:
            self.state = "stop"
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                if not self.lock_y_UP:
                    if self.jump_control < self.jump_limit:
                        if self.jump_control < self.jump_limit // 4:
                                self.jump_control += 18 + self.gravity
                                self.pos_y -= 18 + self.gravity
                                Player2D.events.events_inmoment.append(Player2D.events.event(P2DJUMP, [self, self.pos_y]))
                        elif self.jump_control < self.jump_limit // 3:
                                self.jump_control += 9 + self.gravity
                                self.pos_y -= 9 + self.gravity
                                Player2D.events.events_inmoment.append(Player2D.events.event(P2DJUMP, [self, self.pos_y]))
                        elif self.jump_control < self.jump_limit // 2:
                                self.jump_control += 4 + self.gravity
                                self.pos_y -= 4 + self.gravity
                                Player2D.events.events_inmoment.append(Player2D.events.event(P2DJUMP, [self, self.pos_y]))
        for event in self._get_colect_events():
            event: pygame.event.Event
            if event.type == pygame.KEYUP:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        self.jump_control = self.jump_limit
        if isinstance(special_keys, int):
            if isinstance(consequences, Callable):
                if keys[special_keys]:
                    Player2D.events.events_inmoment.append(Player2D.events.event(P2DSPECIALKEYPRESSED, [self, special_keys, str(consequences)]))
                    consequences()
            elif isinstance(consequences, list):
                a = consequences[0]
                if keys[special_keys]:
                    a()
                    Player2D.events.events_inmoment.append(Player2D.events.event(P2DSPECIALKEYPRESSED, [self, special_keys, str(consequences[0])]))
        elif isinstance(special_keys, list):
            if isinstance(consequences, Callable):
                b = special_keys[0]
                if keys[b]:
                    consequences()
                    Player2D.events.events_inmoment.append(Player2D.events.event(P2DSPECIALKEYPRESSED, [self, special_keys[0], str(consequences)]))
            elif isinstance(consequences, list):
                for i, s_key in enumerate(special_keys):
                    try:
                        c = consequences[i]
                        if keys[s_key]:
                            c()
                            Player2D.events.events_inmoment.append(Player2D.events.event(P2DSPECIALKEYPRESSED, [self, special_keys[i], str(consequences[i])]))
                    except IndexError:
                        pass

    def draw(self, screen, alto_fill: bool = True):
        if not self.alive:
            return
        if self.direction == "right":
            if self.state == "walking":
                try:
                    x = self.pos_x - self.size[0] //2
                    y = self.pos_y - self.size[1] 
                except IndexError:
                    x = self. pos_x - self.size // 2
                    y = self. pos_y - self.size
                if self.frames_control:
                    self.frames_cache["1"] = self.player.extract_frames_gif(self.r_frames_walking, (self.size[0], self.size[1]))
                    self.frames_control = False
            else:
                try:
                    x = self.pos_x - self.size[0] // 2
                    y = self.pos_y - self.size[1]
                except IndexError:
                    x = self. pos_x - self.size // 2
                    y = self. pos_y - self.size 
                if self.frames_control:
                    self.frames_cache["2"] = self.player.extract_frames_gif(self.r_frames, (self.size[0], self.size[1]))
                    self.frames_control = False
        else:
            if self.state == "walking":
                try:
                    x = self.pos_x - self.size[0] // 2
                    y = self.pos_y - self.size[1] 
                except IndexError:
                    x = self. pos_x - self.size // 2
                    y = self. pos_y - self.size 
                if self.frames_control:
                    self.frames_cache["3"] = self.player.extract_frames_gif(self.l_frames_walking, (self.size[0], self.size[1]))
                    self.frames_control = False
            else:
                try:
                    x = self.pos_x - self.size[0] // 2
                    y = self.pos_y - self.size[1]
                except IndexError:
                    x = self. pos_x - self.size // 2
                    y = self. pos_y - self.size
                if self.frames_control:
                    self.frames_cache["4"] = self.player.extract_frames_gif(self.l_frames, (self.size[0], self.size[1]))
                    self.frames_control = False
        if alto_fill:
            screen.fill(0,0,0)
        if self.direction == "right":
            if self.state == "walking":
                self.frames = self.frames_cache["1"]
            else:
                self.frames = self.frames_cache["2"]
        else:
            if self.state == "walking":
                self.frames = self.frames_cache["3"]
            else:
                self.frames = self.frames_cache["4"]
        self.player.animation(self.frames, screen, False, 60, (x, y))
    
    def get_size(self):
        return self.size[0], self.size[1] if isinstance(self.size, tuple) or isinstance(self.size, list) else self.size, self.size


class PlayerRPG:
    def __init__(self, frames_up_stop: list, frames_down_stop: list, frames_left_stop: list, frames_right_stop: list, frames_up_walking: list, frames_down_walking: list, frames_left_walking: list, frames_right_walking: list, size: tuple[int], vel:int, screen):
        from pyga_me import pyga_me
        self.pyga_me = pyga_me
        self.animation = pyga_me.Animation()
        self.frames_up_stop = frames_up_stop
        self.frames_down_stop = frames_down_stop
        self.frames_left_stop = frames_left_stop
        self.frames_right_stop = frames_right_stop
        self.frames_up_walking = frames_up_walking
        self.frames_down_walking = frames_down_walking
        self.frames_left_walking = frames_left_walking
        self.frames_right_walking = frames_right_walking
        self.size = size
        self.inventory = []
        self.alive = True
        self.life = 100
        self.pos_x = 500
        self.pos_y = 500
        self.vel = vel
        self.lock_x_L = False
        self.lock_x_R = False
        self.lock_y_U = False
        self.lock_y_D = False
        self.x, self.y = screen.get_size()
        self.direction = "down"
        self.state = "stop"
        self.cache_frames = {
            "up_stop": self.animation.extract_frames_gif(self.frames_up_stop, (self.size[0], self.size[1])),
            "down_stop": self.animation.extract_frames_gif(self.frames_down_stop, (self.size[0], self.size[1])),
            "left_stop": self.animation.extract_frames_gif(self.frames_left_stop, (self.size[0], self.size[1])),
            "right_stop": self.animation.extract_frames_gif(self.frames_right_stop, (self.size[0], self.size[1])),
            "up_walking": self.animation.extract_frames_gif(self.frames_up_walking, (self.size[0], self.size[1])),
            "down_walking": self.animation.extract_frames_gif(self.frames_down_walking, (self.size[0], self.size[1])),
            "left_walking": self.animation.extract_frames_gif(self.frames_left_walking, (self.size[0], self.size[1])),
            "right_walking": self.animation.extract_frames_gif(self.frames_right_walking, (self.size[0], self.size[1])),
        }
        self.frames_control = True
        self.pyga_me.events.events_inmoment.append(self.pyga_me.events.event(self.pyga_me.RPGCREATED, self))

    def update(self, special_keys: int | list[int], consequences: Callable | list[Callable], AltoXYBarrier: bool = False, screen = None):
        if not self.alive:
            self.pyga_me.events.events_inmoment.append(self.pyga_me.events.event(self.pyga_me.RPGDEAD, self))
            return
        keys = pygame.key.get_pressed()
        if AltoXYBarrier:
            ma0 = max(self.y, self.pos_y)
            ma1 = max(self.x, self.pos_x)
            mim0 = min(0, self.pos_x)
            mim1 = min(0, self.pos_y)
            if not ma0 == self.pos_y or self.lock_y_U:
                if keys[pygame.K_UP]:
                    self.pos_y -= self.vel
                    self.direction = "up"
                    self.state = "walking"
                    self.pyga_me.events.events_inmoment.append(self.pyga_me.events.event(self.pyga_me.RPGMOVE, [self, self.pos_x, self.pos_y]))
            if not mim1 == 0 or self.lock_y_D:
                if keys[pygame.K_DOWN]:
                    self.pos_y += self.vel
                    self.direction = "down"
                    self.state = "walking"
                    self.pyga_me.events.events_inmoment.append(self.pyga_me.events.event(self.pyga_me.RPGMOVE, [self, self.pos_x, self.pos_y]))
            if not ma1 == self.pos_x or self.lock_x_R:
                if keys[pygame.K_LEFT]:
                    self.pos_x -= self.vel
                    self.direction = "left"
                    self.state = "walking"
                    self.pyga_me.events.events_inmoment.append(self.pyga_me.events.event(self.pyga_me.RPGMOVE, [self, self.pos_x, self.pos_y]))
            if not mim0 == 0 or self.lock_x_L:
                if keys[pygame.K_RIGHT]:
                    self.pos_x += self.vel
                    self.direction = "right"
                    self.state = "walking"
                    self.pyga_me.events.events_inmoment.append(self.pyga_me.events.event(self.pyga_me.RPGMOVE, [self, self.pos_x, self.pos_y]))
            if not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                self.state = "stop"
        else:
            if not self.lock_y_U:
                if keys[pygame.K_UP]:
                    self.pos_y -= self.vel
                    self.direction = "up"
                    self.state = "walking"
                    self.pyga_me.events.events_inmoment.append(self.pyga_me.events.event(self.pyga_me.RPGMOVE, [self, self.pos_x, self.pos_y]))
            if not self.lock_y_D:
                if keys[pygame.K_DOWN]:
                    self.pos_y += self.vel
                    self.direction = "down"
                    self.state = "walking"
                    self.pyga_me.events.events_inmoment.append(self.pyga_me.events.event(self.pyga_me.RPGMOVE, [self, self.pos_x, self.pos_y]))
            if not self.lock_x_L:    
                if keys[pygame.K_LEFT]:
                    self.pos_x -= self.vel
                    self.direction = "left"
                    self.state = "walking"
                    self.pyga_me.events.events_inmoment.append(self.pyga_me.events.event(self.pyga_me.RPGMOVE, [self, self.pos_x, self.pos_y]))
            if not self.lock_x_R:
                if keys[pygame.K_RIGHT]:
                    self.pos_x += self.vel
                    self.direction = "right"
                    self.state = "walking"
                    self.pyga_me.events.events_inmoment.append(self.pyga_me.events.event(self.pyga_me.RPGMOVE, [self, self.pos_x, self.pos_y]))
            if not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                self.state = "stop"
        if special_keys and consequences:
                if isinstance(special_keys, int):
                    if isinstance(consequences, Callable):
                        if keys[special_keys]:
                            consequences()
                            self.pyga_me.events.events_inmoment.append(self.pyga_me.events.event(self.pyga_me.RPGSPECIALKEYPRESSED, [self, special_keys, consequences]))
                elif isinstance(special_keys, list):
                    if isinstance(consequences, list):
                        for i, s_key in enumerate(special_keys):
                            try:
                                c = consequences[i]
                                if keys[s_key]:
                                    c()
                                    self.pyga_me.events.events_inmoment.append(self.pyga_me.events.event(self.pyga_me.RPGSPECIALKEYPRESSED, [self, special_keys[i], consequences[i]]))
                            except IndexError:
                                pass
                    elif isinstance(consequences, Callable):
                        a = special_keys[0]
                        if keys[a]:
                            consequences()
                            self.pyga_me.events.events_inmoment.append(self.pyga_me.events.event(self.pyga_me.RPGSPECIALKEYPRESSED, [self, special_keys[0], consequences]))
        
    def draw(self, screen, alto_fill: bool = True):
        if not self.alive:
            return
        if self.direction == "up":
            if self.state == "walking":
                frames = self.cache_frames["up_walking"]
            else:
                frames = self.cache_frames["up_stop"]
            if self.frames_control:
                try:
                    self.cache_frames["up_walking"] = self.animation.extract_frames_gif(self.frames_up_walking, (self.size[0], self.size[1]))
                    self.cache_frames["up_stop"] = self.animation.extract_frames_gif(self.frames_up_stop, (self.size[0], self.size[1]))
                except IndexError:
                    self.cache_frames["up_walking"] = self.animation.extract_frames_gif(self.frames_up_walking, (self.size, self.size))
                    self.cache_frames["up_stop"] = self.animation.extract_frames_gif(self.frames_up_stop, (self.size, self.size))
                finally:
                    self.frames_control = False
        elif self.direction == "down":
            if self.state == "walking":
                frames = self.cache_frames["down_walking"]
            else:
                frames = self.cache_frames["down_stop"]
            if self.frames_control:
                try:
                    self.cache_frames["down_walking"] = self.animation.extract_frames_gif(self.frames_down_walking, (self.size[0], self.size[1]))
                    self.cache_frames["down_stop"] = self.animation.extract_frames_gif(self.frames_down_stop, (self.size[0], self.size[1]))
                except IndexError:
                    self.cache_frames["down_walking"] = self.animation.extract_frames_gif(self.frames_down_walking, (self.size, self.size))
                    self.cache_frames["down_stop"] = self.animation.extract_frames_gif(self.frames_down_stop, (self.size, self.size))
                finally:
                    self.frames_control = False
        elif self.direction == "left":
            if self.state == "walking":
                frames = self.cache_frames["left_walking"]
            else:
                frames = self.cache_frames["left_stop"]
            if self.frames_control:
                try:
                    self.cache_frames["left_walking"] = self.animation.extract_frames_gif(self.frames_left_walking, (self.size[0], self.size[1]))
                    self.cache_frames["left_stop"] = self.animation.extract_frames_gif(self.frames_left_stop, (self.size[0], self.size[1]))
                except IndexError:
                    self.cache_frames["left_walking"] = self.animation.extract_frames_gif(self.frames_left_walking, (self.size, self.size))
                    self.cache_frames["left_stop"] = self.animation.extract_frames_gif(self.frames_left_stop, (self.size, self.size))
                finally:
                    self.frames_control = False
        elif self.direction == "right":
            if self.state == "walking":
                frames = self.cache_frames["right_walking"]
            else:
                frames = self.cache_frames["right_stop"]
            if self.frames_control:
                try:
                    self.cache_frames["right_walking"] = self.animation.extract_frames_gif(self.frames_right_walking, (self.size[0], self.size[1]))
                    self.cache_frames["right_stop"] = self.animation.extract_frames_gif(self.frames_right_stop, (self.size[0], self.size[1]))
                except IndexError:
                    self.cache_frames["right_walking"] = self.animation.extract_frames_gif(self.frames_right_walking, (self.size, self.size))
                    self.cache_frames["right_stop"] = self.animation.extract_frames_gif(self.frames_right_stop, (self.size, self.size))
                finally:
                    self.frames_control = False
        x = self.pos_x - self.size[0] // 2
        y = self.pos_y - self.size[1]
        if alto_fill:
            screen.fill(0,0,0)
        self.animation.animation(frames, screen, False, 60, (x, y))
    
    def get_size(self):
        return self.size[0], self.size[1] if isinstance(self.size, tuple) or isinstance(self.size, list) else self.size, self.size