# Python secrets file.
# In .gitignore and therefore never sent to repo.

# MQTT certificates
from hivemq_root_ca import hivemq_root_ca

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
        'port'   : 1883 },
        
    "mqtt_hivemq" :{
        'server' : 'xxxxxxxxxxxx.s1.eu.hivemq.cloud',
        'port'   : 8883,
        'username' : 'xxxxxx',
        'password' : 'yyyyyy',
        'ca_cert'  : hivemq_root_ca
        }
}

