class MapLoadingFailedMessage(MapMessage):
   
   NO_FILE:int = 0
   
   CLIENT_SHUTDOWN:int = 1
   
   
   errorReason:int
   
   def __init__(self):
      super().__init__()
