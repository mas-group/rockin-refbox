# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import Time_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='RobotInfo.proto',
  package='rockin_msgs',
  serialized_pb='\n\x0fRobotInfo.proto\x12\x0brockin_msgs\x1a\nTime.proto\"\x93\x01\n\x05Robot\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04team\x18\x02 \x02(\t\x12\x0c\n\x04host\x18\x03 \x02(\t\x12$\n\tlast_seen\x18\x04 \x02(\x0b\x32\x11.rockin_msgs.Time\x12\x12\n\nis_logging\x18\x05 \x01(\x08\"&\n\x08\x43ompType\x12\x0c\n\x07\x43OMP_ID\x10\xd0\x0f\x12\x0c\n\x08MSG_TYPE\x10\t\"W\n\tRobotInfo\x12\"\n\x06robots\x18\x01 \x03(\x0b\x32\x12.rockin_msgs.Robot\"&\n\x08\x43ompType\x12\x0c\n\x07\x43OMP_ID\x10\xd0\x0f\x12\x0c\n\x08MSG_TYPE\x10\x08\x42)\n\x16org.rockin.common_msgsB\x0fRobotInfoProtos')



_ROBOT_COMPTYPE = descriptor.EnumDescriptor(
  name='CompType',
  full_name='rockin_msgs.Robot.CompType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='COMP_ID', index=0, number=2000,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MSG_TYPE', index=1, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=154,
  serialized_end=192,
)

_ROBOTINFO_COMPTYPE = descriptor.EnumDescriptor(
  name='CompType',
  full_name='rockin_msgs.RobotInfo.CompType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='COMP_ID', index=0, number=2000,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MSG_TYPE', index=1, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=243,
  serialized_end=281,
)


_ROBOT = descriptor.Descriptor(
  name='Robot',
  full_name='rockin_msgs.Robot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='rockin_msgs.Robot.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='team', full_name='rockin_msgs.Robot.team', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='host', full_name='rockin_msgs.Robot.host', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='last_seen', full_name='rockin_msgs.Robot.last_seen', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_logging', full_name='rockin_msgs.Robot.is_logging', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ROBOT_COMPTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=45,
  serialized_end=192,
)


_ROBOTINFO = descriptor.Descriptor(
  name='RobotInfo',
  full_name='rockin_msgs.RobotInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='robots', full_name='rockin_msgs.RobotInfo.robots', index=0,
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
    _ROBOTINFO_COMPTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=194,
  serialized_end=281,
)

_ROBOT.fields_by_name['last_seen'].message_type = Time_pb2._TIME
_ROBOT_COMPTYPE.containing_type = _ROBOT;
_ROBOTINFO.fields_by_name['robots'].message_type = _ROBOT
_ROBOTINFO_COMPTYPE.containing_type = _ROBOTINFO;
DESCRIPTOR.message_types_by_name['Robot'] = _ROBOT
DESCRIPTOR.message_types_by_name['RobotInfo'] = _ROBOTINFO

class Robot(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROBOT
  
  # @@protoc_insertion_point(class_scope:rockin_msgs.Robot)

class RobotInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROBOTINFO
  
  # @@protoc_insertion_point(class_scope:rockin_msgs.RobotInfo)

# @@protoc_insertion_point(module_scope)
