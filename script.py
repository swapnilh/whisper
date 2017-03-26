#!/usr/bin/env python

import argparse
import sys
import os
import time

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
__echo = 'kv-echo/echo/src'
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

__s = 'small'
__m = 'med'
__l = 'large'

size_l = []
size_l.append(__s)
size_l.append(__m)
size_l.append(__l)

parser = argparse.ArgumentParser(prog="script", description="Buildi, Clean, Run, Update WHISPER")
parser.add_argument('-d', dest='downld', action='store_true', default=False, help="Download workload")
parser.add_argument('-b', dest='build', action='store_true', default=False, help="Build workload")
parser.add_argument('-r', dest='run'  , action='store_true', default=False, help="Run workload")
parser.add_argument('-w', dest='workload', default=__emt, help="Workload", choices=workload_l)
parser.add_argument('-z', dest='size', default=__l, help="Set workload size", choices=size_l)
parser.add_argument('-t', dest='trace', action='store_true', default=False, help="Enable tracing. Need to be root.")
parser.add_argument('-c', dest='clean', action='store_true', default=False, help="Clean workload")
parser.add_argument('-s', dest='scratch', action='store_true', default=False, help="Clean workload and dependencies")
parser.add_argument('-u', dest='update', action='store_true', default=False, help="Update benchmark")
parser.add_argument('-p', dest='mhelp', action='store_true', default=False, help="More help for a workload")


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
	
	print '\n' + '>>> ' + s + '\n'

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
	msg(cmd)
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
		
		cd(d)

		if stat('Makefile') == 1:
			cmd = './bootstrap;./configure'
			sh(cmd)

		cmd = 'make'
		sh(cmd)

		cd(__home)
		
	elif w == __tpc:

		d = __nstr
		
		cd(d)

		if stat('Makefile') == 1:
			cmd = './bootstrap;./configure'
			sh(cmd)

		cmd = 'make'
		sh(cmd)

		cd(__home)

	elif w == __eco:

		d = __echo 
		
		cd(d)

		if stat('malloc/gperftools-2.0/Makefile') == 1:
                	cmd = './make-tcmalloc.sh'
                	sh(cmd)

		cmd = 'make clean && make'
		sh(cmd)

		cd(__home)
		
	elif w == __red:
		d = __reds
		
		cd(d)

		cmd = './build.sh'
		sh(cmd)

		cd(__home)

	elif w == __ctr:
		d = __nvml
		
		cd(d)

		cmd = './build.sh'
		sh(cmd)

		cd(__home)

	elif w == __map:
		d = __nvml
		
		cd(d)

		cmd = './build.sh'
		sh(cmd)

		cd(__home)

	elif w == __mem:
		d = __nemo
		
		cd(d)

		cmd = 'scons --build-bench=memcached --config-ftrace'
		sh(cmd)

		cd(__home)

	elif w == __vac:
		d = __nemo
		
		cd(d)

		cmd = 'scons --build-bench=stamp-kozy --config-ftrace'
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
	s = args.scratch
	
	if w == __ycs:

		d = __nstr
		
		cd(d)

		if s is True:
			cmd = './bootstrap;./configure'
			sh(cmd)
			
		cmd = 'make clean'
		sh(cmd)

		cd(__home)
		
	elif w == __tpc:

		d = __nstr
		
		cd(d)

		if s is True:
			cmd = './bootstrap;./configure'
			sh(cmd)

		cmd = 'make clean'
		sh(cmd)

		cd(__home)

	elif w == __eco:

		d = __echo 
		
		cd(d)

		cmd = 'make clean'
		sh(cmd)

		cd(__home)
		
	elif w == __red:
		d = __reds
		
		cd(d)

		cmd = './clean.sh'
		sh(cmd)

		if s is True:
			cmd = 'make distclean'
			sh(cmd)

		cd(__home)

	elif w == __ctr:
		d = __nvml
		
		cd(d)

		cmd = './clean.sh'
		sh(cmd)
		
		if s is True:
			cmd = 'make distclean'
			sh(cmd)

		cd(__home)

	elif w == __map:
		d = __nvml
		
		cd(d)

		cmd = './clean.sh'
		sh(cmd)
		
		if s is True:
			cmd = 'make distclean'
			sh(cmd)

		cd(__home)

	elif w == __mem:
		d = __nemo
		
		cd(d)

		cmd = 'rm -fr build/memcached*/'
		sh(cmd)
		
		if s is True:
			cmd = 'rm -fr build/'
			sh(cmd)

		cd(__home)

	elif w == __vac:
		d = __nemo
		
		cd(d)

		cmd = 'rm -fr build/stamp*/'
		sh(cmd)
		
		if s is True:
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
		
		cd(d)
		cmd = './run.sh -h'
		sh(cmd)
		cd(__home)
		
	elif w == __tpc:

		d = __nstr

		cd(d)
		cmd = './run.sh -h'
		sh(cmd)
		cd(__home)

	elif w == __eco:

		d = __echo 

		cd(d)
		cmd = './run.sh -h'
		sh(cmd)
		cd(__home)
		

	elif w == __red:
		d = __reds

		cd(d)
		cmd = './run-redis-server.sh -h'
		sh(cmd)
		cmd = './run-redis-cli.sh -h'
		sh(cmd)

		cd(__home)

	elif w == __ctr:
		d = __nvml

		cd(d)
		cmd = './run_ctree.sh -h'
		sh(cmd)
		cd(__home)

	elif w == __map:
		d = __nvml

		cd(d)
		cmd = './run_hashmap.sh -h'
		sh(cmd)
		cd(__home)

	elif w == __mem:
		d = __nemo

		cd(d)
		cmd = './run_memcache.sh -h'
		sh(cmd)
		cmd = './run_memslap.sh -h'
		sh(cmd)
		cd(__home)

	elif w == __vac:
		d = __nemo

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

def z2s(z):
	# convert size variable to string
	
	if z not in size_l:
		msg('please pass a valid workload size from ' + str(size_l))
		ex()
	
	return ' --' + z
	
def w2s(w):
	# convert workload variable to string
	
	if w not in workload_l:
		msg('please pass a valid workload from ' + str(workload_l))
		ex()
	
	return ' --' + w

def t2s(t):
	
	# convert trace variable to string
	
	if t is True:
		msg('For trace : $ cat /sys/kernel/debug/trace_pipe')
		return ' --trace'
	else:
		return ''
		
def su(t):
	
	# convert privileges
	
	if t is True:
		msg('Need to be root for trace.')
		return 'sudo '
	else:
		return ''

def sleep(t):
	time.sleep(t)
	
def run(sysargs):
	
	args = sysargs
	w = args.workload
	z = args.size
	t = args.trace
	
	if w == __ycs:

		d = __nstr
		
		cd(d)
		cmd = su(t) + './run.sh' + z2s(z) + w2s(w) + t2s(t)
		dbg(cmd)
		
		sh(cmd)
		cd(__home)
		
	elif w == __tpc:

		d = __nstr

		cd(d)
		cmd = su(t) + './run.sh' + z2s(z) + w2s(w) + t2s(t)
		dbg(cmd)
		
		sh(cmd)
		cd(__home)

	elif w == __eco:

		d = __echo 

		cd(d)
		cmd = su(t) + './run.sh' + z2s(z) + t2s(t)
		dbg(cmd)
		
		sh(cmd)
		cd(__home)
		

	elif w == __red:
		d = __reds

		cd(d)
		

		cmd = su(t) + './run-redis-server.sh' + t2s(t)
		dbg(cmd)
		sh(cmd)
		
		sleep(2)
		msg('starting redis client')
		
		cmd = './run-redis-cli.sh' + z2s(z)
		dbg(cmd)
		sh(cmd)
		
		cmd = su(t) + "kill -s SIGKILL `pgrep redis`"
		sh(cmd)
		
		cd(__home)

	elif w == __ctr:
		d = __nvml

		cd(d)
		cmd = su(t) + './run_ctree.sh' + z2s(z) + t2s(t)

		sh(cmd)
		cd(__home)

	elif w == __map:
		d = __nvml

		cd(d)
		cmd = su(t) + './run_hashmap.sh' + z2s(z) + t2s(t)
		
		sh(cmd)
		cd(__home)

	elif w == __mem:
		d = __nemo

		cd(d)

		cmd = su(t) + './run_memcache.sh' + t2s(t)
		dbg(cmd)
		sh(cmd)
		
		sleep(2)
		msg('starting memslap client')
		
		cmd = './run_memslap.sh' + z2s(z)
		dbg(cmd)
		sh(cmd)
		
		cmd = su(t) + "kill -s SIGKILL `pgrep memcached`"
		sh(cmd)

		cd(__home)

	elif w == __vac:
		d = __nemo

		cd(d)
		cmd = su(t) + './run.sh' + z2s(z) + w2s(w) + t2s(t)
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

	
if __name__ == '__main__':

	w = args.workload
	d = args.downld
	r = args.run
	c = args.clean
	b = args.build
	t = args.trace
	u = args.update
	p = args.mhelp
	
	if d is True:
		cmd='git submodule update --init'
		sh(cmd)

	if u is True:
		cmd='git pull'
		sh(cmd)
		cmd='git submodule update'
		sh(cmd)
		cmd='git submodule status'
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
	
		
	
