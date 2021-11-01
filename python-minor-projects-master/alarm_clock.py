"""
Alarm Clock - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
"""
import winsound
import time

def play_sound():
    for number in range(3):
        winsound.Beep(1000, 500)
        
while True:
    action = input("\nYour clock here. What should I do?\n[1] Beep after some time [timer function]\n[2] Beep at correct hour [alarm function]\n[3] Exit\n")
    if action == "1":
        print("Set the timer:")
        h_delay = int(input("Hours:"))
        m_delay = int(input("Minutes:"))
        s_delay = int(input("Seconds:"))
        total_delay = h_delay*60*60 + m_delay*60 + s_delay
        print("\nTimer set for: {} hours, {} minutes and {} seconds.".format(h_delay, m_delay, s_delay))
        start_time = time.time()
        while True:    
            elapsed_time = time.time() - start_time
            print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
            if int(elapsed_time) == total_delay:
                print("{} hours, {} minutes and {} seconds reached!".format(h_delay, m_delay, s_delay))
                play_sound()
                break
            else:
                time.sleep(1)
    elif action == "2":
        print("Set the alarm (HH:MM:SS, 24H format):")
        while True:
            h_set = input("Hour:")
            if 0 <= int(h_set) <= 23:
                break
            else:
                print("Type in correct hour!")
        while True:
            m_set = input("Minute:")
            if 0 <= int(m_set) <= 59:
                break
            else:
                print("Type in correct minute!")
        while True:
            s_set = input("Second:")
            if 0 <= int(s_set) <= 59:
                break
            else:
                print("Type in correct second!")
        alarm_set = h_set + ":" + m_set + ":" + s_set 
        print("\nAlarm set for: {}".format(alarm_set))
        while True:
            print(time.strftime("%H:%M:%S", time.localtime()))
            if alarm_set == str(time.strftime("%H:%M:%S", time.localtime())):
                print("\n{} reached!".format(alarm_set))
                play_sound()
                break
            else:
                time.sleep(1)
    elif action == "3":
        print("Bye bye.")
        break
    else:
        print("Choose correct action.")
