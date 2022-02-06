     def getLookDirection4DiagExactByCoord(self, param1:int, param2:int, param3:int, param4:int) -> int:
         if not MapTools.isValidCoord(param1,param2) or not MapTools.isValidCoord(param3,param4):
             return -1
         _loc5_ = param3 - param1
         _loc6_ = param4 - param2
         if _loc5_ == -_loc6_:
             if _loc5_ < 0:
                 return 6
             return 2
         if _loc5_ == _loc6_:
             if _loc5_ < 0:
                 return 4
             return 0
         return -1
