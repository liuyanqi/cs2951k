// Generated by gencpp from file movo_msgs/PanTiltCmd.msg
// DO NOT EDIT!


#ifndef MOVO_MSGS_MESSAGE_PANTILTCMD_H
#define MOVO_MSGS_MESSAGE_PANTILTCMD_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <movo_msgs/PVA.h>
#include <movo_msgs/PVA.h>

namespace movo_msgs
{
template <class ContainerAllocator>
struct PanTiltCmd_
{
  typedef PanTiltCmd_<ContainerAllocator> Type;

  PanTiltCmd_()
    : header()
    , pan_cmd()
    , tilt_cmd()  {
    }
  PanTiltCmd_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , pan_cmd(_alloc)
    , tilt_cmd(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::movo_msgs::PVA_<ContainerAllocator>  _pan_cmd_type;
  _pan_cmd_type pan_cmd;

   typedef  ::movo_msgs::PVA_<ContainerAllocator>  _tilt_cmd_type;
  _tilt_cmd_type tilt_cmd;




  typedef boost::shared_ptr< ::movo_msgs::PanTiltCmd_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::movo_msgs::PanTiltCmd_<ContainerAllocator> const> ConstPtr;

}; // struct PanTiltCmd_

typedef ::movo_msgs::PanTiltCmd_<std::allocator<void> > PanTiltCmd;

typedef boost::shared_ptr< ::movo_msgs::PanTiltCmd > PanTiltCmdPtr;
typedef boost::shared_ptr< ::movo_msgs::PanTiltCmd const> PanTiltCmdConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::movo_msgs::PanTiltCmd_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::movo_msgs::PanTiltCmd_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace movo_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'movo_msgs': ['/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::movo_msgs::PanTiltCmd_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::movo_msgs::PanTiltCmd_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::movo_msgs::PanTiltCmd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::movo_msgs::PanTiltCmd_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::movo_msgs::PanTiltCmd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::movo_msgs::PanTiltCmd_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::movo_msgs::PanTiltCmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "1c8fd5bfa9f9bb5673655828791c82ce";
  }

  static const char* value(const ::movo_msgs::PanTiltCmd_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x1c8fd5bfa9f9bb56ULL;
  static const uint64_t static_value2 = 0x73655828791c82ceULL;
};

template<class ContainerAllocator>
struct DataType< ::movo_msgs::PanTiltCmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "movo_msgs/PanTiltCmd";
  }

  static const char* value(const ::movo_msgs::PanTiltCmd_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::movo_msgs::PanTiltCmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
PVA pan_cmd\n\
PVA tilt_cmd\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: movo_msgs/PVA\n\
float32 pos_rad\n\
float32 vel_rps\n\
float32 acc_rps2\n\
";
  }

  static const char* value(const ::movo_msgs::PanTiltCmd_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::movo_msgs::PanTiltCmd_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.pan_cmd);
      stream.next(m.tilt_cmd);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PanTiltCmd_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::movo_msgs::PanTiltCmd_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::movo_msgs::PanTiltCmd_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "pan_cmd: ";
    s << std::endl;
    Printer< ::movo_msgs::PVA_<ContainerAllocator> >::stream(s, indent + "  ", v.pan_cmd);
    s << indent << "tilt_cmd: ";
    s << std::endl;
    Printer< ::movo_msgs::PVA_<ContainerAllocator> >::stream(s, indent + "  ", v.tilt_cmd);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOVO_MSGS_MESSAGE_PANTILTCMD_H
