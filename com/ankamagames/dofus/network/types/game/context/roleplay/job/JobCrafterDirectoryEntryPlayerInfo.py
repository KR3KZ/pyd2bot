from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


@dataclass
class JobCrafterDirectoryEntryPlayerInfo(NetworkMessage):
    playerId:int
    playerName:str
    alignmentSide:int
    breed:int
    sex:bool
    isInWorkshop:bool
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    canCraftLegendary:bool
    status:PlayerStatus
    
    
    def __post_init__(self):
        super().__init__()
    