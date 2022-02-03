from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ConsoleCommandsListMessage(NetworkMessage):
    aliases:list[str]
    args:list[str]
    descriptions:list[str]
    

    def init(self, aliases:list[str], args:list[str], descriptions:list[str]):
        self.aliases = aliases
        self.args = args
        self.descriptions = descriptions
        
        super().__init__()
    
    