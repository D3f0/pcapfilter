===========
pcapfilter
===========


.. image:: https://img.shields.io/pypi/v/pcapfilter.svg
        :target: https://pypi.python.org/pypi/pcapfilter

.. image:: https://img.shields.io/travis/D3f0/pcapfilter.svg
        :target: https://travis-ci.org/D3f0/pcapfilter

.. image:: https://readthedocs.org/projects/pcapfilter/badge/?version=latest
        :target: https://pcapfilter.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/D3f0/pcapfilter/shield.svg
     :target: https://pyup.io/repos/github/D3f0/pcapfilter/
     :alt: Updates



Python package for packet filtering and manipulation using scapy

.. image:: ./imgs/pcapfilter.svg


* Free software: MIT license
* Documentation: https://pcapfilter.readthedocs.io.


`pcapfilter` introduction
--------------------------

This program takes a network package capture from a file or a sniffer, such as
tcpdump, in pcap format, as standar input. Then it aplies a function to it that can filter or
manipulate each packet. Finally it outputs the packet to the standard output so it can
be stored in a file, viewed in a tool like wireshark or tshark, or sent to some other program.

If any of the previous terms sound alien to you, you can check :doc:`this doc <about_package_capture>`

Reason of existance
-------------------

This tool came in response to the need for inspection and filtering of network traffic.
Which network traffic? Well, it's hard to argue that we live in an age ruled by
communications and we, or more specifically our devices generate a lot of network traffic.

This problem has two parts. The first one is being able to analyze this traffic. It's
quite hard to do any monitoring on factory firmwares of most routers you can get of the
shelf. This can big a big concern given the amount of smart devices consumers are able
to hook up to their networks.
Fortunately this problem can be mitigated for a set of devices using alternative firmwares.
OpenWRT/LEDE is probably the most advanced Open Source firmware for you router, and works
very well with `pcapfilter`. Once you've flashed your router with OpenWRT (or any other
Linux based firmare) you'll gain ssh access and depending on your platform, the `tcpdump`
command line tool (if `opkg` is available in your router, this is as simple as running
the command `opkg install tcpdump`.

The second part of the porblem is analyze the dump that router provides. There are
several tools to which you can pipe your captued traffic such as `tshark` or `wireshark`
that will display in real time the observed packets. `pcapfilter` sits between this
traffic and your user interace all. If you're familiar with ssh and tcpdump, the follwoing
line would illustrate the use case::

    ssh router "tcpdump -i eth1.2 -i br-lan -s0 -w - " | wireshark -k -i -

The second part is making something useful with the captured traffic, and in particuarly
using the Python programming language.
Scapy received a stream of captured traffic in the standard `pcap` format and applies a
python function. This function can let it go through, modify any of the layers Scapy is
capable to interact with and finally
To circumvent the problem of inspecting traffic in a home router, there are alternative,
more secure and mantained firmwares such as OpenWRT that give the power of a Linux enabled
device to your network.


Features
--------

* Define your filters in Python
* Pipe your output to Wireshark or TShark for visualization
* Manipulate the payloads using Python's 3 byte regxes
* Save results to pcap files
* Work in progress *live reload* of your filter file

Credits
-------

This project relies on the power of Scapy_ for either filtering or payload modification.
This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Scapy: https://scapy.net/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
