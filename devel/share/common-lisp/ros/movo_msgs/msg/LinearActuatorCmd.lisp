; Auto-generated. Do not edit!


(cl:in-package movo_msgs-msg)


;//! \htmlinclude LinearActuatorCmd.msg.html

(cl:defclass <LinearActuatorCmd> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (desired_position_m
    :reader desired_position_m
    :initarg :desired_position_m
    :type cl:float
    :initform 0.0)
   (fdfwd_vel_mps
    :reader fdfwd_vel_mps
    :initarg :fdfwd_vel_mps
    :type cl:float
    :initform 0.0))
)

(cl:defclass LinearActuatorCmd (<LinearActuatorCmd>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LinearActuatorCmd>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LinearActuatorCmd)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movo_msgs-msg:<LinearActuatorCmd> is deprecated: use movo_msgs-msg:LinearActuatorCmd instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <LinearActuatorCmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movo_msgs-msg:header-val is deprecated.  Use movo_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'desired_position_m-val :lambda-list '(m))
(cl:defmethod desired_position_m-val ((m <LinearActuatorCmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movo_msgs-msg:desired_position_m-val is deprecated.  Use movo_msgs-msg:desired_position_m instead.")
  (desired_position_m m))

(cl:ensure-generic-function 'fdfwd_vel_mps-val :lambda-list '(m))
(cl:defmethod fdfwd_vel_mps-val ((m <LinearActuatorCmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movo_msgs-msg:fdfwd_vel_mps-val is deprecated.  Use movo_msgs-msg:fdfwd_vel_mps instead.")
  (fdfwd_vel_mps m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LinearActuatorCmd>) ostream)
  "Serializes a message object of type '<LinearActuatorCmd>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'desired_position_m))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'fdfwd_vel_mps))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LinearActuatorCmd>) istream)
  "Deserializes a message object of type '<LinearActuatorCmd>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'desired_position_m) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'fdfwd_vel_mps) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LinearActuatorCmd>)))
  "Returns string type for a message object of type '<LinearActuatorCmd>"
  "movo_msgs/LinearActuatorCmd")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LinearActuatorCmd)))
  "Returns string type for a message object of type 'LinearActuatorCmd"
  "movo_msgs/LinearActuatorCmd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LinearActuatorCmd>)))
  "Returns md5sum for a message object of type '<LinearActuatorCmd>"
  "e09ee2452a894d4a26ff82f8c1b80e6a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LinearActuatorCmd)))
  "Returns md5sum for a message object of type 'LinearActuatorCmd"
  "e09ee2452a894d4a26ff82f8c1b80e6a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LinearActuatorCmd>)))
  "Returns full string definition for message of type '<LinearActuatorCmd>"
  (cl:format cl:nil "Header header~%float32 desired_position_m~%float32 fdfwd_vel_mps~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LinearActuatorCmd)))
  "Returns full string definition for message of type 'LinearActuatorCmd"
  (cl:format cl:nil "Header header~%float32 desired_position_m~%float32 fdfwd_vel_mps~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LinearActuatorCmd>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LinearActuatorCmd>))
  "Converts a ROS message object to a list"
  (cl:list 'LinearActuatorCmd
    (cl:cons ':header (header msg))
    (cl:cons ':desired_position_m (desired_position_m msg))
    (cl:cons ':fdfwd_vel_mps (fdfwd_vel_mps msg))
))
