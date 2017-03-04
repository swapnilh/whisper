#!/usr/bin/env python

import argparse
import sys
import os

DBG = 0

__ycs = 'ycsb'
__tpc = 'tpcc'
__eco = 'echo'
__red = 'redis'
__ctr = 'ctree'
__map = 'hashmap'
__mem = 'memcached'
__vac = 'vacation'
__nfs = 'nfs'
__exm = 'exim'
__sql = 'sql'
__all = 'all'
__emt = 'empty'

workload_l = []
workload_l.append(__ycs)
workload_l.append(__tpc)
workload_l.append(__eco)
workload_l.append(__red)
workload_l.append(__ctr)
workload_l.append(__map)
workload_l.append(__mem)
workload_l.append(__vac)
workload_l.append(__nfs)
workload_l.append(__exm)
workload_l.append(__sql)
workload_l.append(__all)

__home = os.getcwd()
__nstr = 'nstore'
__echo = 'echo-kv/echo/src'
__nemo = 'mnemosyne-gcc/usermode'
__nvml = 'nvml'
__reds = 'redis'
__pmfs = 'PMFS-new'

dir_l = []
dir_l.append(__nstr)
dir_l.append(__echo)
dir_l.append(__nemo)
dir_l.append(__nvml)
dir_l.append(__reds)
dir_l.append(__pmfs)

__l = 'l'
__xl = 'xl'
__xxl = 'xxl'

size_l = []
size_l.append(__l)
size_l.append(__xl)
size_l.append(__xxl)

parser = argparse.ArgumentParser(prog="script", description="Buildi, Clean, Run, Update WHISPER")
parser.add_argument('-b', dest='build', action='store_true', default=False, help="Build workload")
parser.add_argument('-r', dest='run'  , action='store_true', default=False, help="Run workload")
parser.add_argument('-w', dest='workload', default=__emt, help="Workload", choices=workload_l)
parser.add_argument('-z', dest='size', default=__l, help="Set workload size", choices=size_l)
parser.add_argument('-t', dest='trace', action='store_true', default=False, help="Enable tracing. Need to be root.")
parser.add_argument('-c', dest='clean', action='store_true', default=False, help="Clean workload")
parser.add_argument('-u', dest='update', action='store_true', default=False, help="Update benchmark")
parser.add_argument('-p', dest='mhelp', action='store_true', default=False)


try:
	args = parser.parse_args()
except:
	sys.exit(0)

def ex():
	sys.exit(0)
	
def dbg(s):
	
	if DBG == 1:
		print s
	
def msg(s):
	
	print s

def cd(dirt):
	
	dbg(dirt)
	
	if dirt == __home:
		os.chdir(__home);
	else:
	
		path = __home + '/' + dirt
		dbg(path)
		
		try:
			os.chdir(path)
		except:
			print 'invalid directory ', path
			sys.exit(0)
	
def sh(cmd):
	
	dbg(cmd)
	try:
		os.system(cmd)
	except:
		print 'invalid cmd ', cmd
		sys.exit(0)
			
def stat(f):
	
	dbg(os.getcwd() + '/' + f)
	try:
		os.stat(f)
	except:
		dbg('invalid file' + os.getcwd() + '/' + f)
		return 1
	
	return 0
	
def build(sysargs):
	
	args = sysargs
	w = args.workload
	
	if w == __ycs:

		d = __nstr
		dbg(d + ',' + w)
		
		cd(d)

		if stat('Makefile') == 1:
			cmd = './bootstrap;./configure'
			sh(cmd)

		cmd = 'make'
		sh(cmd)

		cd(__home)
		
	elif w == __tpc:

		d = __nstr
		dbg(d + ',' + w)
		
		cd(d)

		if stat('Makefile') == 1:
			cmd = './bootstrap;./configure'
			sh(cmd)

		cmd = 'make'
		sh(cmd)

		cd(__home)

	elif w == __eco:

		d = __echo 
		dbg(d + ',' + w)
		
		cd(d)

		if stat('malloc/gperftools-2.0/Makefile') == 1:
			cmd = './make-tcmalloc.sh'
			sh(cmd)

		cmd = 'make clean && make'
		sh(cmd)

		cd(__home)
		
	elif w == __red:
		d = __reds
		dbg(d + ',' + w)
		
		cd(d)

		cmd = './build.sh'
		sh(cmd)

		cd(__home)

	elif w == __ctr:
		d = __nvml
		dbg(d + ',' + w)
		
		cd(d)

		cmd = './build.sh'
		sh(cmd)

		cd(__home)

	elif w == __map:
		d = __nvml
		dbg(d + ',' + w)
		
		cd(d)

		cmd = './build.sh'
		sh(cmd)

		cd(__home)

	elif w == __mem:
		d = __nemo
		dbg(d + ',' + w)
		
		cd(d)

		cmd = 'scons --build-bench=memcached'
		sh(cmd)

		cd(__home)

	elif w == __vac:
		d = __nemo
		dbg(d + ',' + w)
		
		cd(d)

		cmd = 'scons --build-bench=stamp-kozy'
		sh(cmd)

		cd(__home)

	elif w == __nfs:
		d = __pmfs
		msg('please visit github.com/snalli/PMFS-new');
	elif w == __exm:
		d = __pmfs
		msg('please visit github.com/snalli/PMFS-new');
	elif w == __sql:
		d = __pmfs
		msg('please visit github.com/snalli/PMFS-new');
	else:
		return

def clean(sysargs):
	
	args = sysargs
	w = args.workload
	
	if w == __ycs:

		d = __nstr
		dbg(d + ',' + w)
		
		cd(d)

		if stat('Makefile') == 1:
			cmd = './bootstrap;./configure'
			sh(cmd)

		cmd = 'make clean'
		sh(cmd)

		cd(__home)
		
	elif w == __tpc:

		d = __nstr
		dbg(d + ',' + w)
		
		cd(d)

		if stat('Makefile') == 1:
			cmd = './bootstrap;./configure'
			sh(cmd)

		cmd = 'make clean'
		sh(cmd)

		cd(__home)

	elif w == __eco:

		d = __echo 
		dbg(d + ',' + w)
		
		cd(d)

		if stat('malloc/gperftools-2.0/Makefile') == 1:
			cmd = './make-tcmalloc.sh'
			sh(cmd)

		cmd = 'make clean'
		sh(cmd)

		cd(__home)
		
	elif w == __red:
		d = __reds
		dbg(d + ',' + w)
		
		cd(d)

		cmd = './clean.sh'
		sh(cmd)

		cd(__home)

	elif w == __ctr:
		d = __nvml
		dbg(d + ',' + w)
		
		cd(d)

		cmd = './clean.sh'
		sh(cmd)

		cd(__home)

	elif w == __map:
		d = __nvml
		dbg(d + ',' + w)
		
		cd(d)

		cmd = './clean.sh'
		sh(cmd)

		cd(__home)

	elif w == __mem:
		d = __nemo
		dbg(d + ',' + w)
		
		cd(d)

		cmd = 'rm -fr build/'
		sh(cmd)

		cd(__home)

	elif w == __vac:
		d = __nemo
		dbg(d + ',' + w)
		
		cd(d)

		cmd = 'rm -fr build/'
		sh(cmd)

		cd(__home)

	elif w == __nfs:
		d = __pmfs
		msg('please visit github.com/snalli/PMFS-new');
	elif w == __exm:
		d = __pmfs
		msg('please visit github.com/snalli/PMFS-new');
	elif w == __sql:
		d = __pmfs
		msg('please visit github.com/snalli/PMFS-new');
	else:
		return
		
def more_help(sysargs):
	
	args = sysargs
	w = args.workload
	
	if w == __ycs:

		d = __nstr
		dbg(d + ',' + w)
		
		cd(d)
		cmd = './run.sh -h'
		sh(cmd)
		cd(__home)
		
	elif w == __tpc:

		d = __nstr
		dbg(d + ',' + w)

		cd(d)
		cmd = './run.sh -h'
		sh(cmd)
		cd(__home)

	elif w == __eco:

		d = __echo 
		dbg(d + ',' + w)

		cd(d)
		cmd = './run.sh -h'
		sh(cmd)
		cd(__home)
		

	elif w == __red:
		d = __reds
		dbg(d + ',' + w)

		cd(d)
		cmd = './run-redis-server.sh -h'
		sh(cmd)
		cmd = './run-redis-cli.sh -h'
		sh(cmd)

		cd(__home)

	elif w == __ctr:
		d = __nvml
		dbg(d + ',' + w)

		cd(d)
		cmd = './run_ctree.sh -h'
		sh(cmd)
		cd(__home)

	elif w == __map:
		d = __nvml
		dbg(d + ',' + w)

		cd(d)
		cmd = './run_hashmap.sh -h'
		sh(cmd)
		cd(__home)

	elif w == __mem:
		d = __nemo
		dbg(d + ',' + w)

		cd(d)
		cmd = './run_memcache.sh -h'
		sh(cmd)
		cmd = './run_memslap.sh -h'
		sh(cmd)
		cd(__home)

	elif w == __vac:
		d = __nemo
		dbg(d + ',' + w)

		cd(d)
		cmd = './run_vacation.sh -h'
		sh(cmd)
		cd(__home)


	elif w == __nfs:
		d = __pmfs
		msg('please visit github.com/snalli/PMFS-new');
	elif w == __exm:
		d = __pmfs
		msg('please visit github.com/snalli/PMFS-new');
	elif w == __sql:
		d = __pmfs
		msg('please visit github.com/snalli/PMFS-new');
	else:
		return

def run(sysargs):
	
	args = sysargs
	w = args.workload
	
	print w
	
if __name__ == '__main__':

	w = args.workload
	r = args.run
	c = args.clean
	b = args.build
	t = args.trace
	u = args.update
	p = args.mhelp
	
	if u is True:
		cmd='git submodule update --remote'
		msg(cmd)
		sh(cmd)
		cmd='git submodule status'
		msg(cmd)
		sh(cmd)
		ex()
	
	if p is True:
		more_help(args)
	
	if r is True:
		if w == __all:
			dbg("You can run only one workload at a time.")
			sys.exit(0);
		else:
			if c is True:
				clean(args)
			if b is True:
				build(args)
				
		run(args)
			
	if c is True:
		if w == __all:
			for w in workload_l:
				args.workload = w
				clean(args)
		else:
			clean(args)

	if b is True:
		if w == __all:
			for w in workload_l:
				args.workload = w
				build(args)
		else:
			build(args)
	
		
	
