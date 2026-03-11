import time
from __pyga_me_modules.k_notes import k_notes
from py_me import os_me
from __pyga_me_modules.animation import animation
import os
import hashlib
import requests as rs
import __pyga_me_modules.events as events
import __pyga_me_modules.objects as objects

def init():
    k_notes.init()
    os_me.details.enable_rich_traceback = False
    os_me.details.silent_FileHunter = True
V_NONE = k_notes.NONE
V_DO = k_notes.V_DO
V_RE = k_notes.V_RE
V_MI = k_notes.V_MI
V_FA = k_notes.V_FA
V_SOL = k_notes.V_SOL
V_LA = k_notes.V_LA
V_TI = k_notes.V_TI
V_DO2 = k_notes.V_DO2
V_RE2 = k_notes.V_RE2
V_MI2 = k_notes.V_MI2
NOTEPLAYED = k_notes.NOTEPLAYED
NOTESTOP = k_notes.NOTESTOP
LAGANIMATION = animation.LAGANIMATION
SAFEANIMATION = animation.SAFEANIMATION
NEGATIVEROLL = animation.NEGATIVEROLL
POSITIVEROLL = animation.POSITIVEROLL
GIFEXECUTED = animation.GIFEXECUTED
NOTESTOP_INACCURATE = k_notes.NOTESTOP_INACCURATE
NULLNOTEPLAYED = k_notes.NULLNOTEPLAYED
NULLNOTESTOP = k_notes.NULLNOTESTOP
NULLNOTESTOP_INACCURATE = k_notes.NULLNOTESTOP_INACCURATE
SELECTUP = animation.SELECTUP
SELECTDOWN = animation.SELECTDOWN
SELECTCONFIRM = animation.SELECTCONFIRM
SAFEDOWNLOAD =1073742121
EXCEPTDOWNLOAD = 1073742122
LAGDOWNLOAD = 1073742123
P2DCREATED = objects.P2DCREATED
P2DUPDATE = objects.P2DUPDATE
P2DRMOVE = objects.P2DRMOVE
P2DLMOVE = objects.P2DLMOVE
P2DJUMP = objects.P2DJUMP
P2DLANDED = objects.P2DLANDED
P2DSPECIALKEYPRESSED = objects.P2DSPECIALKEYPRESSED
P2DDEAD = objects.P2DDEAD
RPGCREATED = objects.RPGCREATED
RPGUPDATE = objects.RPGUPDATE
RPGMOVE = objects.RPGMOVE
RPGSPECIALKEYPRESSED = objects.RPGSPECIALKEYPRESSED
RPGDEAD = objects.RPGDEAD
USEREVENT = objects.USEREVENT

def load_file(url, cache_file, extension=None, TimeLimitAllowed: float = 10.0):
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
                events.events_inmoment.append(events.event(LAGDOWNLOAD, elapsed))
            else:
                events.events_inmoment.append(events.event(SAFEDOWNLOAD, elapsed))
        except Exception as e:
            events.events_inmoment.append(events.event(EXCEPTDOWNLOAD, [url, str(e)]))
    return caminho