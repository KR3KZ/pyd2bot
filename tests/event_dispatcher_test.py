from com.ankamagames.jerakine.network.events.iOErrorEvent import IOErrorEvent
from whistle import EventDispatcher, Event



dispatcher = EventDispatcher()
#Add a listener to react to events
def on_spectacle_starts(event):
    print('Please turn down your phones!')

dispatcher.add_listener(IOErrorEvent.IO_ERROR, on_spectacle_starts)
#Dispatch it!
dispatcher.dispatch(IOErrorEvent.IO_ERROR)