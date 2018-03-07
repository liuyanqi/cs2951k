// Generated by gencpp from file movo_msgs/Dynamics.msg
// DO NOT EDIT!


#ifndef MOVO_MSGS_MESSAGE_DYNAMICS_H
#define MOVO_MSGS_MESSAGE_DYNAMICS_H


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
struct Dynamics_
{
  typedef Dynamics_<ContainerAllocator> Type;

  Dynamics_()
    : header()
    , x_vel_target_mps(0.0)
    , y_vel_target_mps(0.0)
    , yaw_rate_target_rps(0.0)
    , linear_actuator_target_m(0.0)
    , x_vel_limit_mps(0.0)
    , y_vel_limit_mps(0.0)
    , yaw_rate_limit_rps(0.0)
    , linear_actuator_vel_limit_mps(0.0)
    , wheel_vel_mps()
    , wheel_pos_m()
    , linear_actuator_vel_mps(0.0)
    , linear_actuator_position_m(0.0)
    , x_accel_mps2(0.0)
    , y_accel_mps2(0.0)
    , yaw_accel_mps2(0.0)
    , yaw_angle_rad(0.0)
    , odom_yaw_angle_rad(0.0)  {
    }
  Dynamics_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , x_vel_target_mps(0.0)
    , y_vel_target_mps(0.0)
    , yaw_rate_target_rps(0.0)
    , linear_actuator_target_m(0.0)
    , x_vel_limit_mps(0.0)
    , y_vel_limit_mps(0.0)
    , yaw_rate_limit_rps(0.0)
    , linear_actuator_vel_limit_mps(0.0)
    , wheel_vel_mps(_alloc)
    , wheel_pos_m(_alloc)
    , linear_actuator_vel_mps(0.0)
    , linear_actuator_position_m(0.0)
    , x_accel_mps2(0.0)
    , y_accel_mps2(0.0)
    , yaw_accel_mps2(0.0)
    , yaw_angle_rad(0.0)
    , odom_yaw_angle_rad(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef float _x_vel_target_mps_type;
  _x_vel_target_mps_type x_vel_target_mps;

   typedef float _y_vel_target_mps_type;
  _y_vel_target_mps_type y_vel_target_mps;

   typedef float _yaw_rate_target_rps_type;
  _yaw_rate_target_rps_type yaw_rate_target_rps;

   typedef float _linear_actuator_target_m_type;
  _linear_actuator_target_m_type linear_actuator_target_m;

   typedef float _x_vel_limit_mps_type;
  _x_vel_limit_mps_type x_vel_limit_mps;

   typedef float _y_vel_limit_mps_type;
  _y_vel_limit_mps_type y_vel_limit_mps;

   typedef float _yaw_rate_limit_rps_type;
  _yaw_rate_limit_rps_type yaw_rate_limit_rps;

   typedef float _linear_actuator_vel_limit_mps_type;
  _linear_actuator_vel_limit_mps_type linear_actuator_vel_limit_mps;

   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _wheel_vel_mps_type;
  _wheel_vel_mps_type wheel_vel_mps;

   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _wheel_pos_m_type;
  _wheel_pos_m_type wheel_pos_m;

   typedef float _linear_actuator_vel_mps_type;
  _linear_actuator_vel_mps_type linear_actuator_vel_mps;

   typedef float _linear_actuator_position_m_type;
  _linear_actuator_position_m_type linear_actuator_position_m;

   typedef float _x_accel_mps2_type;
  _x_accel_mps2_type x_accel_mps2;

   typedef float _y_accel_mps2_type;
  _y_accel_mps2_type y_accel_mps2;

   typedef float _yaw_accel_mps2_type;
  _yaw_accel_mps2_type yaw_accel_mps2;

   typedef float _yaw_angle_rad_type;
  _yaw_angle_rad_type yaw_angle_rad;

   typedef float _odom_yaw_angle_rad_type;
  _odom_yaw_angle_rad_type odom_yaw_angle_rad;




  typedef boost::shared_ptr< ::movo_msgs::Dynamics_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::movo_msgs::Dynamics_<ContainerAllocator> const> ConstPtr;

}; // struct Dynamics_

typedef ::movo_msgs::Dynamics_<std::allocator<void> > Dynamics;

typedef boost::shared_ptr< ::movo_msgs::Dynamics > DynamicsPtr;
typedef boost::shared_ptr< ::movo_msgs::Dynamics const> DynamicsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::movo_msgs::Dynamics_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::movo_msgs::Dynamics_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace movo_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'movo_msgs': ['/home/andrewandjasmine/movo_ws/src/movo_common/movo_msgs/msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::movo_msgs::Dynamics_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::movo_msgs::Dynamics_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::movo_msgs::Dynamics_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::movo_msgs::Dynamics_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::movo_msgs::Dynamics_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::movo_msgs::Dynamics_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::movo_msgs::Dynamics_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dd32431766932850de2062a4263871b4";
  }

  static const char* value(const ::movo_msgs::Dynamics_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xdd32431766932850ULL;
  static const uint64_t static_value2 = 0xde2062a4263871b4ULL;
};

template<class ContainerAllocator>
struct DataType< ::movo_msgs::Dynamics_<ContainerAllocator> >
{
  static const char* value()
  {
    return "movo_msgs/Dynamics";
  }

  static const char* value(const ::movo_msgs::Dynamics_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::movo_msgs::Dynamics_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
float32 x_vel_target_mps\n\
float32 y_vel_target_mps\n\
float32 yaw_rate_target_rps\n\
float32 linear_actuator_target_m\n\
float32 x_vel_limit_mps\n\
float32 y_vel_limit_mps\n\
float32 yaw_rate_limit_rps\n\
float32 linear_actuator_vel_limit_mps\n\
float32[] wheel_vel_mps\n\
float32[] wheel_pos_m\n\
float32 linear_actuator_vel_mps\n\
float32 linear_actuator_position_m\n\
float32 x_accel_mps2\n\
float32 y_accel_mps2\n\
float32 yaw_accel_mps2\n\
float32 yaw_angle_rad\n\
float32 odom_yaw_angle_rad\n\
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

  static const char* value(const ::movo_msgs::Dynamics_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::movo_msgs::Dynamics_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.x_vel_target_mps);
      stream.next(m.y_vel_target_mps);
      stream.next(m.yaw_rate_target_rps);
      stream.next(m.linear_actuator_target_m);
      stream.next(m.x_vel_limit_mps);
      stream.next(m.y_vel_limit_mps);
      stream.next(m.yaw_rate_limit_rps);
      stream.next(m.linear_actuator_vel_limit_mps);
      stream.next(m.wheel_vel_mps);
      stream.next(m.wheel_pos_m);
      stream.next(m.linear_actuator_vel_mps);
      stream.next(m.linear_actuator_position_m);
      stream.next(m.x_accel_mps2);
      stream.next(m.y_accel_mps2);
      stream.next(m.yaw_accel_mps2);
      stream.next(m.yaw_angle_rad);
      stream.next(m.odom_yaw_angle_rad);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Dynamics_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::movo_msgs::Dynamics_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::movo_msgs::Dynamics_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "x_vel_target_mps: ";
    Printer<float>::stream(s, indent + "  ", v.x_vel_target_mps);
    s << indent << "y_vel_target_mps: ";
    Printer<float>::stream(s, indent + "  ", v.y_vel_target_mps);
    s << indent << "yaw_rate_target_rps: ";
    Printer<float>::stream(s, indent + "  ", v.yaw_rate_target_rps);
    s << indent << "linear_actuator_target_m: ";
    Printer<float>::stream(s, indent + "  ", v.linear_actuator_target_m);
    s << indent << "x_vel_limit_mps: ";
    Printer<float>::stream(s, indent + "  ", v.x_vel_limit_mps);
    s << indent << "y_vel_limit_mps: ";
    Printer<float>::stream(s, indent + "  ", v.y_vel_limit_mps);
    s << indent << "yaw_rate_limit_rps: ";
    Printer<float>::stream(s, indent + "  ", v.yaw_rate_limit_rps);
    s << indent << "linear_actuator_vel_limit_mps: ";
    Printer<float>::stream(s, indent + "  ", v.linear_actuator_vel_limit_mps);
    s << indent << "wheel_vel_mps[]" << std::endl;
    for (size_t i = 0; i < v.wheel_vel_mps.size(); ++i)
    {
      s << indent << "  wheel_vel_mps[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.wheel_vel_mps[i]);
    }
    s << indent << "wheel_pos_m[]" << std::endl;
    for (size_t i = 0; i < v.wheel_pos_m.size(); ++i)
    {
      s << indent << "  wheel_pos_m[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.wheel_pos_m[i]);
    }
    s << indent << "linear_actuator_vel_mps: ";
    Printer<float>::stream(s, indent + "  ", v.linear_actuator_vel_mps);
    s << indent << "linear_actuator_position_m: ";
    Printer<float>::stream(s, indent + "  ", v.linear_actuator_position_m);
    s << indent << "x_accel_mps2: ";
    Printer<float>::stream(s, indent + "  ", v.x_accel_mps2);
    s << indent << "y_accel_mps2: ";
    Printer<float>::stream(s, indent + "  ", v.y_accel_mps2);
    s << indent << "yaw_accel_mps2: ";
    Printer<float>::stream(s, indent + "  ", v.yaw_accel_mps2);
    s << indent << "yaw_angle_rad: ";
    Printer<float>::stream(s, indent + "  ", v.yaw_angle_rad);
    s << indent << "odom_yaw_angle_rad: ";
    Printer<float>::stream(s, indent + "  ", v.odom_yaw_angle_rad);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOVO_MSGS_MESSAGE_DYNAMICS_H
