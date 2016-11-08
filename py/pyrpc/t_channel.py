# -*- encoding: utf-8 -*-

import google.protobuf.service

class TRpcChannel(google.protobuf.service.RpcChannel):

  def CallMethod(self, method_descriptor, rpc_controller,
                 request, response_class, done):
    method_idx = method_descriptor.
    """Calls the method identified by the descriptor.

    Call the given method of the remote service.  The signature of this
    procedure looks the same as Service.CallMethod(), but the requirements
    are less strict in one important way:  the request object doesn't have to
    be of any specific class as long as its descriptor is method.input_type.
    """
    raise NotImplementedError



"""
class MethodDescriptor(DescriptorBase):

  Descriptor for a method in a service.

  name: (str) Name of the method within the service.
  full_name: (str) Full name of method.
  index: (int) 0-indexed index of the method inside the service.
  containing_service: (ServiceDescriptor) The service that contains this
    method.
  input_type: The descriptor of the message that this method accepts.
  output_type: The descriptor of the message that this method returns.
  options: (descriptor_pb2.MethodOptions) Method options message or
    None to use default method options.

"""