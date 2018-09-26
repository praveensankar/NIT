import iptc

table = iptc.Table(iptc.Table.FILTER)
chain = iptc.Chain(table,'FORWARD')

#policy = iptc.Policy(iptc.Policy.ACCEPT)

rule = iptc.Rule()
#rule.in_interface = "wlo1"
rule.src="98.136.103.24/255.255.255.0"
rule.dst="98.136.103.24/255.255.255.0"
rule.protocol="tcp"
match=iptc.Match(rule,"state")
match.state="RELATED,ESTABLISHED"
rule.add_match(match)
rule.target=iptc.Target(rule,"DROP")
chain.insert_rule(rule)
table.commit()


#displays all the chains in that particular table
for  chain in table.chains:
    print(chain.name)
    for rule in chain.rules:
        print(rule.protocol,rule.src,rule.dst)
        for match in rule.matches:
            print(match.name)
        print(rule.target.name)
        #chain.delete_rule(rule)

