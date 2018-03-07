// Generated by gencpp from file movo_msgs/Faultlog.msg
// DO NOT EDIT!


#ifndef MOVO_MSGS_MESSAGE_FAULTLOG_H
#define MOVO_MSGS_MESSAGE_FAULTLOG_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace movo_msgs
{
template <class ContainerAllocator>
struct Faultlog_
{
  typedef Faultlog_<ContainerAllocator> Type;

  Faultlog_()
    : data()  {
    }
  Faultlog_(const ContainerAllocator& _alloc)
    : data(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<uint32_t, typename ContainerAllocator::template rebind<uint32_t>::other >  _data_type;
  _data_type data;




  typedef boost::shared_ptr< ::movo_msgs::Faultlog_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::movo_msgs::Faultlog_<ContainerAllocator> const> ConstPtr;

}; // struct Faultlog_

typedef ::movo_msgs::Faultlog_<std::allocator<void> > Faultlog;

typedef boost::shared_ptr< ::movo_msgs::Faultlog > FaultlogPtr;
typedef boost::shared_ptr< ::movo_msgs::Faultlog const> FaultlogConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::movo_msgs::Faultlog_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::movo_msgs::Faultlog_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace movo_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'movo_msgs': ['/home/andrewandjasmine/movo_ws/src/movo_common/movo_msgs/msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::movo_msgs::Faultlog_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::movo_msgs::Faultlog_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::movo_msgs::Faultlog_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::movo_msgs::Faultlog_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::movo_msgs::Faultlog_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::movo_msgs::Faultlog_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::movo_msgs::Faultlog_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a1376ac15481ebcd67c3fe86a75a7d55";
  }

  static const char* value(const ::movo_msgs::Faultlog_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xa1376ac15481ebcdULL;
  static const uint64_t static_value2 = 0x67c3fe86a75a7d55ULL;
};

template<class ContainerAllocator>
struct DataType< ::movo_msgs::Faultlog_<ContainerAllocator> >
{
  static const char* value()
  {
    return "movo_msgs/Faultlog";
  }

  static const char* value(const ::movo_msgs::Faultlog_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::movo_msgs::Faultlog_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint32[] data\n\
";
  }

  static const char* value(const ::movo_msgs::Faultlog_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::movo_msgs::Faultlog_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Faultlog_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::movo_msgs::Faultlog_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::movo_msgs::Faultlog_<ContainerAllocator>& v)
  {
    s << indent << "data[]" << std::endl;
    for (size_t i = 0; i < v.data.size(); ++i)
    {
      s << indent << "  data[" << i << "]: ";
      Printer<uint32_t>::stream(s, indent + "  ", v.data[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOVO_MSGS_MESSAGE_FAULTLOG_H
