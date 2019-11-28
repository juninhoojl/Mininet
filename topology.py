#!/usr/bin/python

"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""

from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
# Talvez essa de baixo nao seja necessaria
from mininet.topolib import TreeTopo


def emptyNet():

    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller )

    #c = RemoteController( 'c', ip='127.0.0.1', port=6633 )
    info( '*** Adding controller\n' )
    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633 )

    #net.addController( 'c' )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='169.0.10.3' )
    h2 = net.addHost( 'h2', ip='169.0.10.4' )
    h3 = net.addHost( 'h3', ip='169.0.10.5' )
    h4 = net.addHost( 'h4', ip='169.0.10.6' )

    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    s3 = net.addSwitch( 's3' )

    info( '*** Creating links\n' )
    net.addLink( h2, s2, bw='1Gbps', delay='1ms' )
    net.addLink( h1, s2, bw='1Gbps', delay='1ms' )
    net.addLink( h3, s3, bw='1Gbps', delay='1ms' )
    net.addLink( h4, s3, bw='1Gbps', delay='1ms' )
    net.addLink( s2, s1, bw='100Mbps', delay='100ms' )
    net.addLink( s3, s1, bw='100Mbps', delay='100ms' )

    info( '*** Starting network\n')
    net.build()
    c0.start()
    s1.start( [c0] )
    s2.start( [c0] )
    s3.start( [c0] )

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
