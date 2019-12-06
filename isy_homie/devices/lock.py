#!/usr/bin/env python

from homie.device_base import Device_Base
from homie.node.node_base import Node_Base

from homie.node.property.property_battery import Property_Battery
from homie.node.property.property_string import Property_String
from homie.node.property.property_enum import Property_Enum

from .base import Base

class Lock (Base,Device_Base):

    def __init__(self, isy_device=None,homie_settings=None, mqtt_settings=None):

        Base.__init__ (self,isy_device)

        Device_Base.__init__ (self,self.get_homie_device_id().replace("_", "-"), isy_device.name, homie_settings, mqtt_settings)

        node = (Node_Base(self,'lock','Lock','lock'))
        self.add_node (node)

        self.status = Property_String (node,'status','Status')
        node.add_property (self.status)

        self.lock_state = Property_Enum (node,id='lockstate',name='Lock State',data_format='LOCK,UNLOCK',set_value = self.set_lock)
        node.add_property (self.lock_state)

        self.battery_level = Property_Battery (node)
        node.add_property (self.battery_level)

        self.start()

    def get_homie_device_id (self):
        return 'lock-' + Base.get_homie_device_id(self)

    def set_lock (self,value):
        if value == 'LOCK':
            self.isy_device.lock ()
        elif value == 'UNLOCK':
            self.isy_device.unlock()
            
    def property_change(self,property_,value):
        if property_ == 'status':
            self.status.value = value
        if property_ == 'state':
            self.lock_state.value = value
        if property_ == 'batterylevel':
            self.battery_level.value = value

        Base.property_change (self,property_,value)

