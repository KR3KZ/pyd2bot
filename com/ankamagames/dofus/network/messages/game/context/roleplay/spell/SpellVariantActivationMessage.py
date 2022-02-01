from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SpellVariantActivationMessage(NetworkMessage):
    spellId:int
    result:bool
    
    
