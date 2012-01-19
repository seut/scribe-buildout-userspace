import logging
import os
import fileinput

log = logging.getLogger('fb303-hook')

def premake(options, buildout):
    # import pdb; pdb.set_trace()
    basedir = options['path']
    makefile_list = [os.path.join(basedir, "Makefile"), 
            os.path.join(basedir, "cpp", "Makefile")]

    log.debug('pre-make-hook on %s' % basedir)

    for makefile in makefile_list:
        log.info("fixing path in ``%s``" % makefile)
        
        try:
            os.remove(makefile+"~")
        except:
            pass;
        os.rename(makefile, makefile+"~")
        dst = open(makefile, "w")
        src = open(makefile+"~", "r")
        
        for line in src:
            if "prefix = /usr/local" in line:
                log.debug("... %s" % line)
                line=line.replace('/usr/local', buildout['thrift']['location'])
                log.info(">>> %s" % line)
            dst.write(line)
        fileinput.close()
