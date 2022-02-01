from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


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
    
    
