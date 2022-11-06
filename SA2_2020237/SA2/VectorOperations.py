from m5.params import *
from m5.SimObject import SimObject

class VectorOperations(SimObject):
    type = 'VectorOperations'
    cxx_header = "learning_gem5/SA2/vector_object.hh"

    t = Param.Latency("ticks")

    cxx_class = "gem5::VectorOperations"
