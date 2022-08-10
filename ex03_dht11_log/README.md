# psos_examples
PSOS Example 3 - DHT11 and Logging

- DHT11 is a fairly common example used in microcontroller micropython examples. The drivers are even part of the standard Micropython build and Micropython.org has examples for both the [ESP8266](https://docs.micropython.org/en/latest/esp8266/quickref.html#dht-driver) and [ESP32](https://docs.micropython.org/en/latest/esp32/quickref.html#dht-driver)
- Our example will be even simpler, since we'll use the reuseable `svc_dht11` service.
- This example uses these [DHT11 devices](https://www.amazon.com/gp/product/B07WT2HJ4F/) from Amazon. They have clearly marked `+`,`-` and `out` pins.
- We'll also introduce the reuseable module `svc_log` service.
- Our example simply uses a new `.json` file and the secrets file from the previous example. If you skipped example 2, check it out in order to create a secrets file needed to connect to WiFi and the HiveMQ public MQTT broker
- At this point we're still using the public HiveMQ MQTT Broker, but we'll change that in the next example.

## Log Service

The log service allows you to specify a logger. Since we're dealing with remote
devices, they may not always be connected to Thonny and so it would be nice to be
able to monitor devices remotely. These loggers will then send messages to the
specified MQTT topic. We'll then use the HiveMQ Websocket client to monitor the 
log messages. 

The log service requires just a simple `.json` file entry.
Here's the entry for the ESP8266:
```json
    {"name": "log",  "module":"svc_log", "pub_log":"psos/d01/log" },
 ```
and the same service for the ESP32

```json
    {"name": "log",  "module":"svc_log", "pub_log":"psos/e01/log" },
```

We've used different topic names for the two loggers so that we can easily
determine which device the log message came from. From here on we'll be using
the name `d01` to refer to the D1 Mini, an ESP8266, and `e01` to refer to 
an ESP32.


## DHT11 Temperature/Humidity Sensor

Here's the DHT11 service JSON file entry for the ESP8266:

```json
    {"name": "temp", "module":"svc_dht11", "dht11_pin":14,
             "subscr_upd":"psos/d01/dht/upd",   "pub_upd":"psos/d01/dht" }
```
and the same service for the ESP32

```json
    {"name": "temp", "module":"svc_dht11", "dht11_pin":5,
             "subscr_upd":"psos/e01/dht/upd",   "pub_upd":"psos/e01/dht" }
```

In both cases we specify an input pin for the DHT11, either pin 14 for the ESP8266, or pin 5 for the ESP32. We've also used two different MQTT topics for the devices, `d01` for the ESP8266 and `e01` for the ESP32.

**Note** that on the ESP8266 the pin name on the board is `D5`, but the internal pin number is `14`. On the ESP32, the board pin `D5` is also the internal pin number `5`. So for both devices, we connect the DHT11 input to the pin marked `D5`, but the internal pin numbers are different. Why? I have no idea.

The `subscr_upd` topic defines a topic that the DHT11 services will subscribe to. When anything is published to that topic, the DHT11 service will publish the current temperature and humidity in a JSON format to the `pub_upd` topic.

To run this example:

- connect the DHT11 sensors to the pin marked D5 on the ESP32 or ESP8266
- connect the devices to Thonny and configure the interpreter (bottom right popup) for the appropriate device, ESP32 or ESP8266
- select the appropriate port
- if you haven't copied the base python code, per the previous example, copy all of the files in the `/base/` folder for this repo to the microcontroller
- save either the `esp32_psos_parms.json` or `esp8266_psos_parms.json` to the microcontroller under the name `psos_parms.json`


- open the [Websocket web page](http://www.hivemq.com/demos/websocket-client/)
- use the `Connect` button to connect to the public HiveMQ MQTT broker
- subscribe to the topic `psos/#` with a QoS of 0
- run `main.py` on the ESP32 and/or ESP8266

In the websocket webpage you should see something such as 
`mqtt: subscribing to psos/e01/dht/upd`  or 
`mqtt: subscribing to psos/d01/dht/upd`  

This is the output from the log service.

- publish a message, either `psos/e01/dht/upd` for the ESP32 or `psos/d01/dht/upd` for the ESP8266. No message is required as we are just triggering the service to generate an update

You may get a message such as `{"hum": "...", "temp": "starting..."}`.

This simply means the reading failed, which it may do when you first start the microcontroller. Try publishing the `.../dht/upd` message again. If you continue to recieve the `starting` message, check your DHT11 pin connections. The DHT11 `+` should be connected to the microcontroller `3v3` pin, the DHT11 `-` to ground and the DHT11 `out` connected to the microcontroller pin marked `D5` for both the ESP32 and ESP8266.

You can now disconnect the microcontrollers from your computer and Thonny and hook them up to USB outlet or batter. You should see the startup message in the webpage again and you should be able to generate updated temperature and humidity messages... anywhere there is a wifi connection for your microcontrollers and an internet connection for your websocket webpage.