from os import path
from uuid import uuid4 as uuid
from pprint import pformat
from com.ankamagames.jerakine.logger.Logger import Logger
import asyncio
import threading
from wdom.document import get_document, set_app
from wdom.server import start_server, start
from wdom.themes import bootstrap3
from wdom.themes.bootstrap3 import *
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from pyd2bot.network.message import Message
from pyd2bot.network.sniffer import DofusSniffer
logger = logging.getLogger("labot")


class SnifferUI(Div):
    def __init__(self, capture_file=None, *args, **kwargs):
        logger.debug(
            f"Initializing sniffer UI with capture file {capture_file}"
        )
        
        self.capture_file = capture_file
        self.stopfun = None
        super().__init__(*args, **kwargs)

        self.append(H1("LaBot sniffer", style="text-align: center;"))

        self.button_wrapper = Div(parent=self)

        startbutton = SuccessButton("start", parent=self.button_wrapper)
        startbutton.addEventListener("click", self.start)

        stopbutton = DangerButton("stop", parent=self.button_wrapper)
        stopbutton.addEventListener("click", self.stop)

        clearbutton = InfoButton("clear", parent=self.button_wrapper)
        clearbutton.addEventListener("click", self.clear)
        self.info = P("Press start", parent=self.button_wrapper)

        self.msgtable = MsgTable(parent=self)
        self.dofusSniffer = DofusSniffer(self.msgtable.appendMsg)

    def start(self, event=None):
        if not self.dofusSniffer.running:
            self.dofusSniffer.start()
            self.info.textContent = "Sniffer started"
        else:
            self.info.textContent = "Sniffer already started"

    def stop(self, event=None):
        logger.debug("Stop button clicked...")
        if self.dofusSniffer.running:
            self.dofusSniffer.stop()
            self.info.textContent = "Sniffer stopped"
        else:
            self.info.textContent = "Sniffer already stopped"

    def clear(self, event):
        self.msgtable.clear(event)


class MsgTable(Table):
    def __init__(self, *args, **kwargs):
        logger.debug("Initializing Message Table")

        super().__init__(class_="table-hover", *args, **kwargs)
        self.thead = Thead(parent=self)
        self.tr1 = Tr(parent=self.thead)
        self.tr1.append(
            Th("Count", class_="col-sm-1"),
            Th("Name", class_="col-sm-3"),
            Th("id", class_="col-sm-1"),
            Th("length", class_="col-sm-1"),
            Th("contents"),
        )
        self.tbody = Tbody(parent=self)

    def appendMsg(self, msg):
        logger.debug("Adding message to table")
        MsgView(msg, parent=self.tbody)

    def clear(self, msg):
        self.tbody.remove()
        self.tbody = Tbody(parent=self)


class MsgView(Tr):
    
    def __init__(self, msg: Message, *args, **kwargs):
        if msg.from_client:
            super().__init__(class_="success", *args, **kwargs)
        else:
            super().__init__(class_="info", *args, **kwargs)
        msg = msg.deserialize()
        logger.debug("Initializing UI Msg: {}".format(msg.__class__.__name__))
        self.msg = msg
        self.addEventListener("click", self.switch_view)
        self.contents = Td("", style="white-space: pre;")
        self.append(
            Td(str(msg._instance_id)),
            Td(msg.__class__.__name__),
            Td(str(msg.getMessageId())),
            Td(str("")),
            self.contents,
        )

    def switch_view(self, event):
        logger.debug("Changing view for message.")
        if not self.contents.textContent:
            self.contents.textContent = pformat(self.msg.to_json())
        else:
            self.contents.textContent = ""


document = get_document()
document.register_theme(bootstrap3)
document.add_jsfile("https://unpkg.com/sticky-table-headers")


def init(capture_file=None):
    logger.debug("Initializing UI...")
    global ui
    ui = SnifferUI(capture_file=capture_file)
    set_app(ui)
    logger.debug("Finished initializing UI.")


def loop_in_thread(loop):
    logger.debug("Starting loop: `{}` in thread".format(loop))
    asyncio.set_event_loop(loop)
    start()
    logger.debug("Started loop in thread")


def async_start():
    logger.debug("Starting sniffer asynchronously...")
    loop = asyncio.get_event_loop()
    t = threading.Thread(target=loop_in_thread, args=(loop,))
    t.start()
    logger.debug("Started sniffer in thread: {}".format(t))


if __name__ == "__main__":
    init(None)
    async_start()
