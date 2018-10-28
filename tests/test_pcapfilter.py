#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tests.utils import (
    PreloadedPcapFile,
    ReadablePcapWriter,
    assert_same_packet,
)
from tests.utils import tcp_packet  # noqa: F401

from pcapfilter.pcapfilter import run_filter


def test_pcap_in_out(cli_runner, tcp_packet):  # noqa: F811

    input_file_handler = PreloadedPcapFile()
    input_file_handler.preload(tcp_packet)

    output_file_handler = ReadablePcapWriter()

    retval = run_filter(
        module=None,
        _input=input_file_handler.get_file(),
        _output=output_file_handler.file_obj,
    )
    assert retval == 0
    output = next(output_file_handler.get_contents())
    assert_same_packet(tcp_packet, output)
