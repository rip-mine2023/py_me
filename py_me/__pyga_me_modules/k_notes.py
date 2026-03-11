import pygame
from py_me import os_me
import events
import time

class k_notes:
    NONE = 1073742094
    V_DO = 1073742095
    V_RE = 1073742096
    V_MI = 1073742097
    V_FA = 1073742098
    V_SOL = 1073742099
    V_LA = 1073742101
    V_TI = 1073742102
    V_DO2 = 1073742103
    V_RE2 = 1073742104
    V_MI2 = 1073742105
    NOTEPLAYED = 1073742106
    NOTESTOP = 1073742107
    NOTESTOP_INACCURATE = 1073742113
    NULLNOTEPLAYED = 1073742118
    NULLNOTESTOP = 1073742119
    NULLNOTESTOP_INACCURATE = 1073742120
    def init(display: pygame.display = None):
        import pyga_me
        k_notes.pyga_me = pyga_me
        os_me.details.enable_rich_traceback = False
        os_me.details.silent_FileHunter = True
        pygame.init()
        pygame.mixer.init()
        pygame.display.init()
        k_notes.a = True
        k_notes.sons = {}
        k_notes.screen = display
        os_me.details.enable_logging = False
        k_notes.extended_mode = False
        k_notes.r, k_notes.g, k_notes.b = 65, 105, 225
        k_notes.animation_timer = {
        "red": 0,
        "green": 0,
        "blue": 0
        }
        k_notes.basic = False
        k_notes.extended_mode_timer = 2000
        try:
            DO = pygame.mixer.Sound(os_me.path.FileHunter_SUPER('notas/do.wav'))
            RE = pygame.mixer.Sound(os_me.path.FileHunter_SUPER('notas/re.wav'))
            MI = pygame.mixer.Sound(os_me.path.FileHunter_SUPER('notas/mi.wav'))
            FA = pygame.mixer.Sound(os_me.path.FileHunter_SUPER('notas/fá.wav'))
            SOL =pygame.mixer.Sound(os_me.path.FileHunter_SUPER('notas/sol.wav'))
            LA = pygame.mixer.Sound(os_me.path.FileHunter_SUPER('notas/lá.wav')) 
            TI = pygame.mixer.Sound(os_me.path.FileHunter_SUPER('notas/si.wav'))
            DO2 = pygame.mixer.Sound(os_me.path.FileHunter_SUPER('notas/do2.wav'))
            RE2 = pygame.mixer.Sound(os_me.path.FileHunter_SUPER('notas/re2.wav'))
            MI2 = pygame.mixer.Sound(os_me.path.FileHunter_SUPER('notas/mi2.wav'))
        except Exception as e:
            raise e
        k_notes.VALUES = [None, DO , RE , MI , FA , SOL ,LA , TI , DO2 , RE2 , MI2]


    def basic_display_test():
        if k_notes.screen is None:
                k_notes.screen = pygame.display.set_mode((400, 300))
                k_notes.basic = True
        return k_notes.screen
    
    class UltraSondService:
            extended_mode: bool = False

            extended_mode_timer: int = 2000

            new_notes: list = []

            note_number: int = 11

            notes_names: dict = {}

            @classmethod
            def music_in_the_keys(cls, *keys: int, note: tuple = ()):
                notes = []
                valid_keys = []
    
                # filtra teclas válidas
                for k in keys:
                    if k in range(pygame.K_UNKNOWN, pygame.K_AC_BACK):
                        valid_keys.append(k)
    
                # pega sons das notas
                for n in note:
                    if n == k_notes.V_DO:
                        notes.append(k_notes.VALUES[1])
                    elif n == k_notes.V_RE:
                        notes.append(k_notes.VALUES[2])
                    elif n == k_notes.V_MI:
                        notes.append(k_notes.VALUES[3])
                    elif n == k_notes.V_FA:
                        notes.append(k_notes.VALUES[4])
                    elif n == k_notes.V_SOL:
                        notes.append(k_notes.VALUES[5])
                    elif n == k_notes.V_LA:
                        notes.append(k_notes.VALUES[6])
                    elif n == k_notes.V_TI:
                        notes.append(k_notes.VALUES[7])
                    elif n == k_notes.V_DO2:
                        notes.append(k_notes.VALUES[8])
                    elif n == k_notes.V_RE2:
                        notes.append(k_notes.VALUES[9])
                    elif n == k_notes.V_MI2:
                        notes.append(k_notes.VALUES[10])
                    else:
                        for nu in cls.new_notes:
                            if n == nu:
                                notes.append(k_notes.VALUES[nu])
    
                # associa tecla → nota
                for k, n in zip(valid_keys, notes):
                    k_notes.sons[k] = n
                
                k_notes.extended_mode =  cls.extended_mode
                k_notes.extended_mode_timer = cls.extended_mode_timer

            @classmethod
            def register_new_note(cls, sound: pygame.mixer.Sound, name: str = "null"):
                    cls.new_notes.append(cls.note_number)
                    k_notes.VALUES.append(sound)
                    cls.notes_names[cls.note_number] = name
                    cls.note_number += 1
                    return cls.note_number - 1

    def name_from_note(note: int) -> str:
            for key, value in k_notes.sons.items():
                if key == note:
                    if value == k_notes.VALUES[1]:
                        return "DO"
                    elif value == k_notes.VALUES[2]:
                        return "RE"
                    elif value == k_notes.VALUES[3]:
                        return "MI"
                    elif value == k_notes.VALUES[4]:
                        return "FA"
                    elif value == k_notes.VALUES[5]:
                        return "SOL"
                    elif value == k_notes.VALUES[6]:
                        return "LA"
                    elif value == k_notes.VALUES[7]:
                        return "TI"
                    elif value == k_notes.VALUES[8]:
                        return "DO2"
                    elif value == k_notes.VALUES[9]:
                        return "RE2"
                    elif value == k_notes.VALUES[10]:
                        return "MI2"
                    else:
                        for idx in k_notes.UltraSondService.notes_names:
                            if k_notes.VALUES[idx] == value:
                                return k_notes.UltraSondService.notes_names[idx]
            return "nota desconhecida"
                
    def sond_service(service: int):
        if service >= 1:
            k_notes.sons.update({
                pygame.K_1: k_notes.VALUES[1],
                pygame.K_2: k_notes.VALUES[2],
                pygame.K_3: k_notes.VALUES[3],
                pygame.K_4: k_notes.VALUES[4],
                pygame.K_5: k_notes.VALUES[5],
                pygame.K_6: k_notes.VALUES[6],
                pygame.K_7: k_notes.VALUES[7],
                pygame.K_8: k_notes.VALUES[8],
                pygame.K_9: k_notes.VALUES[9],
                pygame.K_0: k_notes.VALUES[10]})
        if service >= 2:
            k_notes.sons.update({
                pygame.K_KP1: k_notes.VALUES[1],
                pygame.K_KP2: k_notes.VALUES[2],
                pygame.K_KP3: k_notes.VALUES[3],
                pygame.K_KP4: k_notes.VALUES[4],
                pygame.K_KP5: k_notes.VALUES[5],
                pygame.K_KP6: k_notes.VALUES[6],
                pygame.K_KP7: k_notes.VALUES[7],
                pygame.K_KP8: k_notes.VALUES[8],
                pygame.K_KP9: k_notes.VALUES[9],
                pygame.K_KP0: k_notes.VALUES[10]})
            if service >= 3:
                k_notes.extended_mode = True
            if service >= 4:
                k_notes.sons.update({
                    pygame.K_UP: k_notes.VALUES[1],
                    pygame.K_DOWN: k_notes.VALUES[2],
                    pygame.K_LEFT: k_notes.VALUES[3],
                    pygame.K_RIGHT: k_notes.VALUES[4],
                    pygame.K_w: k_notes.VALUES[5],
                    pygame.K_s: k_notes.VALUES[6],
                    pygame.K_d: k_notes.VALUES[7],
                    pygame.K_a: k_notes.VALUES[8],
                    pygame.K_q: k_notes.VALUES[9],
                    pygame.K_e: k_notes.VALUES[10]
                })

    def extended_mode_config(timeout: int = 2000) -> None:
        k_notes.extended_mode_timer = timeout

    def run_time(event: pygame.event.Event) -> bool:
        if k_notes.basic:
            k_notes.screen.fill((k_notes.r, k_notes.g, k_notes.b))
            k_notes.animation_timer["red"] += 1
            k_notes.animation_timer["green"] += 1
            k_notes.animation_timer["blue"] += 1
            if k_notes.animation_timer["red"] >= 5:
                k_notes.r += 1
                k_notes.animation_timer["red"] = 0
            if k_notes.animation_timer["green"] >= 7:
                k_notes.g += 1
                k_notes.animation_timer["green"] = 0
            if k_notes.animation_timer["blue"] >= 9:
                k_notes.b += 1
                k_notes.animation_timer["blue"] = 0
            if k_notes.r > 255:
                k_notes.r = 0
            if k_notes.g > 255:
                k_notes.g = 0
            if k_notes.b > 255:
                k_notes.b = 0
        if event.type == pygame.QUIT:
            k_notes.a = False
            return k_notes.a
        if event.type == pygame.KEYDOWN:
            if event.key in k_notes.sons:
                if k_notes.sons[event.key] is None:  
                    events.events_inmoment.append(events.event(k_notes.NULLNOTEPLAYED, event.key))
                    return k_notes.a
                # Toca em loop
                k_notes.sons[event.key].play(-1)
                events.events_inmoment.append(events.event(k_notes.NOTEPLAYED, event.key))
    
        elif event.type == pygame.KEYUP:
            if event.key in k_notes.sons:
                if not k_notes.extended_mode:
                    if k_notes.sons[event.key] is None:  
                        events.events_inmoment.append(events.event(k_notes.NULLNOTESTOP, event.key))
                    else:
                        events.events_inmoment.append(events.event(k_notes.NOTESTOP, event.key))
                        # Modo normal: para imediatamente
                        k_notes.sons[event.key].stop()
                else:
                    # Modo extendido: fadeout suave em 2 segundos
                    #mostrar evento de nota parando impreciso para lidar com o tempo de fadeout
                    if k_notes.sons[event.key] is None:
                        events.events_inmoment.append(events.event(k_notes.NULLNOTESTOP_INACCURATE, event.key))
                    else:
                        k_notes.sons[event.key].fadeout(k_notes.extended_mode_timer)
                        events.events_inmoment.append(events.event(k_notes.NOTESTOP_INACCURATE, event.key))
        return k_notes.a