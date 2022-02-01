from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractClientMessage import ChatAbstractClientMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


class ChatClientPrivateMessage(ChatAbstractClientMessage):
    receiver:AbstractPlayerSearchInformation
    
    
