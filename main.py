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
            texttyper(Fore.YELLOW + " ||" + Fore.WHITE + "   1. Make & open new note file \n" + Style.RESET_ALL , 0.003)
            print(Fore.YELLOW + " || --------------------------------------")
            texttyper(Fore.YELLOW + " ||" + Fore.WHITE + "   2. Open/Edit contents of a note file \n" + Style.RESET_ALL , 0.003)
            print(Fore.YELLOW + " || --------------------------------------")
            texttyper(Fore.YELLOW + " ||" + Fore.WHITE + "   3. Clear contents of a note file \n" + Style.RESET_ALL , 0.003)
            print(Fore.YELLOW + " || --------------------------------------")
            texttyper(Fore.YELLOW + " ||" + Fore.WHITE + "   4. Remove a note file \n" + Style.RESET_ALL , 0.003)
            print(Fore.YELLOW + " || --------------------------------------")
            texttyper(Fore.YELLOW + " ||" + Fore.WHITE + "   5. List all note files \n" + Style.RESET_ALL , 0.003)
            print(Fore.YELLOW + " || --------------------------------------")
            texttyper(Fore.YELLOW + " ||" + Fore.RED + "   6. Exit \n" + Style.RESET_ALL , 0.003)
            print(Fore.YELLOW + " =========================================\n")
        
            menuchoice = input(Fore.YELLOW + "\n - Enter Menu Number : " + Style.RESET_ALL)
            print()
            if menuchoice == "1":
                filename = input(" - Enter file name : " + Style.RESET_ALL)
                notefilepath = os.path.join(notes_dir, filename + ".txt")
                if os.path.exists(notefilepath):
                    print(Fore.CYAN + f"\n {filename}.txt Exist! ")
                    print(Fore.CYAN + f" Using Old {filename}.txt...\n" + Style.RESET_ALL)
                    fopenmode = "a"
                    time.sleep(0.1)
                else:
                    fopenmode = "w"
                    time.sleep(0.1)

                texttyper(Fore.YELLOW + " ##################### " + Fore.WHITE +  f"{filename}.txt" + Fore.YELLOW + " #####################" ,0.01)
                texttyper(Fore.YELLOW +"\n Enter your text : " + Style.RESET_ALL , 0.01 )
                usertext = input(Back.LIGHTWHITE_EX + Style.RESET_ALL)
                texttyper(Fore.YELLOW + " ##################### " + Fore.WHITE +  f"{filename}.txt" + Fore.YELLOW + " #####################\n",0.01)

                with open(notefilepath , fopenmode, encoding="utf-8") as txtfile:
                    txtfile.write(usertext + "\n")
                    
                texttyper(Fore.WHITE + f"\n {usertext}" + Fore.GREEN + " Saved in " + Fore.WHITE +  f"{filename}.txt " + Fore.GREEN +  "successfully! \n" + Style.RESET_ALL , 0.005)
                
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
                while True:
                    print(Fore.YELLOW + "\n =============================================== ")
                    texttyper(Fore.YELLOW + " ||" + Fore.WHITE + "      1. Show Contents of a note file \n" + Style.RESET_ALL , 0.005)
                    print(Fore.YELLOW + " || --------------------------------------")
                    texttyper(Fore.YELLOW + " ||" + Fore.WHITE + "      2. Edit a note file \n" + Style.RESET_ALL , 0.005)
                    print(Fore.YELLOW + " || --------------------------------------")
                    texttyper(Fore.YELLOW + " ||" + Fore.RED + "      3. Back to main menu \n" + Style.RESET_ALL , 0.005)
                    print(Fore.YELLOW + " =============================================== ")
                    
                    secondsmchoice = input(Fore.YELLOW + "\n - Enter SubMenu Number : " + Style.RESET_ALL)
                    if secondsmchoice == "1":
                        Rfilename = input("\n - Enter file name : " + Style.RESET_ALL)
                        time.sleep(0.2)
                        
                        Rfilepath = os.path.join(notes_dir, Rfilename + ".txt")
                        if os.path.exists(Rfilepath):
                            with open(Rfilepath, "r") as readingfile:
                                Rfilecontent = readingfile.read()
                                print()
                                texttyper(Fore.YELLOW + f" # {Rfilename}.txt Contents : \n" + Style.RESET_ALL, 0.01)
                                texttyper(Fore.WHITE + f"{Rfilecontent}"  + Style.RESET_ALL, 0.02)
                                
                                input(Fore.YELLOW + "\n   Press any Key to Continue... " + Style.RESET_ALL)
                                time.sleep(0.2)
                        else: 
                            print(Fore.RED + f"\n {Rfilename}.txt does not Exist! ")
                            input(Fore.YELLOW + "\n   Press any Key to Continue... " + Style.RESET_ALL)
                            time.sleep(0.2)
       
                    elif secondsmchoice == "2":
                        Efilename = input("\n - Enter file name : " + Style.RESET_ALL)
                        time.sleep(0.2)
                        
                        Efilepath = os.path.join(notes_dir, Efilename + ".txt")
                        if os.path.exists(Efilepath):
                            with open(Efilepath, "r") as readingfile:
                                Efilecontents = readingfile.read()
                                print()
                                texttyper(Fore.WHITE + f"{Efilecontents}"  + Style.RESET_ALL, 0.01)
                                while True:
                                    aorrchoice = input(Fore.YELLOW + "\n - Add/Remove a content part? (A/R) : " + Style.RESET_ALL)
                                    if aorrchoice == "A".lower():
                                        Rcontent = input("\n - Enter exact part to remove from file : " + Style.RESET_ALL)
                                    elif aorrchoice == "R".lower():
                                        Acontent = input("\n - Enter your text to add in file : " + Style.RESET_ALL)
                                    else:
                                        errorsound()
                                        print(Fore.RED, " ### ENTER A VALID INPUT! (Y/N) ### \n")
                                    
                        else: 
                            print(Fore.RED + f"\n {Efilename}.txt does not Exist! ")
                            input(Fore.YELLOW + "\n   Press any Key to Continue... " + Style.RESET_ALL)
                            time.sleep(0.2)
 
                    elif secondsmchoice == "3":
                        print(Fore.YELLOW + "\n BACK TO MAIN MENU...")
                        time.sleep(0.5)
                        break
                    else:
                        errorsound()
                        print(Fore.RED, " ### ENTER A VALID NUMBER! ### \n")

            elif menuchoice == "3":
                RCfilename = input(" - Enter file name : " + Style.RESET_ALL)
                RCfilepath = os.path.join(notes_dir, RCfilename + ".txt")
                if os.path.exists(RCfilepath):
                    confirmremove = input(Fore.RED + f"\n - ARE YOU SURE YOU WANT TO REMOVE {RCfilename}.txt ? (Y/N) : " + Style.RESET_ALL)
                    
                    if confirmremove == "Y".lower():
                        with open(RCfilepath, "w" , encoding="utf-8") as removecontentfile:
                            removecontentfile.write("")
                            texttyper(Fore.WHITE + f"\n        {RCfilename}.txt " + Fore.GREEN +  "Data removed successfully! \n" + Style.RESET_ALL , 0.005)
                            input(Fore.YELLOW + "\n   Press any Key to Continue... " + Style.RESET_ALL)
                            time.sleep(0.2)
                        
                    elif confirmremove == "N".lower():
                        print(Fore.YELLOW + "\n BACK TO MAIN MENU...")
                        time.sleep(0.5)
                    else:
                        errorsound()
                        print(Fore.RED, " ### ENTER A VALID INPUT! (Y/N) ### \n")                        
                
                else:
                    print(Fore.RED + f"\n {RCfilename}.txt does not Exist! ")
                    input(Fore.YELLOW + "\n   Press any Key to Continue... " + Style.RESET_ALL)
                    time.sleep(0.2)               
                                
            elif menuchoice == "4":
                Dfilename = input(" - Enter file name : " + Style.RESET_ALL)
                Dfilepath = os.path.join(notes_dir, Dfilename + ".txt")
                if os.path.exists(Dfilepath):
                    texttyper(Fore.RED + f"\n - ARE YOU SURE YOU WANT TO REMOVE {Dfilename}.txt ? (Y/N) : " + Style.RESET_ALL, 0.0005)
                    print(Fore.RED + f"#File_Path = {Dfilepath} " + Style.RESET_ALL)
                    confirmremove = input(" ")
                    
                    if confirmremove == "Y".lower():
                        with open(Dfilepath, "w" , encoding="utf-8") as deletefile:
                            os.remove(Dfilepath)
                            texttyper(Fore.WHITE + f"\n        {Dfilename}.txt " + Fore.GREEN +  "file removed successfully! \n" + Style.RESET_ALL , 0.005)
                            input(Fore.YELLOW + "\n   Press any Key to Continue... " + Style.RESET_ALL)
                            time.sleep(0.2)
                        
                    elif confirmremove == "N".lower():
                        print(Fore.YELLOW + "\n BACK TO MAIN MENU...")
                        time.sleep(0.5)
                    else:
                        errorsound()
                        print(Fore.RED, " ### ENTER A VALID INPUT! (Y/N) ### \n")                        
                else:
                    print(Fore.RED + f"\n {Dfilename}.txt does not Exist! ")
                    input(Fore.YELLOW + "\n   Press any Key to Continue... " + Style.RESET_ALL)
                    time.sleep(0.2)        
                    
            elif menuchoice == "6":
                sys.exit()
            
            else:
                errorsound()
                print(Fore.RED, " ### ENTER A VALID NUMBER! ### \n")

        

        
    def run(self):
        pass
        

if __name__ == "__main__":
    app = Main()
    app.run()