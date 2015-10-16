# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='Camera.proto',
  package='rockin_msgs',
  serialized_pb='\n\x0c\x43\x61mera.proto\x12\x0brockin_msgs\"7\n\x0c\x43\x61meraStatus\"\'\n\x08\x43ompType\x12\x0c\n\x07\x43OMP_ID\x10\xd0\x0f\x12\r\n\x08MSG_TYPE\x10\xb0\x02\"8\n\rCameraCommand\"\'\n\x08\x43ompType\x12\x0c\n\x07\x43OMP_ID\x10\xd0\x0f\x12\r\n\x08MSG_TYPE\x10\xb1\x02\x42&\n\x16org.rockin.common_msgsB\x0c\x43\x61meraProtos')



_CAMERASTATUS_COMPTYPE = descriptor.EnumDescriptor(
  name='CompType',
  full_name='rockin_msgs.CameraStatus.CompType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='COMP_ID', index=0, number=2000,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MSG_TYPE', index=1, number=304,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=45,
  serialized_end=84,
)

_CAMERACOMMAND_COMPTYPE = descriptor.EnumDescriptor(
  name='CompType',
  full_name='rockin_msgs.CameraCommand.CompType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='COMP_ID', index=0, number=2000,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MSG_TYPE', index=1, number=305,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=103,
  serialized_end=142,
)


_CAMERASTATUS = descriptor.Descriptor(
  name='CameraStatus',
  full_name='rockin_msgs.CameraStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CAMERASTATUS_COMPTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=29,
  serialized_end=84,
)


_CAMERACOMMAND = descriptor.Descriptor(
  name='CameraCommand',
  full_name='rockin_msgs.CameraCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CAMERACOMMAND_COMPTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=86,
  serialized_end=142,
)

_CAMERASTATUS_COMPTYPE.containing_type = _CAMERASTATUS;
_CAMERACOMMAND_COMPTYPE.containing_type = _CAMERACOMMAND;
DESCRIPTOR.message_types_by_name['CameraStatus'] = _CAMERASTATUS
DESCRIPTOR.message_types_by_name['CameraCommand'] = _CAMERACOMMAND

class CameraStatus(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CAMERASTATUS
  
  # @@protoc_insertion_point(class_scope:rockin_msgs.CameraStatus)

class CameraCommand(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CAMERACOMMAND
  
  # @@protoc_insertion_point(class_scope:rockin_msgs.CameraCommand)

# @@protoc_insertion_point(module_scope)
