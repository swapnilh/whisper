# WHISPER 1.0

**WHISPER**, or **Wisconsin-HPL Suite for Persistence** is a comprehensive benchmark
suite for emerging persistent memory technologies. For more details :

**An Analysis of Persistent Memory Use with WHISPER**. *ASPLOS'17*.

Sanketh Nalli, Swapnil Haria, Mike Swift, Mark Hill, Haris Volos, Kim Keeton.


## IMPORTANT
We are currently testing WHISPER in various environments.
PLEASE USE AT YOUR OWN RISK.
Report issues and suggestions to Swapnil (swapnilh at cs dot wisc edu) or Sanketh (sankey
at cs dot wisc dot edu). 

## To download: 
~~~
   	$ git clone https://github.com/swapnilh/whisper.git
	$ cd whisper
    	$ git submodule update --init
~~~

## To build:
~~~
	$ cd whisper
	$ ./script.py -b -w	{ycsb,tpcc,echo,redis,ctree,hashmap,memcached,vacation,nfs,exim,sql,all}
~~~

## To update:
~~~
	$ cd whisper
	$ git submodule update --remote
~~~


## To run:
~~~
	$ cd whisper
	$ ./script.py -c -z {s|m|l|xl|xxl} -w  {ycsb,tpcc,echo,redis,ctree,hashmap,memcached,vacation,nfs,exim,sql,all}
~~~

## To clean:
~~~
	$ cd whisper
	$ ./script.py -c -w {ycsb,tpcc,echo,redis,ctree,hashmap,memcached,vacation,nfs,exim,sql,all}
~~~

