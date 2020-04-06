#! /usr/bin/env python3
import iptc
import json
import sys


# Input: file name of list IP range
# IPTable manipulate

def add_rule(IPRange):
    
    rule=iptc.Rule()
    # Target
    target_ACCEPT = rule.create_target("ACCEPT")
    target_DROP = rule.create_target("DROP")
    
    # Chain
    chain_input=iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    chain_output=iptc.Chain(iptc.Table(iptc.Table.FILTER), "OUTPUT")
    
    namespace = IPRange[0]
    IP = IPRange[1]
    rule.src = IP
    rule.dst = IP
    if namespace != "all": 
        rule.target = target_ACCEPT
    else:
        rule.target = target_DROP

    chain_input.insert_rule(rule)
    chain_output.insert_rule(rule)
    

def flush_all():
    chain_input=iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    chain_output=iptc.Chain(iptc.Table(iptc.Table.FILTER), "OUTPUT")
    chain_input.flush()
    chain_output.flush()


def Input(filename):
    with open(filename, 'r') as f:
        ip_range_list = json.load(f)
        return ip_range_list

#----------Start From Here-------------------------
if len(sys.argv) > 1:
    filename=sys.argv[1]
else:
    filename="iplist.json"

ip_range_list = Input(filename)

flush_all()

for item in ip_range_list.items():
    add_rule(item)

while True:
    pass

