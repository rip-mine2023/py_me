# py_me

py_me is a Python library that provides modules for audio manipulation (music_me) and Tkinter GUI helpers (tk_me).

## Version

**4.1.1** - released on 2026-03-10

## Changes

- new module called py_game
- The create_dir_tree function has been modified to accept bytes.

## tk_me
### Example:
```python
from py_me import tk_me

win = tk_me.create_window("hi", "100x100") 
def exit_app():
    win.destroy()
tk_me.create_button("exit", 0, 0, "Arial", 14, exit_app)  
win.mainloop()
```
### Functions
- import_script_window
- create_window
- create_label  
- create_button
- create_text_window
- error_window
- destroy_widget
- import_tk_window
- create_slider 
- create_listbox

## music_me
### Example:
```python
from py_me import music_me

music_me.loop_soundtrack(2, "my\\beat.mp3")            
elem = music_me.musical_element(1, "my\\sound.wav", 12)  
music_me.stop_element_after(elem, 10)                  
```
### Functions
- loop_soundtrack(speed, file)  
- musical_element(speed, file, wait_time=0)  
- pitched_musical_element(speed, pitch, file, wait_time=0)   
- stop_element_after(element, seconds_after_start)  
- stop_all_after(delay_seconds)  
- set_element_volume(element, volume, delay) 
- set_master_volume(volume, delay)

## project_me
### Example:
```python
from py_me import project_me

project_me.create_project()
```

### Function
- create_project() 

## os_me
### Example:
```python
from py_me import os_me

a = os_me.path.FileHunter("example.py")
b = os_me.path.FileHunter("second\\example.py")
os_me.file.execution_sequence([a, b], ignore_error=False, list_erros=False)
```

### API overview
- details:
  - helper()
  - configuration fields (log_file, timeline_file, encoding, language, enable_logging, enable_rich_traceback, auto_snapshot_on_edit, avoid_duplicate_snapshots, timestamp_format, custom_logger, silent_FileHunter)
- file:
  - replace(path, content)
  - create(new_path, content="")
  - add(path, content)
  - execution_sequence(paths: list, ignore_error: bool = False, list_erros: bool = False)
- path:
  - FileHunter(relative_path) -> str | None
  - FileHunter_inverse(relative_path, start=None) -> str | None
  - FileHunter_SUPER(relative_path) -> str | None
  - FileHunter_TrueOrFalse(relative_path) -> bool
  - TIMELINE:
    - get_version()
    - get_content()
    - get_TIMELINE()
    - show_TIMELINE()
    - del_TIMELINE()
    - run_version()
    - del_all()
- utilidades:
  - registrar_log(message)
- os_me:
  - create_dir_tree()

## pyga_me
### Example:
```python
import pyga_me
import pygame
import time
pygame.init()

tela = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
rodando = True  
menu = pyga_me.animation.menu()
texto = pyga_me.animation()
image = pyga_me.animation()
img = image.extract_frames_gif("D:\\Isaias\\Saved Games\\put_it_in_your_home_folder\\cache_fnap\\3acb9ab12152ec9a51688688f935b35c.gif", tela.get_size())
img_player = image.extract_frames_gif("D:\\Isaias\\Saved Games\\put_it_in_your_home_folder\\cache_fnap\\3acb9ab12152ec9a51688688f935b35c.gif", (64, 64))
a = ["hello", "hi", "a", "b", "c", "d", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e"]
fonte = pygame.font.Font(None, 40)
clock = pygame.time.Clock()
pyga_me.init()
pyga_me.k_notes.UltraSondService.extended_mode = True
V_null = pyga_me.k_notes.UltraSondService.register_new_note(None, "V_null")
pyga_me.k_notes.UltraSondService.music_in_the_keys(pygame.K_UP, pygame.K_DOWN, pygame.K_0, note= (pyga_me.V_DO2, pyga_me.V_DO, V_null))
ab = ["option 1", "option 2", "option 3", "all" , "sair"]
select = True
rool = 0    
player = pyga_me.objects.Player2D((64, 64), img_player, img_player, img_player, img_player, 1, 10, 1000, tela)
#player = pyga_me.objects.PlayerRPG(, 10, 10, 400, tela)
player.frames_control = False
while select:
    keys = pygame.key.get_pressed()
    for evento in pygame.event.get():
        select = menu.menu_config(tela, ab, fonte, evento)
    for event in pyga_me.events.get_events():
        if event.type == pyga_me.SELECTUP:
            if not event.selected == 0:
                rool += 10
        elif event.type == pyga_me.SELECTDOWN:
            if not event.selected == len(ab) - 1:
                rool -= 10
        elif event.type == pyga_me.SELECTCONFIRM:
            print(f"opção selecionada: {ab[event.selected]}")
            if event.selected == len(ab) - 1:
                rodando = False
            elif event.selected == 0:
                a.append("option 1")
            elif event.selected == 1:
                a.append("option 2")
            elif event.selected == 2:
                a.append("option 3")
            elif event.selected == 3:
                a.append("option 1")
                a.append("option 2")
                a.append("option 3")
            texto.roll = 0
            select = False
    tela.fill((0,0,0))
    image.animation(img, tela, False)
    menu.menu_draw_advanced(tela, ab, fonte, menu.selected, False, (0, 0, 255), (255, 255, 255), True, rool)
    pygame.display.flip()

while rodando:
    keys = pygame.key.get_pressed()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                pyga_me.k_notes.extended_mode = not pyga_me.k_notes.extended_mode
        pyga_me.k_notes.run_time(evento)
        player.colect_events(evento)
    tela.fill((0,0,0))
    if not all(i.get_size() == tela.get_size() for i in img):
        img = image.extract_frames_gif("D:\\Isaias\\Saved Games\\put_it_in_your_home_folder\\cache_fnap\\3acb9ab12152ec9a51688688f935b35c.gif", tela.get_size())
    if player.pos_y >= 400:
        if player.pos_x in range(600, 801):
            player.lock_y_D = False 
        else:
            player.lock_y_D = True
    else:
        player.lock_y_D = False
    mim = min(600, player.pos_x)
    ma2 = max(800, player.pos_x)
    #fazer com que bata nas paredes do buraco
    if player.pos_y > 400:
        if player.pos_x <= mim:
            player.lock_x_L = True
        else:
            player.lock_x_L = False
        if player.pos_x >= ma2:
            player.lock_x_R = True
        else:        
            player.lock_x_R = False
    else:
        player.lock_x_L = False
        player.lock_x_R = False
    if player.pos_y >= tela.get_height() - player.size[1] // 2:
        player.alive = False
    player.update(None, None, True, tela)
    image.animation(img, tela, False, 60)
    player.draw(tela, False)
    texto.scrolling_text(a, fonte, tela, 59)
    if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:  
        pyga_me.events.UserEventsInMoment.append(pyga_me.events.event(pyga_me.USEREVENT + 1, "olá mundo"))

    for event in pyga_me.events.get_events():
        if event.type == pyga_me.NEGATIVEROLL:
            if event.object == texto:
                if event.value > 1000:
                    texto.stop = True
                    texto.roll += 1
        elif event.type == pyga_me.POSITIVEROLL:
            if event.object == texto:
                if event.value > 0:
                    texto.stop = True
                    texto.roll -= 1
        elif event.type == pyga_me.NOTEPLAYED:
            start = time.time()
            print(f"nota: {pyga_me.k_notes.name_from_note(event.note)} tocada")
        elif event.type == pyga_me.NOTESTOP :
            stop = time.time()
            elapsed = stop - start
            print(f"nota: {pyga_me.k_notes.name_from_note(event.note)} parou de ser tocada")
        elif event.type == pyga_me.NOTESTOP_INACCURATE:
            print(f"nota: {pyga_me.k_notes.name_from_note(event.note)} parou de ser tocada (impreciso, pode ter um delay devido ao fadeout)")
        elif event.type == pyga_me.NULLNOTEPLAYED:
            print(f"nota: {pyga_me.k_notes.name_from_note(event.note)} tocada (nota nula)")
        elif event.type == pyga_me.NULLNOTESTOP:
            print(f"nota: {pyga_me.k_notes.name_from_note(event.note)} parou de ser tocada (nota nula)")
        elif event.type == pyga_me.NULLNOTESTOP_INACCURATE:
            print(f"nota: {pyga_me.k_notes.name_from_note(event.note)} parou de ser tocada (impreciso, pode ter um delay devido ao fadeout) (nota nula)")
        elif event.type == pyga_me.LAGANIMATION:
            print(f"lag na animação detectado: {event.delay:.4f} segundos")
        elif event.type == pyga_me.GIFEXECUTED:
            if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
                print(f"animação executada {event.number_of_executions} vezes")
        elif event.type == pyga_me.USEREVENT + 1:
            print(event.data)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
```

### API overview
- pyga_me
  - load_file()
  - init()
  - k_notes:
    - init()
    - basic_display_test()
    - UltraSondService:
      - music_in_the_keys()
      - register_new_note()
    - name_from_note()
    - sond_service()
    - extended_mode_config()
    - run_time()
  - animation:
    - extract_frames_gif()
    - animation()
    - scrolling_text()
    - menu:
      - menu_config()
      - menu_draw_basic()
      - menu_draw_advanced()
  - events:
    - events_inmoment[]
    - UserEventsInMoment[]
    - event:
    - get_events()
  - objects:
    - Player2D:
      - colect_events()
      - _get_colect_events() <-- internal function
      - update()
      - draw()
      - get_size()
    - PlayerRPG:
      - update()
      - draw()
      - get_size()

## author's note

### pyga_me1 <-- temporary
This version is being released ahead of schedule, 
so there are no docstrings yet, 
and there may be bugs, but enjoy! 
Future versions should include docstrings.

### pyga_me2 <-- permanent
The example I provided for this module
is the actual code validation file I used to test my code, 
and since I'm Brazilian, 
there are many variables in Portuguese. 
I hope this doesn't cause too much trouble.

### music_me1 <-- permanet?
The music_me project was put on hold midway through.
I might pick it up again someday, 
but for now there may be bugs, 
and the module is also underdeveloped. 
Thank you for your understanding.


## Dependencies
- pygame
- pydub (requires FFmpeg for many formats)

## Installation

```bash
pip install py-me
```