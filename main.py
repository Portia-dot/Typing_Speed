from tkinter import *
from header import Header
header = Header()
tk = Tk()
tk.title('Typing Calculator')


#Background color
BACKGROUND_COLOR = '#547792'

tk.configure(bg=BACKGROUND_COLOR, padx=20, pady=20)

canvas = Canvas(width=600, height=600)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0)

#Correct CMP
cpm_title_id, cmp_rect_id, cmp_reading_score = header.header_item(canvas, 90, 100, 165, 90,
            210,110, 180, 100, 'Corrected CMP:',
            '0'
            )


#Word Per second

title_id, rect_id, reading_score = header.header_item(canvas, 240, 100, 270, 90,
            310,110, 280, 100, 'WPS:',
            '0'
            )


#Time


time_title_id, time_rect_id, time_reading_score = header.header_item(canvas, 360, 100, 410, 90,
            440,110, 420, 100, 'Time Left:',
            '60'
            )


def reset_wps_cpm_displays():
    """
    Reset the Word Per Second (WPS) and Characters Per Minute (CPM) displays to
    their default values. This function updates the GUI elements to show the default
    initial state.

    :return: None
    """
    canvas.itemconfig(reading_score, text='0')  # Reset WPS
    canvas.itemconfig(cmp_reading_score, text='0')  # Reset CPM
    canvas.itemconfig(time_reading_score, text='60')

def restart():
    """
    Resets the user interface elements and internal variables to their initial state.

    This function restores the user interface components such as text entry and
    display areas to a defined default state. It also clears any applied visual
    tags, resets timer-related variables, and updates any speed displays.

    :return: None
    """
    user_entry.config(state= 'normal')
    user_entry.delete(0, END)
    text_widget.delete(1.0, END)
    text_widget.insert(END, header.sample_text)
    text_widget.tag_remove('correct', '1.0', END)
    text_widget.tag_remove('incorrect', '1.0', END)
    header.reset_timer_variables()
    reset_wps_cpm_displays()



#Reset Button
btn =  Button(tk, text= 'Reset', command= restart)
canvas.create_window(520, 100, window=btn)





#Text Field
def key_released(event):
    """
    Updates the interface and evaluates typed text when a key is released in the text entry field.

    This function is triggered whenever a key is released while typing in the entry widget. It evaluates
    the typed text against a pre-defined sample text, updating visual feedback such as 'correct' and
    'incorrect' tags in the text widget to indicate accuracy. It also calculates and updates performance
    metrics such as words per second (WPS), characters per minute (CPM), elapsed time, and remaining time
    on screen elements using associated canvas items. When the remaining time reaches zero, the text
    entry field is disabled, the entry field is cleared, and a results overlay is displayed.

    :param event: The event object representing the key release event
    :type event: tkinter.Event
    :return: None
    """
    text_widget.tag_config('correct', foreground='green')
    text_widget.tag_config('incorrect', foreground='red')
    typed_text = user_entry.get()
    wps, cpm, elapsed_time, elapsed_minutes, remaining_time = header.calculate_wps(typed_text)
    for i in range(len(typed_text)):
        canvas.itemconfig(reading_score, text = round(wps))
        canvas.itemconfig(cmp_reading_score, text = round(cpm))
        canvas.itemconfig(time_reading_score, text = 60 - round(elapsed_time))
        start_index = f"1.{i}"
        end_index = f"1.{i + 1}"
        text_widget.tag_remove('correct', start_index, end_index)
        text_widget.tag_remove('incorrect', start_index, end_index)

        if typed_text[i] != header.sample_text[i]:
          text_widget.tag_add('incorrect',start_index, end_index)
        else:
            text_widget.tag_add('correct', start_index, end_index)
    if remaining_time <= 0:
        user_entry.config(state= 'disabled')
        user_entry.delete(0, END)
        print('Show result overlay')
        show_result(wps, cpm)

# Creat an overlay for result

def show_result(wps, cpm):
    """
    Displays a user interface overlay showing the provided WPS (Words Per Second) and CPM (Characters Per Minute)
    values within a labeled frame. Includes a button to close the overlay.

    :param wps: Words per second value to display
    :type wps: float or int
    :param cpm: Characters per minute value to display
    :type cpm: float or int
    :return: None
    :rtype: None
    """
    overlay = Frame(tk, bg=BACKGROUND_COLOR, width=300, height=300)
    overlay.place(relx=0.5, rely=0.5, anchor='center')
    wps_label = Label(overlay, text =f'WPS: {wps}', font=('Arial', 10), bg=BACKGROUND_COLOR)
    wps_label.place(relx=0.5, rely=0.3, anchor='center')

    cpm_label  = Label(overlay, text =f'CPM: {cpm}', font=('Arial', 10), bg=BACKGROUND_COLOR)
    cpm_label.place(relx=0.5, rely=0.5, anchor='center')
    btn = Button(overlay, text='Close', command= overlay.destroy)
    btn.place(relx=0.5, rely=0.7, anchor='center')

#Typing Text


text_widget = Text(tk, font=('Arial', 19), width=50, height=10)
text_widget.grid(row=0, column=0)
text_widget.insert(END, header.sample_text)
text_widget.config(state= 'disabled')


#User_Typ
user_entry = Entry(canvas, font=('Arial', 15), width=30)
canvas.create_window(300, 525, window=user_entry)
user_entry.bind('<KeyRelease>', key_released)
user_entry.focus_set()




tk.mainloop()