Scribe Buildout
===============

This is a sandboxed install of "Scribe". Since now it is aimed 
to work on MacOSX Lion. Should be working on other OSX as well, 
for linux at least the include prefix differs. 

The special thing about this buildout is that it does not install
any global files and has no interaction besides the ports to 
be installed. Of course boost could also be built in buildout
but this seems useless to me. 

Prerequisites
-------------

MacOSX
......

Install all necessary ports::

    sudo port -v install libevent boost

Ubuntu (untested)
.................

Install::
    
    sudo aptitude install libc-client2007e-dev 

Installation
------------

As usual for buildout, do the following two commands to setup the
sandbox::

    python bootstrap.py
    bin/buildout -vvN

Credits
-------

Thanks to that buildout for some nice impressions regarding the
buildout structure: https://bitbucket.org/cykooz/scribe-buildout/

Problems
--------

Since now the compile dies during scribe itself, when thrift and stuff
has been built and is in use. Don't know the reason for that yet - 
I'm not a c++ guy.

Compiling thrift 0.4.0
......................

This helps: change ``->filename( )`` to ``->path( ).filename( ).string( )`` 
http://www.codelain.com/forum/index.php?topic=16462.0 but still there 
is no success.

::

    g++ -DPACKAGE_NAME=\"scribe\" -DPACKAGE_TARNAME=\"scribe\" -DPACKAGE_VERSION=\"1.5.0\" -DPACKAGE_STRING=\"scribe\ 1.5.0\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DPACKAGE=\"scribe\" -DVERSION=\"1.5.0\" -DHAVE_BOOST=/\*\*/ -DHAVE_BOOST_SYSTEM=/\*\*/ -DHAVE_BOOST_FILESYSTEM=/\*\*/ -I.  -I.. -I/Users/andi/project/scribe/parts/thrift/include -I/Users/andi/project/scribe/parts/thrift/include/thrift -I/Users/andi/project/scribe/parts/thrift/include/thrift -I/Users/andi/project/scribe/parts/thrift/include/thrift/fb303 -I/usr/local/include -I/opt/local/include   -I /Users/andi/project/scribe/parts/trift/share  -Wall -O3 -MT scribe_server.o -MD -MP -MF .deps/scribe_server.Tpo -c -o scribe_server.o scribe_server.cpp
    mv -f .deps/scribe_server.Tpo .deps/scribe_server.Po
    g++  -Wall -O3 -L/opt/local/lib -lboost_system-mt -lboost_filesystem-mt  -o scribed store.o store_queue.o conf.o file.o conn_pool.o scribe_server.o   -L/Users/andi/project/scribe/parts/thrift/lib -L/Users/andi/project/scribe/parts/thrift/lib -L/usr/local/lib -lfb303 -lthrift -lthriftnb -levent -lpthread  libscribe.a 
    ld: warning: directory not found for option '-L/usr/local/lib'
    Undefined symbols for architecture x86_64:
      "vtable for apache::thrift::protocol::TBinaryProtocol", referenced from:
          apache::thrift::protocol::TBinaryProtocol::TBinaryProtocol(boost::shared_ptr<apache::thrift::transport::TTransport>)in conn_pool.o
          apache::thrift::protocol::TBinaryProtocol::TBinaryProtocol(boost::shared_ptr<apache::thrift::transport::TTransport>, int, int, bool, bool)in scribe_server.o
      NOTE: a missing vtable usually means the first non-inline virtual member function has no definition.
      "virtual thunk to facebook::fb303::FacebookBase::getName(std::basic_string<char, std::char_traits<char>, std::allocator<char> >&)", referenced from:
          vtable for scribeHandlerin scribe_server.o
          construction vtable for facebook::fb303::FacebookBase-in-scribeHandlerin scribe_server.o
      "virtual thunk to facebook::fb303::FacebookBase::aliveSince()", referenced from:
          vtable for scribeHandlerin scribe_server.o
          construction vtable for facebook::fb303::FacebookBase-in-scribeHandlerin scribe_server.o
     ld: symbol(s) not found for architecture x86_64
    collect2: ld returned 1 exit status
    make[3]: *** [scribed] Error 1
    make[2]: *** [all] Error 2
    make[1]: *** [all-recursive] Error 1
    make: *** [all] Error 2

Thrift 0.5.0
............

::

    g++ -DPACKAGE_NAME=\"scribe\" -DPACKAGE_TARNAME=\"scribe\" -DPACKAGE_VERSION=\"1.5.0\" -DPACKAGE_STRING=\"scribe\ 1.5.0\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DPACKAGE=\"scribe\" -DVERSION=\"1.5.0\" -DHAVE_BOOST=/\*\*/ -DHAVE_BOOST_SYSTEM=/\*\*/ -DHAVE_BOOST_FILESYSTEM=/\*\*/ -I.  -I.. -I/Users/andi/project/scribe/parts/thrift/include -I/Users/andi/project/scribe/parts/thrift/include/thrift -I/Users/andi/project/scribe/parts/thrift/include/thrift -I/Users/andi/project/scribe/parts/thrift/include/thrift/fb303 -I/usr/local/include -I/opt/local/include   -I /Users/andi/project/scribe/parts/trift/share  -Wall -O3 -MT store.o -MD -MP -MF .deps/store.Tpo -c -o store.o store.cpp
    In file included from store.cpp:27:
    scribe_server.h:45: error: conflicting return type specified for ‘virtual scribe::thrift::ResultCode scribeHandler::Log(const std::vector<scribe::thrift::LogEntry, std::allocator<scribe::thrift::LogEntry> >&)’
    ../src/gen-cpp/scribe.h:18: error:   overriding ‘virtual scribe::thrift::ResultCode::type scribe::thrift::scribeIf::Log(const std::vector<scribe::thrift::LogEntry, std::allocator<scribe::thrift::LogEntry> >&)’
    /opt/local/include/boost/system/error_code.hpp:214: warning: ‘boost::system::posix_category’ defined but not used
    /opt/local/include/boost/system/error_code.hpp:215: warning: ‘boost::system::errno_ecat’ defined but not used
    /opt/local/include/boost/system/error_code.hpp:216: warning: ‘boost::system::native_ecat’ defined but not used
    make[3]: *** [store.o] Error 1
    make[2]: *** [all] Error 2
    make[1]: *** [all-recursive] Error 1
    make: *** [all] Error 2
