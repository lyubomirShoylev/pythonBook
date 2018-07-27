# lelele
import pickle

f = open("highscores.txt", "w")
kek = [("GOSHO", 10), ("PESHO", 0)]
for i in kek:
    f.write(i[0] + "\n")
    f.write(str(i[1]) + "\n")
f.close()

# i will mess with this file just to test if this is set up corretly