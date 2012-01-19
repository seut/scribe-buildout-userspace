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

Install all necessary ports::

    sudo port -v install libevent boost

Ubuntu Deps
-----------

Install::
    
    sudo aptitude install libc-client2007e-dev 

Credits
-------

Thanks to that buildout for some nice impressions regarding the
buildout structure: https://bitbucket.org/cykooz/scribe-buildout/

Problems
--------

Since now the compile dies during scribe itself, when thrift and stuff
has been built and is in use. Don't know the reason for that yet - 
I'm not a c++ guy. 
