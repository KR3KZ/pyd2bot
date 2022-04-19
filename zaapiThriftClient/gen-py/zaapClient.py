#!/usr/bin/env python


from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import zaap.Zaapi as Zaapi


def main():
    # Make socket
    transport = TSocket.TSocket("localhost", 26116)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Zaapi.Client(protocol)

    # Connect!
    transport.open()

    # client.connect(
    #     "dofus",
    #     "main",
    #     1,
    #     "968d27b034334856f33573bf2f0c28f8",
    # )
    client.auth_getGameToken("498327489327498327", 1)
    # Close!
    transport.close()


if __name__ == "__main__":
    try:
        main()
    except Thrift.TException as tx:
        print(str(tx))
