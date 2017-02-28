#!/usr/bin/env python
## HOW TO GET AROUND THE FACT THAT BENCHMARKS AND WORKLOADS ARE DIFFERENT? ADD
## OPTION --variant?
import argparse
import sys
import os
from subprocess import Popen, PIPE

workloads = ['echo', 'tpcc', 'ycsb', 'nvml', 'redis', 'mnemosyne-gcc']

def runCmd(cmd, err, out, display = False):
    """
    Takes two strings, command and error, runs it in the shell
    and then if error string is found in stdout, exits.
    For no output = no error, use err=""
    """
    print cmd
    (stdout, stderr) = Popen(cmd, shell=True, stdout=PIPE).communicate()
    if display:
        print stdout
        if stderr:
            print stderr
    else:        
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
    parser.add_argument('--sim_size', dest='sim_size', action='store', 
            default='test', help='Simulation size: test, small, medium, large')
    parser.add_argument('--variant', dest='variant', action='store', 
            default='default', help='tpcc/ycsb (for echo), hashmap/ctree (for nvml), vacation/memcached (for mnemosyne)')

    args = parser.parse_args()

    if 'all' in args.benchmarks:
        print "Please choose any one benchmark"
        
    for workload in args.benchmarks:
        os.chdir("benchmarks/%s" % (workload,))
        simCmd = "python run.py "
        simCmd += "--sim_size=%s " % (args.sim_size,) 
        simCmd += "%s " % (args.variant, ) 
        runCmd(simCmd, "Error", "Running %s Failed" % (workload,), True)    
        os.chdir("../../")

if __name__ == "__main__":
    main(sys.argv[1:])
