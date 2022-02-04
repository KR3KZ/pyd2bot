from sys import argv
from com.ankamagames.dofus.misc.utils.AbstractAction import AbstractAction
from com.ankamagames.jerakine.handlers.messages.Action import Action

class CharacterSelectionAction(AbstractAction, Action):
   
   
   characterId:float
   
   btutoriel:bool
   
   def __init__(self, params:list = None):
      super().__init__(params)
   
   def create(self, characterId:float, btutoriel:bool) -> 'CharacterSelectionAction':
      a:CharacterSelectionAction = CharacterSelectionAction(argv)
      a.characterId = characterId
      a.btutoriel = btutoriel
      return a
