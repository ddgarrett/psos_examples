# psos_examples
PSOS Examples

- Examples tested with an [ESP8266 with 4MB](https://www.amazon.com/dp/B073CQVFLK) (a WebMOS D1 Mini clone) and [ESP32](https://www.amazon.com/dp/B07QCP2451)
- At future date may also test with Pico W and Pico with an ESP8266 coprocessor
- Does not cover installing micropython. For that, see instructions for [ESP8266](https://docs.micropython.org/en/latest/esp8266/quickref.html) and [ESP32](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)
- Uses the micropython [`uasyncio` for multitasking](https://docs.micropython.org/en/latest/library/uasyncio.html)
    - will cover some of the basics later starting in example ??? 
- Uses Thonny IDE and [HiveMQ Web Client](http://www.hivemq.com/demos/websocket-client/?)
- [Random Nerd Tutorials](https://randomnerdtutorials.com/projects-esp32-esp8266-micropython/) contains detailed instructions on how to install Thonny IDE and as well as how to flash micropython onto either device
- This is based on MQTT. Should be familiar with that. If not, Random Nerd Tutorials has an excellent [introducton to MQTT](https://randomnerdtutorials.com/what-is-mqtt-and-how-it-works/)
- Uses [HiveMQ](https://www.hivemq.com/) in particular. They have an [open public MQTT broker](https://www.hivemq.com/public-mqtt-broker/) and provide [free private MQTT accounts](https://www.hivemq.com/downloads/) that allows you to connect up to 100 clients at a time.

## Example Summary

1. Blinks the internal LED on the microcontroller
    - Ensures micropython installed correctly on microcontroller
    - Minimal PSOS example

2. Blink via MQTT
    - First use of entire PSOS base python code
    - First connection to WiFi
    - Uses simplest possible MQTT broker, HiveMQ's public broker
    - Introduces use of websocket web page client to trigger services

3. DHT11 with MQTT
    - First use of builtin services, the `svc_dht11` and `svc_log` builtin services.
    - Continues use of websocket client to monitor and trigger temperature/humidity reading
    - Introduces first complex message with JSON format

4. Free Private HiveMQ MQTT Broker Account
    - Begins use of a free private HiveMQ account
    - Easy since the root certificate is included in PSOS base code
    - How to connect websocket client to a private account is a bit different

5. Touch & Memory Check
    - Add two more reuseable services, `svc_touch` and `svc_mem_use`
    - `svc_touch` uses the ESP32 capacitive touch sensors to trigger logging of temperature and memory use

6. LCD and Pipe
    - Use LCD and pipe services to display temperature and memory usage on an LCD, again without any custom code, just via JSON parameters

7. Touch Feedback
    - Add more `svc_touch` services and have all `svc_touch` use the hourglass LCD screen feedback when touched


