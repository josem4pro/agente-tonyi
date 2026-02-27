# software > DP-GEN init

**Source URL:** https://docs.bohrium.com/en/docs/software/DP-GEN_init

---








DP-GEN init | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/software/DP-GEN_init)
* [English](/en/docs/software/DP-GEN_init)
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
* DP-GEN init
# DP-GEN init

This tutorial is based on Bohrium and demonstrates how to perform DP-GEN init.

init has three subcommands, init\_bulk, init\_surf, and init\_reaction

> * init\_bulk: Generating initial data for bulk systems.
> 
> 1. Relax in folder 00.place\_ele
> 2. Perturb and scale in folder 01.scale\_pert
> 3. Run a short AIMD in folder 02.md
> 4. Collect data in folder 02.md.
> 
> * init\_surf: Generating initial data for surface systems.
> 
> 1. Build specific surface in folder 00.place\_ele
> 2. Pertub and scale in folder 01.scale\_pert
> 
> * init\_reaction: Generating initial data for reactive systems.
> 
> 1. Exploring: LAMMPS
> 2. Sampling: MDDatasetBuilder
> 3. Labeling: Gaussian
> 
> For a detailed introduction and parameter description, please refer to [DP-GEN's doc](https://docs.deepmodeling.com/projects/dpgen/en/latest/)

Here, we take the Li-Si crystal structure as an example and explain the usage of init\_bulk in detail.

## Step 1: Prepare input files[​](#step-1-prepare-input-files "标题的直接链接")

Input file list

* INCAR files:
  INCAR\_md
  INCAR\_rlx
* POTCAR (one file per element)
* POSCAR (not necessarily needed)
* param.json
* machine.json

### About INCAR[​](#about-incar "标题的直接链接")

Two INCAR files are needed for init, namely INCAR\_md and INCAR\_rlx, corresponding to atomic relaxation and molecular dynamics calculation jobs, respectively.

In this example, the INCAR files are as follows:

```
INCAR_rlx  
#Parameters  
SYSTEM = dpgen_rlx  
PREC = A  
ISTART = 0  
ICHARG = 2  
#Electronic Relaxation  
ENCUT = 650  
NELM = 100  
NELMIN = 6  
NELMDL = -5  
EDIFF = 1e-06  
LREAL = .False.  
ALGO = Fast # or Normal  
#Ionic Relaxation  
IBRION = 2  
POTIM = 0.2  
ISIF = 3  
EDIFFG = -0.01  
ISYM = 0  
NSW = 100  
ISMEAR = 0  
SIGMA = 0.1  
# Write flags  
LWAVE = .False.  
LCHARG = .False.  
KSPACING = 0.16  
KGAMMA = .False.  
#KPAR = 1  
#NPAR = 1  
PSTRESS = 0.0  
NCORE = 4   

```

INCAR\_md

```
#Parameters  
SYSTEM = dpgen_md  
PREC = A  
ISTART = 0  
ICHARG = 2  
#Electronic Relaxation   
ENCUT = 650   
NELM = 100   
NELMIN = 6  
NELMDL = -5   
EDIFF = 1e-06  
LREAL = False  
ALGO = Fast # or normal  
#Ionic relaxation  
IBRION = 0  
ISIF = 2  
#EDIFFG = -0.01 in  
ISYM = 0  
NSW = 10   
ISMEAR = 0  
SIGMA = 0.1   
# MD related  
SMASS = 0   
POTIM = 2  
TEBEG = 100  
TEEND = 100  
NBLOCK = 1  
KBLOCK = 100  
# Write flags  
LWAVE = False  
LCHARG = False  
#parallel related  
#KPAR = 4  
#NPAR = 1  
KSPACING = 0.16  
KGAMMA = False  
PSTRESS = 0.0  
NCORE = 4  

```
### About param.json and machine.json[​](#about-paramjson-and-machinejson "标题的直接链接")

`param.json` and `machine.json` are the key parameter files for running dpgen. `param.json` tells dpgen what this calculation job is like, while `machine.json` tells dpgen what kind of environment you are in and what kind of machine you are using for the calculation.

This example param.json

```
{  
    "stages" : [1,2,3,4],  
    "elements": ["Li","Si"],  
    "cell_type": "diamond",  
    "latt": 10.0,  
    "super_cell": [1, 1, 1],  
    "potcars":  ["..../POTCAR_Li","..../POTCAR_Si"],   
    "relax_incar": "./INCAR_rlx",  
    "md_incar" : "./INCAR_md",  
    "skip_relax": false,  
    "scale": [0.990,1.00,1.01],  
    "pert_numb": 10,  
    "pert_box": 0.03,  
    "pert_atom": 0.01,  
    "md_nstep" : 10,  
    "coll_ndata": 5000,  
    "type_map" : ["Li","Si"],  
    "_comment": "that's all"  
}  

```

Note:

1. Check the path
   Please check `"potcars"`, `"relax_incar"`, and `"md_incar"` to change the path of the user-specified file (absolute path or relative path).
2. Specify the conformation
   If you want to use POSCAR for the init step, you need to add two parameters to specify the POSCAR file
   ```
   "from_poscar": true,  
   "from_poscar_path": "<your-POSCAR>",  
   
   ```

In the parameter file of this example, the `"cell_type"` and `"latt"` parameters are used to describe the conformation type and automatically generate a diamond-type LiSi alloy. DP-GEN version 0.10.6 and above supports `"cell_type"` values of `"hcp"`, `"fcc"`, `"diamond"`, `"sc"` and `"bcc"`. Please select the conformation according to your specific needs or the description in the literature.

1. Specify the step
   Unlike dpgen run, which records steps with record.dpgen, init does not have this file. The way to specify the step is to check the current step in dpgen.log and use the "stages" parameter to specify the start and end steps. init\_bulk has [1, 2, 3, 4] four steps, and init\_surf has [1, 2] two steps. For example, in init\_bulk, if the relaxation is successful but an error occurs during the perturbation in the second step, you can set "stages" to [2, 3, 4] and start from the second step.

machine.json:

```
{  
  "api_version": "1.0",  
  "deepmd_version": "2.1.0",  
  "train" :[  
    {  
      "command": "dp",  
      "machine": {  
        "batch_type": "Lebesgue",  
        "context_type": "LebesgueContext",  
        "local_root" : "./",  
        "remote_profile":{  
          "email": "",  
          "password": "",  
          "program_id": ,  
            "keep_backup":true,  
            "input_data":{  
                "job_type": "indicate",  
                "log_file": "00*/train.log",  
                "grouped":true,  
                "job_name": "dpgen_train_job",  
                "disk_size": 100,  
                "scass_type":"c4_m15_1 * NVIDIA T4",  
                "checkpoint_files":["00*/checkpoint","00*/model.ckpt*"],  
                "checkpoint_time":30,  
                "platform": "ali",  
                "job_type": "container",  
                "image_address": "registry.dp.tech/dptech/deepmd-kit:2.1.5-cuda11.6" ,  
                "on_demand":0  
            }  
        }  
      },  
      "resources": {  
        "number_node": 1,  
        "cpu_per_node": 4,  
        "gpu_per_node": 1,  
        "queue_name": "T4_4_15",  
        "group_size": 1  
      }  
    }  
  ],  
  "model_devi":  
    [{  
      "command": "lmp -i input.lammps -v restart 0",  
      "machine": {  
        "batch_type": "Lebesgue",  
        "context_type": "LebesgueContext",  
        "local_root" : "./",  
        "remote_profile":{  
          "email": "",  
          "password": "",  
          "program_id": ,  
            "keep_backup":true,  
            "input_data":{  
              "job_type": "indicate",  
              "log_file": "*/model_devi.log",  
              "grouped":true,  
              "job_name": "dpgen_model_devi_job",  
              "disk_size": 200,  
              "scass_type":"c4_m15_1 * NVIDIA T4",  
              "platform": "ali",  
              "job_type": "container",  
              "image_address": "registry.dp.tech/dptech/deepmd-kit:2.1.5-cuda11.6" ,  
              "on_demand":0  
            }  
        }  
      },  
      "resources": {  
        "number_node": 1,  
        "cpu_per_node": 4,  
        "gpu_per_node": 1,  
        "queue_name": "T4_4_15",  
        "group_size": 50  
      }  
    }  
  ],  
  "fp":  
    [{  
      "command": "limit -m unlimited; ulimit -s unlimited; mpirun vasp_std",  
      "machine": {  
        "batch_type": "Lebesgue",  
        "context_type": "LebesgueContext",  
        "local_root" : "./",  
        "remote_profile":{  
          "email": "",  
          "password": "",  
          "program_id": ,  
            "input_data":{  
              "api_version":2,  
              "job_type": "indicate",  
              "log_file": "task*/fp.log",  
              "grouped":true,  
              "job_name": "dpgen_fp_job",  
              "disk_size": 100,  
              "scass_type":"c16_m32_cpu",  
              "platform": "ali",  
                  "job_type": "container",  
              "image_address":"# Fill in the VASP image name here",     
              "on_demand":0  
            }  
        }  
      },  
      "resources": {  
        "number_node": 1,  
        "cpu_per_node": 16,  
        "gpu_per_node": 0,  
        "queue_name": "CPU",  
        "group_size": 50,   
        "source_list": ["/opt/intel/oneapi/setvars.sh"]  
      }  
    }  
  ]  
}  

```

Description:

1. Images

In this example, we have specified the training part to use LBG\_DeePMD-kit\_2.0.1\_v1 image, the exploration part to use LBG\_DeePMD-kit\_2.0.1\_v1 image (which also includes the LAMMPS program combined with DeePMD-kit), and the labeling part to use the VASP image (if you need to use the VASP image, please provide your VASP authorization credentials to bohrium email).

If you want to change the computing image, you can specify it through the image\_address in the machine.json file, such as if you want to use DeePMD-kit 2.2.1 version, just change the image name to registry.dp.tech/dptech/deepmd-kit:2.2.1-cuda11.6. The image name can be viewed on the "Image Center" page.

2. Please pay attention to the "command" part of fp and the "source\_list" under "resource". If there are errors in software call permissions, it may be related to these two parameters.

Preparation is complete, the folder directory is as follows:

```
$ ls  
INCAR_md  INCAR_rlx  INCAR_scf  POTCAR_Li  machine.json  param.json  POTCAR_Si  

```
## Step 2: DP-GEN init[​](#step-2-dp-gen-init "标题的直接链接")

Run in the folder directory with the prepared files:

```
nohup dpgen init_bulk param.json machine.json 1>log 2>err&  

```

Open Bohrium-Job Management and you can see the job that was just successfully submitted. init\_bulk will do two fp steps, which are relaxation and molecular dynamics simulation.

After the job is completed, check the directory:

> To see the directory structure, use the tree command, you need to apt install tree to install tree, and then use the tree command in the file directory to see the tree diagram.

```
.  
├── dpdispatcher.log  
├── dpgen.log  
├── err  
├── INCAR_md  
├── INCAR_rlx  
├── INCAR_scf  
├── lisi.diamond.01x01x01  
│   ├── 00.place_ele  
│   │   ├── Backup files, etc  
│   │   ├── INCAR  
│   │   ├── POSCAR  
│   │   ├── POSCAR.unit  
│   │   ├── POTCAR  
│   │   ├── run_1659588706.sh  
│   │   ├── run_1659589787.sh  
│   │   ├── run_1659590393.sh  
│   │   ├── sys-0001-0001  
│   │   │   ├── 806905fcd0a0ce5b7a072c7ce7e3c1dcfd497471_task_tag_finished  
│   │   │   ├── CHG  
│   │   │   ├── CHGCAR  
│   │   │   ├── CONTCAR  
│   │   │   ├── DOSCAR  
│   │   │   ├── EIGENVAL  
│   │   │   ├── fp.log  
│   │   │   ├── IBZKPT  
│   │   │   ├── INCAR -> ../INCAR  
│   │   │   ├── OSZICAR  
│   │   │   ├── OUTCAR  
│   │   │   ├── PCDAT  
│   │   │   ├── POSCAR  
│   │   │   ├── POTCAR -> ../POTCAR  
│   │   │   ├── REPORT  
│   │   │   ├── vasprun.xml  
│   │   │   ├── WAVECAR  
│   │   │   └── XDATCAR  
│   │   └── tmp_log  
│   ├── 01.scale_pert  
│   │   └── sys-0001-0001  
│   │       └── scale-1.000  
│   │           ├── 000000  
│   │           │   └── POSCAR  
│   │           ├── 000001  
│   │           │   └── POSCAR  
│   │           ├── 000002  
│   │           │   └── POSCAR  
│   │           ├── 000003  
│   │           │   └── POSCAR  
│   │           ├── 000004  
│   │           │   └── POSCAR  
│   │           └── POSCAR  
│   ├── 02.md  
│   │   ├── Backup files, etc  
│   │   ├── INCAR  
│   │   ├── POTCAR  
│   │   ├── run_1659604259.sh  
│   │   ├── sys-0001-0001  
│   │   │   ├── deepmd  
│   │   │   │   ├── box.raw  
│   │   │   │   ├── coord.raw  
│   │   │   │   ├── energy.raw  
│   │   │   │   ├── force.raw  
│   │   │   │   ├── set.000  
│   │   │   │   │   ├── box.npy  
│   │   │   │   │   ├── coord.npy  
│   │   │   │   │   ├── energy.npy  
│   │   │   │   │   ├── force.npy  
│   │   │   │   │   └── virial.npy  
│   │   │   │   ├── type_map.raw  
│   │   │   │   ├── type.raw  
│   │   │   │   └── virial.raw  
│   │   │   └── scale-1.000  
│   │   │       ├── 000000  
│   │   │       │   ├── 00af13e72478f19ea730f67a982bb9c29dcd0c04_task_tag_finished  
│   │   │       │   ├── CHG  
│   │   │       │   ├── CHGCAR  
│   │   │       │   ├── CONTCAR  
│   │   │       │   ├── DOSCAR  
│   │   │       │   ├── EIGENVAL  
│   │   │       │   ├── fp.log  
│   │   │       │   ├── IBZKPT  
│   │   │       │   ├── INCAR -> ../../../INCAR  
│   │   │       │   ├── OSZICAR  
│   │   │       │   ├── OUTCAR  
│   │   │       │   ├── PCDAT  
│   │   │       │   ├── POSCAR  
│   │   │       │   ├── POTCAR -> ../../../POTCAR  
│   │   │       │   ├── REPORT  
│   │   │       │   ├── vasprun.xml  
│   │   │       │   ├── WAVECAR  
│   │   │       │   └── XDATCAR  
│   │   │       ├── 000001  
│   │   │       │   └── ...  
│   │   │       ├── 000002  
│   │   │       │   └── ...  
│   │   │       ├── 000003  
│   │   │       │   └── ...  
│   │   │       └── 000004  
│   │   │           └── ...  
│   │   └── tmp_log  
│   └── param.json  
├── log  
├── machine.json  
├── param.json  
├── POTCAR_Li  
└── POTCAR_Si  

```
## Step 3: Monitor Job Status and Results[​](#step-3-monitor-job-status-and-results "标题的直接链接")

Refer to [Monitor Tasks](/en/docs/quickstart/Status) for monitoring job status.

Refer to [DP-GEN](/en/docs/software/DP-GEN) and [Result Acquisition](/en/docs/quickstart/Result) for obtaining execution results.

At this point, the dataset required for DP training is obtained through the DPGEN init\_bulk process. The next step is to run DPGEN run for iterations and explore the sample space of the entire potential energy surface.

To monitor the job status, refer to [Monitoring Tasks](/en/docs/quickstart/Status).

To obtain the results, refer to [DP-GEN](/en/docs/software/DP-GEN) and [Results Retrieval](/en/docs/quickstart/Result).

At this point, the autotest is completed, and you can view the results in the `confs/mp-3034/<property-name>` folder's `result` file. For example, in this case, the eos result can be found in `confs/mp-3034/eos_00/result.out`.

[PreviousDP-GEN](/en/docs/software/DP-GEN/)[NextDP-GEN simplify](/en/docs/software/DP-GEN_simplify/)

* [Step 1: Prepare input files](#step-1-prepare-input-files)
  + [About INCAR](#about-incar)
  + [About param.json and machine.json](#about-paramjson-and-machinejson)
* [Step 2: DP-GEN init](#step-2-dp-gen-init)
* [Step 3: Monitor Job Status and Results](#step-3-monitor-job-status-and-results)



