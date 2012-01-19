import logging
import os
import fileinput

log = logging.getLogger('Makefile-hook')

def premake_303(options, buildout):
    return _premake(options, buildout, 'prefix', '/usr/local', 
            buildout['thrift']['location'])

def premake_scribe(options, buildout):
    return _premake(options, buildout, 'fb303_home', '/usr/local', 
            buildout['thrift']['location'])

def _premake(options, buildout, what, prefix_pattern, replacement):
    basedir = options['path']
    makefile_list = [os.path.join(basedir, "Makefile"), 
            os.path.join(basedir, "cpp", "Makefile"),
            os.path.join(basedir, "py", "Makefile"),
            os.path.join(basedir, "src", "Makefile"),
            ]

    log.debug('pre-make-hook on %s' % basedir)

    for makefile in makefile_list:
        try:
            os.remove(makefile+"~")
        except:
            pass;

        if os.path.exists(makefile):
            log.info("fixing path in ``%s``" % makefile)
            os.rename(makefile, makefile+"~")
            dst = open(makefile, "w")
            src = open(makefile+"~", "r")
            
            for line in src:
                if "%s = %s" % (what, prefix_pattern) in line:
                    log.debug("... %s" % line)
                    line=line.replace(prefix_pattern, replacement)
                    log.info(">>> %s" % line)
                dst.write(line)
            fileinput.close()
