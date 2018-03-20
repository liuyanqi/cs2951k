// Generated by gencpp from file movo_msgs/LinearActuatorCmd.msg
// DO NOT EDIT!


#ifndef MOVO_MSGS_MESSAGE_LINEARACTUATORCMD_H
#define MOVO_MSGS_MESSAGE_LINEARACTUATORCMD_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace movo_msgs
{
template <class ContainerAllocator>
struct LinearActuatorCmd_
{
  typedef LinearActuatorCmd_<ContainerAllocator> Type;

  LinearActuatorCmd_()
    : header()
    , desired_position_m(0.0)
    , fdfwd_vel_mps(0.0)  {
    }
  LinearActuatorCmd_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , desired_position_m(0.0)
    , fdfwd_vel_mps(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef float _desired_position_m_type;
  _desired_position_m_type desired_position_m;

   typedef float _fdfwd_vel_mps_type;
  _fdfwd_vel_mps_type fdfwd_vel_mps;




  typedef boost::shared_ptr< ::movo_msgs::LinearActuatorCmd_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::movo_msgs::LinearActuatorCmd_<ContainerAllocator> const> ConstPtr;

}; // struct LinearActuatorCmd_

typedef ::movo_msgs::LinearActuatorCmd_<std::allocator<void> > LinearActuatorCmd;

typedef boost::shared_ptr< ::movo_msgs::LinearActuatorCmd > LinearActuatorCmdPtr;
typedef boost::shared_ptr< ::movo_msgs::LinearActuatorCmd const> LinearActuatorCmdConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::movo_msgs::LinearActuatorCmd_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::movo_msgs::LinearActuatorCmd_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::movo_msgs::LinearActuatorCmd_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::movo_msgs::LinearActuatorCmd_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::movo_msgs::LinearActuatorCmd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::movo_msgs::LinearActuatorCmd_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::movo_msgs::LinearActuatorCmd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::movo_msgs::LinearActuatorCmd_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::movo_msgs::LinearActuatorCmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e09ee2452a894d4a26ff82f8c1b80e6a";
  }

  static const char* value(const ::movo_msgs::LinearActuatorCmd_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe09ee2452a894d4aULL;
  static const uint64_t static_value2 = 0x26ff82f8c1b80e6aULL;
};

template<class ContainerAllocator>
struct DataType< ::movo_msgs::LinearActuatorCmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "movo_msgs/LinearActuatorCmd";
  }

  static const char* value(const ::movo_msgs::LinearActuatorCmd_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::movo_msgs::LinearActuatorCmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
float32 desired_position_m\n\
float32 fdfwd_vel_mps\n\
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
";
  }

  static const char* value(const ::movo_msgs::LinearActuatorCmd_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::movo_msgs::LinearActuatorCmd_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.desired_position_m);
      stream.next(m.fdfwd_vel_mps);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct LinearActuatorCmd_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::movo_msgs::LinearActuatorCmd_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::movo_msgs::LinearActuatorCmd_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "desired_position_m: ";
    Printer<float>::stream(s, indent + "  ", v.desired_position_m);
    s << indent << "fdfwd_vel_mps: ";
    Printer<float>::stream(s, indent + "  ", v.fdfwd_vel_mps);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOVO_MSGS_MESSAGE_LINEARACTUATORCMD_H
