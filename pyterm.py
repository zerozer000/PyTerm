import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

import keyboard

class output:
    def oerror(self):
        log["state"] = "normal"
        log.insert("end", f"Error: {self}\n")
        log["state"] = "disabled"

    def oprint(self):
        log["state"] = "normal"
        log.insert("end", f"{self}\n")
        log["state"] = "disabled"
    
class PyTerm:
    commands = (
        "PyTerm.commandlist() - shows a command list\n"
        "PyTerm.help()- help\n"
        "PyTerm.clear() - clear screen\n"
        "PyTerm.outputfont(font) - changes output screen bg color #example: PyTerm.outputfont('{Arial} 14 bold')\n"
        "outputbackground(self)\n"
        "outputbackground(color)\n")
    def help():
        output.oprint(f"PyTerm by zero000zer\nCommands\n{PyTerm.commands}")

    def commandlist():
        output.oprint(PyTerm.commands)
    
    def clear():
        log.delete("1.0")
    
    def outputfont(self):
        try:
            log["font"] = self
            output.oprint(f"font changed to {self}")
        except Exception as exc:
            output.oerror(exc)
    def outputbackground(self):
        log["background"] = self
    
    def execute(self, *file):
        if file.exits:
            pass
        try:
            result = eval(self)
            if result:
                output.oprint("result:"+result)
            
        except Exception as exc:
            output.oerror(exc)
    
def execute_promt():
    command = promt.get()

    log["state"] = "normal"
    log.insert("end", f"{command}\n")
    log["state"] = "disabled"
    try:
        result = eval(command)
        if result:
            output.oprint("result:"+command)

    except Exception as exc:
        output.oerror(exc)
        '''
        log["state"] = "normal"
        log.tag_add("highlightline", "1.0", "end")
        log.insert("end", f"Error: {exc}\n", "end")
        log.tag_configure("highlightline", foreground="red", relief="raised")
        log["state"] = "disabled"
        '''


root = tk.Tk()
root.title("PyTerm")
root.iconbitmap("icon.ico")

#root.overrideredirect(True)
root.config(bg="#B6B6B6")

label_style = ttk.Style()
label_style.configure("My.TLabel",
                    font="{Cascadia Code} 10",
                    foreground="#000000",
                    background="#B6B6B6")

keyboard.add_hotkey("Enter", execute_promt)

log = ScrolledText(state='disabled', background="#B6B6B6",foreground="black" ,font="{Cascadia Code} 10", bd=0)
log.pack(fill="both")

lbltext0 = ttk.Label(text="Enter command", style="My.TLabel")
lbltext0.pack(anchor="w")

promt = tk.Entry(font="{Cascadia Code} 10",foreground="#000000", background="#949494", )
promt.pack(fill="x", expand=5)

execbttn = ttk.Button(promt, text="Exec",command=execute_promt, style="My.TLabel", cursor="hand2")
execbttn.pack(anchor='e')

PyTerm.help()
root.mainloop()