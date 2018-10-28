import pytest
from io import BytesIO
from scapy.all import Ether, IP, TCP, UDP, PcapNgReader, PcapWriter


class PreloadedPcapFile:
    """
    Generates an in-memory file (io.BytesIO) that will be preloaded
    with a set of packets defined either in __init__ or using the
    .preload() method. To get the file
    """

    def __init__(self, preloaded_packets=None, writer_class=PcapWriter):
        self._writer_class = writer_class
        self._preloaded_packets = preloaded_packets or []
        self.file_obj = BytesIO()
        self._writer = None

    def get_file(self):
        if self._writer is None:
            self._writer = self._writer_class(self.file_obj)
            for packet in self._preloaded_packets:
                self._writer.write(packet)
            self.file_obj.seek(0)
        return self.file_obj

    def preload(self, packet):
        if self._writer:
            raise ValueError("Cannot write packet after the file has been generated")
        self._preloaded_packets.append(packet)


class ReadablePcapWriter:
    def __init__(self):
        self.file_obj = BytesIO()

    def __getattr__(self, name):
        return object.__getattribute__(self.file_obj, name)

    def get_contents(self):
        self.file_obj.seek(0)
        reader = PcapNgReader(self.file_obj)
        for pkg in reader:
            yield pkg


def assert_same_packet(p1, p2, layers=None):
    if not layers:
        layers = (Ether, IP, TCP, UDP)
    for layer in layers:
        if layer in p1:
            if layer not in p2:
                raise AssertionError(
                    "{} present in 1st packet but not in 2nd".format(layer)
                )
            assert bytes(p1[layer]) == bytes(p2[layer])


@pytest.fixture
def tcp_packet():
    """Example packet"""
    return Ether() / IP() / TCP()
