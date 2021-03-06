# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from movo_msgs/Propulsion.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class Propulsion(genpy.Message):
  _md5sum = "61491c2b54c7a9e181eff35f997fd6b8"
  _type = "movo_msgs/Propulsion"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
uint32[] wheel_motor_status
float32[] wheel_motor_current_A0pk
float32[] wheel_motor_speed_rps
float32[] wheel_motor_position_rad
uint32 linear_motor_status
float32 linear_motor_current_A0pk
float32 linear_motor_speed_rps
float32 linear_motor_position_rad
 



================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
"""
  __slots__ = ['header','wheel_motor_status','wheel_motor_current_A0pk','wheel_motor_speed_rps','wheel_motor_position_rad','linear_motor_status','linear_motor_current_A0pk','linear_motor_speed_rps','linear_motor_position_rad']
  _slot_types = ['std_msgs/Header','uint32[]','float32[]','float32[]','float32[]','uint32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,wheel_motor_status,wheel_motor_current_A0pk,wheel_motor_speed_rps,wheel_motor_position_rad,linear_motor_status,linear_motor_current_A0pk,linear_motor_speed_rps,linear_motor_position_rad

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Propulsion, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.wheel_motor_status is None:
        self.wheel_motor_status = []
      if self.wheel_motor_current_A0pk is None:
        self.wheel_motor_current_A0pk = []
      if self.wheel_motor_speed_rps is None:
        self.wheel_motor_speed_rps = []
      if self.wheel_motor_position_rad is None:
        self.wheel_motor_position_rad = []
      if self.linear_motor_status is None:
        self.linear_motor_status = 0
      if self.linear_motor_current_A0pk is None:
        self.linear_motor_current_A0pk = 0.
      if self.linear_motor_speed_rps is None:
        self.linear_motor_speed_rps = 0.
      if self.linear_motor_position_rad is None:
        self.linear_motor_position_rad = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.wheel_motor_status = []
      self.wheel_motor_current_A0pk = []
      self.wheel_motor_speed_rps = []
      self.wheel_motor_position_rad = []
      self.linear_motor_status = 0
      self.linear_motor_current_A0pk = 0.
      self.linear_motor_speed_rps = 0.
      self.linear_motor_position_rad = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.wheel_motor_status)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.wheel_motor_status))
      length = len(self.wheel_motor_current_A0pk)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.wheel_motor_current_A0pk))
      length = len(self.wheel_motor_speed_rps)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.wheel_motor_speed_rps))
      length = len(self.wheel_motor_position_rad)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.wheel_motor_position_rad))
      _x = self
      buff.write(_struct_I3f.pack(_x.linear_motor_status, _x.linear_motor_current_A0pk, _x.linear_motor_speed_rps, _x.linear_motor_position_rad))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.wheel_motor_status = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.wheel_motor_current_A0pk = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.wheel_motor_speed_rps = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.wheel_motor_position_rad = struct.unpack(pattern, str[start:end])
      _x = self
      start = end
      end += 16
      (_x.linear_motor_status, _x.linear_motor_current_A0pk, _x.linear_motor_speed_rps, _x.linear_motor_position_rad,) = _struct_I3f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.wheel_motor_status)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.wheel_motor_status.tostring())
      length = len(self.wheel_motor_current_A0pk)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.wheel_motor_current_A0pk.tostring())
      length = len(self.wheel_motor_speed_rps)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.wheel_motor_speed_rps.tostring())
      length = len(self.wheel_motor_position_rad)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.wheel_motor_position_rad.tostring())
      _x = self
      buff.write(_struct_I3f.pack(_x.linear_motor_status, _x.linear_motor_current_A0pk, _x.linear_motor_speed_rps, _x.linear_motor_position_rad))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.wheel_motor_status = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.wheel_motor_current_A0pk = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.wheel_motor_speed_rps = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.wheel_motor_position_rad = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      _x = self
      start = end
      end += 16
      (_x.linear_motor_status, _x.linear_motor_current_A0pk, _x.linear_motor_speed_rps, _x.linear_motor_position_rad,) = _struct_I3f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_I3f = struct.Struct("<I3f")
