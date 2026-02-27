# software > GROMACS

**Source URL:** https://docs.bohrium.com/en/docs/software/GROMACS

---








GROMACS | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/software/GROMACS)
* [English](/en/docs/software/GROMACS)
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
* GROMACS
# GROMACS

This article mainly introduces how to use the Bohrium platform to run GROMACS jobs.

## Introduction[​](#introduction "标题的直接链接")

[GROMACS](https://www.gromacs.org/about.html) is an open source and free molecular dynamics simulation software that adheres to the LGPL v2.1 protocol and is often used for simulating biological and organic molecular systems such as proteins, phospholipids, nucleic acids, etc. The code for GROMACS is entirely written in C/C++and has been high-performance optimized for GPU, resulting in fast computation speed. For a more detailed introduction to GROMACS, please refer to its[official website](https://www.gromacs.org/)or[document](https://manual.gromacs.org/current/index.html)。Beginners can also refer to the[document](http://www.mdtutorials.com/gmx/)to quickly get started with GROMACS.

## How to run GROMACS jobs on Bohrium[​](#how-to-run-gromacs-jobs-on-bohrium "标题的直接链接")

> The job in this case will take 1 min 30 s

### Step 1, prepare to input data[​](#step-1-prepare-to-input-data "标题的直接链接")

First, you need to enable the [New Nodes](/en/docs/quickstart/FirstRun#3-create-the-management-node-optional)，In this case, the image is selected as ubuntu:20.04-py37。After connecting to the management node through [Web Shell](/en/docs/userguide/WebShell), the input file can be prepared.

The input files for GROMACS (including the coordinate file `conf.gro`, simulation parameter file `prod.mdp`, topology file `topol.top`, run script `rungmx.sh`, and bohr configuration file `job.json`) have been stored in the `Bohrium_GROMACS_example` folder. After entering the data disk using the `cd /personal` command, execute the following commands in sequence to download and unzip the input files:

```
wget https://bohrium-example.oss-cn-zhangjiakou.aliyuncs.com/Bohrium_GROMACS_example.zip  

```
```
unzip Bohrium_GROMACS_example.zip  

```
```
cd Bohrium_GROMACS_example  

```
### Step 2: Prepare the Configuration File[​](#step-2-prepare-the-configuration-file "标题的直接链接")

The folder already contains the configuration file `job.json`. In the [Files Management](https://bohrium.dp.tech/workspace) page , you can double-click the `job.json` file in the left file tree to edit and save it online. You can also edit it in the command line window:

```
vi job.json  

```

Enter edit mode by typing `i`, and after making the modifications, press esc to exit edit mode. Then, type `:` to enter the command-line mode, and input `wq` to save and exit. The content of the configuration file is as follows:

**Note**: Replace the `0000` after `"project_id":` with your own project ID, which can be found on the "[Project Management](https://bohrium.dp.tech/projects)" page.

```
{  
    "job_name": "bohrium-gmx-example",  
    "command": "bash rungmx.sh > log",  
    "log_file": "log",  
    "backward_files": [],  
    "project_id": 0000,  
    "image_address": "registry.dp.tech/dptech/gromacs:2022.2",  
    "machine_type": "c16_m62_1 * NVIDIA T4",  
    "platform": "ali",  
    "job_type": "container"  
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
## Check Job[​](#check-job "标题的直接链接")

You can learn how to check the job status on the Bohrium platform in the [Monitoring job Document](/en/docs/quickstart/Status).

## Download Results[​](#download-results "标题的直接链接")

You can learn how to download job results on the Bohrium platform in the [Result Download Document](/en/docs/quickstart/Result).

[PreviousDP-GEN Auto-test](/en/docs/software/DP-GEN_autotest/)[NextLAMMPS](/en/docs/software/LAMMPS/)

* [Introduction](#introduction)
* [How to run GROMACS jobs on Bohrium](#how-to-run-gromacs-jobs-on-bohrium)
  + [Step 1, prepare to input data](#step-1-prepare-to-input-data)
  + [Step 2: Prepare the Configuration File](#step-2-prepare-the-configuration-file)
  + [Step 3: Submit the job Submit the job using Bohrium CLI : Therefore, you first need to install the Bohrium CLI.](#step-3-submit-the-job--submit-the-job-using-bohrium-cli---therefore-you-first-need-to-install-the-bohrium-cli)
* [Check Job](#check-job)
* [Download Results](#download-results)



