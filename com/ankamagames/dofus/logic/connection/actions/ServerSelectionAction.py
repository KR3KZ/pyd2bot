from sys import argv
from com.ankamagames.dofus.misc.utils.AbstractAction import AbstractAction
from com.ankamagames.jerakine.handlers.Action import Action 


class ServerSelectionAction(AbstractAction, Action):
   
   serverId:int
   
   def __init__(self, *params):
      super().__init__(*params)
   
   def create(self, serverId:int) -> 'ServerSelectionAction':
      a = ServerSelectionAction(argv)
      a.serverId = serverId
      return a
