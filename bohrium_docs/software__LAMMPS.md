# software > LAMMPS

**Source URL:** https://docs.bohrium.com/en/docs/software/LAMMPS

---








LAMMPS | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/software/LAMMPS)
* [English](/en/docs/software/LAMMPS)
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
* LAMMPS
# LAMMPS

This article introduces how to run LAMMPS jobs on the Bohrium platform.

## Introduction[​](#introduction "标题的直接链接")

LAMMPS is a classical molecular dynamics (MD) code used for simulating collections of particles in liquid, solid, or gaseous states. It can model atoms, polymers, biomolecules, solids (metals, ceramics, oxides), particles, coarse-grained, or macroscopic systems using various interatomic potentials (force fields) and boundary conditions. It can model 2D or 3D systems containing only a few particles up to millions or even billions.

For more information about LAMMPS, please refer to <https://docs.lammps.org/>

## How to run LAMMPS jobs on Bohrium[​](#how-to-run-lammps-jobs-on-bohrium "标题的直接链接")

> The job in this case takes approximately 1 minute to run

### Step 1, prepare to input data[​](#step-1-prepare-to-input-data "标题的直接链接")

First, you need to enable the [management node](/en/docs/quickstart/FirstRun#3-create-the-management-node-optional), and in this case, select the ubuntu:20.04-py37 image. After connecting to the management node through the [Web Shell](/en/docs/userguide/WebShell), you can start preparing the input files.

The input files for LAMMPS are stored in the `Bohrium_LAMMPS_example` folder. After entering the data disk using the `cd /personal` command, execute the following commands in sequence to download and extract the input files:

```
wget https://bohrium-example.oss-cn-zhangjiakou.aliyuncs.com/Bohrium_LAMMPS_example.zip  

```
```
unzip Bohrium_LAMMPS_example.zip  

```
```
cd Bohrium_LAMMPS_example  

```
### Step 2: Prepare the configuration file[​](#step-2-prepare-the-configuration-file "标题的直接链接")

The folder already contains the configuration file `job.json`. In the [Files Management](https://bohrium.dp.tech/workspace) page , you can double-click the `job.json` file in the left file tree to edit and save it online, or you can edit it in the command line window.

```
vi job.json  

```

Enter the edit mode by typing `i`, make the changes, then press esc to exit edit mode. Type `:` to enter command-line mode, and then type `wq` to save and exit. The content of the configuration file is as follows:

**Note**: Replace the `0000` after `"project_id":` with your own project ID, which can be viewed on the "[Project Management](https://bohrium.dp.tech/projects)" page.

```
{  
    "job_name": "lammps_tutorial",  
    "job_type": "container",  
    "command": "mpirun -n 32 lmp_mpi -i in.shear > log",  
    "log_file": "log",  
    "backward_files": [],  
    "project_id": 0000,  
    "platform": "ali",  
    "machine_type": "c32_m64_cpu",  
    "image_address": "registry.dp.tech/dptech/lammps:29Sep2021"  
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
## View Jobs[​](#view-jobs "标题的直接链接")

You can learn how to view job status on the Bohrium platform in the [Monitoring Jobs Document](/en/docs/quickstart/Status).

## Download Results[​](#download-results "标题的直接链接")

You can learn how to download job results on the Bohrium platform in the [Results Download Document](/en/docs/quickstart/Result).

[PreviousGROMACS](/en/docs/software/GROMACS/)[NextQuantumEspresso](/en/docs/software/QuantumEspresso/)

* [Introduction](#introduction)
* [How to run LAMMPS jobs on Bohrium](#how-to-run-lammps-jobs-on-bohrium)
  + [Step 1, prepare to input data](#step-1-prepare-to-input-data)
  + [Step 2: Prepare the configuration file](#step-2-prepare-the-configuration-file)
  + [Step 3: Submit the job Submit the job using Bohrium CLI : Therefore, you first need to install the Bohrium CLI.](#step-3-submit-the-job--submit-the-job-using-bohrium-cli---therefore-you-first-need-to-install-the-bohrium-cli)
* [View Jobs](#view-jobs)
* [Download Results](#download-results)



