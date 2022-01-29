from enum import Enum


class ConnectionType(Enum):
   
   DISCONNECTED:str = "disconnected"
   
   TO_LOGIN_SERVER:str = "serverloggerin"
   
   TO_GAME_SERVER:str = "server_game"
   
   TO_KOLI_SERVER:str = "server_koli"
   
   TO_ALL_SERVERS:str = "all"
      
   
   def __init__(self):
      super().__init__()
