# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/audio2face.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/audio2face.proto',
  package='nvidia.audio2face',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16proto/audio2face.proto\x12\x11nvidia.audio2face\"{\n\x10PushAudioRequest\x12\x15\n\rinstance_name\x18\x01 \x01(\t\x12\x12\n\nsamplerate\x18\x02 \x01(\x05\x12\x12\n\naudio_data\x18\x03 \x01(\x0c\x12(\n block_until_playback_is_finished\x18\x04 \x01(\x08\"5\n\x11PushAudioResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x85\x01\n\x16PushAudioStreamRequest\x12@\n\x0cstart_marker\x18\x01 \x01(\x0b\x32(.nvidia.audio2face.PushAudioRequestStartH\x00\x12\x14\n\naudio_data\x18\x02 \x01(\x0cH\x00\x42\x13\n\x11streaming_request\"l\n\x15PushAudioRequestStart\x12\x15\n\rinstance_name\x18\x01 \x01(\t\x12\x12\n\nsamplerate\x18\x02 \x01(\x05\x12(\n block_until_playback_is_finished\x18\x03 \x01(\x08\";\n\x17PushAudioStreamResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xd4\x01\n\nAudio2Face\x12X\n\tPushAudio\x12#.nvidia.audio2face.PushAudioRequest\x1a$.nvidia.audio2face.PushAudioResponse\"\x00\x12l\n\x0fPushAudioStream\x12).nvidia.audio2face.PushAudioStreamRequest\x1a*.nvidia.audio2face.PushAudioStreamResponse\"\x00(\x01\x62\x06proto3'
)




_PUSHAUDIOREQUEST = _descriptor.Descriptor(
  name='PushAudioRequest',
  full_name='nvidia.audio2face.PushAudioRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='nvidia.audio2face.PushAudioRequest.instance_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='samplerate', full_name='nvidia.audio2face.PushAudioRequest.samplerate', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audio_data', full_name='nvidia.audio2face.PushAudioRequest.audio_data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_until_playback_is_finished', full_name='nvidia.audio2face.PushAudioRequest.block_until_playback_is_finished', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=168,
)


_PUSHAUDIORESPONSE = _descriptor.Descriptor(
  name='PushAudioResponse',
  full_name='nvidia.audio2face.PushAudioResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='nvidia.audio2face.PushAudioResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='nvidia.audio2face.PushAudioResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=223,
)


_PUSHAUDIOSTREAMREQUEST = _descriptor.Descriptor(
  name='PushAudioStreamRequest',
  full_name='nvidia.audio2face.PushAudioStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_marker', full_name='nvidia.audio2face.PushAudioStreamRequest.start_marker', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audio_data', full_name='nvidia.audio2face.PushAudioStreamRequest.audio_data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='streaming_request', full_name='nvidia.audio2face.PushAudioStreamRequest.streaming_request',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=226,
  serialized_end=359,
)


_PUSHAUDIOREQUESTSTART = _descriptor.Descriptor(
  name='PushAudioRequestStart',
  full_name='nvidia.audio2face.PushAudioRequestStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='nvidia.audio2face.PushAudioRequestStart.instance_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='samplerate', full_name='nvidia.audio2face.PushAudioRequestStart.samplerate', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_until_playback_is_finished', full_name='nvidia.audio2face.PushAudioRequestStart.block_until_playback_is_finished', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=469,
)


_PUSHAUDIOSTREAMRESPONSE = _descriptor.Descriptor(
  name='PushAudioStreamResponse',
  full_name='nvidia.audio2face.PushAudioStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='nvidia.audio2face.PushAudioStreamResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='nvidia.audio2face.PushAudioStreamResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=471,
  serialized_end=530,
)

_PUSHAUDIOSTREAMREQUEST.fields_by_name['start_marker'].message_type = _PUSHAUDIOREQUESTSTART
_PUSHAUDIOSTREAMREQUEST.oneofs_by_name['streaming_request'].fields.append(
  _PUSHAUDIOSTREAMREQUEST.fields_by_name['start_marker'])
_PUSHAUDIOSTREAMREQUEST.fields_by_name['start_marker'].containing_oneof = _PUSHAUDIOSTREAMREQUEST.oneofs_by_name['streaming_request']
_PUSHAUDIOSTREAMREQUEST.oneofs_by_name['streaming_request'].fields.append(
  _PUSHAUDIOSTREAMREQUEST.fields_by_name['audio_data'])
_PUSHAUDIOSTREAMREQUEST.fields_by_name['audio_data'].containing_oneof = _PUSHAUDIOSTREAMREQUEST.oneofs_by_name['streaming_request']
DESCRIPTOR.message_types_by_name['PushAudioRequest'] = _PUSHAUDIOREQUEST
DESCRIPTOR.message_types_by_name['PushAudioResponse'] = _PUSHAUDIORESPONSE
DESCRIPTOR.message_types_by_name['PushAudioStreamRequest'] = _PUSHAUDIOSTREAMREQUEST
DESCRIPTOR.message_types_by_name['PushAudioRequestStart'] = _PUSHAUDIOREQUESTSTART
DESCRIPTOR.message_types_by_name['PushAudioStreamResponse'] = _PUSHAUDIOSTREAMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PushAudioRequest = _reflection.GeneratedProtocolMessageType('PushAudioRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUSHAUDIOREQUEST,
  '__module__' : 'proto.audio2face_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.audio2face.PushAudioRequest)
  })
_sym_db.RegisterMessage(PushAudioRequest)

PushAudioResponse = _reflection.GeneratedProtocolMessageType('PushAudioResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUSHAUDIORESPONSE,
  '__module__' : 'proto.audio2face_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.audio2face.PushAudioResponse)
  })
_sym_db.RegisterMessage(PushAudioResponse)

PushAudioStreamRequest = _reflection.GeneratedProtocolMessageType('PushAudioStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUSHAUDIOSTREAMREQUEST,
  '__module__' : 'proto.audio2face_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.audio2face.PushAudioStreamRequest)
  })
_sym_db.RegisterMessage(PushAudioStreamRequest)

PushAudioRequestStart = _reflection.GeneratedProtocolMessageType('PushAudioRequestStart', (_message.Message,), {
  'DESCRIPTOR' : _PUSHAUDIOREQUESTSTART,
  '__module__' : 'proto.audio2face_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.audio2face.PushAudioRequestStart)
  })
_sym_db.RegisterMessage(PushAudioRequestStart)

PushAudioStreamResponse = _reflection.GeneratedProtocolMessageType('PushAudioStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUSHAUDIOSTREAMRESPONSE,
  '__module__' : 'proto.audio2face_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.audio2face.PushAudioStreamResponse)
  })
_sym_db.RegisterMessage(PushAudioStreamResponse)



_AUDIO2FACE = _descriptor.ServiceDescriptor(
  name='Audio2Face',
  full_name='nvidia.audio2face.Audio2Face',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=533,
  serialized_end=745,
  methods=[
  _descriptor.MethodDescriptor(
    name='PushAudio',
    full_name='nvidia.audio2face.Audio2Face.PushAudio',
    index=0,
    containing_service=None,
    input_type=_PUSHAUDIOREQUEST,
    output_type=_PUSHAUDIORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PushAudioStream',
    full_name='nvidia.audio2face.Audio2Face.PushAudioStream',
    index=1,
    containing_service=None,
    input_type=_PUSHAUDIOSTREAMREQUEST,
    output_type=_PUSHAUDIOSTREAMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUDIO2FACE)

DESCRIPTOR.services_by_name['Audio2Face'] = _AUDIO2FACE

# @@protoc_insertion_point(module_scope)
