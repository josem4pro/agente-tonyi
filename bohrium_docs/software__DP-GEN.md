# software > DP-GEN

**Source URL:** https://docs.bohrium.com/en/docs/software/DP-GEN

---








DP-GEN | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/software/DP-GEN)
* [English](/en/docs/software/DP-GEN)
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
* DP-GEN
# DP-GEN

This article introduces how to run a typical DP-GEN job on Bohrium.

## Introduction[​](#introduction "标题的直接链接")

DP-GEN (Deep Potential Generator) is committed to solving the following two problems:

1. How to sufficiently sample the potential energy surface and effectively cover the sample space required for training reliable models?
2. How to efficiently screen samples and select conformations with high training value for first-principles calculations?

The workflow is shown as follows: the "explore-label-train" loop iterates until the potential function accuracy meets the expected requirements.

To facilitate data generation and monitor the accuracy of the potential function, DP-GEN also integrates modules such as init\_bulk, init\_surf, autotest, and simplify.

![DPGEN](/en/assets/images/dpgen_scheduler-e2f39723cb340be83e35a4d717d9d59b.png)

For more DP-GEN introductions, please refer to <https://github.com/deepmodeling/dpgen>

## How to run DP-GEN jobs on Bohrium[​](#how-to-run-dp-gen-jobs-on-bohrium "标题的直接链接")

> This case takes about 60 min to run

### Step 1, prepare input data[​](#step-1-prepare-input-data "标题的直接链接")

First, you need to start the [management node](/en/docs/quickstart/FirstRun#3-create-the-management-node-optional), and select the image dpgen:0.10.6 for this case. Connect to the management node through the [Web Shell](/en/docs/userguide/WebShell), and execute the following statement to ensure that DP-GEN and its dependencies are correctly installed:

```
dpgen -h   

```

If everything is normal, the DP-GEN version and information about some dependent libraries will be printed, as shown in the following example:

```
Version: 0.10.6  
Date:    Nov-01-2022  
Path:    /opt/miniconda/lib/python3.7/site-packages/dpgen  
  
Dependency  
------------  
     numpy     1.21.6   /opt/miniconda/lib/python3.7/site-packages/numpy  
    dpdata     0.2.10   /opt/miniconda/lib/python3.7/site-packages/dpdata  
  pymatgen            unknown version or path  
     monty   2022.9.9   /opt/miniconda/lib/python3.7/site-packages/monty  
       ase     3.22.1   /opt/miniconda/lib/python3.7/site-packages/ase  
  paramiko     2.11.0   /opt/miniconda/lib/python3.7/site-packages/paramiko  
 custodian  2022.5.26   /opt/miniconda/lib/python3.7/site-packages/custodian  
  
Reference  
------------  
Please cite:  
Yuzhi Zhang, Haidi Wang, Weijie Chen, Jinzhe Zeng, Linfeng Zhang, Han Wang, and Weinan E,  
DP-GEN: A concurrent learning platform for the generation of reliable deep learning  
based potential energy models, Computer Physics Communications, 2020, 107206.  
------------  
  
Description  
------------  
usage: dpgen [-h]  
             {init_surf,init_bulk,auto_gen_param,init_reaction,run,run/report,collect,simplify,autotest,db}  
             ...  
  
dpgen is a convenient script that uses DeepGenerator to prepare initial data,  
drive DeepMDkit and analyze results. This script works based on several sub-  
commands with their own options. To see the options for the sub-commands, type  
"dpgen sub-command -h".  
  
positional arguments:  
  {init_surf,init_bulk,auto_gen_param,init_reaction,run,run/report,collect,simplify,autotest,db}  
    init_surf           Generating initial data for surface systems.  
    init_bulk           Generating initial data for bulk systems.  
    auto_gen_param      auto gen param.json  
    init_reaction       Generating initial data for reactive systems.  
    run                 Main process of Deep Potential Generator.  
    run/report          Report the systems and the thermodynamic conditions of  
                        the labeled frames.  
    collect             Collect data.  
    simplify            Simplify data.  
    autotest            Auto-test for Deep Potential.  
    db                  Collecting data from DP-GEN.  
  
optional arguments:  
  -h, --help            show this help message and exit  

```

Please ensure that the information is correct before preparing the input files. Using methane as an example, DP-GEN input files are stored in the `Bohrium_DP-GEN_run_example` folder. After entering the data disk with the `cd /data` command, execute the following commands in sequence to download and unzip the input files:

```
wget https://bohrium-example.oss-cn-zhangjiakou.aliyuncs.com/Bohrium_DP-GEN_run_example.zip  

```
```
unzip Bohrium_DP-GEN_run_example.zip  

```
```
cd Bohrium_DP-GEN_run_example  

```

Use the `tree . -L 2` command to view the input files, which mainly include the following content:

```
.  
|-- CH4.POSCAR  
|-- CH4.POSCAR.01x01x01  
|   |-- 00.place_ele  
|   |-- 01.scale_pert  
|   |-- 02.md  
|   `-- param.json  
|-- INCAR_methane  
|-- INCAR_methane.md  
|-- INCAR_methane.rlx  
|-- POTCAR_C  
|-- POTCAR_H  
|-- init.json  
|-- machine.json  
`-- run_param.json  

```

Explanation of files required for DP-GEN operation:
File/Folder Name|Description
:-:|-|
CH4.POSCAR.01x01x01 folder|VASP structure file
machine.json|Machine configuration file; including computing resources, logs, etc.
INCAR\_methane|VASP calculation parameter file; single point energy, used in this tutorial run process
POTCAR\_C, POTCAR\_H|VASP pseudopotential files; set according to the number of system elements
run\_param.json|Calculation parameter file

### Step 2, Prepare Configuration Files[​](#step-2-prepare-configuration-files "标题的直接链接")

The folder already contains the configuration file `machine.json`. In the [Files Management](https://bohrium.dp.tech/workspace) page, you can double-click the `machine.json` file in the left file tree to edit and save it online, or you can edit it in the command line window:

```
vi machine.json  

```

Enter `i` to enter edit mode, complete the modification, press esc to exit edit mode and enter `:` to enter the last line command mode, then enter `wq` to save and exit. The content of the configuration file is as follows:

**Note**:

1. Replace the `0000` after `"project_id"` with your own project ID, which can be viewed on the "[Project Management](https://bohrium.dp.tech/projects)" page. There are three locations to be replaced.
2. Fill in your Bohrium account email and password for `emails` and `password`. There are three locations to be modified.
3. Adjust the `image_address` according to your needs. In this example, the training part uses `registry.dp.tech/dptech/deepmd-kit:2.1.5-cuda11.6`, the exploration part uses `registry.dp.tech/dptech/deepmd-kit:2.1.5-cuda11.6`, and the labeling part uses the VASP image (if you need to use the VASP image, please provide your VASP authorization certificate to the Bohrium email).

```
{  
  "api_version": "1.0",  
  "deepmd_version": "2.1.5",  
  "train" :[  
    {  
      "command": "dp",  
      "machine": {  
        "batch_type": "Bohrium",  
        "context_type": "BohriumContext",  
        "local_root" : "./",  
        "remote_profile":{  
          "email": "",  
          "password": "",  
          "program_id": 0000,  
            "keep_backup":true,  
            "input_data":{  
                "log_file": "00*/train.log",  
                "grouped":true,  
                "job_name": "dpgen_train_job",  
                "disk_size": 100,  
                "scass_type":"c8_m32_1 * NVIDIA V100",  
                "checkpoint_files":["00*/checkpoint","00*/model.ckpt*"],  
                "checkpoint_time":30,  
                "platform": "ali",  
                "job_type": "container",  
                "image_address":"registry.dp.tech/dptech/deepmd-kit:2.1.5-cuda11.6",  
                "on_demand":0  
            }  
        }  
      },  
      "resources": {  
        "number_node": 1,  
        "cpu_per_node": 8,  
        "gpu_per_node": 1,  
        "queue_name": "V100_8_32",  
        "group_size": 1,  
        "custom_flags": [],  
        "strategy": {"if_cuda_multi_devices": true},  
        "para_deg": 3,  
        "source_list": []  
      }  
  
    }],  
  
  "model_devi":[  
    {  
      "command": "lmp -i input.lammps -v restart 0",  
      "machine": {  
        "batch_type": "Bohrium",  
        "context_type": "BohriumContext",  
        "local_root" : "./",  
        "remote_profile":{  
          "email": "",  
          "password": "",  
          "program_id":0000,  
            "keep_backup":true,  
            "input_data":{  
              "log_file": "*/model_devi.log",  
              "grouped":true,  
              "job_name": "dpgen_model_devi_job",  
              "disk_size": 200,  
              "scass_type":"c8_m32_1 * NVIDIA V100",  
              "platform": "ali",  
              "job_type": "container",  
              "image_address":"registry.dp.tech/dptech/deepmd-kit:2.1.5-cuda11.6",  
              "on_demand":0  
            }  
        }  
      },  
      "resources": {  
        "number_node": 1,  
        "cpu_per_node": 8,  
        "gpu_per_node": 1,  
        "queue_name": "V100_8_32",  
        "group_size": 250,  
        "source_list": []  
      }  
    }],  
  
  "fp":[  
    {  
      "command": "ulimit -s unlimited; mpirun -np 32 vasp_std",  
      "machine": {  
        "batch_type": "Bohrium",  
        "context_type": "BohriumContext",  
        "local_root" : "./",  
        "remote_profile":{  
          "email": "",  
          "password": "",  
          "program_id":0000,  
            "input_data":{  
              "api_version":2,  
              "log_file": "task*/fp.log",  
              "grouped":true,  
              "job_name": "dpgen_fp_job",  
              "disk_size": 100,  
              "scass_type":"c32_m64_cpu",  
              "platform": "ali",  
              "job_type":"container",  
              "image_address":"You need to provide an Authorization certificate via WeChat Work at 17710231129 to get the VASP image.",  
              "on_demand":0  
            }  
        }  
      },  
      "resources": {  
        "number_node": 4,  
        "cpu_per_node": 8,  
        "gpu_per_node": 0,  
        "queue_name": "CPU",  
        "group_size": 10,  
        "source_list": ["/opt/intel/oneapi/setvars.sh"]  
      }  
    }]  
  
}  

```
### Step 3, Submit the Job[​](#step-3-submit-the-job "标题的直接链接")

```
nohup dpgen run run_param.json machine.json 1>log 2>err&  

```

**Note**: The DP-GEN process needs to wait for the job to complete before submitting further rounds of jobs, so please do not close the management node.

## Check the Job[​](#check-the-job "标题的直接链接")

You can learn how to view the job status on the Bohrium platform in the [Monitor Task Document](/en/docs/quickstart/Status).

## Download the Results[​](#download-the-results "标题的直接链接")

You can learn how to download the job results on the Bohrium platform in the [Result Download Document](/en/docs/quickstart/Result).

## More DP-GEN Parameter Introduction[​](#more-dp-gen-parameter-introduction "标题的直接链接")

If you want to use a custom input.lammps template in the model\_devi step, such as implementing plumed functions, please refer to the document [DP-GEN model\_devi Step LAMMPS Custom Template](/en/docs/software/DP-GEN_lmp_template)

For more detailed settings of DP-GEN parameters, please refer to the [DP-GEN Source Code Repository](https://github.com/deepmodeling/dpgen) and [DP-GEN Official Documentation](https://docs.deepmodeling.com/projects/dpgen/en/latest/).

[PreviousDeePMD-kit](/en/docs/software/DeePMD-kit/)[NextDP-GEN init](/en/docs/software/DP-GEN_init/)

* [Introduction](#introduction)
* [How to run DP-GEN jobs on Bohrium](#how-to-run-dp-gen-jobs-on-bohrium)
  + [Step 1, prepare input data](#step-1-prepare-input-data)
  + [Step 2, Prepare Configuration Files](#step-2-prepare-configuration-files)
  + [Step 3, Submit the Job](#step-3-submit-the-job)
* [Check the Job](#check-the-job)
* [Download the Results](#download-the-results)
* [More DP-GEN Parameter Introduction](#more-dp-gen-parameter-introduction)



