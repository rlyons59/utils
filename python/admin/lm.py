#!/usr/bin/python
#
# Utils is always imported first
#

def main():
    #import lank.utils
    # print (logfile)'
    #lank.utils.logit("hello",1,"crit")
    
    #from lank import utils
    #import utils
    #utils.init()
    #utils.hello()
    #utils.logit("hello","critical")
    #utils.logit("hello","error")
    #utils.logit("hello","warning")
    #utils.logit("hello","info")
    #utils.logit("hello","debug")
    
    #utils.runcmd('ps -eaf')
    #utils.runcmd('ifconfig -a')

    # OO Programming

    # we set PYTHONPATH env variable
    #import sys
    #sys.path.append('/u/gitwork/utils/python/admin/lank')

    import obj_utils

    mylog = obj_utils.logme()
    mylog.critical('Critical Message')
    mylog.error('Error Message')
    mylog.warning('Warning Message')

if __name__ == "__main__":
    main()