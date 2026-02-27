from rich.console import Console
from colorama import Fore, Style
import pyfiglet
import pyautogui
import urllib.request
import time
import random
import string
import os

def tool_help():
    print(Fore.RED + """
    _  _ ____ _    ___     ____ ____ ____ ___ _ ____ _  _    
    |__| |___ |    |__]    [__  |___ |    |  | | |  | |- |    
    |  | |___ |___ |       ___] |___ |___  |  | |__| | -|    
                                                         
""" + Style.RESET_ALL + Fore.GREEN + """
             
Features """ + Style.RESET_ALL + Fore.MAGENTA + """
        - User-Typed Message: Manually type and send messages repeatedly.
        - Auto-Typed Message: Automated message-sending options.
        - Counting: Sends sequentially numbered messages.
        - Random Generator: Sends messages with random words.
""" + Style.RESET_ALL)
    spammer()

def user_typed_message():
    print(Fore.LIGHTMAGENTA_EX + "\n[*] User typed message" + Style.RESET_ALL + Fore.RED + "\t\t<SELECTED>" + Style.RESET_ALL)
    available_smg = input(Fore.GREEN + Style.BRIGHT + "[+] How many different messages? (Default 1) ->  " + Style.RESET_ALL)
    if available_smg.strip() == "": available_smg = 1
    elif available_smg == "0": exit_from_tool()
    else:
        try: available_smg = int(available_smg)
        except: user_typed_message()

    num_of_smg = 0
    list_of_smg = []
    print()
    while num_of_smg < available_smg:
        smg = input(Fore.GREEN + "[+] Enter message -> " + Style.RESET_ALL)
        list_of_smg.append(smg if smg.strip() != "" else "ERROR!")
        num_of_smg += 1
    
    number_of_smg = input(Fore.GREEN + Style.BRIGHT + "[+] How many times to repeat? (Default 1) -> "+ Style.RESET_ALL)
    if number_of_smg.strip() == "": number_of_smg = 1
    else:
        try: number_of_smg = int(number_of_smg)
        except: user_typed_message()
    
    print(Fore.RED + "\nFocus the message box now (any platform)!\n" + Style.RESET_ALL)
    user_is_ready = input(Fore.GREEN + Style.BRIGHT + "[+] Ready? Press Enter (10s delay) -> "+ Style.RESET_ALL)
    if user_is_ready.strip() in ["", "1"]:
        print(Fore.RED + "[ALERT!!!] Starting in 10 seconds. Move your cursor!\n" + Style.RESET_ALL)
        time.sleep(10)
        for _ in range(int(number_of_smg)):
            for message in list_of_smg:
                pyautogui.write(message)
                pyautogui.press('enter')
                print("Sent...")
        spammer()
    else: exit_from_tool()

def message_with_counting():
    print(Fore.LIGHTMAGENTA_EX + "\n[*] Message with counting" + Style.RESET_ALL)
    no_of_messages = input(Fore.GREEN + Style.BRIGHT + "[+] Number of messages? ->  " + Style.RESET_ALL)
    try: no_of_messages = int(no_of_messages) if no_of_messages.strip() != "" else 1
    except: message_with_counting()
    message = input(Fore.GREEN + Style.BRIGHT + "[+] Enter message ->  " + Style.RESET_ALL)
    print(Fore.RED + "\n[ALERT!!!] 10 seconds to focus the message box.\n" + Style.RESET_ALL)
    time.sleep(10)
    for i in range(no_of_messages):
        pyautogui.write(message + " " + str(i + 1))
        pyautogui.press('enter')
        print("Sent...")
    spammer()

def random_message_generator():
    print(Fore.LIGHTMAGENTA_EX + "\n[*] Random Message Generator" + Style.RESET_ALL)
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    try:
        response = urllib.request.urlopen(url)
        word_list = response.read().decode().splitlines()
    except:
        word_list = ["apple", "code", "spam", "python"]
    no_of_message = input(Fore.GREEN + Style.BRIGHT + "[+] How many messages? ->  " + Style.RESET_ALL)
    message_length = input(Fore.GREEN + Style.BRIGHT + "[+] Words per message? ->  " + Style.RESET_ALL)
    print(Fore.RED + "\nStarting in 10 seconds. Move your cursor to the message box!\n" + Style.RESET_ALL)
    time.sleep(10)
    for _ in range(int(no_of_message or 1)):
        sentence = " ".join(random.choice(word_list) for _ in range(int(message_length or 1)))
        pyautogui.write(sentence)
        pyautogui.press('enter')
        print("Sent...")
    spammer()

def auto_typed_message():
    print(Fore.LIGHTMAGENTA_EX + "\n[*] Auto typed message" + Style.RESET_ALL)
    print("[1] Counting\n[2] Random\n[0] Back")
    choice = input(Fore.GREEN + "[+] Option -> "+ Style.RESET_ALL)
    if choice == "1": message_with_counting()
    elif choice == "2": random_message_generator()
    else: spammer()

def spammer(): 
    print(Fore.YELLOW + "\nMain Menu:" + Style.RESET_ALL)
    print("[1] User typed message")
    print("[2] Auto typed message")
    print("[4] Help")
    print("[0] Quit")
    choice = input(Fore.GREEN + "[+] Select -> "+ Style.RESET_ALL)
    if choice == "1": user_typed_message()
    elif choice == "2": auto_typed_message()
    elif choice == "4": tool_help()
    elif choice == "0": exit_from_tool()
    else: spammer()

def exit_from_tool():
    print(Fore.RED + "\nExiting..." + Style.RESET_ALL)
    os._exit(0)

name_of_tool = pyfiglet.figlet_format("msg-spam")
colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]
Console().print(name_of_tool, style=random.choice(colors), end="\t\t\t-")
print(Fore.GREEN + Style.BRIGHT + 'lz'+ Style.RESET_ALL)

spammer()