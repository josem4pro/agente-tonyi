# software > VASP

**Source URL:** https://docs.bohrium.com/en/docs/software/VASP

---








VASP | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/software/VASP)
* [English](/en/docs/software/VASP)
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
* VASP
# VASP

This article introduces how to submit VASP jobs in Bohrium.

## How to run VASP jobs on Bohrium[​](#how-to-run-vasp-jobs-on-bohrium "标题的直接链接")

> This case job takes about 1 min to run

### Step 1: Prepare input data[​](#step-1-prepare-input-data "标题的直接链接")

First, you need to enable the [management node](/en/docs/quickstart/FirstRun#3-create-the-management-node-optional), and choose the ubuntu:20.04-py37 image in this example. After connecting to the management node via [Web Shell](/en/docs/userguide/WebShell), you can start preparing the input files.

The input files for VASP are stored in the `Bohrium_VASP_example` folder. Use the `cd /perosnal` command to enter the data disk, and execute the following commands in sequence to download and unzip the input files:

```
wget https://bohrium-example.oss-cn-zhangjiakou.aliyuncs.com/Bohrium_VASP_example.zip  

```
```
unzip Bohrium_VASP_example.zip  

```
```
cd Bohrium_VASP_example  

```
### Step 2: Prepare the configuration file[​](#step-2-prepare-the-configuration-file "标题的直接链接")

The folder already contains the configuration file `job.json`. In [Files Management](https://bohrium.dp.tech/workspace) page , you can double-click the `job.json` file in the left file tree to edit and save it online, or you can edit it in the command line window:

```
vi job.json  

```

Enter `i` to enter edit mode, and after completing the modifications, press esc to exit edit mode and enter `:` to enter the last line command mode, then enter `wq` to save and exit. The content of the configuration file is as follows:

**Note**: The `0000` after `"project_id"`: needs to be replaced with your own project ID, which can be viewed on the "[Project Management](https://bohrium.dp.tech/projects)" page.

```
{  
    "job_name": "Bohrium-VASP",  
    "job_type": "container",  
    "command": "source /opt/intel/oneapi/setvars.sh && mpirun -n 16 vasp_std ",  
    "log_file": "tmp_log",  
    "backward_files": [],  
    "project_id":0000,  
    "platform": "ali",  
    "machine_type": "c2_m8_cpu",  
    "image_address": "You need to provide authorization credentials to the bohrium email to get the VASP image address"  
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
## View jobs[​](#view-jobs "标题的直接链接")

You can learn how to view job status in Bohrium platform in the [Monitor Task Document](/en/docs/quickstart/Status).

## Download results[​](#download-results "标题的直接链接")

You can learn how to download job results in Bohrium platform in the [Result Download Document](/en/docs/quickstart/Result).

[PreviousQuantumEspresso](/en/docs/software/QuantumEspresso/)[NextCustom Software](/en/docs/software/OtherSoftwares/)

* [How to run VASP jobs on Bohrium](#how-to-run-vasp-jobs-on-bohrium)
  + [Step 1: Prepare input data](#step-1-prepare-input-data)
  + [Step 2: Prepare the configuration file](#step-2-prepare-the-configuration-file)
  + [Step 3: Submit the job Submit the job using Bohrium CLI : Therefore, you first need to install the Bohrium CLI.](#step-3-submit-the-job--submit-the-job-using-bohrium-cli---therefore-you-first-need-to-install-the-bohrium-cli)
* [View jobs](#view-jobs)
* [Download results](#download-results)



