
from mimetypes import init


print ("Welcome to Simon's Autism Simulator")

""" class city:
    def __init__(self, name, node, extractor, stockpile, consumption, manpower, modifier, 
                edicts, provincemod, countrymodifier, factories):
        self.name = name
        self.factories = factories
        self.node = node
        self.extractor = extractor
        self.stockpile = stockpile
"""
# Object that works the value modifications in the economy tab. MORE RESEARCH NECESSARY
class econMods:
    def __init__(self, city, key, val):
        self.city = city
        self.key = key
        self.val = val

        city[key] = val

class colonize:
    def __init__(self, playerNation, city):
        self.city = city
        self.playerNation = playerNation

        playerNation.append[city]


# Dictionary list to fill for each city. Work for Simon. The Key is the unchanging part like 'coalStock' and the value like how much coal is in there.
# Template City = ['actuallyFillThisInFirst : Value']
York = ['Key : Value', 'Key2 : Value2']
Cambridge = ['Key : Value', 'Key2 : Value2', 'Key3 : Value3']


# List of dictionary lists for each faction
playerNation = [York, Cambridge]
