# software > DP-GEN simplify

**Source URL:** https://docs.bohrium.com/en/docs/software/DP-GEN_simplify

---








DP-GEN simplify | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/software/DP-GEN_simplify)
* [English](/en/docs/software/DP-GEN_simplify)
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
* DP-GEN simplify
# DP-GEN simplify

This article introduces how to perform DP-GEN simplify on the Bohrium platform.

## Step 1: Turn on the node[​](#step-1-turn-on-the-node "标题的直接链接")

Refer to the "[DPGEN Tutorial](/en/docs/software/DP-GEN)" for how to turn on the node.

## Step 2: Prepare input files[​](#step-2-prepare-input-files "标题的直接链接")

To use DP-GEN simplify, you need to prepare initial data, parameter files, and calculation files. Take perovskite as an example:

```
(base) ➜ example tree  
.  
├── data  
│   ├── init.000  
│   │   ├── set.000  
│   │   │   ├── box.npy  
│   │   │   ├── coord.npy  
│   │   │   ├── energy.npy  
│   │   │   ├── force.npy  
│   │   │   └── virial.npy  
│   │   ├── type_map.raw  
│   │   └── type.raw  
│   ├── sys.000  
│   │   ├── set.000  
│   │   │   ├── box.npy  
│   │   │   ├── coord.npy  
│   │   │   ├── energy.npy  
│   │   │   ├── force.npy  
│   │   │   └── virial.npy  
│   │   ├── type_map.raw  
│   │   └── type.raw  
│   └── sys.001  
│       ├── set.000  
│       │   ├── box.npy  
│       │   ├── coord.npy  
│       │   ├── energy.npy  
│       │   ├── force.npy  
│       │   └── virial.npy  
│       ├── type_map.raw  
│       └── type.raw  
├── simplify_example  
│   ├── INCAR  
│   ├── machine_test_simplify.json  
│   └── simplify.json  
└── vasp_inputs  
    ├── POTCAR_C  
    ├── POTCAR_H  
    ├── POTCAR_I  
    ├── POTCAR_N  
    └── POTCAR_Pb_d  

```
### Example simplify.json[​](#example-simplifyjson "标题的直接链接")

```
{  
  "type_map": ["I","Pb","C","N","H"],  
  "mass_map": [126.90447, 207.2, 12.0108, 14.0067, 1.00795],  
  
  "pick_data":  "../data",   
  "init_data_prefix": "",  
  "init_data_sys":   [],  
  "sys_configs": [null],  
  "sys_batch_size":  [1,1,1],   
  
  "_comment": " 00.train ",  
  "numb_models": 4,  
  "model_devi_activation_func":[["tanh","tanh"],["tanh","gelu"],["gelu","gelu"],["gelu","tanh"]],  
  
  "train_param": "input.json",  
   
  "default_training_param": {  
    "model": {  
      "type_map":           ["I","Pb","C","N","H"],  
      "descriptor": {          
        "type":             "se_e2_a",  
        "sel":   
        [  
          20,  
          8,  
          8,  
          8,  
          48  
        ],  
        "rcut_smth":        2.00,  
        "rcut":             6.00,  
        "neuron":           [25, 50, 100],  
        "resnet_dt":        false,  
        "type_one_side":     true,  
        "trainable":      true,  
          "axis_neuron":      12,  
        "seed":             0  
      },  
      "fitting_net": {  
        "neuron":           [240, 240, 240],  
        "resnet_dt":        true,  
        "trainable":      [true, true, true, true],  
        "seed": 0  
      }  
    },  
      "loss": {  
        "start_pref_e": 0.02,  
        "limit_pref_e": 2,  
        "start_pref_f": 1000,  
        "limit_pref_f": 2,  
        "start_pref_v": 0.01,  
        "limit_pref_v": 1  
    },  
      "learning_rate": {  
        "type":              "exp",  
        "start_lr":          0.001,  
        "decay_steps":       100000,  
        "decay_rate":        0.95  
    },  
      "training": {  
        "set_prefix":        "set",  
        "stop_batch":        1000000,  
        "batch_size":        "auto",  
        "seed": 1,  
        "_comment":          "frequencies counted in batch",  
        "disp_file":         "lcurve.out",  
        "disp_freq":         100000,  
        "numb_test":         4,  
        "save_freq":         100000,  
        "save_ckpt":         "model.ckpt",   
        "disp_training":     true,  
        "time_training":     true,  
        "profiling":         false,  
        "profiling_file":    "timeline.json"  
    }  
  },  
  
  "_comment":                   "02.fp",  
  "fp_style":                   "vasp",  
  "fp_skip_bad_box":  "length_ratio:5;height_ratio:5",  
  "fp_accurate_threshold":       0.95,  
  "fp_accurate_soft_threshold":  0.90,  
  "shuffle_poscar":              false,  
  "fp_task_max":                 20,  
  "fp_task_min":                 5,  
  "ratio_failed":                0.30,  
  "fp_pp_path": "../vasp_inputs/",  
  "fp_pp_files": ["POTCAR_I","POTCAR_Pb_d","POTCAR_C","POTCAR_N","POTCAR_H"],  
  "fp_incar": "INCAR",  
  
  "use_clusters": false,  
  "labeled": false,  
  "init_pick_number":20,  
  "iter_pick_number":20,  
  "model_devi_f_trust_lo":0.30,  
  "model_devi_f_trust_hi":100.00,   
  "cvasp": false  
}  
  

```
### Example machine.json[​](#example-machinejson "标题的直接链接")

```
{  
    "api_version": "1.0",  
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
          "project_id": 0000,  
              "input_data":{  
                  "api_version":2,  
                  "job_type": "indicate",  
                  "log_file": "00*/lcurve.out",  
                  "grouped": true,  
                  "job_name": "simplify_MAPbI3-scan_train_job",  
                  "disk_size": 100,  
                  "scass_type":"c8_m32_1 * NVIDIA V100",  
                  "platform": "ali",  
                  "checkpoint_files": ["00*/model.ckpt*", "00*/checkpoint"],  
                  "checkpoint_time": 15,  
                  "job_type": "container",  
                  "image_address": "registry.dp.tech/dptech/deepmd-kit:2.1.5-cuda11.6" ,  
                  "on_demand":0  
              }  
          }  
        },  
        "resources": {  
          "number_node": 15,  
          "cpu_per_node": 4,  
          "gpu_per_node": 1,  
          "queue_name": "V100_8_32",  
          "group_size": 1  
        }  
      }],  
    "model_devi":  
      [{  
        "command": "dp",  
        "machine": {  
        "batch_type": "Lebesgue",  
        "context_type": "LebesgueContext",  
        "local_root" : "./",  
          "remote_profile":{  
          "email": "",  
          "password": "",  
          "project_id": 0000,  
              "input_data":{  
                "api_version":2,  
                "job_type": "indicate",  
                "log_file": "cubic-*/*/md.log",  
                "grouped": true,  
                "job_name": "MAPbI3-scan_md_job",  
                "disk_size": 100,  
                "scass_type":"c8_m32_1 * NVIDIA V100",  
                "platform": "ali",  
                "checkpoint_files": "sync_files",  
                "checkpoint_time": 15,  
                "job_type": "container",  
                "image_address": "registry.dp.tech/dptech/deepmd-kit:2.1.5-cuda11.6" ,  
                "on_demand":0  
              }  
          }  
        },  
        "resources": {  
          "number_node": 15,  
          "cpu_per_node": 4,  
          "gpu_per_node": 1,  
          "queue_name": "V100_8_32",  
          "group_size": 1  
        }  
      }],  
    "fp":  
      [{  
        "command": "ulimit -m unlimited; ulimit -s unlimited; mpirun -n 32 vasp_std",  
        "machine": {  
        "batch_type": "Lebesgue",  
        "context_type": "LebesgueContext",  
        "local_root" : "./",  
          "remote_profile":{  
          "email": "",  
          "password": "",  
          "project_id": 0000,  
              "input_data":{  
                "api_version":2,  
                "job_type": "indicate",  
                "log_file": "**/fp.log",  
                "grouped": true,  
                "job_name": "simplify_MAPbI3-scan_fp_job",  
                "disk_size": 100,  
                "scass_type":"c32_m256_cpu",  
                "platform": "ali",  
                "checkpoint_files": "sync_files",  
                "checkpoint_time": 15,  
                "job_type": "container",  
                "image_address":"You need to provide an Authorization certificate via WeChat Work at 17710231129 to obtain the VASP image address.",  
                "on_demand":0  
              }  
          }  
        },  
        "resources": {  
          "number_node": 15,  
          "cpu_per_node": 32,  
          "gpu_per_node": 0,  
          "queue_name": "CPU",  
          "group_size": 1,  
      "source_list": ["/opt/intel/oneapi/setvars.sh"]  
        }  
      }  
    ]  
  }  

```

Please note that the `"project_id":` followed by `0000` in the document needs to be replaced with your own project ID, which can be viewed on the "[Project Management](https://bohrium.dp.tech/projects)" page.

## Step 3: Submit Job[​](#step-3-submit-job "标题的直接链接")

Execute the following command in the `/simplify_example` directory:

```
nohup dpgen simplify simplify.json machine.json 1>log 2>err&  

```

To monitor job status and obtain results, please refer to the [DP-GEN](/en/docs/software/DP-GEN) documentation.

[PreviousDP-GEN init](/en/docs/software/DP-GEN_init/)[NextDP-GEN Auto-test](/en/docs/software/DP-GEN_autotest/)

* [Step 1: Turn on the node](#step-1-turn-on-the-node)
* [Step 2: Prepare input files](#step-2-prepare-input-files)
  + [Example simplify.json](#example-simplifyjson)
  + [Example machine.json](#example-machinejson)
* [Step 3: Submit Job](#step-3-submit-job)



