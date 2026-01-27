import tkinter as tk
import random as ram
import sys
import threading
import os
    
class NoReturn:
    pass

class tk_me:
    """
    Utilities to make creating Tk apps faster and less repetitive.
    tk_me provides helper functions to create common Tk widgets and
    small helper windows that simulate terminal behavior and other effects.

    Methods (English names, Portuguese aliases preserved at end):
        import_script_window(window_name, window_size, script_path)
        create_window(window_name, window_size)
        create_label(text, x, y, font, size)
        create_button(text, x, y, font, size, command)
        create_text_window(height, width, x, y)
        error_window()
        destroy_widget(widget)
        import_tk_window(window_name, script_path, label_text, button_text)
        create_slider(min_val, max_val, command, x, y)
    """

    def import_script_window(window_name: str, window_size: str, script_path: str) -> NoReturn:
        """
        Create a Tk window that runs a Python script with redirected print/input.

        Args:
            window_name (str): Window title.
            window_size (str): Window geometry like "1000x700".
            script_path (str): Path to the Python file to execute.

        Behavior:
            - creates a window that simulates a terminal
            - redirects print and stderr to a large Text widget
            - simulates input() using Entry widgets below the run button
            - provides a button to start/reset execution and a status label

        Example:
            >>> from py_me import tk_me
            >>> tk_me.import_script_window("win1", "1000x700", "myscript.py")

        Returns:
            None
        """
        try:
            window = tk.Tk()
            window.title(window_name)
            window.geometry(window_size)

            status_label = tk.Label(window, text=f"enjoy {window_name}")
            status_label.pack(pady=20)

            output = tk.Text(window, height=30, width=100)
            output.pack()

            class Redirector:
                def __init__(self, widget):
                    self.widget = widget
                def write(self, text):
                    self.widget.insert(tk.END, text)
                    self.widget.see(tk.END)
                def flush(self):
                    pass

            sys.stdout = Redirector(output)
            sys.stderr = Redirector(output)

            info_label = tk.Label(window, text="Click the button below to start. Enter inputs in the fields under the button and press Enter.")
            info_label.pack(pady=10)

            entry_main = tk.Entry(window)
            entry_main.pack()

            entries = []
            current_step = [0]

            def create_entries(qty):
                for i in range(qty):
                    new_entry = tk.Entry(window)
                    new_entry.pack()
                    new_entry.config(state='disabled')
                    entries.append(new_entry)
                if entries:
                    entries[0].config(state='normal')

            def reset_entries():
                current_step[0] = 0
                for e in entries:
                    e.delete(0, tk.END)
                    e.config(state='disabled')
                if entries:
                    entries[0].config(state='normal')

            def fake_input(prompt=''):
                idx = current_step[0]
                if idx >= len(entries):
                    output.insert(tk.END, "\n")
                    reset_entries()
                    return ""
                ent = entries[idx]
                output.insert(tk.END, f"{prompt}\n")
                ent.config(state="normal")
                ent.focus()
                val_var = tk.StringVar()
                def confirm(event=None):
                    val = ent.get().strip()
                    if val:
                        val_var.set(val)
                    else:
                        output.insert(tk.END, "empty!\n")
                ent.bind("<Return>", confirm)
                window.wait_variable(val_var)
                current_step[0] += 1
                if current_step[0] < len(entries):
                    entries[current_step[0]].config(state='normal')
                else:
                    output.insert(tk.END, "\n")
                    reset_entries()
                return val_var.get()

            def run_code():
                status_label.config(text="running... press button to reset if needed.")
                try:
                    if getattr(sys, 'frozen', False):
                        base_dir = sys._MEIPASS
                    else:
                        base_dir = os.path.dirname(__file__)
                    script_full = os.path.join(base_dir, script_path)
                    with open(script_full, "r", encoding="utf-8") as f:
                        content = f.read()
                        exec(content, {**globals(), 'input': fake_input})
                except Exception as e:
                    status_label.config(text=f"Error: {e}")

            def click():
                current_step[0] = 0
                for e in entries:
                    e.delete(0, tk.END)
                    e.config(state='disabled')
                if entries:
                    entries[0].config(state='normal')
                thread = threading.Thread(target=run_code)
                thread.start()

            run_button = tk.Button(window, text="start/reset", command=click)
            run_button.pack(pady=10)
            create_entries(1)
            window.mainloop()
        except Exception as p:
            print("error:", p)

    def create_window(window_name: str, window_size: str) -> tk.Tk:
        """
        Create a simple Tk window.

        Args:
            window_name (str): Title of the window.
            window_size (str): Geometry string like "800x600".

        Returns:
            tkinter.Tk: created window instance.
        """
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        try:
            window = tk.Tk()
            window.title(window_name)
            window.geometry(window_size)
            return window
        except Exception as e:
            print("error:", e)

    def create_label(text: str, x: int, y: int, font: str, size: int) -> tk.Label:
        """
        Create and place a Tk Label.

        Args:
            text (str): label text.
            x (int): x position.
            y (int): y position.
            font (str): font family.
            size (int): font size.

        Returns:
            tkinter.Label: created Label.
        """
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        try:
            lbl = tk.Label(text=text, font=(font, size))
            lbl.place(x=x, y=y)
            return lbl
        except Exception as e:
            print("error:", e)

    def create_button(text: str, x: int, y: int, font: str, size: int, command: callable) -> tk.Button:
        """
        Create and place a Tk Button.

        Args:
            text (str): button text (can be empty).
            x (int): x position.
            y (int): y position.
            font (str): font family.
            size (int): font size.
            command (Callable): function to call on click.

        Returns:
            tkinter.Button: created Button.
        """
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        try:
            if text != "":
                btn = tk.Button(text=text, command=command, font=(font, size))
                btn.place(x=x, y=y)
                return btn
            else:
                btn = tk.Button(command=command, font=(font, size))
                btn.place(x=x, y=y)
                return btn
        except Exception as e:
            print("error:", e)

    def create_text_window(height: int, width: int, x: int, y: int) -> tk.Text:
        """
        Create and place a Tk Text widget.

        Args:
            height (int): number of lines.
            width (int): number of characters.
            x (int): x position.
            y (int): y position.

        Returns:
            tkinter.Text: created Text widget.
        """
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        txt = tk.Text(height=height, width=width)
        txt.place(x=x, y=y)
        return txt

    def error_window() -> NoReturn:
        """
        Create an 'error' window that randomizes font and size periodically.

        Useful for visual/demo effects.

        Returns:
            None
        """
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        window = tk.Tk()
        window.title("error")
        window.geometry("1600x700")
        status_label = tk.Label(text="", font=("Arial", 14))
        status_label.pack()
        def random_error():
            a = ram.randint(1,5)
            nu = ram.randint(1,500)
            fonts = {1: "Arial", 3: "Calibri", 4: "Times New Roman"}
            chosen = fonts.get(a, "Verdana")
            status_label.config(text="error", font=(chosen, nu))
            window.after(100, random_error)
        random_error()
        def close():
            window.destroy()
        btn = tk.Button(text="close", font=("Arial", 14), command=close)
        btn.place(x=1000, y=100)
        window.mainloop()

    def destroy_widget(widget: tk.Widget) -> NoReturn:
        """
        Destroy a Tk widget.

        Args:
            widget (tk widget): widget to destroy.

        Returns:
            None
        """
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        widget.destroy()

    def import_tk_window(window_name: str, script_path: str, label_text: str, button_text: str) -> NoReturn:
        """
        Create a 500x500 Tk window with a label and a button that runs a script.

        The executed script will receive 'window' in its global scope.

        Args:
            window_name (str)
            script_path (str)
            label_text (str)
            button_text (str)

        Returns:
            None
        """
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        window = tk.Tk()
        window.title(window_name)
        window.geometry("500x500")
        label = tk.Label(window, text=label_text, font=("Arial", 14))
        label.place(x=150, y=200)
        def run():
            window.destroy()
            try:
                with open(script_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    exec(content, {"window": window})
            except Exception as e:
                print(f"Error running script: {e}")
        btn = tk.Button(window, text=button_text, font=("Arial", 14), command=run)
        btn.place(x=150, y=250)
        window.mainloop()

    def create_slider(num_min: int, num_max: int, command: callable, x: int, y: int) -> tk.Scale:
        """
        Quickly create a horizontal Scale (slider).

        Args:
            num_min (int): slider minimum.
            num_max (int): slider maximum.
            command (callable): function to call on change.
            x (int): x position.
            y (int): y position.

        Returns:
            tkinter.Scale: created slider.
        """
        slider = tk.Scale(from_=num_min, to=num_max, orient="horizontal", command=command, length=400)
        slider.place(x=x, y=y)
        return slider