import pyshark as ps
from src.message.app_message import parseMsgs
from src.message.message import Message
from src.socket.buffer import Buffer
from src.deserializer.exchange_craft_results import deserialize_4294, deserialize_4738
import socket


#capture = ps.LiveCapture('Ethernet', bpf_filter='tcp port 5555 and len > 66', output_file="testout.cap")

def sniffLive():
    capture = ps.LiveCapture('Ethernet', bpf_filter='tcp port 5555 and len > 66', output_file="testout.cap")
    capture.sniff(timeout=5)



def sniffFile():
    capture = ps.FileCapture("testout.cap")
    for packet in capture:
        print()
        if packet.ip.src == socket.gethostbyname(socket.gethostname()):
            continue
        data = ''.join(packet.tcp.payload.split(":"))
        messages = parseMsgs(Buffer.from_str(data))
        for message in messages:
            print(message)
            if message.id == 4294:

                print(deserialize_4294(message.msg))
            elif message.id == 4738:
                print(deserialize_4738(message.msg))



sniffFile()
