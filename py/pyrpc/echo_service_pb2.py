# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: echo_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='echo_service.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x12\x65\x63ho_service.proto\"\x1b\n\x0b\x45\x63hoRequest\x12\x0c\n\x04ping\x18\x01 \x02(\x05\"\x1c\n\x0c\x45\x63hoResponse\x12\x0c\n\x04pong\x18\x01 \x02(\x05\x32\x32\n\x0b\x45\x63hoService\x12#\n\x04\x45\x63ho\x12\x0c.EchoRequest\x1a\r.EchoResponseB\x06\x80\x01\x01\x90\x01\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ECHOREQUEST = _descriptor.Descriptor(
  name='EchoRequest',
  full_name='EchoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ping', full_name='EchoRequest.ping', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=49,
)


_ECHORESPONSE = _descriptor.Descriptor(
  name='EchoResponse',
  full_name='EchoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pong', full_name='EchoResponse.pong', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=79,
)

DESCRIPTOR.message_types_by_name['EchoRequest'] = _ECHOREQUEST
DESCRIPTOR.message_types_by_name['EchoResponse'] = _ECHORESPONSE

EchoRequest = _reflection.GeneratedProtocolMessageType('EchoRequest', (_message.Message,), dict(
  DESCRIPTOR = _ECHOREQUEST,
  __module__ = 'echo_service_pb2'
  # @@protoc_insertion_point(class_scope:EchoRequest)
  ))
_sym_db.RegisterMessage(EchoRequest)

EchoResponse = _reflection.GeneratedProtocolMessageType('EchoResponse', (_message.Message,), dict(
  DESCRIPTOR = _ECHORESPONSE,
  __module__ = 'echo_service_pb2'
  # @@protoc_insertion_point(class_scope:EchoResponse)
  ))
_sym_db.RegisterMessage(EchoResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\200\001\001\220\001\001'))

_ECHOSERVICE = _descriptor.ServiceDescriptor(
  name='EchoService',
  full_name='EchoService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=81,
  serialized_end=131,
  methods=[
  _descriptor.MethodDescriptor(
    name='Echo',
    full_name='EchoService.Echo',
    index=0,
    containing_service=None,
    input_type=_ECHOREQUEST,
    output_type=_ECHORESPONSE,
    options=None,
  ),
])

EchoService = service_reflection.GeneratedServiceType('EchoService', (_service.Service,), dict(
  DESCRIPTOR = _ECHOSERVICE,
  __module__ = 'echo_service_pb2'
  ))

EchoService_Stub = service_reflection.GeneratedServiceStubType('EchoService_Stub', (EchoService,), dict(
  DESCRIPTOR = _ECHOSERVICE,
  __module__ = 'echo_service_pb2'
  ))


# @@protoc_insertion_point(module_scope)
