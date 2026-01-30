import os
import nbtlib
import tkinter
from tkinter import filedialog

class Player:
    def __init__(self, datfile):
        data = nbtlib.load(datfile)
        self.data_dict = dict(data)
        self.uuid = self.uuid_parse(self.data_dict)
        self.xp = self.xp_parse(self.data_dict)
        self.effects = self.effect_parse(self.data_dict)
        self.gamemode = self.gamemode_parse(self.data_dict)
        self.inventory = self.inventory_parse(self.data_dict)
        self.lastdeath = self.lastdeath_parse(self.data_dict)
        self.recipes = self.recipes_parse(self.data_dict)

    def recipes_parse(self, data_dict):
        try:
            recipe = data_dict['recipeBook']['recipes']
        except:
            recipe = "No info"
        return recipe

    def lastdeath_parse(self, data_dict):
        try:
            lastdeath = [data_dict['LastDeathLocation']['pos'], data_dict['LastDeathLocation']['dimension']]
        except:
            lastdeath = "No info"
        return lastdeath

    def gamemode_parse(self, data_dict):
        try:
            gamemode = data_dict['playerGameType']
        except:
            gamemode = "No info"
        return gamemode

    def xp_parse(self, data_dict):
        try:
            xp = int(str(data_dict['XpTotal']).replace("Int(", "").replace(")", ""))
        except:
            xp = "No info"
        return xp

    def uuid_parse(self, data_dict):
        try:
            uuid = data_dict['UUID']
        except:
            uuid = "No info"
        return uuid

    def effect_parse(self, data_dict):
        try:
            dictt = data_dict['active_effects']
            result = list()
            for key in dictt:
                result.append(key["id"])
        except:
            result = "No info"
        return result

    def inventory_parse(self, data_dict):
        try:
            dictt = data_dict['Inventory']
            result = list()
            for key in dictt:
                result.append(key["id"])
        except:
            result = "No info"
        return result

class MainWindow:
    def __init__(self, window):
        self.allfiles = {}
        self.window = window
        self.window.title("Nbtanalizer")
        self.menu = tkinter.Menu(self.window)
        openitem = tkinter.Menu(self.menu)
        openitem.add_command(label="Open", command=self.openfile)
        self.menu.add_cascade(label="File", menu=openitem)
        self.uuidlabel = tkinter.Label(self.window, text="UUID : ")
        self.uuidlabel.grid(row=0, column=0, sticky="w")
        self.gamemodelabel = tkinter.Label(self.window, text="Gamemode : ")
        self.gamemodelabel.grid(row=1, column=0, sticky="w")
        self.xplabel = tkinter.Label(self.window, text="XP : ")
        self.xplabel.grid(row=2, column=0, sticky="w")
        self.inventorylabel = tkinter.Label(self.window, text="Inventory : ")
        self.inventorylabel.grid(row=3, column=0, sticky="w")
        self.lastdeathlabel = tkinter.Label(self.window, text="Last Death : ")
        self.lastdeathlabel.grid(row=4, column=0, sticky="w")
        self.effectlabel = tkinter.Label(self.window, text="Effects : ")
        self.effectlabel.grid(row=5, column=0, sticky="w")
        self.recipeslabel = tkinter.Label(self.window, text="Recipes : ")
        self.recipeslabel.grid(row=6, column=0, sticky="w")
        self.window.config(menu=self.menu)

    def openfile(self):
        file_path = filedialog.askopenfilename()
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        self.allfiles[file_name] = Player(file_path)
        self.uuidlabel.config(text=f"UUID : {str(self.allfiles[file_name].uuid)}")
        self.gamemodelabel.config(text=f"Gamemode : {str(self.allfiles[file_name].gamemode)}")
        self.xplabel.config(text=f"XP : {str(self.allfiles[file_name].xp)}")
        self.inventorylabel.config(text=f"Inventory : {len(self.allfiles[file_name].inventory)}")
        self.lastdeathlabel.config(text=f"Last Death : {str(self.allfiles[file_name].lastdeath)}")
        self.effectlabel.config(text=f"Effects : {str(self.allfiles[file_name].effects)}")
        self.recipeslabel.config(text=f"Recipes : {len(self.allfiles[file_name].recipes)}")




if __name__ == "__main__":
    root = tkinter.Tk()
    app = MainWindow(root)
    root.mainloop()