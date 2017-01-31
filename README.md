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
