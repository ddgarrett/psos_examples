"""
    Blink Internal LED Service
        
    Blink internal LED on either D1 Mini or ESP32.
    
"""

from psos_svc import PsosService
import uasyncio

from machine import Pin

import queue

# All initialization classes are named ModuleService
class ModuleService(PsosService):
    
    def __init__(self, parms):
        super().__init__(parms)
        
        # Service specific initialization
        # Set LED pin out
        self._led = Pin(2, Pin.OUT)

        # get name of topic to subscribe to
        self._subscr_topic = parms.get_parm("subscr_topic")
        self._trigger_q = queue.Queue()

        print("in example 02 svc_blink.__init__")
        
    async def run(self):
        
        mqtt = self.get_mqtt()
        await mqtt.subscribe(self._subscr_topic,self._trigger_q)

        print("in example 02 svc_blink.run")

        while True:
            data = await self._trigger_q.get()
            print(data)
            self._led(int(data[2]))
            
