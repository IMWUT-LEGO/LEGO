

"""
<plugin key="ZhimiFan_LEGO" name="ZhimiFan_LEGO" author="LEGO" version="0.1.0">
    <description>
        <h2>ZhimiFan_LEGO</h2><br/>
        <h3>Configuration</h3>
        Enter the IP Address and Token of your devices.  <br/>
        Set the scene parameter "show" to display scenes, otherwise set to "hide".

    </description>
    <params>
        <param field="Address" label="IP Address" width="200px" required="true" default=""/>
        <param field="Mode1" label="Token" width="300px" required="true" default=""/>
        <param field="Mode3" label="Mode" width="75px">
            <options>
                <option label="Show" value="Show" default="True" />
                <option label="Hide" value="Hide" />
            </options>
        </param>
        <param field="Mode2" label="Debug" width="75px">
            <options>
                <option label="True" value="Debug"/>
                <option label="False" value="Normal" default="True" />
            </options>
        </param>
    </params>
</plugin>
"""



import os
import sys
import time
import os.path
import json
import random
import binascii

import Domoticz

module_paths = [x[0] for x in os.walk( os.path.join(os.path.dirname(__file__), '.', '.env/lib/') ) if x[0].endswith('site-packages') ]
for mp in module_paths:
    sys.path.append(mp)


from miio.integrations.fan.zhimi.fan import Fan



class BasePlugin:

    UNIT_FAN = 1
    UNIT_SCENES = 2

    pollTime = 1
    nextTimeSync = 0
    handshakeTime = 0

    def __init__(self):
        return

    def onStart(self):
        Domoticz.Debug("onStart called")
        if Parameters['Mode2'] == 'Debug': Domoticz.Debugging(1)

        if self.UNIT_FAN not in Devices:
            Domoticz.Device(Name='Power/Direct_speed',  Unit=self.UNIT_FAN, Type=241, Subtype=8, Switchtype=7, Used=1).Create()

        if ((Parameters['Mode3'] == 'Show') and (self.UNIT_SCENES not in Devices)):
            Options = { "Scenes": "|||||", "LevelNames": "Off|1|2|3|4", "LevelOffHidden": "true", "SelectorStyle": "0" }
            Domoticz.Device(Name="Modes", Unit=self.UNIT_SCENES, Type=244, Subtype=62 , Switchtype=18, Options = Options, Used=1).Create()
        
        Options = { "Scenes": "||", "LevelNames": "Off|Off|On", "LevelOffHidden": "true", "SelectorStyle": "0" }
        Domoticz.Device(Name="Buzzer", Unit=3, TypeName="Selector Switch", Switchtype=18, Options=Options).Create()
        Domoticz.Device(Name="Childlock", Unit=4, TypeName="Selector Switch", Switchtype=18, Options=Options).Create()


        global Fan1
        Fan1 = Fan(Parameters['Address'],Parameters['Mode1'])

        self.pollTime = random.randrange(5, 16)
        self.nextTimeSync = 0

        DumpConfigToLog()
        Domoticz.Heartbeat(20)

        Domoticz.Debug('Plugin started.')
        Domoticz.Log('Poll time is every {0} minute'.format(self.pollTime))

    def onStop(self):
        Domoticz.Debug("onStop called")

    def onConnect(self, Connection, Status, Description):
        Domoticz.Debug("onConnect called")

    def onMessage(self, Connection, Data):
        Domoticz.Debug("onMessage called")

    def onHeartbeat(self):
        Domoticz.Debug("onHeartbeat called")

        self.nextTimeSync -= 1
        self.handshakeTime -= 1

        try:
            if (self.nextTimeSync <= 0) and (self.UNIT_FAN in Devices):
                Domoticz.Debug('Sync on time: every {0} minute called'.format(self.pollTime))
                self.nextTimeSync = int((self.pollTime*60)/20)

                status = Fan1.status()

                if status.is_on:

                    if ((Devices[self.UNIT_FAN].sValue != str(status.direct_speed)) or (Devices[self.UNIT_FAN].nValue != 1) or (Devices[self.UNIT_FAN].TimedOut == True)):
                        Devices[self.UNIT_FAN].Update(nValue=1, sValue=str(status.direct_speed), TimedOut = False)

                if not status.is_on:
                    if ((Devices[self.UNIT_FAN].nValue != 0) or (Devices[self.UNIT_FAN].TimedOut == True)):
                        Devices[self.UNIT_FAN].Update(nValue=0, sValue='Off', TimedOut = False)

                if ((self.UNIT_SCENES in Devices) and (str(int(status.angle)) != Devices[self.UNIT_SCENES].sValue)):
                    if int(status.angle) == 0:
                        Devices[self.UNIT_SCENES].Update(nValue=0, sValue="0")
                    else: Devices[self.UNIT_SCENES].Update(nValue=1, sValue=str(int(status.angle)))
                
                if status.buzzer:
                    Devices[3].Update(nValue=1, sValue='On', TimedOut = False)
                else:
                    Devices[3].Update(nValue=1, sValue='Off', TimedOut = False)
                
                if status.child_lock:
                    Devices[4].Update(nValue=1, sValue='On', TimedOut = False)
                else:
                    Devices[4].Update(nValue=1, sValue='Off', TimedOut = False)

        except Exception as e:
            Devices[self.UNIT_FAN].Update(nValue=Devices[self.UNIT_FAN].nValue, sValue=Devices[self.UNIT_FAN].sValue, TimedOut = True)
            self.handshakeTime = 0
            self.nextTimeSync = 0

    def onCommand(self, Unit, Command, Level, Color):

        Level = max(min(Level, 100), 1)

        try:

            if Command == 'On':
                Fan1.on()
                Devices[Unit].Update(nValue=1, sValue='On', TimedOut = False)

            elif Command == 'Off':
                Fan1.off()
                Devices[Unit].Update(nValue=0, sValue='Off', TimedOut = False)
                if self.UNIT_SCENES in Devices: Devices[self.UNIT_SCENES].Update(nValue=0, sValue='0')

            elif Command == 'Set Level':
                Fan1.set_direct_speed(Level)
                Devices[Unit].Update(nValue=1, sValue=str(Level), TimedOut = False)


        except Exception as e:
            Devices[Unit].Update(nValue=Devices[Unit].nValue, sValue=Devices[Unit].sValue, TimedOut = True)
            self.handshakeTime = 0
            self.nextTimeSync = 0

    def onNotification(self, Name, Subject, Text, Status, Priority, Sound, ImageFile):
        Domoticz.Debug("Notification: " + Name + "," + Subject + "," + Text + "," + Status + "," + str(Priority) + "," + Sound + "," + ImageFile)

    def onDisconnect(self, Connection):
        Domoticz.Debug("onDisconnect called")




global _plugin
_plugin = BasePlugin()

def onStart():
    global _plugin
    _plugin.onStart()

def onStop():
    global _plugin
    _plugin.onStop()

def onConnect(Connection, Status, Description):
    global _plugin
    _plugin.onConnect(Connection, Status, Description)

def onMessage(Connection, Data):
    global _plugin
    _plugin.onMessage(Connection, Data)

def onCommand(Unit, Command, Level, Hue):
    global _plugin
    _plugin.onCommand(Unit, Command, Level, Hue)

def onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile):
    global _plugin
    _plugin.onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile)

def onDisconnect(Connection):
    global _plugin
    _plugin.onDisconnect(Connection)

def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()

    # Generic helper functions
def DumpConfigToLog():
    for x in Parameters:
        if Parameters[x] != "":
            Domoticz.Debug( "'" + x + "':'" + str(Parameters[x]) + "'")
    Domoticz.Debug("Device count: " + str(len(Devices)))
    for x in Devices:
        Domoticz.Debug("Device:           " + str(x) + " - " + str(Devices[x]))
        Domoticz.Debug("Device ID:       '" + str(Devices[x].ID) + "'")
        Domoticz.Debug("Device Name:     '" + Devices[x].Name + "'")
        Domoticz.Debug("Device nValue:    " + str(Devices[x].nValue))
        Domoticz.Debug("Device sValue:   '" + Devices[x].sValue + "'")
        Domoticz.Debug("Device LastLevel: " + str(Devices[x].LastLevel))
        Domoticz.Debug("Device TimedOut: " + str(Devices[x].TimedOut))
    return
