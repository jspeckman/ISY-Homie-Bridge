#!/usr/bin/env python

from homie.device_base import Device_Base
from homie.node.node_base import Node_Base

from homie.node.property.property_string import Property_String
from homie.node.property.property_enum import Property_Enum

from .base import Base

class Lock (Base,Device_Base):

    def __init__(self, isy_device=None,homie_settings=None, mqtt_settings=None):

        Base.__init__ (self,isy_device)

        Device_Base.__init__ (self,self.get_homie_device_id(), isy_device.name, homie_settings, mqtt_settings)

        node = (Node_Base(self,'lock','Lock','lock'))
        self.add_node (node)

        self.status = Property_String (node,'status','Status')
        node.add_property (self.status)

        self.run = Property_Enum (node,id='lock',name='Lock',data_format='LOCK,UNLOCK',set_value = self.set_lock)
        node.add_property (self.lock)

        self.start()

    def get_homie_device_id (self):
        return 'lock-' + Base.get_homie_device_id(self)

    def set_lock (self,value):
        if value == 'LOCK':
            self.isy_device.set_lock (1)
        elif value == 'UNLOCK':
            self.isy_device.set_lock(0)
            
    def property_change(self,property_,value):
        if property_ == 'state':
            self.status.value = value

        Base.property_change (self,property_,value)

