# py_me

**py_me** is a Python library that provides modules for sound manipulation (`music_me`) and Tkinter GUI helpers (`tk_me`).

## Version

**3.4.1** - *released on 2026-01-27*

**name** - *now with a new look* 

## Changes

- full translation into English
- Adding new "accessories" to make py_me prettier.

## tk_me
### Example:
```python
from py_me import tk_me

win = tk_me.apenas_criar("hi", "100x100")
def exit_app():
    win.destroy()
tk_me.botão("exit", 0, 0, "Arial", 14, exit_app)
win.mainloop()
```
### Functions
- tk_import(window_name, window_size, import_file)
- apenas_criar(window_name, window_size)  (alias for create_window)
- label(text, X, Y, font, size)  (alias for create_label)
- botão(text, X, Y, font, size, command)  (alias for create_button)
- janela_de_Texto(height, width, X, Y)  (alias for create_text_window)
- janela_error()  (alias for error_window)
- destruir_objetos(widget)  (alias for destroy_widget)
- tk_import_tk(window_name, tk_file, label_text, button_text)  (alias for import_tk_window)
- slider(min, max, command, X, Y)  (alias for create_slider)

## music_me
### Example:
```python
from py_me import music_me

music_me.trilha_sonora_inloop(2, "my\\beat.mp3")
elem = music_me.elemento_musical(1, "my\\sound.wav", 12)
music_me.dell(elem, 10)
```
### Functions
- trilha_sonora_inloop(speed, file)  (alias loop_soundtrack)
- elemento_musical(speed, file, wait_time=0)  (alias musical_element)
- elemento_musical_entonado(speed, pitch, file, wait_time=0)  (alias pitched_musical_element)
- dell(element, seconds_after_start)  (alias stop_element_after)
- stop(delay_seconds)  (alias stop_all_after)
- volume_elemento(element, volume, delay)  (alias set_element_volume)
- volume_geral(volume, delay)  (alias set_master_volume)

## project_me
### Example:
```python
from py_me import project_me

project_me.criar_projeto()
```

### Function
- criar_projeto()  (alias create_project)

## os_me
### Example:
```python
from py_me import os_me
a = os_me.path.FileHunter("example.py")
b = os_me.path.FileHunter("second\\example.py")
os_me.file.execution_sequence([a, b], False, False)
```

### API overview
- file:
  - replace
  - create
  - add
  - execution_sequence
- path:
  - FileHunter
  - FileHunter_inverse
  - FileHunter_SUPER
  - FileHunter_TrueOrFalse
  - TIMELINE:
    - get_version
    - get_content
    - get_TIMELINE
    - show_TIMELINE
    - del_TIMELINE
    - run_version
    - del_all
- details:
  - helper

## Dependencies
- pygame
- pydub
  - FFmpeg

## Installation

```bash
pip install py-me
```