# software > DP-GEN autotest

**Source URL:** https://docs.bohrium.com/en/docs/software/DP-GEN_autotest

---








DP-GEN Auto-test | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/software/DP-GEN_autotest)
* [English](/en/docs/software/DP-GEN_autotest)
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
* DP-GEN Auto-test
# DP-GEN Auto-test

This article is based on Bohrium and takes the Al-Mg-Cu potential function in DP-Library as an example (upgraded with DeePMD-kit after downloading from DPLibrary) for property calculation.

Note: The software versions used in this tutorial: DP-GEN 0.10.6, DP-Dispatcher 0.4.16, dpdata 0.2.8.

## Step 1: Prepare files and folders[​](#step-1-prepare-files-and-folders "标题的直接链接")

First, create a new working directory, here we use a folder named autotest as an example, and put the model file you want to calculate (e.g., graph.pb) inside.

In this example, the model file needs to be upgraded to the corresponding version of dp. You can use the `dp convert-from 1.1 -i graph.pb -o new_graph.pb` command to upgrade the model under the DeePMD-kit image. You can view the usage of this command with `dp convert-from -h`.
You can rename the old model to old\_graph.pb and use this script to submit jobs and recycle files in Bohrium without opening a new node, which is very convenient.

submit.json

```
{  
    "job_name": "dp-update-model",  
    "job_type": "container",  
    "image_address": "registry.dp.tech/dptech/deepmd-kit:2.1.5-cuda11.6",  
    "command": "dp convert-from 1.1 -i old_graph.pb -o graph.pb",  
    "log_file": "tmp_log",  
    "backward_files": ["graph.pb"],  
    "program_id": 0000,  
    "platform": "ali",  
    "disk_size": 200,  
    "machine_type": "c16_m32_cpu"  
}  

```

**Note**: Replace the `0000` after `"project_id":` with your own project ID, which can be viewed on the "[Project Management](https://bohrium.dp.tech/projects)" page.

Since you need to use the Bohrium CLI to submit tasks, you first need to [install the Bohrium CLI](/en/docs/bohrctl/install#preparation).

Run the following commands respectively:

```
mkdir autotest  
cd autotest  
mv <the-path-where-you-download-graph.pb>/graph.pb old_graph.pb  
bohr job submit -i submit.json -p ./  

```

(If the file graph.pb is not automatically returned, you need to download it from the job management page and place it in the current autotest folder.)

> Note: If your model does not require an upgrade, you only need the following command.

```
mkdir autotest  
cd autotest  
mv <the-path-where-graph.pb-is>/graph.pb graph.pb   

```

---

Prepare the configuration folder and parameter files:

```
mkdir confs  
cd confs  
mkdir mp-3034  
cd ..  
touch relaxation.json  
touch machine.json  
touch property.json  

```

1. In the confs folder, use the MaterialsProject configuration number mp-xxx to name the folder, and autotest will automatically download the corresponding POSCAR file from the MaterialsProject.
   
   If you obtain the configuration through MaterialsProject, you need to configure the API key for the server.
   
   If you use autotest without configuring the MaterialsProject API key, you will see an error like this:

```
(base) ➜ autotest_demo dpgen autotest make relaxation.json                
NOTE: Some configuration directories are not set up yet:   
        /root/.gromacswrapper  
        /root/.gromacswrapper/qscripts  
        /root/.gromacswrapper/templates  
NOTE: You can create the configuration file and directories with:  
        >>> import gromacs  
        >>> gromacs.config.setup()  
/opt/anaconda3/lib/python3.9/site-packages/gromacs/__init__.py:286: GromacsImportWarning: Some Gromacs commands were NOT found; maybe source GMXRC first? The following are missing:  
['release']  
  
  warnings.warn("Some Gromacs commands were NOT found; "  
DeepModeling  
------------  
Version: 0.10.6  
Date:    Jul-11-2022  
Path:    /opt/anaconda3/lib/python3.9/site-packages/dpgen  
  
Dependency  
------------  
     numpy     1.20.3   /opt/anaconda3/lib/python3.9/site-packages/numpy  
    dpdata      0.2.8   /opt/anaconda3/lib/python3.9/site-packages/dpdata  
  pymatgen            unknown version or path  
     monty  2022.3.12   /opt/anaconda3/lib/python3.9/site-packages/monty  
       ase     3.22.1   /opt/anaconda3/lib/python3.9/site-packages/ase  
  paramiko     2.10.3   /opt/anaconda3/lib/python3.9/site-packages/paramiko  
 custodian  2022.2.13   /opt/anaconda3/lib/python3.9/site-packages/custodian  
  
Reference  
------------  
Please cite:  
Yuzhi Zhang, Haidi Wang, Weijie Chen, Jinzhe Zeng, Linfeng Zhang, Han Wang, and Weinan E,  
DP-GEN: A concurrent learning platform for the generation of reliable deep learning  
based potential energy models, Computer Physics Communications, 2020, 107206.  
------------  
  
Description  
------------  
You have to get a MAPI_KEY from materials.org  
and execute following command:  
echo "export MAPI_KEY=yourkey">> ~/.bashrc  
source ~/.bashrc  

```

Of course, you can also configure with ~ / .zshrc on Bohrium:

```
echo "export MAPI_KEY=yourkey">> ~/.zshrc  
source ~/.zshrc  

```
> The API key for MaterialsProject can be obtained [here](https://legacy.materialsproject.org/janrain/loginpage/?next=/dashboard) (if you haven't registered/logged in, log in and then click this link)

1. If you use the `std-xxx` naming, autotest can also automatically generate the corresponding configuration. DP-GEN 0.10.6 and later versions support `std-fcc`, `std-hcp`, `std-bcc`, `std-dhcp`, `std-diamond`, and `std-sc`.
2. Of course, you can also use other naming methods, place the corresponding POSCAR file in `confs/<your-conf-name>`, and then use the same steps (make-run-post).

The specific reading method of POSCAR in DP-GEN is as follows:

```
    if len(ele_list) == 1 or 'single' in inter_param:  
        if 'single' in inter_param:  
            element_label = int(inter_param['single'])  
        else:  
            element_label = 0  
        for ii in conf_dirs:  
            os.chdir(ii)  
            crys_type = ii.split('/')[-1]  
            dlog.debug('crys_type: %s' % crys_type)  
            dlog.debug('pwd: %s' % os.getcwd())  
            if crys_type == 'std-fcc':  
                if not os.path.exists('POSCAR'):  
                    crys.fcc1(ele_list[element_label]).to('POSCAR', 'POSCAR')  
            elif crys_type == 'std-hcp':  
                if not os.path.exists('POSCAR'):  
                    crys.hcp(ele_list[element_label]).to('POSCAR', 'POSCAR')  
            elif crys_type == 'std-dhcp':  
                if not os.path.exists('POSCAR'):  
                    crys.dhcp(ele_list[element_label]).to('POSCAR', 'POSCAR')  
            elif crys_type == 'std-bcc':  
                if not os.path.exists('POSCAR'):  
                    crys.bcc(ele_list[element_label]).to('POSCAR', 'POSCAR')  
            elif crys_type == 'std-diamond':  
                if not os.path.exists('POSCAR'):  
                    crys.diamond(ele_list[element_label]).to('POSCAR', 'POSCAR')  
            elif crys_type == 'std-sc':  
                if not os.path.exists('POSCAR'):  
                    crys.sc(ele_list[element_label]).to('POSCAR', 'POSCAR')  
  
            os.chdir(cwd)  
    task_dirs = []  
    # make task directories like mp-xxx/relaxation/relax_task  
    # if mp-xxx/exists then print a warning and exit.  
    # ...  
    for ii in conf_dirs:  
        crys_type = ii.split('/')[-1]  
        dlog.debug('crys_type: %s' % crys_type)  
  
        if 'mp-' in crys_type and not os.path.exists(os.path.join(ii, 'POSCAR')):  
            get_structure(crys_type).to('POSCAR', os.path.join(ii, 'POSCAR'))  
  
        poscar = os.path.abspath(os.path.join(ii, 'POSCAR'))  

```

---

The prepared files are in the folder where you want to perform autotest. For example, let's call this folder autotest. Then the files and folders you created in the above steps are: (Folder names are in bold)

```
autotest ──  relaxation.json  
                |──  property.json  
                |──  machine.json  
                |──  confs ── mp-3034  
                └──  graph.pb  

```
## Step 2: Relaxation[​](#step-2-relaxation "标题的直接链接")

In the autotest directory, first prepare the relaxation.json, which is the parameter file needed for autotest to do relaxation.

The example relaxation.json is as follows:

```
{  
    "structures":         ["confs/mp-3034"],  
    "interaction": {  
            "type":        "deepmd",  
            "model":       "graph.pb",  
            "in_lammps":   "lammps_input/in.lammps",  
            "type_map":   {"Mg":0,"Al": 1,"Cu":2}   
    },  
    "relaxation": {  
            "cal_setting":{"etol": 1e-12,  
                           "ftol": 1e-6,  
                           "maxiter": 5000,  
                           "maximal": 500000,  
                           "relax_shape":     true,  
                           "relax_vol":       true}  
    }  
}  

```

Then execute the command in the autotest directory

```
dpgen autotest make relaxation.json  
dpgen autotest run relaxation.json machine.json  
dpgen autotest post relaxation.json   

```

Note:

1. The old version of DP-GEN has a problem generating scripts in the make step, and you need to add "\* \*" after pair\_coeff.
   You can add it manually or use the following command

```
sed -i "s/pair_coeff/pair_coeff * */g"  `grep pair_coeff -rl ${_Path}/${array_mp[${i}]}  

```

2. The relaxation step only does minimization, without specifying the ensemble.

Step 3: Calculate properties

* Currently, autotest can calculate the following properties:
  + EOS
  + Elastic
  + Vacancy
  + Surface
  + Interstitial

The example property.json template is as follows:

```
{  
    "structures":       ["confs/mp-3034"],  
    "interaction": {  
        "type":          "deepmd",  
        "model":         "graph.pb",  
        "deepmd_version":"2.1.0",  
        "type_map":     {"Mg":0,"Al": 1,"Cu":2}  
    },  
    "properties": [  
        {  
         "type":         "eos",  
         "vol_start":    0.9,  
         "vol_end":      1.1,  
         "vol_step":     0.01,  
        "fix_shape":true  
        },  
        {  
         "type":         "elastic",  
         "norm_deform":  2e-2,  
         "shear_deform": 5e-2  
        },  
        {  
         "type":             "vacancy",  
         "supercell":        [1, 1, 1]  
        },  
        {  
         "type":         "interstitial",  
         "supercell":   [3, 3, 3],  
         "insert_ele":  ["Mg","Al","Cu"],  
         "conf_filters":{"min_dist": 1.5},  
         "cal_setting": {"input_prop": "lammps_input/lammps_high"}  
        },  
        {  
         "type":           "surface",  
         "min_slab_size":  10,  
         "min_vacuum_size":11,  
         "max_miller":     1,  
         "cal_type":       "static",  
         "static-opt": true,  
        "pert_xz":0.01,  
        "relax_box":false  
        }  
    ]  
}  

```

Next, run the following commands in the autotest directory:

```
dpgen autotest make property.json  
nohup dpgen autotest run property.json machine.json &  
dpgen autotest post property.json   

```
> Note: In older versions of DP-GEN, there is a problem with the generated script after the "make" step. You need to add " \* \*" after "pair\_coeff". You can either add it manually or use the following command:

```
sed -i "s/pair_coeff/pair_coeff * */g"  `grep pair_coeff -rl ${_Path}/${array_mp[${i}]}  

```
## Step 3: Monitor job status and results[​](#step-3-monitor-job-status-and-results "标题的直接链接")

To monitor the job status, refer to [Monitoring Tasks](/en/docs/quickstart/Status).

To obtain the results, refer to [DP-GEN](/en/docs/software/DP-GEN) and [Results Retrieval](/en/docs/quickstart/Result).

At this point, the autotest is completed, and you can view the results in the `confs/mp-3034/<property-name>` folder's `result` file. For example, in this case, the eos result can be found in `confs/mp-3034/eos_00/result.out`.

[PreviousDP-GEN simplify](/en/docs/software/DP-GEN_simplify/)[NextGROMACS](/en/docs/software/GROMACS/)

* [Step 1: Prepare files and folders](#step-1-prepare-files-and-folders)
* [Step 2: Relaxation](#step-2-relaxation)
* [Step 3: Monitor job status and results](#step-3-monitor-job-status-and-results)



