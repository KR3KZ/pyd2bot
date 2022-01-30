from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorBasicInformations import TaxCollectorBasicInformations


class TaxCollectorMovementMessage(NetworkMessage):
    protocolId = 4589
    movementType:int
    basicInfos:TaxCollectorBasicInformations
    playerId:float
    playerName:str
    
