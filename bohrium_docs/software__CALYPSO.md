# software > CALYPSO

**Source URL:** https://docs.bohrium.com/en/docs/software/CALYPSO

---








CALYPSO | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/software/CALYPSO)
* [English](/en/docs/software/CALYPSO)
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
* CALYPSO
# CALYPSO

This article introduces how to run CALYPSO jobs on Bohrium.

## Introduction[​](#introduction "标题的直接链接")

Finding the minimum energy point structure on the potential energy surface has been a long-term goal of structure prediction. Based on the CALYPSO material structure prediction method and software (see <http://www.calypso.cn>) developed by independent innovation in China, it can predict the microstructure of materials based on the chemical composition of materials alone. It has been widely used in innovative design of crystals, surfaces (including two-dimensional single/multi-layer materials), interfaces, clusters, and transition states, and can carry out function-oriented (such as band gap, hardness, and electron density, etc.) reverse material design.

> This case will take the B-N variable composition structure prediction as an example to introduce the basic usage of CALYPSO\_SaaS.

[Reference paper](/en/docs/software/​http://calypso.cn/documentation/)

## I. Running CALYPSO jobs on Bohrium[​](#i-running-calypso-jobs-on-bohrium "标题的直接链接")

> This case takes about 40 minutes to complete.

Contact Bohrium staff via WeChat Work at 17710231129 to obtain CALYPSO-SaaS usage permission.

### 1. Start the calypso-bohrium node[​](#1-start-the-calypso-bohrium-node "标题的直接链接")

In the [Bohrium node console](/en/docs/software/​https://bohrium.dp.tech/nodes), `create a new node`-`create a container node`, select the image `calypso-bohrium:7.2.4`, and configure the node arbitrarily. After the node is turned on, connect to the control node.

### 2. Prepare input data[​](#2-prepare-input-data "标题的直接链接")

Download the sample file.

To facilitate subsequent visualization, the example needs to be stored in the `/personal` or `/share` directory (the share directory is shared among projects, using the personal directory as an example):

```
cd /personal  
wget ​https://bohrium-example.oss-cn-zhangjiakou.aliyuncs.com/CALYPSO-Bohrium-example.zip  
unzip CALYPSO-Bohrium-example.zip  
cd /personal/CALYPSO-Bohrium-example  

```

You can download the sample file at any time through [this link](/en/docs/software/​https://bohrium-example.oss-cn-zhangjiakou.aliyuncs.com/CALYPSO-Bohrium-example.zip).

> After this case is over, you can choose whether to keep the directory `/personal/CALYPSO-Bohrium-example`.

The directory contains:

1. `templates/input.dat.example/`, sample input.dat for crystal prediction, layered structure prediction, and variable composition structure prediction (VSC)
2. `templates/abacus_example/`, all inputs required for CALYPSO structure prediction using ABACUS as the first-principles calculation software
3. `templates/qe_example/`, all inputs required for CALYPSO structure prediction using QE as the first-principles calculation software
4. `templates/vasp_example/`, all inputs required for CALYPSO structure prediction using VASP as the first-principles calculation software

This article will use `vasp_example` as an example.

```
cd templates/vasp_example  

```

The directory contains:

1. CALYPSO and VASP input files:
   * `input.dat`, CALYPSO control file (for detailed parameter description, please refer to the [English manual](/en/docs/software/​http://www.calypso.cn/documentation/CALYPSO_Manual_English.pdf) or [Chinese manual](/en/docs/software/​http://www.calypso.cn/documentation/CALYPSO_Manual_Chinese.pdf))
   * `INCAR_*`, control files for VASP optimization of each structure
   * `POTCAR`, VASP pseudopotential
2. Calculation resource configuration file (see below):
   * `machine.json`, dpdispatcher parameter file, controls the use of images
   * `resources.json`, dpdispatcher parameter file, controls the number of jobs run on each machine
3. Auxiliary control files:
   * `run.sh`, CALYPSO-SaaS job submission script
   * `del.sh`, CALYPSO-Saas directory cleaning script, used to batch delete useless files when recalculating in the same directory

### 3. Modify the CALYPSO control file[​](#3-modify-the-calypso-control-file "标题的直接链接")

Modify the CALYPSO control file `input.dat` according to your structure prediction needs. This case demonstrates the B-N variable composition structure prediction, you can directly copy `templates/input.dat.example/pso/input.dat.vsc` to replace the `input.dat` in this directory:

```
cp /personal/CALYPSO-Bohrium-example/templates/input.dat.example/pso/input.dat.vsc /personal/CALYPSO-Bohrium-example/templates/vasp_example/input.dat  

```
### 4. Modify the Bohrium configuration file[​](#4-modify-the-bohrium-configuration-file "标题的直接链接")

Modify the calculation resource configuration `machine.json`:

> CALYPSO-SaaS job submission and recovery are all completed by [dpdispatcher](/en/docs/software/​https://github.com/deepmodeling/dpdispatcher), so you need to modify the dpdispatcher configuration file `machine.json`.

In the [Files Management](https://bohrium.dp.tech/workspace) page , you can double-click the `machine.json` file in the left file tree to edit and save it online, or you can edit it in the command line window:

```
vi machine.json  

```

Enter `i` to enter edit mode. After completing the modification, press `esc` to exit edit mode, then enter `:` to enter the end line command mode, and then enter `wq` to save and exit. The configuration file content is as follows:

```
{  
  "batch_type": "Lebesgue",  
  "context_type": "LebesgueContext",  
  "local_root": "./",  
  "remote_profile": {  
    "email": "******",  
    "password": "******",  
    "program_id": 000000,  
    "_keep_backup": true,  
    "input_data": {  
      "job_name": "calypso.Bohrium.test.1",  
      "image_address": "******",  
      "job_type": "indicate",  
      "log_file": "log",  
      "grouped": true,  
      "disk_size": 200,  
      "max_run_time": 40,  
      "machine_type": "c16_m64_cpu",  
      "platform": "paratera",  
      "on_demand": 0,  
      "out_files": ["OUTCAR", "CONTCAR", "OSZICAR", "fp.log", "log", "err"]  
    }  
  }  
}  

```

The parts that need to be modified:

1. `email`, your login email for authentication on the computing node
2. `password`, your account password for authentication on the computing node
3. `program_id` (number), the billing project ID of the computing node, check [Bohrium Project Console](https://bohrium.dp.tech/projects)
4. `job_name`, the job name, which will be displayed in [Bohrium job Console](https://bohrium.dp.tech/projects), avoid duplicate names to distinguish jobs
5. `image_address`, the image address of the first-principles calculation software (you need to provide authorization credentials to Bohrium email to obtain the address)

Some other parameters:

1. `platform`, the platform for running the calculation job, optional `paratera` (Parallel Technology), `ali` (Alibaba Cloud), etc.
2. `machine_type`, the machine specification for running the calculation job

### 5、Submit the job[​](#5submit-the-job "标题的直接链接")

Execute the job submission script `run.sh` to submit the CALYPSO job to the Bohrium cloud platform, and redirect the log to the out file:

```
bash run.sh  

```
> Or manually execute through `run_calypso`, redirect to `out`:
> `nohup run_calypso > out 2>&1 &`

### 6、View the job[​](#6view-the-job "标题的直接链接")

After successful submission, you can query the job running status with the `showjob` command:

```
showjob  
# >>> name                                PID                   work_path  
# >>> run_calypso                         ***                   /personal/***  

```

At the same time, you can also learn how to view the job status on the Bohrium platform in the [Monitoring Jobs Page](/en/docs/quickstart/Status).

## II. job Result Analysis[​](#ii-job-result-analysis "标题的直接链接")

We have prepared an updated structure prediction result analysis script `cak3.py` in the image. At present, in addition to the basic functions, this script also supports visual analysis of the structure prediction evolution process, and visual analysis of the `convex hull` for variable component structure prediction.

### Predicted structure extraction[​](#predicted-structure-extraction "标题的直接链接")

The results of CALYPSO run are all stored in the `results` folder in the running directory. Enter this directory:

```
cd results  

```

Run `cak3.py`, the program will automatically analyze your prediction results and store the structure information of the top 50 structures with the lowest enthalpy in `Analysis_Output.dat`:

```
cak3.py  

```

`--vasp` option to output `vasp` format, `-a` to output all structures, `-m` for multiple symmetry tolerance:

```
cak3.py --vasp -a -m "0.1 0.3 0.5"  

```

When the system is a variable component structure prediction, it will output according to the component subfolder.

### Visualization of structure prediction evolution process[​](#visualization-of-structure-prediction-evolution-process "标题的直接链接")

```
cak3.py --plotevo  

```

Output `evo.png`, which can be viewed directly in WebShell.

### Visualization of variable component structure prediction phase diagram[​](#visualization-of-variable-component-structure-prediction-phase-diagram "标题的直接链接")

Draw `convex hull`:

> Running this command requires specifying the energy per atom of each elemental substance in `input.dat` in advance

```
cak3.py --plotch  

```

Output `convexhull.csv`, `convexhull.png`, which can be viewed directly in WebShell.

## III. Calculation directory cleanup[​](#iii-calculation-directory-cleanup "标题的直接链接")

Quickly clean up unnecessary files in the directory when recalculating:

```
bash del.sh  

```
> Executing this command will delete all files matching `POSCAR_*、caly.log、contcar.py、cp2k.py、get*、gpid.py、gulpt.py、mpi*、pos*、pwscf.py、read*、remoteparallel.py、results/、rvasp.py、surface_run.py、v2lammps.py、writekp.py、step*、step、pwscf_*、data、log_dir、backup、*.sub、 lbg-*.sh、*_finish` and others.
> Please carefully check before running this command to avoid deleting files you need to keep!

## IV. Restart calculation[​](#iv-restart-calculation "标题的直接链接")

After submitting the `CALYPSO` structure prediction job on the Bohrium platform using `dpdispatcher`, if the job is accidentally interrupted, a restart is required, which can be divided into two categories:

### 1. The evolution of CALYPSO's structure is completed in a certain generation and the job has been submitted, but the connection with the computing node is lost[​](#1-the-evolution-of-calypsos-structure-is-completed-in-a-certain-generation-and-the-job-has-been-submitted-but-the-connection-with-the-computing-node-is-lost "标题的直接链接")

The CALYSPO control node needs to maintain communication with the computing node to send jobs and obtain results from the computing node. If the control node is shut down or the background `CALYPSO` job script is accidentally killed during the process of waiting for the computing node to calculate, the connection between the control node and the computing node will be lost.

1. Check the `CALYPSO` log to determine the current running generation
   If the job is run through `bash run.sh`, the log is in the `out` file. If it exists, you can open it and determine the current generation by checking the number of generated structures or according to the `step=n` under the `CALYPSO` icon. After determining the current generation, proceed with the following steps.
2. Modify the following in `input.dat` (add these lines if they do not exist)
   1. `PickUp=T`
   2. `PickStep=n`
3. Resubmit the job

```
bash run.sh  
# or  
nohup run_calypso >> out 2>&1 &  

```

Only the exact same \*.json can be continued! dpdispatcher will trigger continuation based on the hash value of the current parameter file (`machine.json` & `resources.json`). If the hash value of the current continuation is the same as the previous submission, the continuation will be triggered.

> If you want to continue, do not change the `\\*.json` files; on the contrary, if you make any changes to the `\\*.json` files (such as adding or deleting a space), it will not continue, but will start the calculation from the first generation.

### 2. Interruption of CALYPSO structure evolution process in a certain generation[​](#2-interruption-of-calypso-structure-evolution-process-in-a-certain-generation "标题的直接链接")

The calculation nodes have completed the calculation, and the results have been pulled back to the `CALYPSO` control node. An exception occurs when generating the next generation structure, such as CALYPSO error interruption, node shutdown, or manual termination, etc.
`./data` saves the output files of all generations calculated before. Taking `VASP` as an example, suppose we want to continue from the n-th generation DFT calculation after `CALYPSO`:

1. Determine the continuation generation, which can be judged through the log files as before, assuming the continuation generation is n.
2. Modify `input.dat`
   1. `PickUp=T`
   2. `PickStep=n`
3. Copy the OUTCAR, CONTCAR, and POSCAR of the n-th generation structure from `./data` to the current directory and rename them to \*\_n. This step can be completed by modifying the generation in `back.sh` to n and then executing `bash back.sh`.
4. Create a file named restart in the current folder with `touch restart`.
5. Run `bash run.sh`.

## V. Job termination and deletion[​](#v-job-termination-and-deletion "标题的直接链接")

To terminate the job, you need to kill the processes on the Calypso control node and the compute nodes in turn:

1. Kill the calypso process on the calypso control node:
   To distinguish different jobs on the control node, you can use the aforementioned showjob command to quickly view the currently running calypso programs, PIDs, and running directories, and kill them according to the PIDs.
2. Kill the compute node processes:
   Killing the calypso on the control node will not terminate the jobs currently being calculated on the compute nodes, so you need to manually kill the compute node jobs.
   Each generation structure submission will be bound under a group\_id, and the Bohrium main page job panel can see the various job group ids.
   After the control node process is killed, you can use the [bohr job management command](/en/docs/bohrctl/job) to delete it in the command line, or log in to the Bohrium interface to delete it.
   * If you want to kill the jobs of a certain job group, you can determine the jobs to be killed based on the job name (job\_name in machine.json) or group\_id, and select terminate job or delete on the right.
   * If you want to kill a specific job, you need to determine the job\_id of the job, go to the job group to find the corresponding job\_id to terminate or delete.

> Note: `terminate job` can safely stop the running task and save the results. `kill job` will stop the running task but will **not save the results**. `delete job` will **remove all calculation data** entirely.

[PreviousABACUS](/en/docs/software/ABACUS/)[NextTBPLaS](/en/docs/software/TBPLaS/)

* [Introduction](#introduction)
* [I. Running CALYPSO jobs on Bohrium](#i-running-calypso-jobs-on-bohrium)
  + [1. Start the calypso-bohrium node](#1-start-the-calypso-bohrium-node)
  + [2. Prepare input data](#2-prepare-input-data)
  + [3. Modify the CALYPSO control file](#3-modify-the-calypso-control-file)
  + [4. Modify the Bohrium configuration file](#4-modify-the-bohrium-configuration-file)
  + [5、Submit the job](#5submit-the-job)
  + [6、View the job](#6view-the-job)
* [II. job Result Analysis](#ii-job-result-analysis)
  + [Predicted structure extraction](#predicted-structure-extraction)
  + [Visualization of structure prediction evolution process](#visualization-of-structure-prediction-evolution-process)
  + [Visualization of variable component structure prediction phase diagram](#visualization-of-variable-component-structure-prediction-phase-diagram)
* [III. Calculation directory cleanup](#iii-calculation-directory-cleanup)
* [IV. Restart calculation](#iv-restart-calculation)
  + [1. The evolution of CALYPSO's structure is completed in a certain generation and the job has been submitted, but the connection with the computing node is lost](#1-the-evolution-of-calypsos-structure-is-completed-in-a-certain-generation-and-the-job-has-been-submitted-but-the-connection-with-the-computing-node-is-lost)
  + [2. Interruption of CALYPSO structure evolution process in a certain generation](#2-interruption-of-calypso-structure-evolution-process-in-a-certain-generation)
* [V. Job termination and deletion](#v-job-termination-and-deletion)



