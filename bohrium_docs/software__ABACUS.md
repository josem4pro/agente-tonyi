# software > ABACUS

**Source URL:** https://docs.bohrium.com/en/docs/software/ABACUS

---








ABACUS | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/software/ABACUS)
* [English](/en/docs/software/ABACUS)
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
* ABACUS
# ABACUS

This article introduces how to run ABACUS jobs on Bohrium.

## Introduction[​](#introduction "标题的直接链接")

ABACUS density functional theory software is a domestically developed open-source density functional theory software with completely independent intellectual property rights, led by Professor He Lixin, Researcher Ren Xinguo, and Researcher Chen Mohan. ABACUS can use plane wave basis vectors and numerical atomic orbit basis vectors for simulation calculations, obtain the ground state charge density distribution of materials by solving the Kohn-Sham equation, and calculate various physical properties of the target materials based on this. At present, ABACUS is developing a machine learning-assisted functional model DeePKS, which provides a strong foundation for realizing multi-scale molecular dynamics simulations. In addition, the software development team is also developing density functional theories suitable for various scenarios (such as orbital-free density functional theory suitable for large-scale calculations and random wave function density functional theory suitable for high temperature and high pressure conditions).

[Code Repository](https://github.com/deepmodeling/abacus-develop)

[Software Documentation](https://abacus.deepmodeling.com/)

## How to run ABACUS jobs on Bohrium[​](#how-to-run-abacus-jobs-on-bohrium "标题的直接链接")

> This case takes about 40s to run

### Step 1: Prepare input data[​](#step-1-prepare-input-data "标题的直接链接")

First, you need to enable the [management node](/en/docs/quickstart/FirstRun#3-create-the-management-node-optional), and the image is selected as ubuntu:20.04-py37 in this case. After connecting to the management node via [Web Shell](/en/docs/userguide/WebShell), you can prepare the input files.

The input files of ABACUS (such as input parameters, pseudopotential files, configuration files, etc.) are stored in the `Bohrium_ABACUS_example` folder. After entering the data disk using the `cd /personal` command, execute the following commands in sequence to download and unzip the input files:

```
wget https://bohrium-example.oss-cn-zhangjiakou.aliyuncs.com/Bohrium_ABACUS_example.zip  

```
```
unzip Bohrium_ABACUS_example.zip  

```
```
cd Bohrium_ABACUS_example  

```
### Step 2: Prepare configuration file[​](#step-2-prepare-configuration-file "标题的直接链接")

The folder already contains the configuration file `job.json`. In the [Files Management](https://bohrium.dp.tech/workspace) page , you can double-click the `job.json` file in the left file tree to edit and save it online, or you can edit it in the command line window:

```
vi job.json  

```

Enter `i` to enter edit mode, press esc to exit edit mode after completing the modification, then enter `:` to enter the last line command mode, and then enter `wq` to save and exit. The content of the configuration file is as follows:

**Note**: Replace the `0000` after `"project_id"`: with your own project ID, which can be viewed on the "[Project Management](https://bohrium.dp.tech/projects)" page. It is recommended to set the number of MPI processes to the number of CPU cores / 2. For example, if the machine type selected in this case is a 16-core 32G memory CPU machine, use `mpirun -np 8` to submit the job.

```
{  
    "job_name": "ABACUS test",  
    "command": "OMP_NUM_THREADS=1 mpirun -np 8 abacus > log",  
    "log_file": "log",  
    "backward_files": [],  
    "project_id": 0000,  
    "platform": "ali",  
    "job_type": "container",  
    "machine_type": "c16_m32_cpu",  
    "image_address": "registry.dp.tech/dptech/abacus:3.0.0"  
}  

```
### Step 3: Submit the job Submit the job using Bohrium CLI : Therefore, you first need to [install the Bohrium CLI](/en/docs/bohrctl/install#Preparation).[​](#step-3-submit-the-job--submit-the-job-using-bohrium-cli---therefore-you-first-need-to-install-the-bohrium-cli "标题的直接链接")

Therefore, you first need to [install the Bohrium CLI](/en/docs/bohrctl/install#Preparation).

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
## View job[​](#view-job "标题的直接链接")

You can learn how to view the job status on the Bohrium platform in the [Monitor Task Documentation](/en/docs/quickstart/Status).

## Download Results[​](#download-results "标题的直接链接")

You can learn how to download the job results on the Bohrium platform in the [Result Download Documentation](/en/docs/quickstart/Result).

[PreviousProject Management and Collaboration](/en/docs/userguide/coorperation/)[NextCALYPSO](/en/docs/software/CALYPSO/)

* [Introduction](#introduction)
* [How to run ABACUS jobs on Bohrium](#how-to-run-abacus-jobs-on-bohrium)
  + [Step 1: Prepare input data](#step-1-prepare-input-data)
  + [Step 2: Prepare configuration file](#step-2-prepare-configuration-file)
  + [Step 3: Submit the job Submit the job using Bohrium CLI : Therefore, you first need to install the Bohrium CLI.](#step-3-submit-the-job--submit-the-job-using-bohrium-cli---therefore-you-first-need-to-install-the-bohrium-cli)
* [View job](#view-job)
* [Download Results](#download-results)



