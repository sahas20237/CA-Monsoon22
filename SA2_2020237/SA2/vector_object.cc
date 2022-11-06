#include "base/trace.hh"
#include "learning_gem5/SA2/vector_object.hh"
#include <iostream>
#include <cmath>
#include "debug/ADDRESULT.hh"
#include "debug/DOTRESULT.hh"
#include "debug/NORMALIZE.hh"
#include "debug/VECTOR.hh"

namespace gem5
{
int A[4][1] = {{1}, {2}, {3}, {4}};
int B[4][1] = {{2}, {3}, {4}, {5}}; 

VectorOperations::VectorOperations(const VectorOperationsParams &params) : 
    SimObject(params), 
    VectorAddition([this]{processEvent1();}, name()),
    VectorDotProduct([this]{processEvent2();}, name()),
    NormalizeVector([this]{processEvent3();}, name()), 
    latency(params.t)
{
    DPRINTF(VECTOR, "Input vector 1: [ %d %d %d %d ] \n", A[0][0], A[1][0], A[2][0], A[3][0]);
    DPRINTF(VECTOR, "Input vector 2: [ %d %d %d %d ] \n", B[0][0], B[1][0], B[2][0], B[3][0]);
}

void
VectorOperations::startup()
{
    schedule(VectorAddition, latency);
    schedule(VectorDotProduct, latency);
    schedule(NormalizeVector, latency);
}

void
VectorOperations::processEvent1()
{
    int sum[4][1] = {{0}, {0}, {0}, {0}};

    for (int i=0; i<4; i++){
        for (int j=0; j<1; j++){
            sum[i][j] = A[i][j] + B[i][j];
        }
    }

    DPRINTF(ADDRESULT, "Output Sum Vector: [ %d %d %d %d ] \n", sum[0][0], sum[1][0], sum[2][0], sum[3][0]);

}

void
VectorOperations::processEvent2()
{
    int dot[4][1] = {{0}, {0}, {0}, {0}};

    for (int i=0; i<4; i++){
        for (int j=0; j<1; j++){
            dot[i][j] = A[i][j]*B[i][j];
        }
    }

    DPRINTF(DOTRESULT, "Output Dot Vector: [ %d %d %d %d ] \n", dot[0][0], dot[1][0], dot[2][0], dot[3][0]);
}

void
VectorOperations::processEvent3()
{
    float nor1[4][1] = {{0}, {0}, {0}, {0}};
    float nor2[4][1] = {{0}, {0}, {0}, {0}};

    float n1 = 0;
    float n2 = 0;
    for (int i=0; i<4; i++){
        for (int j=0; j<1; j++){
            n1 += pow(A[i][j], 2);
            n2 += pow(B[i][j], 2);
        }
    }
    n1 = pow(n1, 0.5);
    n2 = pow(n2, 0.5);
    for (int i=0; i<4; i++){
        for (int j=0; j<1; j++){
            nor1[i][j] = (A[i][j]/n1);
            nor2[i][j] = (B[i][j]/n2);
        }
    }

    DPRINTF(NORMALIZE, "Normalized Vectors: \n");
    DPRINTF(NORMALIZE, "Vector 1: [ %f %f %f %f ] \n", nor1[0][0], nor1[1][0], nor1[2][0], nor1[3][0]);
    DPRINTF(NORMALIZE, "Vector 2: [ %f %f %f %f ] \n", nor2[0][0], nor2[1][0], nor2[2][0], nor2[3][0]);

}
}
