# Python secrets file.
# In .gitignore and therefore never sent to repo.

# WiFi environments
wifi =  {
    "wifi_home":{
        'ssid'     : 'xxxxx',
        'password' : 'xxxxx'
        }

    }

# MQTT environemts
# Note that docer server IP address may vary by wifi network
mqtt =  {
    "mqtt_hivemq_public" :{
        'server' : 'broker.mqttdashboard.com',
        'port'   : 1883 }
}

