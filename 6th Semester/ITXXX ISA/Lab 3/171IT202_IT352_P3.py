from scapy.all import *

import pandas as pd
import numpy as np
import math


def acl_rule_extractor():
    acl_rules = pd.read_excel('ACL-File-Lab-Program-3.xlsx', na_values=[]).fillna(-1).values

    num_rules = 0
    num_cols = acl_rules.shape[1]

    for i in range(acl_rules.shape[0]):
        flag = 1
        for j in range(acl_rules.shape[1]):
            if acl_rules[i][j] == -1:
                flag = 0    
                break

        if flag == 1:
            num_rules = num_rules + 1

    acl_rules = acl_rules[:num_rules, :]

    return acl_rules


def parse_hexdump(data_list, acl_rules, filename):

    data = []
    for d in data_list.split():
        data.append(int(d,16))
    
    dataset_list = data_list.split()

    mac_addr = dict()
    mac_addr['destination'] = dataset_list[0:6]
    mac_addr['source'] = dataset_list[6:12]

    print('Source MAC Address:', ":".join(map(str, mac_addr['source'])), file=open(filename, "a+"))
    print('Destination MAC Address:', ":".join(map(str, mac_addr['destination'])), file=open(filename, "a+"))

    etherType = data[12:14]

    packet_type = ""

    # IPv4 Packet
    if etherType[0] == 8 and etherType[1] == 0:

        print('Packet Type: IPv4', file=open(filename, "a+"))

        protocol_num = data[23]
        protocol_name = ''

        if protocol_num == 6:
            protocol_name = 'TCP'
        elif protocol_num == 17:
            protocol_name = 'UDP'

        print('IPv4 Packet Protocol:', protocol_name, file=open(filename, "a+"))

        packet_length = int((data[16] * math.pow(2, 8)) + data[17])
        print('Packet Length:', packet_length, file=open(filename, "a+"))


        time_to_live = data[22]
        print('Time To Live (TTL):', time_to_live, file=open(filename, "a+"))

        ip_addr = dict()
        ip_addr['source'] = data[26:30]
        ip_addr['destination'] = data[30:34]

        port_num = dict()
        port_num['source'] = int((data[34] * math.pow(2,8)) + data[35])
        port_num['destination'] = int((data[36] * math.pow(2,8)) + data[37])

        print('Source IP Address:', ".".join(map(str, ip_addr['source'])), file=open(filename, "a+"))
        print('Source IP Port:', port_num['source'], file=open(filename, "a+"))
        print('Destination IP Address:', ".".join(map(str, ip_addr['destination'])), file=open(filename, "a+"))
        print('Destination IP Port:', port_num['destination'], file=open(filename, "a+"))

        rule_matched = False

        for rule in acl_rules:
            agreements = 0

            if rule[0] != 'Any':
                flag = True
                ip_addr_check = rule[0].split('.')
                for i in range(4):
                    if (ip_addr_check[i] != '*') and (ip_addr['source'][i] != int(ip_addr_check[i])):
                        flag = False
                        break
                if flag:
                    agreements = agreements + 1
            else:
                agreements = agreements + 1

            if rule[1] != 'Any':
                port_num_check = rule[1]
                if (port_num_check == port_num['source']):
                    agreements = agreements + 1
            else:
                agreements = agreements + 1

            if rule[2] != 'Any':
                flag = True
                ip_addr_check = rule[2].split('.')

                for i in range(4):
                    if (ip_addr_check[i] != '*') and (ip_addr['destination'][i] != int(ip_addr_check[i])):
                        flag = False
                        break
                if flag:
                    agreements = agreements + 1
            else:
                agreements = agreements + 1

            if rule[3] != 'Any':
                port_num_check = rule[3]
                if (port_num_check == port_num['destination']):
                    agreements = agreements + 1
            else:
                agreements = agreements + 1

            if (agreements == 4):
                print('Rule matched:', ', '.join(list(map(str, rule))), file=open(filename, "a+"))
                print('Action:', rule[4], file=open(filename, "a+"))
                rule_matched = True

            if rule_matched == True:
                break

    # ARP Packet
    elif etherType[0] == 8 and etherType[1] == 6:

        print('Packet Type: ARP', file=open(filename, "a+"))

        ip_addr = dict()
        ip_addr['source'] = ".".join(map(str, data[28:32]))
        ip_addr['destination'] = ".".join(map(str, data[38:42]))

        print('Source IP Address:', ip_addr['source'], file=open(filename, "a+"))
        print('Destination IP Address:', ip_addr['destination'], file=open(filename, "a+"))

        print('Action: Deny', file=open(filename, "a+"))


def main():
    
    acl_rules = acl_rule_extractor()
    filename = '171IT202_IT352_P3_Output_TC5.txt'

    # Replace dst with src for Source IP filtering
    filter_ = 'dst host 100.102.100.102'
    a = sniff(count=1, filter=filter_)
    print('Raw Packet:',raw(a[0]),file=open(filename, "a+"))
    dump_str = chexdump(a[0], dump=True)
    hexdump_str = ' '.join(list(map(lambda x: x[-2:], dump_str.split(','))))
    print('Hexdump of Packet:', hexdump_str, file=open(filename, "a+"))
    
    parse_hexdump(hexdump_str, acl_rules, filename)

    file2 = open(filename, 'r')
    lines = file2.readlines()
    for line in lines:
        print(line, end="")

if __name__ == '__main__':
    main()
