#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='192.168.100.0/24')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')

    slan1 = net.addSwitch('slan1', cls=OVSKernelSwitch, failMode='standalone')
    slan2 = net.addSwitch('slan2', cls=OVSKernelSwitch, failMode='standalone')
    slan3 = net.addSwitch('slan3', cls=OVSKernelSwitch, failMode='standalone')
    slan4 = net.addSwitch('slan4', cls=OVSKernelSwitch, failMode='standalone')
    slan5 = net.addSwitch('slan5', cls=OVSKernelSwitch, failMode='standalone')
    slan6 = net.addSwitch('slan6', cls=OVSKernelSwitch, failMode='standalone')

    swan1 = net.addSwitch('swan1', cls=OVSKernelSwitch, failMode='standalone')
    swan2 = net.addSwitch('swan2', cls=OVSKernelSwitch, failMode='standalone')
    swan3 = net.addSwitch('swan3', cls=OVSKernelSwitch, failMode='standalone')
    swan4 = net.addSwitch('swan4', cls=OVSKernelSwitch, failMode='standalone')
    swan5 = net.addSwitch('swan5', cls=OVSKernelSwitch, failMode='standalone')
    swan6 = net.addSwitch('swan6', cls=OVSKernelSwitch, failMode='standalone')

    info( '*** Add hosts\n')
    rcentral = net.addHost('rcentral', cls=Node, ip='')
    rcentral.cmd('sysctl -w net.ipv4.ip_forward=1')

    rsuc1 = net.addHost('rsuc1', cls=Node, ip='')
    rsuc2 = net.addHost('rsuc2', cls=Node, ip='')
    rsuc3 = net.addHost('rsuc3', cls=Node, ip='')
    rsuc4 = net.addHost('rsuc4', cls=Node, ip='')
    rsuc5 = net.addHost('rsuc5', cls=Node, ip='')
    rsuc6 = net.addHost('rsuc6', cls=Node, ip='')

    h1_suc1 = net.addHost('h1_suc1', cls=Host, ip='10.0.1.254/24', defaultRoute=None)
    h1_suc2 = net.addHost('h1_suc2', cls=Host, ip='10.0.2.254/24', defaultRoute=None)
    h1_suc3 = net.addHost('h1_suc3', cls=Host, ip='10.0.3.254/24', defaultRoute=None)
    h1_suc4 = net.addHost('h1_suc4', cls=Host, ip='10.0.4.254/24', defaultRoute=None)
    h1_suc5 = net.addHost('h1_suc5', cls=Host, ip='10.0.5.254/24', defaultRoute=None)
    h1_suc6 = net.addHost('h1_suc6', cls=Host, ip='10.0.6.254/24', defaultRoute=None)

    rsuc1.cmd('sysctl -w net.ipv4.ip_forward=1')
    rsuc2.cmd('sysctl -w net.ipv4.ip_forward=1')
    rsuc3.cmd('sysctl -w net.ipv4.ip_forward=1')
    rsuc4.cmd('sysctl -w net.ipv4.ip_forward=1')
    rsuc5.cmd('sysctl -w net.ipv4.ip_forward=1')
    rsuc6.cmd('sysctl -w net.ipv4.ip_forward=1')


    info( '*** Add links\n')

    net.addLink(h1_suc1,slan1)
    net.addLink(rsuc1,slan1, intfName1='rsuc1-eth0', params1={ 'ip' : '10.0.1.1/24'})
    net.addLink(rsuc1,swan1, intfName1='rsuc1-eth1', params1={ 'ip' : '192.168.100.1/29'})
    net.addLink(rcentral,swan1, intfName1='rcentral-eth0', params1={ 'ip' : '192.168.100.6/29'})

    net.addLink(h1_suc2,slan2)
    net.addLink(rsuc2,slan2, intfName1='rsuc2-eth0', params1={ 'ip' : '10.0.2.1/24'})
    net.addLink(rsuc2,swan2, intfName1='rsuc2-eth1', params1={ 'ip' : '192.168.100.9/29'})
    net.addLink(rcentral,swan2, intfName1='rcentral-eth1', params1={ 'ip' : '192.168.100.14/29'})

    net.addLink(h1_suc3,slan3)
    net.addLink(rsuc3,slan3, intfName1='rsuc3-eth0', params1={ 'ip' : '10.0.3.1/24'})
    net.addLink(rsuc3,swan3, intfName1='rsuc3-eth1', params1={ 'ip' : '192.168.100.17/29'})
    net.addLink(rcentral,swan3, intfName1='rcentral-eth2', params1={ 'ip' : '192.168.100.22/29'})

    net.addLink(h1_suc4,slan4)
    net.addLink(rsuc4,slan4, intfName1='rsuc4-eth0', params1={ 'ip' : '10.0.4.1/24'})
    net.addLink(rsuc4,swan4, intfName1='rsuc4-eth1', params1={ 'ip' : '192.168.100.25/29'})
    net.addLink(rcentral,swan4, intfName1='rcentral-eth3', params1={ 'ip' : '192.168.100.30/29'})

    net.addLink(h1_suc5,slan5)
    net.addLink(rsuc5,slan5, intfName1='rsuc5-eth0', params1={ 'ip' : '10.0.5.1/24'})
    net.addLink(rsuc5,swan5, intfName1='rsuc5-eth1', params1={ 'ip' : '192.168.100.33/29'})
    net.addLink(rcentral,swan5, intfName1='rcentral-eth4', params1={ 'ip' : '192.168.100.38/29'})

    net.addLink(h1_suc6,slan6)
    net.addLink(rsuc6,slan6, intfName1='rsuc6-eth0', params1={ 'ip' : '10.0.6.1/24'})
    net.addLink(rsuc6,swan6, intfName1='rsuc6-eth1', params1={ 'ip' : '192.168.100.41/29'})
    net.addLink(rcentral,swan6, intfName1='rcentral-eth5', params1={ 'ip' : '192.168.100.46/29'})

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('slan1').start([])
    net.get('slan2').start([])
    net.get('slan3').start([])
    net.get('slan4').start([])
    net.get('slan5').start([])
    net.get('slan6').start([])

    net.get('swan1').start([])
    net.get('swan2').start([])
    net.get('swan3').start([])
    net.get('swan4').start([])
    net.get('swan5').start([])
    net.get('swan6').start([])

    h1_suc1.cmd("ip route add 0.0.0.0/0 via 10.0.1.1")
    h1_suc2.cmd("ip route add 0.0.0.0/0 via 10.0.2.1")
    h1_suc3.cmd("ip route add 0.0.0.0/0 via 10.0.3.1")
    h1_suc4.cmd("ip route add 0.0.0.0/0 via 10.0.4.1")
    h1_suc5.cmd("ip route add 0.0.0.0/0 via 10.0.5.1")
    h1_suc6.cmd("ip route add 0.0.0.0/0 via 10.0.6.1")

    rcentral.cmd("ip ro add 10.0.1.0/24 via 192.168.100.1")
    rcentral.cmd("ip ro add 10.0.2.0/24 via 192.168.100.9")
    rcentral.cmd("ip ro add 10.0.3.0/24 via 192.168.100.17")
    rcentral.cmd("ip ro add 10.0.4.0/24 via 192.168.100.25")
    rcentral.cmd("ip ro add 10.0.5.0/24 via 192.168.100.33")
    rcentral.cmd("ip ro add 10.0.6.0/24 via 192.168.100.41")

    rsuc1.cmd('ip ro add 10.0.0.0/21 via 192.168.100.6')
    rsuc2.cmd('ip ro add 10.0.0.0/21 via 192.168.100.14')
    rsuc3.cmd('ip ro add 10.0.0.0/21 via 192.168.100.22')
    rsuc4.cmd('ip ro add 10.0.0.0/21 via 192.168.100.30')
    rsuc5.cmd('ip ro add 10.0.0.0/21 via 192.168.100.38')
    rsuc6.cmd('ip ro add 10.0.0.0/21 via 192.168.100.46')

    """
    ¿Por que no necesito esto?
    con solo poner el routing de arriba basta.¿Por que?
    rsuc1.cmd('ip ro add 192.168.100.0/24 via 192.168.100.6')
    rsuc2.cmd('ip ro add 192.168.100.0/24 via 192.168.100.14')
    rsuc3.cmd('ip ro add 192.168.100.0/24 via 192.168.100.22')
    rsuc4.cmd('ip ro add 192.168.100.0/24 via 192.168.100.30')
    rsuc5.cmd('ip ro add 192.168.100.0/24 via 192.168.100.38')
    rsuc6.cmd('ip ro add 192.168.100.0/24 via 192.168.100.46')
    """

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

