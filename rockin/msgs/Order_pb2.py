# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import Inventory_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='Order.proto',
  package='rockin_msgs',
  serialized_pb='\n\x0bOrder.proto\x12\x0brockin_msgs\x1a\x0fInventory.proto\"\xb3\x03\n\x05Order\x12\n\n\x02id\x18\x01 \x02(\x04\x12)\n\x06status\x18\x02 \x02(\x0e\x32\x19.rockin_msgs.Order.Status\x12-\n\x06object\x18\x03 \x02(\x0b\x32\x1d.rockin_msgs.ObjectIdentifier\x12\x30\n\tcontainer\x18\x04 \x01(\x0b\x32\x1d.rockin_msgs.ObjectIdentifier\x12\x1a\n\x12quantity_delivered\x18\x05 \x02(\x04\x12\x1a\n\x12quantity_requested\x18\x06 \x01(\x04\x12\x34\n\x0b\x64\x65stination\x18\x07 \x01(\x0b\x32\x1f.rockin_msgs.LocationIdentifier\x12/\n\x06source\x18\x08 \x01(\x0b\x32\x1f.rockin_msgs.LocationIdentifier\x12\x17\n\x0fprocessing_team\x18\t \x01(\t\"Z\n\x06Status\x12\x0b\n\x07OFFERED\x10\x01\x12\x0b\n\x07TIMEOUT\x10\x02\x12\x0f\n\x0bIN_PROGRESS\x10\x03\x12\n\n\x06PAUSED\x10\x04\x12\x0b\n\x07\x41\x42ORTED\x10\x05\x12\x0c\n\x08\x46INISHED\x10\x06\"X\n\tOrderInfo\x12\"\n\x06orders\x18\x01 \x03(\x0b\x32\x12.rockin_msgs.Order\"\'\n\x08\x43ompType\x12\x0c\n\x07\x43OMP_ID\x10\xd0\x0f\x12\r\n\x08MSG_TYPE\x10\xd2\x01\"F\n\x0fOrderAcceptance\x12\n\n\x02id\x18\x01 \x03(\x04\"\'\n\x08\x43ompType\x12\x0c\n\x07\x43OMP_ID\x10\xd0\x0f\x12\r\n\x08MSG_TYPE\x10\xd3\x01\x42)\n\x16org.rockin.common_msgsB\x0fOrderInfoProtos')



_ORDER_STATUS = descriptor.EnumDescriptor(
  name='Status',
  full_name='rockin_msgs.Order.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='OFFERED', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TIMEOUT', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='IN_PROGRESS', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PAUSED', index=3, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ABORTED', index=4, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FINISHED', index=5, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=391,
  serialized_end=481,
)

_ORDERINFO_COMPTYPE = descriptor.EnumDescriptor(
  name='CompType',
  full_name='rockin_msgs.OrderInfo.CompType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='COMP_ID', index=0, number=2000,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MSG_TYPE', index=1, number=210,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=532,
  serialized_end=571,
)

_ORDERACCEPTANCE_COMPTYPE = descriptor.EnumDescriptor(
  name='CompType',
  full_name='rockin_msgs.OrderAcceptance.CompType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='COMP_ID', index=0, number=2000,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MSG_TYPE', index=1, number=211,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=604,
  serialized_end=643,
)


_ORDER = descriptor.Descriptor(
  name='Order',
  full_name='rockin_msgs.Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='rockin_msgs.Order.id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='status', full_name='rockin_msgs.Order.status', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='object', full_name='rockin_msgs.Order.object', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='container', full_name='rockin_msgs.Order.container', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='quantity_delivered', full_name='rockin_msgs.Order.quantity_delivered', index=4,
      number=5, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='quantity_requested', full_name='rockin_msgs.Order.quantity_requested', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='destination', full_name='rockin_msgs.Order.destination', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='source', full_name='rockin_msgs.Order.source', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='processing_team', full_name='rockin_msgs.Order.processing_team', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ORDER_STATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=46,
  serialized_end=481,
)


_ORDERINFO = descriptor.Descriptor(
  name='OrderInfo',
  full_name='rockin_msgs.OrderInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='orders', full_name='rockin_msgs.OrderInfo.orders', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ORDERINFO_COMPTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=483,
  serialized_end=571,
)


_ORDERACCEPTANCE = descriptor.Descriptor(
  name='OrderAcceptance',
  full_name='rockin_msgs.OrderAcceptance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='rockin_msgs.OrderAcceptance.id', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ORDERACCEPTANCE_COMPTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=573,
  serialized_end=643,
)

_ORDER.fields_by_name['status'].enum_type = _ORDER_STATUS
_ORDER.fields_by_name['object'].message_type = Inventory_pb2._OBJECTIDENTIFIER
_ORDER.fields_by_name['container'].message_type = Inventory_pb2._OBJECTIDENTIFIER
_ORDER.fields_by_name['destination'].message_type = Inventory_pb2._LOCATIONIDENTIFIER
_ORDER.fields_by_name['source'].message_type = Inventory_pb2._LOCATIONIDENTIFIER
_ORDER_STATUS.containing_type = _ORDER;
_ORDERINFO.fields_by_name['orders'].message_type = _ORDER
_ORDERINFO_COMPTYPE.containing_type = _ORDERINFO;
_ORDERACCEPTANCE_COMPTYPE.containing_type = _ORDERACCEPTANCE;
DESCRIPTOR.message_types_by_name['Order'] = _ORDER
DESCRIPTOR.message_types_by_name['OrderInfo'] = _ORDERINFO
DESCRIPTOR.message_types_by_name['OrderAcceptance'] = _ORDERACCEPTANCE

class Order(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ORDER
  
  # @@protoc_insertion_point(class_scope:rockin_msgs.Order)

class OrderInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ORDERINFO
  
  # @@protoc_insertion_point(class_scope:rockin_msgs.OrderInfo)

class OrderAcceptance(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ORDERACCEPTANCE
  
  # @@protoc_insertion_point(class_scope:rockin_msgs.OrderAcceptance)

# @@protoc_insertion_point(module_scope)
