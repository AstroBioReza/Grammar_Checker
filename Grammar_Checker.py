import tkinter as tk
from tkinter import scrolledtext
import language_tool_python

def correct_text():
    input_text = text_input.get("1.0", tk.END)
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(input_text)
    corrected_text = language_tool_python.utils.correct(input_text, matches)
    text_output.config(state=tk.NORMAL)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.INSERT, corrected_text)
    text_output.config(state=tk.DISABLED)
#window
root = tk.Tk()
root.title("Grammar and Spell Checker")
root.geometry("600x400")
#input
text_input_label = tk.Label(root, text="Input:")
text_input_label.pack()
text_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=10)
text_input.pack(padx=10, pady=10)
#button
correct_button = tk.Button(root, text="Check!", command=correct_text)
correct_button.pack(pady=10)
#output
text_output_label = tk.Label(root, text="Outout:")
text_output_label.pack()
text_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=10)
text_output.pack(padx=10, pady=10)
text_output.config(state=tk.DISABLED)
root.mainloop()
