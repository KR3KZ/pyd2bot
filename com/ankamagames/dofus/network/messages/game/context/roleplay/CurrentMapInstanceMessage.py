from com.ankamagames.dofus.network.messages.game.context.roleplay.CurrentMapMessage import CurrentMapMessage


class CurrentMapInstanceMessage(CurrentMapMessage):
    protocolId = 7422
    instantiatedMapId:int
    
    
