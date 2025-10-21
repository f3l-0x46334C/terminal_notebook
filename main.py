import os
import sys
import time
from colorama import Fore, Back, Style

maintextfile = "notes.txt"

def texttyper(text, speed):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
        
def errorsound():
    print("\a")
                
class Main:
    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        notes_dir = os.path.join(base_path, "Notes")
        os.makedirs(notes_dir, exist_ok=True)

        print(Fore.LIGHTMAGENTA_EX + "\n ================= Terminal Notebook =================")
        time.sleep(0.1)
        texttyper(Fore.LIGHTMAGENTA_EX + " =================" + Fore.WHITE + " Created by -- F3L " + Fore.LIGHTMAGENTA_EX + "=================" + Style.RESET_ALL, 0.02)
        print("\n")
        
        input(Fore.YELLOW + "   Press any Key to Continue... " + Style.RESET_ALL)
        print(Style.RESET_ALL)
        
        while True:
            print(Fore.YELLOW + "\n =========================================")
            texttyper(Fore.YELLOW + " ||" + Fore.WHITE + "   1. Make & open new note file \n" + Style.RESET_ALL , 0.005)
            print(Fore.YELLOW + " || --------------------------------------")
            texttyper(Fore.YELLOW + " ||" + Fore.WHITE + "   2. Open/Edit a note file \n" + Style.RESET_ALL , 0.005)
            print(Fore.YELLOW + " || --------------------------------------")
            texttyper(Fore.YELLOW + " ||" + Fore.WHITE + "   3. Clear contents of a note file \n" + Style.RESET_ALL , 0.005)
            print(Fore.YELLOW + " || --------------------------------------")
            texttyper(Fore.YELLOW + " ||" + Fore.WHITE + "   4. Remove a note file \n" + Style.RESET_ALL , 0.005)
            print(Fore.YELLOW + " || --------------------------------------")
            texttyper(Fore.YELLOW + " ||" + Fore.RED + "   5. Exit \n" + Style.RESET_ALL , 0.005)
            print(Fore.YELLOW + " =========================================\n")
        
            menuchoice = input(Fore.YELLOW + "\n - Enter Menu Number : ")
            print()
            if menuchoice == "1":
                filename = input(" - Enter file name : " + Style.RESET_ALL)
                notefilepath = os.path.join(notes_dir, filename + ".txt")
                if os.path.exists(notefilepath):
                    print(Fore.CYAN + f"\n {filename}.txt Exists! ")
                    print(Fore.CYAN + f" Using Old {filename}.txt...\n" + Style.RESET_ALL)
                    fopenmode = "a"
                    time.sleep(0.1)
                else:
                    print(Fore.GREEN + f"\n {filename}.txt Created succesfully! \n" + Style.RESET_ALL)
                    fopenmode = "w"
                    time.sleep(0.1)

                texttyper(Fore.YELLOW + " ##################### " + Fore.WHITE +  f"{filename}.txt" + Fore.YELLOW + " #####################" ,0.01)
                texttyper(Fore.YELLOW +"\n Enter your text : " + Style.RESET_ALL , 0.01 )
                usertext = input(Back.LIGHTWHITE_EX + Style.RESET_ALL)
                texttyper(Fore.YELLOW + " ##################### " + Fore.WHITE +  f"{filename}.txt" + Fore.YELLOW + " #####################\n",0.01)

                with open(notefilepath , fopenmode, encoding="utf-8") as txtfile:
                    txtfile.write(usertext + "\n")
                    
                texttyper(Fore.WHITE + f"\n {usertext}" + Fore.GREEN + " Saved in " + Fore.WHITE +  f"{filename}.txt " + Fore.GREEN +  "Succesfully! \n" + Style.RESET_ALL , 0.005)
                
                while True:
                    addmorechoice = input(Fore.YELLOW + "\n - Want to add more this file? (y/n) : ")
                    
                    if addmorechoice == "Y".lower():
                        texttyper(Fore.YELLOW + "\n ##################### " + Fore.WHITE +  f"{filename}.txt" + Fore.YELLOW + " #####################" ,0.01)
                        texttyper(Fore.YELLOW +"\n Enter your text : " + Style.RESET_ALL , 0.01 )
                        usertext = input()
                        texttyper(Fore.YELLOW + " ##################### " + Fore.WHITE +  f"{filename}.txt" + Fore.YELLOW + " #####################\n",0.01)

                        with open(notefilepath , "a", encoding="utf-8") as txtfile:
                            txtfile.write(usertext + "\n")                       
                        
                    elif addmorechoice == "N".lower():
                        print(Fore.YELLOW + "\n BACK TO MAIN MENU...")
                        time.sleep(0.5)
                        break
                    else:
                        errorsound()
                        print(Fore.RED, " ### ENTER A VALID INPUT! (Y/N) ### \n")

            
                
                    
            elif menuchoice == "2":
                pass
            elif menuchoice == "3":
                pass
            elif menuchoice == "4":
                pass
            elif menuchoice == "5":
                sys.exit()
            
            else:
                errorsound()
                print(Fore.RED, " ### ENTER A VALID NUMBER! ### \n")

        

        
    def run(self):
        pass
        

if __name__ == "__main__":
    app = Main()
    app.run()