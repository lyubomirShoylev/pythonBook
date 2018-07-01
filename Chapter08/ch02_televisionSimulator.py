# Television Simulator
#
# Simulates a television. The user is able to switch channels and
# change volume levels, if they are within valid range.

class Television(object):
    """A television simulator"""
    def __init__(self, channel = 1, volume = 50):
        self.channel = channel
        self.volume = volume
        print(f"Your television is set at channel {self.channel} and volume {self.volume}.")
    
    def __str__(self):
        ret = f"Television:\nchannel = {self.channel}\nvolume = {self.volume}"
        return ret
    
    # deprecated, another implementation
    # def setter(self, chan = -1, vol = -1):
        # if 1 <= chan <=50:
        #     self.channel = chan
        # else:
        #     ""
        #     self.channel = self.channel
        
    #     if 0 <= vol <= 100:
    #         self.volume = vol
    #     else:
    #         self.volume = self.volume
    def setChannel(self, chan = 0):
        if 1 <= chan <=50:
            self.channel = chan
            print(f"Television successfully set to channel {self.channel}")
        else:
            print("Value out of range! Try again.")
    
    def raiseVolume(self, vol = -1):
        if self.volume + vol <= 100:
            self.volume += vol
            print(f"Television successfully set to volume {self.volume}")
        elif vol + self.volume > 100:
            print(f"Value too high! Current volume is {self.volume}")
    
    def lowerVolume(self, vol = -1):
        if 0 <= self.volume - vol:
            self.volume -= vol
            print(f"Television successfully set to volume {self.volume}")
        elif 0 > self.volume - vol:
            print(f"Value too high! Current volume is {self.volume}")

def main():
    tv = Television()

    choice = None
    while choice != "0":
        print \
        ("""
        Television Simulator

        0 - Quit
        1 - Change the channel
        2 - Raise the volume
        3 - Lower the volume
        """)

        choice = input("Choice: ")
        print()
        
        # exit
        if choice == "0":
            print("Good-bye.")
        
        # change the channel
        elif choice == "1":
            num = int(input("\n\tWhich channel to change to? "))
            tv.setChannel(num)
        
        # raise the volume
        elif choice == "2":
            amount = int(input("\n\tRaise the volume by: "))
            tv.raiseVolume(amount)
        
        # lower the volume
        elif choice == "3":
            amount = int(input("\n\tLower the volume by: "))
            tv.lowerVolume(amount)
        
        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
input("\n\nPress the enter key to exit")