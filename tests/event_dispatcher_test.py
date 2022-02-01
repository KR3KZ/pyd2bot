from com.ankamagames.dofus.network.messages.common.basic.BasicPongMessage import BasicPongMessage
from com.ankamagames.jerakine.network.NetworkSentEvent import NetworkSentEvent
from com.ankamagames.jerakine.events.BasicEvent import BasicEvent
from com.ankamagames.jerakine.events.IOErrorEvent import IOErrorEvent
from whistle import EventDispatcher, Event




dispatcher = EventDispatcher()
def handler(event:NetworkSentEvent):
    if event.name == BasicEvent.CONNECT:
        print("Connected to the server")
    elif event.name == BasicEvent.CLOSE:
        print("Disconnected from the server")
    elif event.name == NetworkSentEvent.EVENT_SENT:
        print("Message sent: {}".format(event.message))


msg = BasicPongMessage()
dispatcher.add_listener(NetworkSentEvent.EVENT_SENT, handler)
dispatcher.add_listener(BasicEvent.CONNECT, handler)
dispatcher.dispatch(NetworkSentEvent.EVENT_SENT, NetworkSentEvent(msg))
dispatcher.dispatch(BasicEvent.CONNECT)
