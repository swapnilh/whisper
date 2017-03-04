# WHISPER 1.0

**WHISPER**, or **Wisconsin-HPL Suite for Persistence** is a comprehensive benchmark
suite for emerging persistent memory technologies. For more details :

An Analysis of Persistent Memory Use with WHISPER. ASPLOS'17.

Sanketh Nalli, Swapnil Haria, Mike Swift, Mark Hill, Haris Volos, Kim Keeton.


## IMPORTANT
We are currently testing WHISPER in various environments.
PLEASE USE AT YOUR OWN RISK.
Report issues and suggestions to Swapnil (swapnilh at cs dot wisc edu) or Sanketh (sankey
at cs dot wisc dot edu). 

## Dependencies
glib2-devel or libglib2.0-dev
libtoolize
librpmem

## To download: 
~~~
    git clone https://github.com/swapnilh/whisper.git
    cd whisper
    git submodule update --init
~~~

## To build:
~~~
	$ cd whisper
	$ ./script.py -b -w {all,ycsb,tpcc,echo,redis,ctree,hashmap,memcached,vacation}
~~~

## To run:
~~~
	$ cd whisper
	$ ./script.py -r -z {s|m|l} -w {ycsb,tpcc,echo,redis,ctree,hashmap,memcached,vacation}
~~~

## To clean:
~~~
	$ cd whisper
	$ ./script.py -c -w {all,ycsb,tpcc,echo,redis,ctree,hashmap,memcached,vacation}
~~~

