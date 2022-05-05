#!/usr/bin/env python

# ============================================================================== #
#                                                                                #
#   (c) Copyright, 2013 University Corporation for Atmospheric Research (UCAR).  #
#       All rights reserved.                                                     #
#                                                                                #
#       File: $RCSfile: fileheader,v $                                           #
#       Version: $Revision: 1.1 $  Dated: $Date: 2013/09/30 14:44:18 $           #
#                                                                                #
# ============================================================================== #

"""
THIS IS A SKELETON OF WHAT A NORMAL PYTHON SCRIPT SHOULD LOOK LIKE
SOME MORE TEXT
"""

import time, os, sys
from datetime import datetime
from optparse import OptionParser
import log_msg

def process(in_file, out_file, logg):
    """
    """

    return

def main():
    usage_str = "%prog in_file output_file"
    parser = OptionParser(usage = usage_str)
    parser.add_option("-l", "--log", dest="log", help="write log messages to specified file")
        
    (options, args) = parser.parse_args()
    
    if len(args) < 2:
        parser.print_help()
        sys.exit(2)

    if options.log:
        logg = log_msg.LogMessage(options.log)
        logg.set_suffix(".asc")
    else:
        logg = log_msg.LogMessage("")
                                  
    in_file = args[0]
    out_file = args[1]

    logg.write_starting()

    process(in_file, out_file, logg)

    logg.write_ending()


if __name__ == "__main__":
    main()
