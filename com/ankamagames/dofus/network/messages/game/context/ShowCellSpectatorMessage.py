from com.ankamagames.dofus.network.messages.game.context.ShowCellMessage import ShowCellMessage


class ShowCellSpectatorMessage(ShowCellMessage):
    protocolId = 6320
    playerName:str
    
