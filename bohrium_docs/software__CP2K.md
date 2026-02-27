# software > CP2K

**Source URL:** https://docs.bohrium.com/en/docs/software/CP2K

---








CP2K | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/software/CP2K)
* [English](/en/docs/software/CP2K)
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
* CP2K
# CP2K

This article introduces how to run CP2K jobs on Bohrium.

## Introduction[​](#introduction "标题的直接链接")

CP2K is the fastest open-source software for first-principles materials calculation and simulation. It can study large systems with thousands of atoms and is widely used in the simulation of solids, liquids, molecules, periodic, materials, crystals, and biological systems. It was initiated by the Max Planck Research Center in 2000 as a project for solid-state physics research, and all the code is written in Fortran 2003. It is now maintained by ETH Zurich and the University of Zurich as an open-source project that follows the GPL license. Users can download the source code from its [official website](https://www.cp2k.org/). This tutorial mainly introduces how to run CP2K calculation jobs on the Bohrium platform.

## How to run CP2K jobs on Bohrium[​](#how-to-run-cp2k-jobs-on-bohrium "标题的直接链接")

> The running time of this case job is about 1 min 30 s.

### Step 1: Prepare input data[​](#step-1-prepare-input-data "标题的直接链接")

First, you need to enable the [management node](/en/docs/quickstart/FirstRun#3-create-the-management-node-optional), and select the ubuntu:20.04-py37 image in this case. After connecting to the management node through the [Web Shell](/en/docs/userguide/WebShell), you can start preparing the input files.

Take methane and the personal directory as an example. The input files of CP2K are all stored in the `Bohrium_CP2K_example` folder. After entering the data disk with the `cd /personal` command, execute the following commands in sequence to download and unzip the input files:

```
wget https://bohrium-example.oss-cn-zhangjiakou.aliyuncs.com/Bohrium_CP2K_example.zip  

```
```
unzip Bohrium_CP2K_example.zip  

```
```
cd Bohrium_CP2K_example  

```
### Step 2: Prepare configuration file[​](#step-2-prepare-configuration-file "标题的直接链接")

The configuration file `job.json` is already included in the folder. In the [Files Management](https://bohrium.dp.tech/workspace) page , you can double-click the `job.json` file in the left file tree to edit and save it online. You can also edit it in the command-line window:

```
vi job.json  

```

Enter `i` to enter edit mode, after completing the modification, press esc to exit edit mode and enter `:` to enter the command-line mode, then enter `wq` to save and exit. The content of the configuration file is as follows:

**Note**: Replace the `0000` after `"project_id"`: with your own project ID, which can be viewed on the "[Project Management](https://bohrium.dp.tech/projects)" page.

```
{  
    "job_name": "CP2K_Si_opt",  
    "command": "source /cp2k-7.1/tools/toolchain/install/setup && mpirun -n 16 --allow-run-as-root --oversubscribe cp2k.popt -i input.inp -o output.log",  
    "log_file": "output.log",  
    "backward_files": ["output.log"],  
    "project_id": 0000,  
    "platform": "ali",  
    "job_type": "container",  
    "machine_type": "c16_m32_cpu",  
    "image_address": "registry.dp.tech/dptech/cp2k:7.1"  
}  

```
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

[PreviousTBPLaS](/en/docs/software/TBPLaS/)[NextDeePMD-kit](/en/docs/software/DeePMD-kit/)

* [Introduction](#introduction)
* [How to run CP2K jobs on Bohrium](#how-to-run-cp2k-jobs-on-bohrium)
  + [Step 1: Prepare input data](#step-1-prepare-input-data)
  + [Step 2: Prepare configuration file](#step-2-prepare-configuration-file)
  + [Step 3: Submit the job Submit the job using Bohrium CLI : Therefore, you first need to install the Bohrium CLI.](#step-3-submit-the-job--submit-the-job-using-bohrium-cli---therefore-you-first-need-to-install-the-bohrium-cli)
* [Check the job](#check-the-job)
* [Download results](#download-results)



