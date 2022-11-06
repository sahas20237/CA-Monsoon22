#ifndef __LEARNING_GEM5_VECTOR_OPERATIONS_HH__
#define __LEARNING_GEM5_VECTOR_OPERATIONS_HH__

#include "params/VectorOperations.hh"
#include "sim/sim_object.hh"

namespace gem5 
{

class VectorOperations : public SimObject
{
  private:
    void processEvent1();
    void processEvent2();
    void processEvent3();

    EventFunctionWrapper VectorAddition;
    EventFunctionWrapper VectorDotProduct;
    EventFunctionWrapper NormalizeVector;

    Tick latency;

  public:
    VectorOperations(const VectorOperationsParams &p);

    void startup();
};

}

#endif
