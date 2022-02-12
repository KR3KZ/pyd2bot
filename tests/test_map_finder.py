



from com.ankamagames.jerakine.resources.loaders.MapLoader import MapLoader


if __name__ == '__main__':
    sourceMapId = 185862146
    
    srcMap = MapLoader().load(sourceMapId)
    srcMap.printGrid()
    print(len(srcMap.zones))
    
    