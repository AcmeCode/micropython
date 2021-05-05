import network

def version():
    return "1.0"

def fileExists(fileName):
    result = True
    try:
        f = open( fileName, 'r' )
    except:
        result = False
    return result

def joinNetwork():
    print('joinNetwork: ' + ssid + '/' + key)
    sta_if = network.WLAN(network.STA_IF)
    if sta_if.isconnected():
        sta_if.disconnect()
    if sta_if.active():
        sta_if.active(False)
    sta_if.active(True)
    config = getNetworkConfig()
    sta_if.connect(config[0], config[1])
    while not sta_if.isconnected():
        pass
    
def getNetworkConfig():
    if fileExists("/network.json"):
        with open('network.json') as fp:
            data = ujson.load(fp)
            result = (data['ssid'],data['key'])
    else:
        print( "No network configuration file")
        result = ()