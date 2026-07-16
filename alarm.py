import tkinter as tk, pywhatkit, datetime, time, pyautogui
from plyer import notification
import winsound
'''
Note:
1. Please dont close the programme after scheduling message or setting an alarm...
2. please change the year if its not 2026
3. Must log on whatsapp web if you want to schedule a message
4. If there is problem of sending message after it has been typed in the chatbox, please increase the number under time.sleep after the code to send message 
5. Please follow the instructions correctly to make it run smoothly

Thanks!

'''

pressed_bt = []
run = True
    
def mode(button):
    pressed_bt.append(button)
    for b in btns:  
        b.destroy()
    print("Pressed:", pressed_bt)

    if button == "Alarm":
        def set_alarm():
            try:
                hour = int(hour_entry.get())
                minute = int(min_entry.get()) 
                day = int(day_entry.get())
                month = int(mon_entry.get())
                year = 2026  # current year
                ampm = ampm_entry.get().strip().upper()


                if ampm == "PM" and hour != 12:
                    hour += 12
                elif ampm == "AM" and hour == 12:
                    hour = 0

                alarm_time = datetime.datetime(year,month, day, hour, minute)
                notification.notify(
                    title="Alarm",
                    message=f"Alarm set for {alarm_time.strftime('%Y-%m-%d %I:%M %p')}",
                    timeout=10
                )

                def wait_for_alarm():
                    now = datetime.datetime.now()
                    if now >= alarm_time:
                        notification.notify(
                            title="Alarm",
                            message="Time's up! Your alarm is ringing!",
                            timeout=10
                        )
                        for i in range(20):
                            winsound.Beep(1000, 500)
                            time.sleep(0.5)
                    else:
                        root.after(1000, wait_for_alarm)
                wait_for_alarm()
            except Exception as e:
                notification.notify(
                    title="An error occured",
                    message=str(e),
                    timeout=10
                )
        tk.Label(root, text="Hour(1 - 12):", bg="red", fg="white").grid(row=0, column=0, padx=15, pady=15, ipadx=15, ipady=24, sticky="nsew")
        hour_entry = tk.Entry(root, font=("Helvetica", 14))
        hour_entry.grid(row=0, column=1, padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")

        tk.Label(root, text="Minute(0 - 59):", bg="red", fg="white").grid(row=1, column=0, padx=15, pady=15, ipadx=15, ipady=24, sticky="nsew")
        min_entry = tk.Entry(root, font=("Helvetica", 14))
        min_entry.grid(row=1, column=1, padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")

        tk.Label(root, text="Day(1 - 31):", bg="red", fg="white").grid(row=2, column=0,padx=15, pady=15, ipadx=15, ipady=24, sticky="nsew")
        day_entry = tk.Entry(root, font=("Helvetica", 14))
        day_entry.grid(row=2, column=1,padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")

        tk.Label(root, text="Month(1 - 12):", bg="red", fg="white").grid(row=3, column=0, padx=15, pady=15, ipadx=15, ipady=24, sticky="nsew")
        mon_entry = tk.Entry(root, font=("Helvetica", 14))
        mon_entry.grid(row=3, column=1,padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")

        tk.Label(root, text="AM/PM:", bg="red", fg="white").grid(row=4 , column=0, padx=15, pady=15, ipadx=15, ipady=24, sticky="nsew")
        ampm_entry = tk.Entry(root, font=("Helvetica", 14))
        ampm_entry.grid(row=4, column=1, padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")
        
        buttton = tk.Button(root, text="Set Alarm", bg="green", fg="white",font=("Helvetica", 14, "bold"), command= set_alarm)
        buttton.grid(row=5, column=0,padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")
    if button == "Timer":
        def set_timer():
            def countdown(t):
                if t > 0:
                    screen.delete("1.0", tk.END)
                    screen.insert(tk.END, f"Time: {t} seconds...")
                    root.after(1000, countdown, t-1)
                else:

                    notification.notify(
                        title="Timer",
                        message="Time's up! Your timer has finished.",
                        timeout=10
                    )
                    for i in range(12):
                        winsound.Beep(1000, 500)
                        time.sleep(0.5)
            countdown(int(lenght_of_timer.get()))

        screen = tk.Text(root, font=("Helvetica", 32), height=1,  bg="white", fg="black")
        screen.grid(row=1, column=0, rowspan=1, columnspan=4)   
        tk.Label(root, text="Enter lenght of timer in seconds:", bg="red", fg="white").grid(row=0, column=0, padx=15, pady=15, ipadx=15, ipady=24, sticky="nsew")
        lenght_of_timer = tk.Entry(root, font=("Helvetica", 14, "bold"))
        lenght_of_timer.grid(row=0, column=1, padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")
        buttton = tk.Button(root, text="Start Timer", bg="green", fg="white",font=("Helvetica", 14, "bold"), command= set_timer)
        buttton.grid(row=6, column=0,padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")
    if button == "Stopwatch":
        def set_stopwatch(t=0):
            if run:  
                screen.delete("1.0", tk.END)
                screen.insert(tk.END, f"Time: {t} seconds...")
                root.after(1000, set_stopwatch, t+1)

        def start():
            global run
            run = True
            set_stopwatch(0)

        def stop():
            global run
            run = False

        screen = tk.Text(root, font=("Helvetica", 32), height=1, bg="white", fg="black")
        screen.grid(row=1, column=0, rowspan=1, columnspan=4)

        start_button = tk.Button(root, text="Start Stopwatch", bg="green", fg="white",
                                 
                                font=("Helvetica", 14, "bold"), command=start)
        start_button.grid(row=2, column=0, padx=15, pady=15, ipadx=24, ipady=24)

        stop_button = tk.Button(root, text="Stop Stopwatch", bg="red", fg="white",
                                font=("Helvetica", 14, "bold"), command=stop)
        stop_button.grid(row=3, column=0, padx=15, pady=15, ipadx=24, ipady=24)
    if button == "Message":
        def send_message():
            try:
                hour = int(hour_entry.get())
                minute = int(min_entry.get())

                ampm = ampm_entry.get().strip().upper()
                message = msg_entry.get()
                number = num_entry.get()


                if ampm == "PM" and hour != 12:
                    hour += 12
                elif ampm == "AM" and hour == 12:
                    hour = 0
                notification.notify(
                    title="Message Scheduled",
                    message=f'Your message to {number} will be sent at {hour:02d}:{minute:02d}.',
                    timeout=10
                )
                pywhatkit.sendwhatmsg(number, message, hour, minute)
                time.sleep(30)
                pyautogui.press("enter")
            except Exception as e:
                notification.notify(
                    title="Error",
                    message=str(e),
                    timeout=10
                )
        tk.Label(root, text="Hour(1 - 12):", bg="red", fg="white").grid(row=0, column=0, padx=15, pady=15, ipadx=15, ipady=24, sticky="nsew")
        hour_entry = tk.Entry(root, font=("Helvetica", 14))
        hour_entry.grid(row=0, column=1, padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")

        tk.Label(root, text="Minute(0 - 59):", bg="red", fg="white").grid(row=1, column=0, padx=15, pady=15, ipadx=15, ipady=24, sticky="nsew")
        min_entry = tk.Entry(root, font=("Helvetica", 14))
        min_entry.grid(row=1, column=1, padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")


        tk.Label(root, text="AM/PM:", bg="red", fg="white").grid(row=2 , column=0, padx=15, pady=15, ipadx=15, ipady=24, sticky="nsew")
        ampm_entry = tk.Entry(root, font=("Helvetica", 14))
        ampm_entry.grid(row=2, column=1, padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")

        tk.Label(root, text="Whatsapp Number(with country code):", bg="red", fg="white").grid(row=3, column=0, padx=15, pady=15, ipadx=15, ipady=24, sticky="nsew")
        num_entry = tk.Entry(root, font=("Helvetica", 14))
        num_entry.grid(row=3, column=1, padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")

        tk.Label(root, text="Enter message:", bg="red", fg="white").grid(row=4 , column=0, padx=15, pady=15, ipadx=15, ipady=24, sticky="nsew")
        msg_entry = tk.Entry(root, font=("Helvetica", 14))
        msg_entry.grid(row=4, column=1, padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")
        
        buttton = tk.Button(root, text="Set Alarm for automatic message", bg="green", fg="white",font=("Helvetica", 14, "bold"), command= send_message)
        buttton.grid(row=5, column=0,padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")

root = tk.Tk()
root.title("Arnav's Clock")
root.geometry("1000x900")
root.config(bg="black")

frame = tk.Frame(root, bg="black")
frame.grid(row=2, column=0)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)

btns = []

b1 = tk.Button(frame, text="Alarm", command=lambda: mode("Alarm"),
               bg="#39FF14", fg="black", font=("Helvetica", 14, "bold"))
b1.grid(row=0, column=0, padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")
btns.append(b1)

b2 = tk.Button(frame, text="Timer", command=lambda: mode("Timer"),
               bg="#39FF14", fg="black", font=("Helvetica", 14, "bold"))
b2.grid(row=1, column=0, padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")
btns.append(b2)

b3 = tk.Button(frame, text="Stopwatch", command=lambda: mode("Stopwatch"),
               bg="#39FF14", fg="black", font=("Helvetica", 14, "bold"))
b3.grid(row=2, column=0, padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")
btns.append(b3)

b4 = tk.Button(frame, text="Message", command=lambda: mode("Message"),
               bg="#39FF14", fg="black", font=("Helvetica", 14, "bold"))
b4.grid(row=3, column=0, padx=15, pady=15, ipadx=24, ipady=24, sticky="nsew")
btns.append(b4)

root.mainloop()
