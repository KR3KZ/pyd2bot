from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


class JobCrafterDirectoryEntryPlayerInfo(NetworkMessage):
    protocolId = 4905
    playerId:float
    playerName:str
    alignmentSide:int
    breed:int
    sex:bool
    isInWorkshop:bool
    worldX:int
    worldY:int
    mapId:float
    subAreaId:int
    canCraftLegendary:bool
    status:PlayerStatus
    
