#!/usr/bin/env python


from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    # Make socket
    transport = TSocket.TSocket("localhost", 63572)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Calculator.Client(protocol)

    # Connect!
    transport.open()

    client.ping()
    print("ping()")

    sum_ = client.add(1, 1)
    print("1+1=%d" % sum_)

    work = Work()

    work.op = Operation.DIVIDE
    work.num1 = 1
    work.num2 = 0

    try:
        quotient = client.calculate(1, work)
        print("Whoa? You know how to divide by zero?")
        print("FYI the answer is %d" % quotient)
    except InvalidOperation as e:
        print("InvalidOperation: %r" % e)

    work.op = Operation.SUBTRACT
    work.num1 = 15
    work.num2 = 10

    diff = client.calculate(1, work)
    print("15-10=%d" % diff)

    log = client.getStruct(1)
    print("Check log: %s" % log.value)

    # Close!
    transport.close()


if __name__ == "__main__":
    try:
        main()
    except Thrift.TException as tx:
        print("%s" % tx.message)
