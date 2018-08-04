import socket
import time
import sys
from ctypes import *
import struct


class Machine:
    services = {"ftp":21, "ssh":22, "smtp":25, "http":80}
    address = ""
    Name = ""

    def __init__(self, IP_addr, name):
        self.address = IP_addr
        self.Name = name


class IP(Structure):
    _fields_ = [
        ("ihl",              c_byte, 4),
        ("version",         c_ubyte, 4),
        ("tos",             c_ubyte),
        ("len",             c_ushort),
        ("id",              c_ushort),
        ("offset",          c_ushort),
        ("ttl",             c_ubyte),
        ("protocol",        c_ubyte),
        ("sum",             c_ushort),
        ("src",             c_ulong),
        ("dst",             c_ulong)
    ]

    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        # Map Protocol Names to Numbers
        self.protocol_mapping = {1:"ICMP", 6:"TCP", 17:"UDP"}
        # make IP Address Human Readable
        self.src_address = socket.inet_ntoa((struct.pack("<L", self.src)))
        self.dst_address = socket.inet_ntoa((struct.pack("<L", self.dst)))

        try:
            self.protocol_mapping = self.protocol_mapping[self.protocol]
        except:
            self.protocol = str(self.protocol)


class ICMP(Structure):
    _fields_ = [
        ("type",            c_ubyte),
        ("code",            c_ubyte),
        ("checksum",        c_ushort),
        ("unused",          c_ushort),
        ("next_hop_mtu",    c_ushort)
    ]

    def __new__(self, socket_buff):
        return self.from_buffer_copy(socket_buff)

    def __init__(self, socket_buff):
        pass


def create_sniffer(host):
    start = time.time()
    socket_protocol = socket.IPPROTO_ICMP
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((host, 0))
    # Get IP Headers
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    smell = ""
    try:
        while True:
            # Take in packet
            smell = sniffer.recvfrom(65565)[0]
            ip_header = IP(smell[0:32])
            print "Protocol: %s %s -> %s" % (ip_header.protocol,
                                            ip_header.src_address,
                                            ip_header.dst_address)
            if ip_header.protocol == "ICMP":
                offset = ip_header.protocol_mapping["ihl"]*4
                # create ICMP structure
                buff = smell[offset:offset + sizeof(ICMP)]
                icmp_header = ICMP(buff)

                print "ICMP -> Type: %d Code: %d " % (icmp_header.type,icmp_header.cpde)
    except KeyboardInterrupt:
        stop = time.time()
        print "[ "+str(stop-start)+"s Elapsed]"


def usage():
    print "* - - -|//|_INCORRECT_USAGE_|\\\\| - - -*"
    print "* python <ip address> -Mode             *"
    print "* Ex: python 10.10.0.3 -sniff           *"
    print "*---------------------------------------*"


def read_configuration(config_filename):
    hostname = ""
    ip = ""
    config_file = open(config_filename, 'r')
    ln = 0
    unused = 0
    for line in config_file:
        if ln == 0:
            hostname = line.replace("\n","")
        else:
            try:
                ip = line.split("inet ")[1].split(" netmask")[0]
            except:
              unused += 1
        ln += 1
    return hostname, ip


def main():
    if len(sys.argv) < 2:
        usage()
    else:
        hostname, ip = read_configuration(sys.argv[1])
        create_sniffer(ip)
        computer = Machine(hostname, ip)


if __name__ == "__main__":
    main()
