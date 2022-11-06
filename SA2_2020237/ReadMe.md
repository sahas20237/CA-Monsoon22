# SA2 - Computer Architecture Monsoon 2022

Name: Sahas Marwah  
Roll Number: 2020237

## Overview of files

There are two main folders paths in the project namely  

    gem5/src/learning_gem5/SA2

and 
    
    gem5/configs/learning_gem5/SA2

The former should contain 4 files namely  
* VectorOperations.py  
* vector_object.hh  
* vector_object.cc  
* SConscript  

and the latter should contain only 1 file  
* run_vectoroperations.py


## Logistics

First _COPY_ the SA2 folder from here and put it into ```gem5/src/learning_gem5/``` folder on your system and remove any part2 folder in that place if any.
    
Then go to ```gem5/configs/learning_gem5/``` on the command line and write the following  commands:  
    
    mkdir SA2
    cd SA2

Now, _COPY_ the ```run_vectoroperations.py``` file from here and put it into ```gem5/configs/learning_gem5/SA2``` folder on your system, also remove any part2 folder in that place if any.


## Running the Scripts

Now when you match the description given in [Overview of files](#Overview-of-files) you can start running and building the files.  

To get started, go to ```gem5/``` directory and write the following command to build  

    scons build/X86/gem5.opt

(Optional) We can also build our ```run_vectoroperations.py``` file just to check everything is fine. For that run the following command:  

    build/X86/gem5.opt configs/learning_gem5/SA2/run_vectoroperations.py 

After the building has been completed, we can test the _FLAGS_  

There are 4 commands to test the four flags  
Run the commands _ONE BY ONE_ as we have to give tick rate _inputs_ after every command

    build/X86/gem5.opt --debug-flags=VECTOR configs/learning_gem5/SA2/run_vectoroperations.py

    build/X86/gem5.opt --debug-flags=ADDRESULT configs/learning_gem5/SA2/run_vectoroperations.py

    build/X86/gem5.opt --debug-flags=DOTRESULT configs/learning_gem5/SA2/run_vectoroperations.py

    build/X86/gem5.opt --debug-flags=NORMALIZE configs/learning_gem5/SA2/run_vectoroperations.py


After running any 1 of the 4 commands, you will be prompted to  

    Enter ticks:  

Enter a string like: ```2ns``` for 2000 cycles or ```10ns``` for 10000 cycle catch.

## Some sample input/output:  


    gem5 Simulator System.  https://www.gem5.org
    gem5 is copyrighted software; use the --copyright option for details.

    gem5 version 22.0.0.2
    gem5 compiled Nov  5 2022 03:47:09
    gem5 started Nov  5 2022 11:12:24
    gem5 executing on LAPTOP-SAHAS, pid 4771
    command line: build/X86/gem5.opt --debug flags=ADDRESULT configs/learning_gem5/SA2/run_vectoroperations.py

    Enter ticks: 2ns
    Global frequency set at 1000000000000 ticks per second
    warn: No dot file generated. Please install pydot to generate the dot file and pdf.
    Beginning simulation!
    build/X86/sim/simulate.cc:194: info: Entering event queue @ 0.  Starting simulation...
       2000: hello: Output Sum Vector: [ 3 5 7 9 ] 
    Exiting @ tick 18446744073709551615 because simulate() limit reached

------

    command line: build/X86/gem5.opt --debug-flags=VECTOR configs/learning_gem5/SA2/run_vectoroperations.py  

    Enter ticks: 0ns
    Global frequency set at 1000000000000 ticks per second
    warn: No dot file generated. Please install pydot to generate the dot file and pdf.
      0: hello: Input vector 1: [ 1 2 3 4 ] 
      0: hello: Input vector 2: [ 2 3 4 5 ] 
    Beginning simulation!
    build/X86/sim/simulate.cc:194: info: 
    Entering event queue @ 0.  Starting simulation...
    Exiting @ tick 18446744073709551615 because simulate() limit reached

------

    command line: build/X86/gem5.opt --debug-flags=DOTRESULT configs/learning_gem5/SA2/run_vectoroperations.py

    Enter ticks: 3ns
    Global frequency set at 1000000000000 ticks per second
    warn: No dot file generated. Please install pydot to generate the dot file and pdf.
    Beginning simulation!
    build/X86/sim/simulate.cc:194: info: 
    Entering event queue @ 0.  Starting simulation...
       3000: hello: Output Dot Vector: [ 2 6 12 20 ] 
    Exiting @ tick 18446744073709551615 because simulate() limit reached

------

    command line: build/X86/gem5.opt --debug-flags=NORMALIZE configs/learning_gem5/SA2/run_vectoroperations.py

    Enter ticks: 10ns
    Global frequency set at 1000000000000 ticks per second
    warn: No dot file generated. Please install pydot to generate the dot file and pdf.
    Beginning simulation!
    build/X86/sim/simulate.cc:194: info: 
    Entering event queue @ 0.  Starting simulation...
      10000: hello: Normalized Vectors: 
      10000: hello: Vector 1: [ 0.182574 0.365148 0.547723 0.730297 ] 
      10000: hello: Vector 2: [ 0.272166 0.408248 0.544331 0.680414 ] 
    Exiting @ tick 18446744073709551615 because simulate() limit reached

## Understanding the Code
Use of files:  
* The ```VectorOperations.py``` contains class of our object where we can define the parameters. As it is a .py file, it can be controlled from the python configuration files. 

* The ```.hh``` file is the header file for the ```.cc``` file. Here we declare our object class and initialize all functions that we are going to use. 

* The ```.cc``` file is the so called main file where we write the actual code. Here we also implement the constructor for our object, schedule events and control what outputs we want to give.

* The ```SConscript``` file is where we tell the build system about our python and C++ files.

* The ```run_vectoroperations.py``` file is our _Python Config File_. After everything has been compiled and build, we run the simulation. This file helps us to run the simulation, give inputs and define parameters.

## Flow of my Code

We had to make our own Simple Object by compiling CPP files and parsing python files by building gem5. 

The basic flow is that there are 3 events which we have to catch at specific cycles. The events have been initialized in the Header File and the main code is written in the .cc file. The python files provide an interface to run and define parameters. 

The .cc file contains 3 functions/processes that are user-defined. When the schedule function catches the specific cycle, we process the operations and give our output.

## References
https://www.gem5.org/documentation/learning_gem5/part2/helloobject/