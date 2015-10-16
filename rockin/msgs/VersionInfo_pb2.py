# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='VersionInfo.proto',
  package='rockin_msgs',
  serialized_pb='\n\x11VersionInfo.proto\x12\x0brockin_msgs\"\x92\x01\n\x0bVersionInfo\x12\x15\n\rversion_major\x18\x01 \x02(\r\x12\x15\n\rversion_minor\x18\x02 \x02(\r\x12\x15\n\rversion_micro\x18\x03 \x02(\r\x12\x16\n\x0eversion_string\x18\x04 \x02(\t\"&\n\x08\x43ompType\x12\x0c\n\x07\x43OMP_ID\x10\xd0\x0f\x12\x0c\n\x08MSG_TYPE\x10\x03\x42\'\n\x16org.rockin.common_msgsB\rVersionProtos')



_VERSIONINFO_COMPTYPE = descriptor.EnumDescriptor(
  name='CompType',
  full_name='rockin_msgs.VersionInfo.CompType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='COMP_ID', index=0, number=2000,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MSG_TYPE', index=1, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=143,
  serialized_end=181,
)


_VERSIONINFO = descriptor.Descriptor(
  name='VersionInfo',
  full_name='rockin_msgs.VersionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='version_major', full_name='rockin_msgs.VersionInfo.version_major', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='version_minor', full_name='rockin_msgs.VersionInfo.version_minor', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='version_micro', full_name='rockin_msgs.VersionInfo.version_micro', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='version_string', full_name='rockin_msgs.VersionInfo.version_string', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VERSIONINFO_COMPTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=35,
  serialized_end=181,
)

_VERSIONINFO_COMPTYPE.containing_type = _VERSIONINFO;
DESCRIPTOR.message_types_by_name['VersionInfo'] = _VERSIONINFO

class VersionInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VERSIONINFO
  
  # @@protoc_insertion_point(class_scope:rockin_msgs.VersionInfo)

# @@protoc_insertion_point(module_scope)
