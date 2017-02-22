# WHISPER 1.0

**WHISPER**, or **Wisconsin-HPL Suite for Persistence** is a comprehensive benchmark
suite for emerging persistent memory technologies. *Persistent Memory* (PM) is
non-volatile memory accessed with byte addressability (not just blocks) at low
latency (not I/O bus) via regular memory instructions (not system calls).
WHISPER captures unique properties of PM applications establishing a firm
foundation for the design of future hardware and software systems for persistent
memory. It covers a wide variety of interfaces to PM including custom PM
key-value stores Echo and Redis, a PM database N-store, PM transactional
libraries Mnemosyne and NVML and a PM filesystem PMFS. We developed Eliza and a
framework, to analyze WHISPER applications which can easily be used to analyze
future PM interfaces. Please read our
[paper](http://research.cs.wisc.edu/multifacet/papers/asplos17_whisper.pdf) for
more details. Contact Swapnil (swapnilh at cs dot wisc edu) or Sanketh (sankey
at cs dot wisc dot edu) for details.

## Download instructions
We use git submodules to track each of the individual applications of the suite.
As such, simply doing 'git clone' only retrieves the wrapper repo, and not
each of the workloads. Follow these steps to download **WHISPER**.

    git clone https://github.com/swapnilh/whisper
    cd whisper
    git submodule update --init
    python install.py -h


## Install instructions
We have provided a simple install.py which handles installation and cleans of
the individual workloads. It can be run as :

    python install.py <workloadA workloadB ..> --build --clean

List of workloads: ['echo', 'nstore', 'nvml', 'redis', 'mnemosyne']
Use all to build all the workloads.

Examples:
For a clean build of all workloads:
    python install.py all --build --clean

For simply building echo and nvml:
    python install.py echo nvml --build
