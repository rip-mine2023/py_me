import time
from py_me import os_me
import os
import hashlib
import requests as rs
import pygame
from PIL import Image, ImageSequence
from py_me import os_me
import time
from collections import deque
from dataclasses import dataclass
from typing import Callable


class pyga_me:
    """pyga_me is a pygame helper module for sound, animation, and 2D object management.

    classes:
    - Values
    - k_notes
      - UltraSondService
    - events
      - event
    - animation
      - menu
    - objects
      - Player2D
      - PlayerRPG

    def:
    - init
    - load_file
    """
    @dataclass
    class Values:
        """Shared runtime state and note/event constants for pyga_me."""
        a: bool 
        sons: dict 
        extended_mode: bool
        r: int
        g: int
        b: int
        animation_timer: dict
        basic: bool
        extended_mode_timer: int
        VALUES: list[None | pygame.mixer.Sound]
        V_NONE: int = 1073742094
        V_DO: int = 1073742095
        V_RE: int = 1073742096
        V_MI: int = 1073742097
        V_FA: int = 1073742098
        V_SOL: int = 1073742099
        V_LA: int = 1073742100
        V_TI: int = 1073742101
        V_DO2: int = 1073742102
        V_RE2: int = 1073742103
        V_MI2: int = 1073742104
        NOTEPLAYED: int = 1073742105
        NOTESTOP: int = 1073742106
        LAGANIMATION: int = 1073742107
        SAFEANIMATION: int = 1073742108
        NEGATIVEROLL: int = 1073742109
        POSITIVEROLL: int = 1073742110
        GIFEXECUTED: int = 1073742111
        NOTESTOP_INACCURATE: int = 1073742112
        NULLNOTEPLAYED: int = 1073742113
        NULLNOTESTOP: int = 1073742114
        NULLNOTESTOP_INACCURATE: int = 1073742115
        SELECTUP: int = 1073742116
        SELECTDOWN: int = 1073742117
        SELECTCONFIRM: int = 1073742118
        SAFEDOWNLOAD: int =1073742119
        EXCEPTDOWNLOAD: int = 1073742120
        LAGDOWNLOAD: int = 1073742121
        P2DCREATED: int = 1073742122
        P2DUPDATE: int = 1073742123
        P2DRMOVE: int = 1073742124
        P2DLMOVE: int = 1073742125
        P2DJUMP: int = 1073742126
        P2DLANDED: int = 1073742127
        P2DSPECIALKEYPRESSED: int = 1073742128
        P2DDEAD: int = 1073742129
        RPGCREATED: int = 1073742130
        RPGUPDATE: int = 1073742131
        RPGMOVE: int = 1073742132
        RPGSPECIALKEYPRESSED: int = 1073742133
        RPGDEAD: int = 1073742134
        USEREVENT: int = 1073742135
        screen: pygame.Surface

    def init():
        """Initialize the pyga_me system and configure helper settings.

        Behavior:
            - initializes the internal note subsystem
            - disables rich traceback output
            - enables silent file searching

        Example:
            >>> pyga_me.init()

        Returns:
            None
        """
        pyga_me.k_notes.init()
        os_me.details.enable_rich_traceback = False
        os_me.details.silent_FileHunter = True
    

    class k_notes:
        """Collection of note management and basic pygame helpers."""
        def init(display: pygame.display = None):
            """Initialize pygame, mixer, display settings, and default note values.

            Args:
                display (pygame.display, optional): Existing pygame display surface to reuse.
                    Defaults to None.

            Behavior:
                - initializes pygame subsystems
                - configures default note state and colors
                - loads standard note audio files

            Example:
                >>> pyga_me.k_notes.init()

            Returns:
                None
            """
            os_me.details.enable_rich_traceback = False
            os_me.details.silent_FileHunter = True
            pygame.init()
            pygame.mixer.init()
            pygame.display.init()
            pyga_me.Values.a = True
            pyga_me.Values.sons = {}
            pyga_me.k_notes.screen = display
            os_me.details.enable_logging = False
            pyga_me.Values.extended_mode = False
            pyga_me.Values.r, pyga_me.Values.g, pyga_me.Values.b = 65, 105, 225
            pyga_me.Values.animation_timer = {
            "red": 0,
            "green": 0,
            "blue": 0
            }
            pyga_me.Values.basic = False
            pyga_me.Values.extended_mode_timer = 2000
            do = pyga_me.load_file("https://s3.ustatik.com/audio.com.audio/source/66/67/1859866551426766-1859866551770905.wav?response-content-disposition=attachment%3B%20filename%3D%22do.wav%22&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=F0E8U41NBMMW3Y027UTJ%2F20260317%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20260317T002357Z&X-Amz-SignedHeaders=host&X-Amz-Expires=518400&X-Amz-Signature=a9ae55ea4a5fb0834bf5d9a7411a1a94474ce98f5161ca8d53a73ff6b1db2dd4")
            re = pyga_me.load_file("https://s3.ustatik.com/audio.com.audio/source/65/83/1859866698638365-1859866699039589.wav?response-content-disposition=attachment%3B%20filename%3D%22re.wav%22&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=F0E8U41NBMMW3Y027UTJ%2F20260317%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20260317T002807Z&X-Amz-SignedHeaders=host&X-Amz-Expires=518400&X-Amz-Signature=511a399a32e232350e7ff55fbc0aecc30dae705286c3221ff91e18e9d0605320")
            mi = pyga_me.load_file("https://s3.ustatik.com/audio.com.audio/source/98/42/1859866631184298-1859866631546701.wav?response-content-disposition=attachment%3B%20filename%3D%22mi.wav%22&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=F0E8U41NBMMW3Y027UTJ%2F20260317%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20260317T002703Z&X-Amz-SignedHeaders=host&X-Amz-Expires=518400&X-Amz-Signature=f0273d38b94ee488b6d80adfaf02dbd1020e1f6eb34629c7a3b5be7f625f2dfc")
            fa = pyga_me.load_file("https://s3.ustatik.com/audio.com.audio/source/70/93/1859866550769370-1859866551195151.wav?response-content-disposition=attachment%3B%20filename%3D%22f%C3%A1.wav%22&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=F0E8U41NBMMW3Y027UTJ%2F20260317%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20260317T002433Z&X-Amz-SignedHeaders=host&X-Amz-Expires=518400&X-Amz-Signature=cc7de37e630d1aada09ce8c94611300617446c4babe97de56c682128a9462a71")
            sol = pyga_me.load_file("https://s3.ustatik.com/audio.com.audio/source/14/48/1859866875324814-1859866875555275.wav?response-content-disposition=attachment%3B%20filename%3D%22sol.wav%22&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=F0E8U41NBMMW3Y027UTJ%2F20260317%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20260317T002904Z&X-Amz-SignedHeaders=host&X-Amz-Expires=518400&X-Amz-Signature=358bfbcf0e54095f90221e56f3cd463b400dd6327dcc2247eb2eee04ed6e8664")
            la = pyga_me.load_file("https://s3.ustatik.com/audio.com.audio/source/26/02/1859866620380226-1859866620481124.wav?response-content-disposition=attachment%3B%20filename%3D%22l%C3%A1.wav%22&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=F0E8U41NBMMW3Y027UTJ%2F20260317%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20260317T002557Z&X-Amz-SignedHeaders=host&X-Amz-Expires=518400&X-Amz-Signature=3b008b3b7c3ad2a4926c2a7d502a219a73ebc880feb6e15434530f188ceafde8")
            ti = pyga_me.load_file("https://s3.ustatik.com/audio.com.audio/source/15/04/1859866833550415-1859866833965277.wav?response-content-disposition=attachment%3B%20filename%3D%22si.wav%22&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=F0E8U41NBMMW3Y027UTJ%2F20260317%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20260317T002956Z&X-Amz-SignedHeaders=host&X-Amz-Expires=518400&X-Amz-Signature=f62e4efe387158244245e84d501cc7ee59dd11c8f0fbfdef7f66c6617fbf444a")
            do2 =pyga_me.load_file("https://s3.ustatik.com/audio.com.audio/source/85/33/1859866551863385-1859866551967504.wav?response-content-disposition=attachment%3B%20filename%3D%22do2.wav%22&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=F0E8U41NBMMW3Y027UTJ%2F20260317%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20260317T002501Z&X-Amz-SignedHeaders=host&X-Amz-Expires=518400&X-Amz-Signature=0e4fabf7523a45db9e2079b4e8fe0d69905cb7a3977acc59517612e0dbfed237")
            re2 = pyga_me.load_file("https://s3.ustatik.com/audio.com.audio/source/07/08/1859866819730807-1859866819941843.wav?response-content-disposition=attachment%3B%20filename%3D%22re2.wav%22&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=F0E8U41NBMMW3Y027UTJ%2F20260317%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20260317T002841Z&X-Amz-SignedHeaders=host&X-Amz-Expires=518400&X-Amz-Signature=9db9659518cf32fe7260254eba44c35e14ace612032da85d7eb1990192a30a87")
            mi2 = pyga_me.load_file("https://s3.ustatik.com/audio.com.audio/source/19/23/1859866668502319-1859866668656658.wav?response-content-disposition=attachment%3B%20filename%3D%22mi2.wav%22&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=F0E8U41NBMMW3Y027UTJ%2F20260317%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20260317T002731Z&X-Amz-SignedHeaders=host&X-Amz-Expires=518400&X-Amz-Signature=bee0a3937dcddb557be2bd1ee0e7a015b0c1f08dcec26c9d726c335f1b7ed900")
            DO = pygame.mixer.Sound(os_me.path.FileHunter_SUPER(os.path.join("Notas@$$$", do)))
            RE = pygame.mixer.Sound(os_me.path.FileHunter_SUPER(os.path.join("Notas@$$$", re)))
            MI = pygame.mixer.Sound(os_me.path.FileHunter_SUPER(os.path.join("Notas@$$$", mi)))
            FA = pygame.mixer.Sound(os_me.path.FileHunter_SUPER(os.path.join("Notas@$$$", fa)))
            SOL =pygame.mixer.Sound(os_me.path.FileHunter_SUPER(os.path.join("Notas@$$$", sol)))
            LA = pygame.mixer.Sound(os_me.path.FileHunter_SUPER(os.path.join("Notas@$$$", la))) 
            TI = pygame.mixer.Sound(os_me.path.FileHunter_SUPER(os.path.join("Notas@$$$", ti)))
            DO2 = pygame.mixer.Sound(os_me.path.FileHunter_SUPER(os.path.join("Notas@$$$", do2)))
            RE2 = pygame.mixer.Sound(os_me.path.FileHunter_SUPER(os.path.join("Notas@$$$", re2)))
            MI2 = pygame.mixer.Sound(os_me.path.FileHunter_SUPER(os.path.join("Notas@$$$", mi2)))
            
            pyga_me.Values.VALUES = [None, DO , RE , MI , FA , SOL ,LA , TI , DO2 , RE2 , MI2]


        def basic_display_test():
            """Create a basic pygame display window and enable simple rendering mode.

            Behavior:
                - creates a 400x300 pygame display surface if none exists
                - sets the basic mode flag

            Example:
                >>> screen = pyga_me.k_notes.basic_display_test()

            Returns:
                pygame.Surface: The display surface used for basic rendering.
            """
            if pyga_me.Values.screen is None:
                pyga_me.Values.screen = pygame.display.set_mode((400, 300))
                pyga_me.Values.basic = True
            return pyga_me.Values.screen
    
        class UltraSondService:
            """Service class for advanced key-to-note mapping and custom note registration."""
            extended_mode: bool = False

            extended_mode_timer: int = 2000

            new_notes: list = []

            note_number: int = 11

            notes_names: dict = {}

            @classmethod
            def music_in_the_keys(cls, *keys: int, note: tuple = ()):
                """Map one or more keyboard keys to musical note sounds.

                Args:
                    *keys (int): pygame keyboard codes to bind.
                    note (tuple, optional): Note constants to assign to the keys.
                        Defaults to ().

                Behavior:
                    - filters out invalid pygame key codes
                    - resolves note constants to sound objects
                    - associates valid keys with the resolved sounds
                    - applies extended mode settings if configured

                Example:
                    >>> pyga_me.k_notes.UltraSondService.music_in_the_keys(
                    ...     pygame.K_1, pygame.K_2, note=(pyga_me.Values.V_DO, pyga_me.Values.V_RE)
                    ... )

                Returns:
                    None
                """

                notes = []
                valid_keys = []
    
                # filtra teclas válidas
                for k in keys:
                    if k in range(pygame.K_UNKNOWN, pygame.K_AC_BACK):
                        valid_keys.append(k)
    
                # pega sons das notas
                for n in note:
                    if n == pyga_me.Values.V_DO:
                        notes.append(pyga_me.Values.VALUES[1])
                    elif n == pyga_me.Values.V_RE:
                        notes.append(pyga_me.Values.VALUES[2])
                    elif n == pyga_me.Values.V_MI:
                        notes.append(pyga_me.Values.VALUES[3])
                    elif n == pyga_me.Values.V_FA:
                        notes.append(pyga_me.Values.VALUES[4])
                    elif n == pyga_me.Values.V_SOL:
                        notes.append(pyga_me.Values.VALUES[5])
                    elif n == pyga_me.Values.V_LA:
                        notes.append(pyga_me.Values.VALUES[6])
                    elif n == pyga_me.Values.V_TI:
                        notes.append(pyga_me.Values.VALUES[7])
                    elif n == pyga_me.Values.V_DO2:
                        notes.append(pyga_me.Values.VALUES[8])
                    elif n == pyga_me.Values.V_RE2:
                        notes.append(pyga_me.Values.VALUES[9])
                    elif n == pyga_me.Values.V_MI2:
                        notes.append(pyga_me.Values.VALUES[10])
                    else:
                        for nu in cls.new_notes:
                            if n == nu:
                                notes.append(pyga_me.Values.VALUES[nu])
    
                # associa tecla → nota
                for k, n in zip(valid_keys, notes):
                    pyga_me.Values.sons[k] = n
                
                pyga_me.Values.extended_mode =  cls.extended_mode
                pyga_me.Values.extended_mode_timer = cls.extended_mode_timer

            @classmethod
            def register_new_note(cls, sound: pygame.mixer.Sound | None, name: str = "null"):
                """Register a custom sound note and return its new note index.

                Args:
                    sound (pygame.mixer.Sound | None): Sound object to register or None.
                    name (str, optional): Human-readable name for the note.
                        Defaults to "null".

                Behavior:
                    - appends the new sound to the shared VALUES list
                    - stores the custom name by note index
                    - increments the next available note index

                Example:
                    >>> note_id = pyga_me.k_notes.UltraSondService.register_new_note(my_sound, "custom")

                Returns:
                    int: The assigned custom note index.
                """
                cls.new_notes.append(cls.note_number)
                pyga_me.Values.VALUES.append(sound)
                cls.notes_names[cls.note_number] = name
                cls.note_number += 1
                return cls.note_number - 1

        def name_from_note(note: int) -> str:
            """Resolve the display name of a note based on its current key mapping.

            Args:
                note (int): Keyboard key code for the note event.

            Behavior:
                - compares the mapped sound for the key against known note objects
                - returns the matching note name or a custom registered note name
                - returns a fallback label when not recognized

            Example:
                >>> pyga_me.k_notes.name_from_note(pygame.K_1)
                'DO'

            Returns:
                str: The recognized note name or 'nota desconhecida'.
            """
            for key, value in pyga_me.Values.sons.items():
                if key == note:
                    if value == pyga_me.Values.VALUES[1]:
                        return "DO"
                    elif value == pyga_me.Values.VALUES[2]:
                        return "RE"
                    elif value == pyga_me.Values.VALUES[3]:
                        return "MI"
                    elif value == pyga_me.Values.VALUES[4]:
                        return "FA"
                    elif value == pyga_me.Values.VALUES[5]:
                        return "SOL"
                    elif value == pyga_me.Values.VALUES[6]:
                        return "LA"
                    elif value == pyga_me.Values.VALUES[7]:
                        return "TI"
                    elif value == pyga_me.Values.VALUES[8]:
                        return "DO2"
                    elif value == pyga_me.Values.VALUES[9]:
                        return "RE2"
                    elif value == pyga_me.Values.VALUES[10]:
                        return "MI2"
                    else:
                        for idx in pyga_me.k_notes.UltraSondService.notes_names:
                            if pyga_me.Values.VALUES[idx] == value:
                                return pyga_me.k_notes.UltraSondService.notes_names[idx]
            return "nota desconhecida"
                
        def sond_service(service: int):
            """Configure default key-to-note mappings according to service level.

            Args:
                service (int): Service level that determines key mappings.

            Behavior:
                - maps number keys to diatonic notes for service level 1
                - adds keypad mappings for service level 2
                - activates extended mode at level 3
                - adds navigation and letter key mappings at level 4

            Example:
                >>> pyga_me.k_notes.sond_service(4)

            Returns:
                None
            """
            if service >= 1:
                pyga_me.Values.sons.update({
                    pygame.K_1: pyga_me.Values.VALUES[1],
                    pygame.K_2: pyga_me.Values.VALUES[2],
                    pygame.K_3: pyga_me.Values.VALUES[3],
                    pygame.K_4: pyga_me.Values.VALUES[4],
                    pygame.K_5: pyga_me.Values.VALUES[5],
                    pygame.K_6: pyga_me.Values.VALUES[6],
                    pygame.K_7: pyga_me.Values.VALUES[7],
                    pygame.K_8: pyga_me.Values.VALUES[8],
                    pygame.K_9: pyga_me.Values.VALUES[9],
                    pygame.K_0: pyga_me.Values.VALUES[10]})
            if service >= 2:
                pyga_me.Values.sons.update({
                    pygame.K_KP1: pyga_me.Values.VALUES[1],
                    pygame.K_KP2: pyga_me.Values.VALUES[2],
                    pygame.K_KP3: pyga_me.Values.VALUES[3],
                    pygame.K_KP4: pyga_me.Values.VALUES[4],
                    pygame.K_KP5: pyga_me.Values.VALUES[5],
                    pygame.K_KP6: pyga_me.Values.VALUES[6],
                    pygame.K_KP7: pyga_me.Values.VALUES[7],
                    pygame.K_KP8: pyga_me.Values.VALUES[8],
                    pygame.K_KP9: pyga_me.Values.VALUES[9],
                    pygame.K_KP0: pyga_me.Values.VALUES[10]})
                if service >= 3:
                    pyga_me.Values.extended_mode = True
                if service >= 4:
                    pyga_me.Values.sons.update({
                        pygame.K_UP: pyga_me.Values.VALUES[1],
                        pygame.K_DOWN: pyga_me.Values.VALUES[2],
                        pygame.K_LEFT: pyga_me.Values.VALUES[3],
                        pygame.K_RIGHT: pyga_me.Values.VALUES[4],
                        pygame.K_w: pyga_me.Values.VALUES[5],
                        pygame.K_s: pyga_me.Values.VALUES[6],
                        pygame.K_d: pyga_me.Values.VALUES[7],
                        pygame.K_a: pyga_me.Values.VALUES[8],
                        pygame.K_q: pyga_me.Values.VALUES[9],
                        pygame.K_e: pyga_me.Values.VALUES[10]
                    })

        def extended_mode_config(timeout: int = 2000) -> None:
            """Configure the extended mode fadeout timeout for note release.

            Args:
                timeout (int, optional): Fadeout duration in milliseconds.
                    Defaults to 2000.

            Behavior:
                - updates the shared extended mode timer value

            Example:
                >>> pyga_me.k_notes.extended_mode_config(1500)

            Returns:
                None
            """
            pyga_me.Values.extended_mode_timer = timeout

        def run_time(event: pygame.event.Event) -> bool:
            """Handle a pygame event and manage playback state for note input.

            Args:
                event (pygame.event.Event): The pygame event to process.

            Behavior:
                - animates the basic display background when enabled
                - starts, stops, or fades out note sounds
                - emits runtime events for note playback and stop actions
                - returns False on pygame.QUIT to signal exit

            Example:
                >>> running = pyga_me.k_notes.run_time(event)

            Returns:
                bool: Current running state after processing the event.
            """
            if pyga_me.Values.basic:
                pyga_me.Values.screen.fill((pyga_me.Values.r, pyga_me.Values.g, pyga_me.Values.b))
                pyga_me.Values.animation_timer["red"] += 1
                pyga_me.Values.animation_timer["green"] += 1
                pyga_me.Values.animation_timer["blue"] += 1
                if pyga_me.Values.animation_timer["red"] >= 5:
                    pyga_me.Values.r += 1
                    pyga_me.Values.animation_timer["red"] = 0
                if pyga_me.Values.animation_timer["green"] >= 7:
                    pyga_me.Values.g += 1
                    pyga_me.Values.animation_timer["green"] = 0
                if pyga_me.Values.animation_timer["blue"] >= 9:
                    pyga_me.Values.b += 1
                    pyga_me.Values.animation_timer["blue"] = 0
                if pyga_me.Values.r > 255:
                    pyga_me.Values.r = 0
                if pyga_me.Values.g > 255:
                    pyga_me.Values.g = 0
                if pyga_me.Values.b > 255:
                    pyga_me.Values.b = 0
            if event.type == pygame.QUIT:
                pyga_me.Values.a = False
                return pyga_me.Values.a
            if event.type == pygame.KEYDOWN:
                if event.key in pyga_me.Values.sons:
                    if pyga_me.Values.sons[event.key] is None:  
                        pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.NULLNOTEPLAYED, event.key))
                        return pyga_me.Values.a
                    # Toca em loop
                    pyga_me.Values.sons[event.key].play(-1)
                    pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.NOTEPLAYED, event.key))
    
            elif event.type == pygame.KEYUP:
                if event.key in pyga_me.Values.sons:
                    if not pyga_me.Values.extended_mode:
                        if pyga_me.Values.sons[event.key] is None:  
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.NULLNOTESTOP, event.key))
                        else:
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.NOTESTOP, event.key))
                            # Modo normal: para imediatamente
                            pyga_me.Values.sons[event.key].stop()
                    else:
                        # Modo extendido: fadeout suave em 2 segundos
                        #mostrar evento de nota parando impreciso para lidar com o tempo de fadeout
                        if pyga_me.Values.sons[event.key] is None:
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.NULLNOTESTOP_INACCURATE, event.key))
                        else:
                            pyga_me.Values.sons[event.key].fadeout(pyga_me.Values.extended_mode_timer)
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.NOTESTOP_INACCURATE, event.key))
            return pyga_me.Values.a
    
    class events:
        """Event queue manager for pyga_me runtime and user-defined events."""
        events_inmoment = deque()
        UserEventsInMoment = deque()

        class event:
            """Represents a single event with a typed payload."""
            def __init__(self, type, data):
                """Create a new runtime event with the provided type and payload.

                Args:
                    type: Event type constant.
                    data: Associated event payload.

                Returns:
                    None
                """
                self.type = type

                if self.type == pyga_me.Values.NOTEPLAYED:
                    self.note =  data
        
                elif self.type == pyga_me.Values.NOTESTOP:
                    self.note = data
        
                elif self.type == pyga_me.Values.LAGANIMATION:
                    self.delay = data

                elif self.type == pyga_me.Values.SAFEANIMATION:
                    self.delay = data

                elif self.type == pyga_me.Values.NEGATIVEROLL:
                    self.object = data[0]
                    self.value = data[1]

                elif self.type == pyga_me.Values.POSITIVEROLL:
                    self.object = data[0]
                    self.value = data[1]

                elif self.type == pyga_me.Values.GIFEXECUTED:
                    self.number_of_executions = data
        
                elif self.type == pyga_me.Values.NOTESTOP_INACCURATE:
                    self.note = data
        
                elif self.type == pyga_me.Values.SELECTUP:
                    self.selected = data

                elif self.type == pyga_me.Values.SELECTDOWN:
                    self.selected = data

                elif self.type == pyga_me.Values.SELECTCONFIRM:
                    self.selected = data

                elif self.type == pyga_me.Values.NULLNOTEPLAYED:
                    self.note = data
        
                elif self.type == pyga_me.Values.NULLNOTESTOP:
                    self.note = data
        
                elif self.type == pyga_me.Values.NULLNOTESTOP_INACCURATE:
                    self.note = data
        
                elif self.type == pyga_me.Values.LAGDOWNLOAD:
                    self.delay = data
        
                elif self.type == pyga_me.Values.SAFEDOWNLOAD:
                    self.delay = data
        
                elif self.type == pyga_me.Values.EXCEPTDOWNLOAD:
                    self.url = data[0]
                    self.exception = data[1]
        
                elif self.type == pyga_me.Values.P2DCREATED:
                    self.player = data

                elif self.type == pyga_me.Values.P2DUPDATE:
                    self.player = data
        
                elif self.type == pyga_me.Values.P2DRMOVE:
                    self.player = data[0]
                    self.posX = data[1]
        
                elif self.type == pyga_me.Values.P2DLMOVE:
                    self.player = data[0]
                    self.posX = data[1]
        
                elif self.type == pyga_me.Values.P2DJUMP:
                    self.player = data[0]
                    self.posY = data[1]

                elif self.type == pyga_me.Values.P2DLANDED:
                    self.player = data[0]
                    self.posY = data [1]
        
                elif self.type == pyga_me.Values.P2DSPECIALKEYPRESSED:
                    self.player = data[0]
                    self.key = data[1]
                    self.consequence = data[2]
        
                elif self.type == pyga_me.Values.P2DDEAD:
                    self.player = data
        
                else:
                    self.data = data

        def get_events():
            """Collect and validate all pending events from the internal queues.

            Behavior:
                - drains the engine event queue
                - drains the user event queue
                - returns only events with valid types

            Example:
                >>> events = pyga_me.events.get_events()

            Returns:
                list[pyga_me.events.event]: Validated accumulated events.
            """
            validated: list[pyga_me.events.event] = []
            while pyga_me.events.events_inmoment: 
                ev = pyga_me.events.events_inmoment.popleft()
                if ev.type in range(pyga_me.Values.V_NONE, pyga_me.Values.USEREVENT + 1): 
                    validated.append(ev)
            while pyga_me.events.UserEventsInMoment:
                ev = pyga_me.events.UserEventsInMoment.popleft()
                validated.append(ev)
            return validated
    class animation:
        """Animation helper for frame extraction, playback, and event timing."""
        idd = 1
        def __init__(self):
            """Initialize animation timing state and assign a unique animation id."""
            os_me.details.enable_rich_traceback = False
            os_me.details.silent_FileHunter = True
            self.frame_timer = 0
            self.frame_index = 0
            self.roll = 0
            self._play = True
            self.stop = False
            self._start = None
            self._nunber_of_executions = 0
            self.id = pyga_me.animation.idd
            pyga_me.animation.idd += 1

        def extract_frames_gif(self, path_gif, size):
            """Load and resize each frame from a GIF for pygame rendering.

            Args:
                path_gif (str): Path to the source GIF file.
                size (tuple[int, int]): Target frame width and height.

            Behavior:
                - opens the GIF file
                - converts each frame to RGBA
                - resizes and converts frames to pygame surfaces

            Example:
                >>> frames = anim.extract_frames_gif('walk.gif', (64, 64))

            Returns:
                list[pygame.Surface]: Processed frames ready for blitting.
            """
            gif = Image.open(path_gif)
            frames = []
            for frame in ImageSequence.Iterator(gif):
                fr = frame.convert("RGBA").resize(size)
                surf = pygame.image.fromstring(fr.tobytes(), fr.size, fr.mode).convert_alpha()
                frames.append(surf)
            return frames

        def animation(self, frames: list, screen, auto_fill: bool = True, Clok_value: int  = None, coordinates: tuple[int] = (0,0)):
            """Animate a sequence of frames, measure timing, and emit lag events.

            Args:
                frames (list): Sequence of pygame surfaces to display.
                screen: Target pygame display surface.
                auto_fill (bool): Clear the screen before drawing if True.
                Clok_value (int | None): Optional target FPS reference.
                coordinates (tuple[int, int]): Draw position for the frame.

            Behavior:
                - advances the frame index on a timer
                - blits the current frame to screen
                - appends lag or safe animation events based on timing

            Example:
                >>> anim.animation(frames, screen, False, 60, (0, 0))

            Returns:
                None
            """
            self._nunber_of_executions += 1
            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.GIFEXECUTED, self._nunber_of_executions))
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
                        pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.LAGANIMATION, lag))
                elif lag > 0.01667:  # considerando 60 FPS como referência
                    events.events_inmoment.append(events.event(pyga_me.Values.LAGANIMATION, lag))
                else:
                    events.events_inmoment.append(events.event(pyga_me.Values.SAFEANIMATION, lag))
                self.frame_timer= 0
                self._play = True
            screen.blit(frames[self.frame_index], coordinates)

        def scrolling_text(self, text: list, font: pygame.font.Font, screen, space: int, roll: int = 10):
            """Render scrolling text and emit roll events based on user input.

            Args:
                text (list): Lines of text to render.
                font (pygame.font.Font): Font used for rendering.
                screen: Target pygame surface to draw on.
                space (int): Vertical starting offset.
                roll (int): Scroll increment for each up/down press.

            Behavior:
                - renders each line centered horizontally
                - updates roll position with arrow key input
                - emits POSITIVEROLL or NEGATIVEROLL events

            Example:
                >>> anim.scrolling_text(['Line 1', 'Line 2'], font, screen, 20)

            Returns:
                None
            """
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
                    pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.POSITIVEROLL, [self, self.roll]))
                if self.roll < 0:
                    pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.NEGATIVEROLL, [self, self.roll * -1]))
    
        class menu:
            """Menu helper for drawing option lists and handling navigation events."""
            def __init__(self):
                """Initialize menu layout state and selected index."""
                self.x = 0
                self.y = 0
                self.selected = 0
            def menu_config(self, screen, options: list[str], font: pygame.font.Font, evento=None):
                """Update the menu selection based on a pygame event.

                Args:
                    screen: pygame surface used to compute menu dimensions.
                    options (list[str]): Menu item labels.
                    font (pygame.font.Font): Font used to render menu items.
                    evento: Optional pygame event to process.

                Behavior:
                    - updates current selection for up/down keys
                    - emits SELECTUP, SELECTDOWN, and SELECTCONFIRM events
                    - stops the menu on QUIT events

                Example:
                    >>> menu.menu_config(screen, ['Play', 'Exit'], font, event)

                Returns:
                    bool: True while the menu remains active.
                """
                pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.NEWMENU, self))
                menu_ativo = True
                self.x = screen.get_width()
                self.y = screen.get_height()
            
                if evento:
                    if evento.type == pygame.QUIT:
                        menu_ativo = False
                    elif evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_UP:
                            self.selected = (self.selected - 1) % len(options)
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.SELECTUP, self.selected))
                        elif evento.key == pygame.K_DOWN:
                            self.selected = (self.selected + 1) % len(options)
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.SELECTDOWN, self.selected))
                        elif evento.key == pygame.K_RETURN:
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.SELECTCONFIRM, self.selected))
                            return menu_ativo
                return menu_ativo
                        
            def menu_draw_basic(self, screen, options: list[str], font: pygame.font.Font, select: int, auto_fill: bool = True):
                """Draw a simple centered menu with one selected highlight.

                Args:
                    screen: pygame surface to render on.
                    options (list[str]): Menu labels.
                    font (pygame.font.Font): Font used for rendering.
                    select (int): Index of selected menu item.
                    auto_fill (bool): If True, clear the screen before drawing.

                Returns:
                    None
                """
                if auto_fill:
                    screen.fill((0,0,0))
                for i, option in enumerate(options):
                    color = (255, 0, 0) if i == select else (255, 255, 255)
                    text_surface = font.render(option, True, color)
                    x = self.x // 2 - text_surface.get_width() // 2
                    y = self.y // 2 - len(options) * 30 + i * 60
                    screen.blit(text_surface, (x, y))

            def menu_draw_advanced(self, screen, options: list[str], font: pygame.font.Font, select: int, auto_fill: bool = True, color_selected: tuple = (255, 0, 0), color_unselected: tuple = (255, 255, 255), roll_mode: bool = False, roll_config: int = 0):
                """Draw a customizable menu with optional roll offset support.

                Args:
                    screen: pygame surface to render on.
                    options (list[str]): Menu labels.
                    font (pygame.font.Font): Font used for text rendering.
                    select (int): Index of selected menu item.
                    auto_fill (bool): If True, clear the screen before drawing.
                    color_selected (tuple): Color for selected option.
                    color_unselected (tuple): Color for unselected options.
                    roll_mode (bool): Enable roll offset.
                    roll_config (int): Vertical offset value when roll_mode is enabled.

                Returns:
                    None
                """
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
    
    class objects:
        """Container for game object classes that support 2D and RPG movement."""
        class Player2D:
            """2D player object with walking, jumping, and animation support."""
            def __init__(self, size: tuple[int], right_frames_stop: list[pygame.Surface]| str , left_frames_stop: list[pygame.Surface]| str, right_frames_walking: list[pygame.Surface]| str, left_frames_walking: list[pygame.Surface]| str, gravity: int, vel:int, jump_limit: int, screen):
                """Initialize a 2D player with frame assets, physics, and event emission.

                Args:
                    size (tuple[int]): Player width and height.
                    right_frames_stop (list|str): Right-facing idle frames or GIF path.
                    left_frames_stop (list|str): Left-facing idle frames or GIF path.
                    right_frames_walking (list|str): Right-facing walking frames or GIF path.
                    left_frames_walking (list|str): Left-facing walking frames or GIF path.
                    gravity (int): Gravity applied during updates.
                    vel (int): Horizontal movement velocity.
                    jump_limit (int): Maximum jump energy.
                    screen: pygame surface used to compute screen bounds.

                Returns:
                    None
                """
                pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.P2DCREATED, self))
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
                self.player = pyga_me.animation()
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
                self.alive = True
                self._eventsinmoment: deque[pygame.event.Event] = deque()

            def colect_events(self, event: pygame.event.Event):
                """Queue a pygame event for later player-specific processing."""
                self._eventsinmoment.append(event)
    
            def _get_colect_events(self):
                """Consume and return any queued player events.

                Returns:
                    list: Collected pygame events for this player.
                """
                events = []
                try:
                    ev: pygame.event.Event = self._eventsinmoment.popleft()
                    events.append(ev)
                except:
                    pass
                return events
        
            def update(self, special_keys: int | list[int], consequences: Callable | list[Callable], AltoXYBarrier: bool = True, screen = None):
                """Update the player position, jump state, and special key actions.

                Args:
                    special_keys (int | list[int]): Key or keys that trigger special consequences.
                    consequences (Callable | list[Callable]): Action(s) to invoke when special keys are pressed.
                    AltoXYBarrier (bool): Enable boundary-aware gravity and movement.
                    screen: pygame surface used to compute bounds.

                Behavior:
                    - applies gravity and movement based on arrow keys
                    - handles jumping with space/up keys
                    - emits movement and special key press events

                Returns:
                    None
                """
                if not self.alive:
                    self.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.P2DDEAD, self))
                    return 
                pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.P2DUPDATE, self))
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
                        pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.P2DLANDED, [self, self.pos_y]))
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
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.P2DRMOVE, [self, self.pos_x]))
                    else:
                        if not self.lock_x_R:
                            self.state = "walking"
                            self.pos_x += self.vel
                            self.direction = "right"
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.P2DRMOVE, [self, self.pos_x]))
                elif keys[pygame.K_LEFT]:
                    if AltoXYBarrier:
                        mim = min(0, self.pos_x)
                        if not self.lock_x_L and mim == 0:
                            self.state = "walking"
                            self.pos_x -= self.vel
                            self.direction = "left"
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.P2DLMOVE, [self, self.pos_x]))
                    else:
                        if not self.lock_x_L:
                            self.state = "walking"
                            self.pos_x -= self.vel
                            self.direction = "left"
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.P2DLMOVE, [self, self.pos_x]))
                if not keys[pygame.K_RIGHT] or not keys[pygame.K_LEFT]:
                    self.state = "stop"
                if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                        if not self.lock_y_UP:
                            if self.jump_control < self.jump_limit:
                                if self.jump_control < self.jump_limit // 4:
                                        self.jump_control += 18 + self.gravity
                                        self.pos_y -= 18 + self.gravity
                                        pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.P2DJUMP, [self, self.pos_y]))
                                elif self.jump_control < self.jump_limit // 3:
                                        self.jump_control += 9 + self.gravity
                                        self.pos_y -= 9 + self.gravity
                                        pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.P2DJUMP, [self, self.pos_y]))
                                elif self.jump_control < self.jump_limit // 2:
                                        self.jump_control += 4 + self.gravity
                                        self.pos_y -= 4 + self.gravity
                                        pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.P2DJUMP, [self, self.pos_y]))
                for event in self._get_colect_events():
                    event: pygame.event.Event
                    if event.type == pygame.KEYUP:
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                                self.jump_control = self.jump_limit
                if isinstance(special_keys, int):
                    if isinstance(consequences, Callable):
                        if keys[special_keys]:
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.P2DSPECIALKEYPRESSED, [self, special_keys, str(consequences)]))
                            consequences()
                    elif isinstance(consequences, list):
                        a = consequences[0]
                        if keys[special_keys]:
                            a()
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.P2DSPECIALKEYPRESSED, [self, special_keys, str(consequences[0])]))
                elif isinstance(special_keys, list):
                    if isinstance(consequences, Callable):
                        b = special_keys[0]
                        if keys[b]:
                            consequences()
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.P2DSPECIALKEYPRESSED, [self, special_keys[0], str(consequences)]))
                    elif isinstance(consequences, list):
                        for i, s_key in enumerate(special_keys):
                            try:
                                c = consequences[i]
                                if keys[s_key]:
                                    c()
                                    pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.P2DSPECIALKEYPRESSED, [self, special_keys[i], str(consequences[i])]))
                            except IndexError:
                                pass

            def draw(self, screen, alto_fill: bool = True):
                """Render the player using the current animation frames and direction.

                Args:
                    screen: pygame surface to draw on.
                    alto_fill (bool): Clear the screen before drawing if True.

                Returns:
                    None
                """
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
                """Return the player size as a width/height tuple.

                Returns:
                    tuple[int, int]: Player width and height.
                """
                return self.size[0], self.size[1] if isinstance(self.size, tuple) or isinstance(self.size, list) else self.size, self.size


        class PlayerRPG:
            """RPG-style player object with directional movement and animation."""
            def __init__(self, frames_up_stop: list, frames_down_stop: list, frames_left_stop: list, frames_right_stop: list, frames_up_walking: list, frames_down_walking: list, frames_left_walking: list, frames_right_walking: list, size: tuple[int], vel:int, screen):
                """Initialize an RPG player with directional frame animations.

                Args:
                    frames_up_stop (list): Up-facing idle frames or GIF path.
                    frames_down_stop (list): Down-facing idle frames or GIF path.
                    frames_left_stop (list): Left-facing idle frames or GIF path.
                    frames_right_stop (list): Right-facing idle frames or GIF path.
                    frames_up_walking (list): Up-facing walking frames or GIF path.
                    frames_down_walking (list): Down-facing walking frames or GIF path.
                    frames_left_walking (list): Left-facing walking frames or GIF path.
                    frames_right_walking (list): Right-facing walking frames or GIF path.
                    size (tuple[int]): Character width and height.
                    vel (int): Movement velocity.
                    screen: pygame surface used to compute bounds.

                Returns:
                    None
                """
                self.animation = pyga_me.animation()
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
                pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.RPGCREATED, self))

            def update(self, special_keys: int | list[int], consequences: Callable | list[Callable], AltoXYBarrier: bool = False, screen = None):
                """Update the RPG player movement and handle special key actions.

                Args:
                    special_keys (int | list[int]): Trigger keys for special actions.
                    consequences (Callable | list[Callable]): Action(s) invoked on key press.
                    AltoXYBarrier (bool): Enable boundary-aware movement.
                    screen: pygame surface used to compute bounds.

                Behavior:
                    - moves the player based on arrow keys
                    - updates direction and walking state
                    - emits RPGMOVE and RPGSPECIALKEYPRESSED events

                Returns:
                    None
                """
                if not self.alive:
                    pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.RPGDEAD, self))
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
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.RPGMOVE, [self, self.pos_x, self.pos_y]))
                    if not mim1 == 0 or self.lock_y_D:
                        if keys[pygame.K_DOWN]:
                            self.pos_y += self.vel
                            self.direction = "down"
                            self.state = "walking"
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.RPGMOVE, [self, self.pos_x, self.pos_y]))
                    if not ma1 == self.pos_x or self.lock_x_R:
                        if keys[pygame.K_LEFT]:
                            self.pos_x -= self.vel
                            self.direction = "left"
                            self.state = "walking"
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.RPGMOVE, [self, self.pos_x, self.pos_y]))
                    if not mim0 == 0 or self.lock_x_L:
                        if keys[pygame.K_RIGHT]:
                            self.pos_x += self.vel
                            self.direction = "right"
                            self.state = "walking"
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.RPGMOVE, [self, self.pos_x, self.pos_y]))
                    if not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                        self.state = "stop"
                else:
                    if not self.lock_y_U:
                        if keys[pygame.K_UP]:
                            self.pos_y -= self.vel
                            self.direction = "up"
                            self.state = "walking"
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.RPGMOVE, [self, self.pos_x, self.pos_y]))
                    if not self.lock_y_D:
                        if keys[pygame.K_DOWN]:
                            self.pos_y += self.vel
                            self.direction = "down"
                            self.state = "walking"
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.RPGMOVE, [self, self.pos_x, self.pos_y]))
                    if not self.lock_x_L:    
                        if keys[pygame.K_LEFT]:
                            self.pos_x -= self.vel
                            self.direction = "left"
                            self.state = "walking"
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.RPGMOVE, [self, self.pos_x, self.pos_y]))
                    if not self.lock_x_R:
                        if keys[pygame.K_RIGHT]:
                            self.pos_x += self.vel
                            self.direction = "right"
                            self.state = "walking"
                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.RPGMOVE, [self, self.pos_x, self.pos_y]))
                    if not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                        self.state = "stop"
                if special_keys and consequences:
                        if isinstance(special_keys, int):
                            if isinstance(consequences, Callable):
                                if keys[special_keys]:
                                    consequences()
                                    pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.RPGSPECIALKEYPRESSED, [self, special_keys, consequences]))
                        elif isinstance(special_keys, list):
                            if isinstance(consequences, list):
                                for i, s_key in enumerate(special_keys):
                                    try:
                                        c = consequences[i]
                                        if keys[s_key]:
                                            c()
                                            pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.RPGSPECIALKEYPRESSED, [self, special_keys[i], consequences[i]]))
                                    except IndexError:
                                        pass
                            elif isinstance(consequences, Callable):
                                a = special_keys[0]
                                if keys[a]:
                                    consequences()
                                    pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.RPGSPECIALKEYPRESSED, [self, special_keys[0], consequences]))
        
            def draw(self, screen, alto_fill: bool = True):
                """Render the RPG player based on current direction and walking state.

                Args:
                    screen: pygame surface to draw on.
                    alto_fill (bool): Clear the screen before drawing if True.

                Returns:
                    None
                """
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
                """Return the RPG player size as a width/height tuple.

                Returns:
                    tuple[int, int]: Player width and height.
                """
                return self.size[0], self.size[1] if isinstance(self.size, tuple) or isinstance(self.size, list) else self.size, self.size

    def load_file(url, cache_file, extension=None, TimeLimitAllowed: float = 10.0):
        """Download or retrieve a cached file from a URL using hashed cache naming.

        Args:
            url (str): Remote resource URL.
            cache_file (str): Local cache directory or relative path.
            extension (str, optional): Force a file extension for the saved file.
                Defaults to None.
            TimeLimitAllowed (float, optional): Threshold in seconds for download timing.
                Defaults to 10.0.

        Behavior:
            - finds or creates the cache directory
            - generates a consistent hashed filename
            - downloads the remote resource only when missing locally
            - logs download lag or success events
            - returns the local cached path

        Example:
            >>> path = pyga_me.load_file('https://example.com/sound.wav', 'cache')

        Returns:
            str: Path to the downloaded or cached file.
        """
        if os_me.path.FileHunter_TrueOrFalse(cache_file):
            cache = os_me.path.FileHunter(cache_file)
        else:
            os.makedirs(os.path.dirname(cache_file))
            cache = cache_file
        nome = hashlib.md5(url.encode()).hexdigest()
        if not extension:
            if url.lower().endswith(".wav"):
                nome += ".wav"
            elif url.lower().endswith(".ogg"):
                nome += ".ogg"
            elif url.lower().endswith(".mp3"):
                nome += ".mp3"
            elif url.lower().endswith("png"):
                nome += ".png"
            elif url.lower().endswith("gif"):
                nome += ".gif"
            elif url.lower().endswith("mp4"):
                nome += ".mp4"
            else:
                nome += ".dat"
        else:
            nome += extension
        caminho = os.path.join(cache, nome)
        if not os_me.path.FileHunter_TrueOrFalse(caminho):
            try:
                start = time.time()
                r = rs.get(url, timeout=10)
                r.raise_for_status()
                with open(caminho, "wb") as f:
                    f.write(r.content)
                stop = time.time()
                elapsed = stop - start
                if elapsed > TimeLimitAllowed:
                    pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.LAGDOWNLOAD, elapsed))
                else:
                    pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.SAFEDOWNLOAD, elapsed))
            except Exception as e:
                pyga_me.events.events_inmoment.append(pyga_me.events.event(pyga_me.Values.EXCEPTDOWNLOAD, [url, str(e)]))
        return caminho