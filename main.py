

def connectToWifiAndUpdate():
    import time, machine, network, gc, app.secrets as secrets
    time.sleep(1)
    print('Memory free', gc.mem_free())

    from app.ota_updater import OTAUpdater

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    #Importante que el repositorio tenga releases y cofiguras las versiones. #Dejando main_dir='' se accede a la carpeta general del repositorio si se desea acceder a una carpeta en específio se escribe en este parametro
    otaUpdater = OTAUpdater('https://github.com/JuanRodriguezUV/medicion-inteligente', main_dir='', secrets_file="secrets.py")
    hasUpdated = otaUpdater.install_update_if_available()
    if hasUpdated:
        machine.reset()
    else:
        del(otaUpdater)
        gc.collect()

def startApp():
    import app.main


connectToWifiAndUpdate()
startApp()