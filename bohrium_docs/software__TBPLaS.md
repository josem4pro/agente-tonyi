# software > TBPLaS

**Source URL:** https://docs.bohrium.com/en/docs/software/TBPLaS

---








TBPLaS | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/software/TBPLaS)
* [English](/en/docs/software/TBPLaS)
[Console](https://bohrium.dp.tech/home)

* [Homepage](/en/docs/)
* [Quick Start](#)
* [Command Line（New）](#)
* [Command Line](#)
* [Best Practice](#)
* [User Guide](#)
* [Softwares](#)
  + [ABACUS](/en/docs/software/ABACUS)
  + [CALYPSO](/en/docs/software/CALYPSO)
  + [TBPLaS](/en/docs/software/TBPLaS)
  + [CP2K](/en/docs/software/CP2K)
  + [DeePMD-kit](/en/docs/software/DeePMD-kit)
  + [DP-GEN](/en/docs/software/DP-GEN)
  + [DP-GEN init](/en/docs/software/DP-GEN_init)
  + [DP-GEN simplify](/en/docs/software/DP-GEN_simplify)
  + [DP-GEN Auto-test](/en/docs/software/DP-GEN_autotest)
  + [GROMACS](/en/docs/software/GROMACS)
  + [LAMMPS](/en/docs/software/LAMMPS)
  + [Quantum Espresso](/en/docs/software/QuantumEspresso)
  + [VASP](/en/docs/software/VASP)
  + [Custom Software](/en/docs/software/OtherSoftwares)
* [FAQ](#)
* [More Help](/en/docs/MoreHelp)
* [Extensions](#)


* Softwares
* TBPLaS
# TBPLaS

This article introduces how to submit TBPLaS jobs in Bohrium.

## Introduction[​](#introduction "标题的直接链接")

**TBPLaS** is a computational physics software for studying large-scale condensed matter physics systems based on the tight-binding approximation, developed by Professor Yuan Shengjun's research group at Wuhan University. The software mainly relies on the linear-scaling TBPM method developed by the research group, which calculates the electrical, optical, transport, and plasmonic properties of solid-state electronic systems by simulating the time evolution of wave functions. The TBPM method bypasses the diagonalization process in traditional property calculations, and its resource consumption is linearly related to the system size. The simulation scales up to nearly 10 orders of magnitude, reaching billions of atoms or even larger complex quantum systems, which is an improvement of at least 5-6 orders of magnitude compared to traditional methods.

For more information, please refer to the [TBPLaS paper](https://www.sciencedirect.com/science/article/pii/S0010465522003514) and the [official documentation](http://www.tbplas.net/).

## How to run TBPLaS jobs on Bohrium[​](#how-to-run-tbplas-jobs-on-bohrium "标题的直接链接")

### Step 1: Prepare input data[​](#step-1-prepare-input-data "标题的直接链接")

First, you need to start the management node. In this case, the image selected is `tbplas:1.4-py3.10-intel2022-ilp64`. After connecting to the management node through Web Shell, you can proceed with the preparation of the input file.

**Note**: The reason for using this image as the management node is that it already contains the TBPLaS software and related example scripts. In practice, if the calculation scripts is already prepared in advance, any image can be used as the management node.

After the management node is created, connect to it through Web Shell, navigate to the `~/src` directory, and unzip the downloaded TBPLaS source code:

```
cd ~/src; tar -xvf tbplas.tar.bz2  

```

Navigate to the unzipped directory `examples/sample/tbpm` folder:

```
cd tbplas/examples/sample/tbpm  
tree  
.  
|-- diffusion_coeff.py  
|-- graphene.py  
`-- graphene_mpi.py  

```

This folder contains three scripts. Taking `graphene_mpi.py` as an example, this script includes how to build the structure, construct the tight-binding Hamiltonian, and how to calculate DOS, AC/DC conductivity, and dynamic polarizability based on the TBPM method using the tight-binding model. In this case, we will use this script as the calculation script.

### Step 2: Prepare configuration file[​](#step-2-prepare-configuration-file "标题的直接链接")

Create and edit the job configuration file:

```
touch job.json  
vim job.json  

```

Enter the following content in the editor:

```
{  
    "job_name": "TBPLaS example",  
    "command": "OMP_NUM_THREADS=4 mpirun -np 4 python -u graphene_mpi.py  > log",  
    "log_file": "log",  
    "backward_files": [],  
    "project_id": 0000,  
    "platform": "ali",  
    "job_type": "container",  
    "machine_type": "c16_m32_cpu",  
    "image_address": "registry.dp.tech/dptech/tbplas:1.4-py3.10-intel2022-ilp64"  
}  

```

**Notice**： Replace the `0000` after `"project_id"`: with your own project ID, which can be viewed on the "[Project Management](https://bohrium.dp.tech/projects)" page. It is recommended to set the number of MPI processes to the number of CPU cores / 2. For example, if the selected machine type has a 16-core 32GB memory CPU, you can use `mpirun -np 8` to submit the job.

Please note that the number of MPI processes is a factor of the number of random samples calculated in the script: for example, in this script, the number of samples is 4.

```
config.generic['nr_random_samples'] = 4  

```

Therefore, the number of MPI processes should be a multiple of 4, such as 2, 4, etc. At the same time, to ensure the efficiency of a single sample, OMP parallelism should also be provided.

### Step 3: Submit the job Submit the job using Bohrium CLI : Therefore, you first need to [install the Bohrium CLI](/en/docs/bohrctl/install#Preparation).[​](#step-3-submit-the-job--submit-the-job-using-bohrium-cli---therefore-you-first-need-to-install-the-bohrium-cli "标题的直接链接")

```
bohr job submit -i job.json -p ./  

```

Where:

* -i specifies the configuration file of the job, which is job.json in this case
* -p specifies the directory where the input files are located, Bohrium will package and upload the specified directory, unzip it on the computing node, and switch the working directory to that directory. In this case, it is ./

If you see the following output in the command line, it means the submission is successful. You can also see the JOB ID of the job, which can be used to track the progress of the job later.

```
Submit job succeed.   
JobId:  <JOB ID>  
JobGroupId:  <JOB GROUP ID>  

```
## Check the job[​](#check-the-job "标题的直接链接")

You can learn how to check the job status on the Bohrium platform in the [Monitor jobs Documentation](/en/docs/quickstart/Status).

## Download results[​](#download-results "标题的直接链接")

You can learn how to download job results on the Bohrium platform in the [Results Download Documentation](/en/docs/quickstart/Result).

[PreviousCALYPSO](/en/docs/software/CALYPSO/)[NextCP2K](/en/docs/software/CP2K/)

* [Introduction](#introduction)
* [How to run TBPLaS jobs on Bohrium](#how-to-run-tbplas-jobs-on-bohrium)
  + [Step 1: Prepare input data](#step-1-prepare-input-data)
  + [Step 2: Prepare configuration file](#step-2-prepare-configuration-file)
  + [Step 3: Submit the job Submit the job using Bohrium CLI : Therefore, you first need to install the Bohrium CLI.](#step-3-submit-the-job--submit-the-job-using-bohrium-cli---therefore-you-first-need-to-install-the-bohrium-cli)
* [Check the job](#check-the-job)
* [Download results](#download-results)



