from com.ankamagames.dofus.network.messages.game.ui.ClientUIOpenedMessage import ClientUIOpenedMessage


class ClientUIOpenedByObjectMessage(ClientUIOpenedMessage):
    protocolId = 8823
    uid:int
    
    
