

from pyd2bot.gameData.IdAccessors import IdAccessors

   
MODULE:str = "SpellStates"

id:int

nameId:int

preventsSpellCast:bool

preventsFight:bool

isSilent:bool

cantDealDamage:bool

invulnerable:bool

incurable:bool

cantBeMoved:bool

cantBePushed:bool

cantSwitchPosition:bool

effectsIds:list[int]

icon:str = ""

iconVisibilityMask:int

invulnerableMelee:bool

invulnerableRange:bool

cantTackle:bool

cantBeTackled:bool

displayTurnRemaining:bool

def getSpellStateById(id:int):
   return GameData.getObject(MODULE, id)

def getSpellStates() -> list:
   return GameData.getObjects(MODULE)

idAccessors:IdAccessors = IdAccessors(getSpellStateById, getSpellStates)