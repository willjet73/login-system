
# libraries Import
from tkinter import *
import customtkinter

# Main Window Properties

window = Tk()
window.title("Attack")
window.geometry("800x350")
window.configure(bg="#FFFFFF")


Button_id1 = customtkinter.CTkButton(
    master=window,
    text="Run",
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=30,
    width=95,
    border_width=2,
    corner_radius=6,
    border_color="#ffffff",
    bg_color="#FFFFFF",
    fg_color="#c93636",
    )
Button_id1.place(x=680, y=300)
Entry_id3 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="RUN ATTACK?",
    placeholder_text_color="#454545",
    font=("Arial", 41),
    text_color="#000000",
    height=150,
    width=400,
    border_width=2,
    corner_radius=6,
    border_color="#ffffff",
    bg_color="#FFFFFF",
    fg_color="#ffffff",
    )
Entry_id3.place(x=250, y=20)
Button_id2 = customtkinter.CTkButton(
    master=window,
    text="Cancel",
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=30,
    width=95,
    border_width=2,
    corner_radius=6,
    border_color="#fffafa",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Button_id2.place(x=30, y=300)



#run the main loop
window.mainloop()