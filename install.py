#!/usr/bin/env python

import argparse
import sys
import os
from subprocess import Popen, PIPE

workloads = ['echo', 'nstore', 'nvml', 'redis', 'mnemosyne']

def runCmd(cmd, err, out):
    """
    Takes two strings, command and error, runs it in the shell
    and then if error string is found in stdout, exits.
    For no output = no error, use err=""
    """
    print cmd
    (stdout, stderr) = Popen(cmd, shell=True, stdout=PIPE).communicate()
    if err is None:
        if stdout != "":
            print "Error: %s" %(out,)
            print "Truncated stdout below:"
            print '... ', stdout[-500:]
            sys.exit(2)
    else:
        if err in stdout:
            print "Error: %s" %(out,)
            print "Truncated stdout below:"
            print '... ', stdout[-500:]
            sys.exit(2)

def main(argv): 
    """
    Parses the arguments and cleans and/or builds the specified
    workloads of the whisper suite
    """
    parser = argparse.ArgumentParser(description='Build workloads from the whisper suite.')
    parser.add_argument('benchmarks', metavar='workload', type=str, nargs='+',
                help='workloads to be built (use all to build everything):' + ", ".join(workloads))
    parser.add_argument('--clean', dest='clean', action='store_true',
                default='false',
                help='clean')
    parser.add_argument('--build', dest='build', action='store_true',
                default='false',
                help='build')

    args = parser.parse_args()

    if 'all' in args.benchmarks:
        args.benchmarks = workloads
        
    for workload in args.benchmarks:
        os.chdir("benchmarks/%s" % (workload,))
        buildCmd = "python install.py "
        if args.clean == True:
            print "Cleaning " + workload
            buildCmd += "--c "
        if args.build == True:
            buildCmd += "--b "
            print "Building " + workload
        runCmd(buildCmd, "Failed", "Building %s Failed" % (workload,))    
        os.chdir("../../")

if __name__ == "__main__":
    main(sys.argv[1:])
