# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='BenchmarkInfo.proto',
  package='rockin_msgs',
  serialized_pb='\n\x13\x42\x65nchmarkInfo.proto\x12\x0brockin_msgs\"G\n\rBenchmarkInfo\x12\x0e\n\x06object\x18\x01 \x01(\t\"&\n\x08\x43ompType\x12\x0c\n\x07\x43OMP_ID\x10\xd0\x0f\x12\x0c\n\x08MSG_TYPE\x10hB-\n\x16org.rockin.common_msgsB\x13\x42\x65nchmarkInfoProtos')



_BENCHMARKINFO_COMPTYPE = descriptor.EnumDescriptor(
  name='CompType',
  full_name='rockin_msgs.BenchmarkInfo.CompType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='COMP_ID', index=0, number=2000,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MSG_TYPE', index=1, number=104,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=69,
  serialized_end=107,
)


_BENCHMARKINFO = descriptor.Descriptor(
  name='BenchmarkInfo',
  full_name='rockin_msgs.BenchmarkInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='object', full_name='rockin_msgs.BenchmarkInfo.object', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BENCHMARKINFO_COMPTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=36,
  serialized_end=107,
)

_BENCHMARKINFO_COMPTYPE.containing_type = _BENCHMARKINFO;
DESCRIPTOR.message_types_by_name['BenchmarkInfo'] = _BENCHMARKINFO

class BenchmarkInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BENCHMARKINFO
  
  # @@protoc_insertion_point(class_scope:rockin_msgs.BenchmarkInfo)

# @@protoc_insertion_point(module_scope)
