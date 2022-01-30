from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockContentInformations import PaddockContentInformations


class GuildPaddockBoughtMessage(INetworkMessage):
    protocolId = 6217
    paddockInfo:PaddockContentInformations
    
    
