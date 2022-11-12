# Name: Sahas Marwah
# Roll Number: 2020237
# CA Assignment 1

# Reference for this assignemt: 
# 1. https://www.gem5.org/documentation/learning_gem5/part1/cache_config/
# 2. Hennesy and Patterson Edition 5 and class slides

# Import gem5 library
import m5 
from m5.objects import * 

# Cache Implementations
##############################################################################
# Creating L1 Cache
class L1Cache(Cache):  
    # Main parameters  
    assoc = 2
    tag_latency = 2
    data_latency = 2
    response_latency = 2

    # Other parameters
    mshrs = 4
    tgts_per_mshr = 20

    def connectBus(self, bus):
        self.mem_side = bus.cpu_side_ports

# Making L1I cache using L1 cache
class L1ICache(L1Cache):
    size = '16kB'
    def connectCPU(self, cpu):
        self.cpu_side = cpu.icache_port

# Making L1D cache using L1 cache
class L1DCache(L1Cache):
    size = '16kB'
    def connectCPU(self, cpu):
        self.cpu_side = cpu.dcache_port

# Creating L2 Cache
class L2Cache(Cache):
    # Main parameters
    size = '256kB'
    assoc = 1
    tag_latency = 10
    data_latency = 10
    response_latency = 10

    # Other parameters
    mshrs = 20
    tgts_per_mshr = 12

    def connectCPUSideBus(self, bus):
        self.cpu_side = bus.mem_side_ports

    def connectMemSideBus(self, bus):
        self.mem_side = bus.cpu_side_ports
##########################################################################

# Creating the system to simulate
system = System()

# Setting the clock frequency of the system
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain()

# Setting the memory system
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

# Creating a simple CPU
system.cpu = TimingSimpleCPU()

system.cpu.icache = L1ICache()
system.cpu.dcache = L1DCache()

system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)

system.l2bus = L2XBar()

system.cpu.icache.connectBus(system.l2bus)
system.cpu.dcache.connectBus(system.l2bus)

system.l2cache = L2Cache()
system.l2cache.connectCPUSideBus(system.l2bus)

# Creating a memory bus
system.membus = SystemXBar()

system.l2cache.connectMemSideBus(system.membus)

# For x86 only, make sure the interrupts are connected to the memory
# Note: these are directly connected to the memory bus and are not cached
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

# Creating DDR3 memory controller and connecting it to the membus
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

# Connecting system to the membus
system.system_port = system.membus.cpu_side_ports

# Getting the ISA
isa = 'x86'

# binary = 'tests/test'
binary = 'configs/mibench/automotive/qsort/outfile'
inputfile = 'configs/mibench/automotive/qsort/input_small.dat'

system.workload = SEWorkload.init_compatible(binary)

# Creating a process for application
process = Process()
#Setting the command for executables
process.cmd = [binary, inputfile]
# Setting up the CPU to use the process as its workload
system.cpu.workload = process
# Creating thread contexts
system.cpu.createThreads()

# Setting up root SimObjects and start the simulation
root = Root(full_system = False, system = system)
m5.instantiate()

print("Beginning simulation!")
exit_event = m5.simulate()
print('Exiting @ tick {} because {}'.format(m5.curTick(), exit_event.getCause()))