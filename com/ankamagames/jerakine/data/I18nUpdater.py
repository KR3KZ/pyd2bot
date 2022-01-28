                              
import pathlib
from pyd2bot.jerakine.data.I18nFileAccessor import I18nFileAccessor
from pyd2bot.jerakine import JerakineConstants
from pyd2bot.jerakine.managers import StoreDataManager


class I18nUpdater(DataUpdateManager):      
   _versions = []
   _language:str
   _files:list = []

   
   def initI18n(self, language:str, metaFileListe:Uri, clearAll:bool = False) -> None:
      self._language = language
      super().init(metaFileListe, clearAll)
   
   def checkFileVersion(self, sFileName:str, sVersion:str) -> bool:
      return False
   
   def clear(self) -> None:
      self.fileaccessor.close()
   
   def onLoaded(self, file_path:str, version, ftype) -> None:
      meta:LangMetaData = None
      uri:pathlib.Path = None
      realCount:int = 0
      file = None

      if ftype =="d2i":
            self.fileaccessor = I18nFileAccessor(file_path)
            self._versions[file_path] = version
            StoreDataManager.setData(JerakineConstants.DATASTORE_FILES_INFO, _storeKey, self._versions)
            dispatchEvent(LangFileEvent(LangFileEvent.COMPLETE, False, False, file_path))
            _dataFilesLoaded = True
            _loadedFileCount += 1
            break

      elif ftype == "meta":
            meta = LangMetaData.fromXml(e.resource, file_path.uri, self.checkFileVersion())
            realCount = 0
            for file in meta.clearFile:
               if file.find("_" + self._language) != -1:
                  uri = pathlib.Path(file_path) + "/" + file
                  uri.tag = {
                     "version":meta.clearFile[file],
                     "file": file_path.split(".")[0] + "." + file
                  }
                  self._files.append(uri)
                  realCount += 1
            if realCount:
               _loader.load(_files)
            else:
               dispatchEvent(Event(Event.COMPLETE))
            break
      else:
         super().onLoaded(e)
