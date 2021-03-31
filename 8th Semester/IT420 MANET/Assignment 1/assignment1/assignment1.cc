/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation;
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */

#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/csma-module.h"
#include "ns3/internet-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/applications-module.h"
#include "ns3/ipv4-global-routing-helper.h"

#include "ns3/netanim-module.h"

// Default Network Topology
//
//       10.1.1.0
// n0 -------------- n1   n2   n3   n4   n5
//    point-to-point  |    |    |    |   |
//                    ====================
//                      LAN 10.1.2.0


using namespace ns3;

NS_LOG_COMPONENT_DEFINE ("SecondScriptExample");

int main (int argc, char *argv[]) {

  bool verbose = true; // refers to command line
  uint32_t nCsma = 3; //number of csma nodes is 3 (setting default value to nCsma. It can be read from command line also.

  CommandLine cmd; // create a command line object
  cmd.AddValue ("nCsma", "Number of \"extra\" CSMA nodes/devices", nCsma); //reading extra csma nodes from command line
  cmd.AddValue ("verbose", "Tell echo applications to log if true", verbose);

  cmd.Parse (argc,argv);

  if (verbose)
    {
      LogComponentEnable ("UdpEchoClientApplication", LOG_LEVEL_INFO);
      LogComponentEnable ("UdpEchoServerApplication", LOG_LEVEL_INFO);
    }

  nCsma = nCsma == 0 ? 1 : nCsma; // if extra nodes are specified or no? ncsma=0 or more.

  NodeContainer p2pNodes;
  p2pNodes.Create (2);

  NodeContainer p2pNodes_1;
  // 2nd node in first p2p network
  p2pNodes_1.Add (p2pNodes.Get (1)); 
  p2pNodes_1.Create (1);

  NodeContainer csmaNodes;
  // 2nd node in first p2p network 
  csmaNodes.Add (p2pNodes_1.Get (1)); 
  csmaNodes.Create (nCsma);

  PointToPointHelper pointToPoint; // Define the link attributes like Datarate, Delay
  pointToPoint.SetDeviceAttribute ("DataRate", StringValue ("5Mbps"));
  pointToPoint.SetChannelAttribute ("Delay", StringValue ("2ms"));

  NetDeviceContainer p2pDevices; // Add NICs to p2pNodes n0,n1
  p2pDevices = pointToPoint.Install (p2pNodes);

  PointToPointHelper pointToPoint_1;
  pointToPoint_1.SetDeviceAttribute ("DataRate", StringValue ("5Mbps"));
  pointToPoint_1.SetChannelAttribute ("Delay", StringValue ("2ms"));

  NetDeviceContainer p2pDevices_1; // Add NICs to p2pNodes n0,n1
  p2pDevices_1 = pointToPoint_1.Install (p2pNodes_1);

  CsmaHelper csma; // This is new to us now. LAN will have more bandwidth and delay.
  csma.SetChannelAttribute ("DataRate", StringValue ("100Mbps"));
  csma.SetChannelAttribute ("Delay", TimeValue (NanoSeconds (6560)));

  NetDeviceContainer csmaDevices; // Install NICs on csmaNodes
  csmaDevices = csma.Install (csmaNodes);

  InternetStackHelper stack; //Install protocol stack onto the devices.
  stack.Install (p2pNodes);
  stack.Install (csmaNodes);

  Ipv4AddressHelper address; // Add Network address to the p2p network and CSMA LAN
  address.SetBase ("10.1.1.0", "255.255.255.0");
  Ipv4InterfaceContainer p2pInterfaces;
  p2pInterfaces = address.Assign (p2pDevices);

  address.SetBase ("10.1.2.0", "255.255.255.0");
  Ipv4InterfaceContainer p2pInterfaces_1;
  p2pInterfaces_1 = address.Assign (p2pDevices_1);

  address.SetBase ("10.1.3.0", "255.255.255.0");
  Ipv4InterfaceContainer csmaInterfaces;
  csmaInterfaces = address.Assign (csmaDevices);

  //Defining client and server now.
  UdpEchoServerHelper echoServer (9); 

  ApplicationContainer serverApps = echoServer.Install (csmaNodes.Get (nCsma));
  serverApps.Start (Seconds (1.0));
  serverApps.Stop (Seconds (10.0));

  UdpEchoClientHelper echoClient (csmaInterfaces.GetAddress (nCsma), 9); //get ip and port number of server
  echoClient.SetAttribute ("MaxPackets", UintegerValue (1)); 
  echoClient.SetAttribute ("Interval", TimeValue (Seconds (1.0)));
  echoClient.SetAttribute ("PacketSize", UintegerValue (512));

  ApplicationContainer clientApps = echoClient.Install (p2pNodes.Get (0)); //client is n0
  clientApps.Start (Seconds (2.0));
  clientApps.Stop (Seconds (10.0));

  Ipv4GlobalRoutingHelper::PopulateRoutingTables (); //Using routing table 

  pointToPoint.EnablePcap ("assignment1", p2pDevices.Get (0), true);
  pointToPoint.EnablePcap ("assignment1", p2pDevices.Get (1), true);
  csma.EnablePcap ("assignment1", csmaDevices.Get (0), true);

  if (nCsma >= 3) {
    csma.EnablePcap ("assignment1", csmaDevices.Get (3), true);
  }

  //Echo in the class names indicates that whatever the client sends to the server, server sends the same data back.

  //Simulation code

  AnimationInterface anim("assignment1.xml");
  anim.SetConstantPosition(p2pNodes.Get(0),10.0,10.0);
  anim.SetConstantPosition(p2pNodes.Get(1),20.0,10.0);
  anim.SetConstantPosition(csmaNodes.Get(0),30.0,10.0);
  anim.SetConstantPosition(csmaNodes.Get(1),40.0,10.0);
  anim.SetConstantPosition(csmaNodes.Get(2),50.0,10.0);
  anim.SetConstantPosition(csmaNodes.Get(3),60.0,10.0);


  //Trace Metrics - ASCII Trace Format - prints log file in ASCII format
  AsciiTraceHelper ascii;
  pointToPoint.EnableAsciiAll(ascii.CreateFileStream("assignment1.tr"));

  Simulator::Run ();
  Simulator::Destroy ();
  return 0;
}
