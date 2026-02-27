# software > DeePMD-kit

**Source URL:** https://docs.bohrium.com/en/docs/software/DeePMD-kit

---








DeePMD-kit | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/software/DeePMD-kit)
* [English](/en/docs/software/DeePMD-kit)
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
* DeePMD-kit
# DeePMD-kit

This article introduces how to run DeePMD-kit tasks on Bohrium.

## Introduction[​](#introduction "标题的直接链接")

DeePMD-kit is a software for molecular dynamics simulation that uses neural networks to fit potential energy models based on first-principles data. Without manual intervention, it can transform user-provided data into deep potential models in a matter of hours, which can seamlessly interface with common molecular dynamics simulation software (such as LAMMPS, OpenMM, and GROMACS). DeePMD-kit can improve the calculation speed of molecular dynamics by several orders of magnitude while maintaining the accuracy of quantum mechanics. It has been used by thousands of research groups in physics, chemistry, materials, biology, and other fields.

This article uses the combination of DeePMD-kit 2.1.5 and LAMMPS as an example. The LAMMPS part of DeePMD-kit is divided into three parts: the first part constructs the neighbor table, which has been GPU-optimized; the second part calls the DP model to calculate the force field, which is also performed on the GPU; and the third part runs MD according to Newton's second law, which runs on the CPU. The software `registry.dp.tech/dptech/deepmd-kit:2.1.5-cuda11.6` used in this example comes pre-installed with DeePMD-kit 2.1.5 and LAMMPS and supports PLUMED.

## How to run DeePMD-kit tasks on Bohrium[​](#how-to-run-deepmd-kit-tasks-on-bohrium "标题的直接链接")

> This job takes about 10 minutes to run

### Step 1: Prepare input data[​](#step-1-prepare-input-data "标题的直接链接")

First, you need to turn on the [management node](/en/docs/quickstart/FirstRun#3-create-the-management-node-optional), with ubuntu:20.04-py37 as the image in this example. After connecting to the management node via [Web Shell](/en/docs/userguide/WebShell), you can prepare the input files.

The input files for DeePMD-kit are stored in the `Bohrium_DeePMD-kit_example` folder. After entering the data disk using the `cd /personal` command, execute the following commands in sequence to download and unzip the input files:

```
wget https://bohrium-example.oss-cn-zhangjiakou.aliyuncs.com/Bohrium_DeePMD-kit_example.zip  

```
```
unzip Bohrium_DeePMD-kit_example.zip  

```
```
cd Bohrium_DeePMD-kit_example  

```
### Step 2, prepare the configuration file[​](#step-2-prepare-the-configuration-file "标题的直接链接")

The folder already contains the configuration file `job.json`. In the [Files Management](https://bohrium.dp.tech/workspace) page , you can double-click the `job.json` file in the left file tree to edit and save it online, or you can edit it in the command line window:

```
vi job.json  

```

Press `i` to enter edit mode. After completing the modifications, press esc to exit edit mode, then enter `:` to enter the command-line mode, and enter `wq` to save and exit. The content of the configuration file is as follows:

**Note**: All `"project_id":` followed by `0000` need to be replaced with your own project ID, which can be viewed on the "[Project Management](https://bohrium.dp.tech/projects)" page. The format of the json file requires that there is no comma after the last field in the {} block, otherwise, there will be a syntax error.

```
{  
    "job_name": "DeePMD-kit test",  
    "command": " cd se_e2_a && dp train input.json > tmp_log 2>&1 && dp freeze -o graph.pb",  
    "log_file": "se_e2_a/tmp_log",  
    "backward_files": ["se_e2_a/lcurve.out","se_e2_a/graph.pb"],  
    "project_id": 0000,  
    "platform": "ali",  
    "machine_type": "c4_m15_1 * NVIDIA T4",  
    "job_type": "container",  
    "image_address": "registry.dp.tech/dptech/deepmd-kit:2.1.5-cuda11.6"  
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

You can learn how to view the job status on the Bohrium platform in the [Monitoring Jobs Documentation](/en/docs/quickstart/Status).

## Download the results[​](#download-the-results "标题的直接链接")

You can learn how to download the job results on the Bohrium platform in the [Result Download Documentation](/en/docs/quickstart/Result).

[PreviousCP2K](/en/docs/software/CP2K/)[NextDP-GEN](/en/docs/software/DP-GEN/)

* [Introduction](#introduction)
* [How to run DeePMD-kit tasks on Bohrium](#how-to-run-deepmd-kit-tasks-on-bohrium)
  + [Step 1: Prepare input data](#step-1-prepare-input-data)
  + [Step 2, prepare the configuration file](#step-2-prepare-the-configuration-file)
  + [Step 3: Submit the job Submit the job using Bohrium CLI : Therefore, you first need to install the Bohrium CLI.](#step-3-submit-the-job--submit-the-job-using-bohrium-cli---therefore-you-first-need-to-install-the-bohrium-cli)
* [Check the job](#check-the-job)
* [Download the results](#download-the-results)



