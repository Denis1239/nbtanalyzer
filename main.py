import nbtlib
import json

data = nbtlib.load('player.dat')
data_dict = dict(data)

class Player:
    def __init__(self, datfile):
        data = nbtlib.load(datfile)
        data_dict = dict(data)
        self.uuid = self.uuid_parse(data_dict)
        self.xp = self.xp_parse(data_dict)
        self.effects = self.effect_parse(data_dict)
        self.gamemode = self.gamemode_parse(data_dict)
        self.inventory = self.inventory_parse(data_dict)
        self.lastdeath = self.lastdeath_parse(data_dict)
        self.recipes = self.recipes_parse(data_dict)

    def recipes_parse(self, data_dict):
        try:
            recipe = data_dict['recipeBook']['recipe']
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
            xp = data_dict['XpTotal']
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
