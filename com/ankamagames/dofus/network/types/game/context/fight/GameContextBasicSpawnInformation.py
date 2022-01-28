



from com.ankamagames.dofus.network.types.game.context.GameContextActorPositionInformations import GameContextActorPositionInformations


class GameContextBasicSpawnInformation:
   teamId:int = 2
   alive:bool = False
   informations:GameContextActorPositionInformations
   
   def __init__(self):
      self.informations = GameContextActorPositionInformations()
      super().__init__()
   
   def initGameContextBasicSpawnInformation(self, teamId:int = 2, alive:bool = False, informations:GameContextActorPositionInformations = None) -> 'GameContextBasicSpawnInformation':
      self.teamId = teamId
      self.alive = alive
      self.informations = informations
      return self
   
   def reset(self) -> None:
      self.teamId = 2
      self.alive = False
      self.informations = GameContextActorPositionInformations()
