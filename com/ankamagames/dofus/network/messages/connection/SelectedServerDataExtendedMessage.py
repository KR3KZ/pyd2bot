from com.ankamagames.dofus.network.messages.connection.SelectedServerDataMessage import SelectedServerDataMessage
from com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations


class SelectedServerDataExtendedMessage(SelectedServerDataMessage):
    protocolId = 2850
    servers:GameServerInformations
    
