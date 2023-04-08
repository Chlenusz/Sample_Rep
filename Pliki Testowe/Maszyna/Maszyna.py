import random
import tkinter as tk

class Maszyna():
    
    def generator(self, max):
        temp = 0
        self.lokalizajca = "D:\Programy Python\Pliki Testowe\Dane.txt"
        while temp <= max:
            lista = ['4','1','6','2','0','3']
            for i in lista:
                string = random.sample(lista,4)
            numbers = list(map(int,string))
            mystring = " ".join(map(str,numbers))
            with open(self.lokalizacja,"a") as f:
                f.write(mystring)
                f.write("\n")
            f.close()
            temp += 1

    def reset(self):
        try:
            with open(self.lokalizacja,"w") as f:
                f.write("")
            f.close()
            print(self.lokalizacja)
        except:
            print("ćoś poszło nie tak :(")
            print(self.lokalizacja)
            return

    def mediana(self):
        with open(self.lokalizacja, "r") as f:
            data = f.read()
            f.close()
        test = [int(digit) for digit in data if digit.isdigit()]
        test.sort()
        n = len(test)
        if n % 2 == 0:
            median = (test[n//2-1] + test[n//2]) / 2
        else:
            median = test[n//2]
        return median

class App:
    def __init__(self, master):
        self.master = master
        master.title("Maszyna")
        self.label = tk.Label(master, text="Kliknij przycisk 'Wygeneruj' aby wygenerować cyfry.")
        self.label.pack()
        self.button = tk.Button(master, text="Wygeneruj", command=self.run_machine)
        self.button.pack()
        self.button = tk.Button(master, text="Restuj Baze", command=Maszyna().reset)
        self.button.pack()
        self.median_label = tk.Label(master, text="")
        self.median_label.pack()

    def run_machine(self):
        Maszyna().generator(5)
        median = Maszyna().mediana()
        self.median_label.config(text=f"Mediana: {median}")
        

root = tk.Tk()
app = App(root)
root.mainloop()