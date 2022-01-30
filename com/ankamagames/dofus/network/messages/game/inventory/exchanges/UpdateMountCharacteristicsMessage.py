from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.mount.UpdateMountCharacteristic import UpdateMountCharacteristic


class UpdateMountCharacteristicsMessage(INetworkMessage):
    protocolId = 9937
    rideId:int
    boostToUpdateList:UpdateMountCharacteristic
    
    
