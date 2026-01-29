import nbtlib
import json

data = nbtlib.load('player.dat')
data_dict = dict(data)

class Player():
    def __init__(self):
        data = nbtlib.load('player.dat')
        data_dict = dict(data)
        self.uuid = data_dict['UUID']
        self.xp = data_dict['XpTotal']
        self.effects = self.effect_parse(data_dict)
        self.gamemode = data_dict['playerGameType']
        self.inventory = self.inventy_parse(data_dict)
        self.lastdeath = [data_dict['LastDeathLocation']['pos'], data_dict['LastDeathLocation']['dimension']]
        self.resipes = data_dict['recipeBook']['recipes']
        print(self.uuid)
        print(self.xp)
        print(self.effects)
        print(self.gamemode)
        print(self.inventory)
        print(self.lastdeath)
        #print(self.resipes)

    def effect_parse(self, data_dict):
        dictt = data_dict['active_effects']
        result = list()
        for key in dictt:
            result.append(key["id"])
        return result

    def inventy_parse(self, data_dict):
        dictt = data_dict['Inventory']
        result = list()
        for key in dictt:
            result.append(key["id"])
        return result



Player()