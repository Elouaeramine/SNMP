from pysnmp.hlapi import * 

data =(
    ObjectType(ObjectIdentity('SNMPv2-MIB' , 'sysLocation', 0)),
    ObjectType(ObjectIdentity('SNMPv2-MIB' , 'sysDescr', 0)),
    ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.10.38'))
)


g = getCmd(SnmpEngine() ,
            CommunityData('com', mpModel=0) ,
            UdpTransportTarget(('127.0.0.1', 161)) ,
            ContextData() ,
            *data
        )

errorIndication, errorStatus, errorIndex, varBinds = next(g)
if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint() ,
         errorIndex and varBinds[int(errorIndex) - 1][0] or '?' ) )
else:
    for varBind in varBinds:
        # print(' = '.join([x.prettyPrint() for x in varBind]))
        l = [str(x) for x in varBind]
        print (l[0] ," = " , l[1])