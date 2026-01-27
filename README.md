# py_me

py_me is a Python library that provides modules for audio manipulation (music_me) and Tkinter GUI helpers (tk_me).

## Version

**3.4.1** - released on 2026-01-27

## Changes

- Full translation into English
- Added new helper utilities and aesthetic improvements

## tk_me
### Example:
```python
from py_me import tk_me

win = tk_me.create_window("hi", "100x100")  # Portuguese alias: apenas_criar
def exit_app():
    win.destroy()
tk_me.create_button("exit", 0, 0, "Arial", 14, exit_app)  # Portuguese alias: botão
win.mainloop()
```
### Functions
- import_script_window(window_name, window_size, import_file)  (Portuguese alias: tk_import)
- create_window(window_name, window_size)  (Portuguese alias: apenas_criar)
- create_label(text, x, y, font, size)  (Portuguese alias: label)
- create_button(text, x, y, font, size, command)  (Portuguese alias: botão)
- create_text_window(height, width, x, y)  (Portuguese alias: janela_de_Texto)
- error_window()  (Portuguese alias: janela_error)
- destroy_widget(widget)  (Portuguese alias: destruir_objetos)
- import_tk_window(window_name, tk_file, label_text, button_text)  (Portuguese alias: tk_import_tk)
- create_slider(min, max, command, x, y)  (Portuguese alias: slider)

## music_me
### Example:
```python
from py_me import music_me

music_me.loop_soundtrack(2, "my\\beat.mp3")            # Portuguese alias: trilha_sonora_inloop
elem = music_me.musical_element(1, "my\\sound.wav", 12)  # Portuguese alias: elemento_musical
music_me.stop_element_after(elem, 10)                  # Portuguese alias: dell
```
### Functions
- loop_soundtrack(speed, file)  (Portuguese alias: trilha_sonora_inloop)
- musical_element(speed, file, wait_time=0)  (Portuguese alias: elemento_musical)
- pitched_musical_element(speed, pitch, file, wait_time=0)  (Portuguese alias: elemento_musical_entonado)
- stop_element_after(element, seconds_after_start)  (Portuguese alias: dell)
- stop_all_after(delay_seconds)  (Portuguese alias: stop)
- set_element_volume(element, volume, delay)  (Portuguese alias: volume_elemento)
- set_master_volume(volume, delay)  (Portuguese alias: volume_geral)

## project_me
### Example:
```python
from py_me import project_me

project_me.create_project()  # Portuguese alias: criar_projeto
```

### Function
- create_project()  (interactive helper to scaffold a basic Python project; Portuguese alias: criar_projeto)

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
  - helper
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
    - get_version
    - get_content
    - get_TIMELINE
    - show_TIMELINE
    - del_TIMELINE
    - run_version
    - del_all
- utilidades:
  - registrar_log(message)

## Dependencies
- pygame
- pydub (requires FFmpeg for many formats)

## Installation

```bash
pip install py-me
```