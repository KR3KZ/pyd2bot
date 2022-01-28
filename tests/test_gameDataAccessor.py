


from time import perf_counter
from com.ankamagames.dofus.datacenter.monsters.monster import Monster
from com.ankamagames.jerakine.data.gameDataFileAccessor import GameDataFileAccessor


if __name__ == '__main__':
   
   f = r"C:\Users\majdoub\AppData\Local\Ankama\Dofus\data\common\Monsters.d2o"


   a = GameDataFileAccessor()

   a.init(f)
   t = perf_counter()
   monster:Monster = a.getObject("Monsters", 56)
   print(perf_counter() - t)
