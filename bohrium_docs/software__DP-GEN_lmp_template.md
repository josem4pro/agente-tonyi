# software > DP-GEN lmp template

**Source URL:** https://docs.bohrium.com/en/docs/software/DP-GEN_lmp_template

---








Custom LAMMPS template for DP-GEN model\_devi step | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/software/DP-GEN_lmp_template)
* [English](/en/docs/software/DP-GEN_lmp_template)
[Console](https://bohrium.dp.tech/home)
# Custom LAMMPS template for DP-GEN model\_devi step

Sometimes in the DP-GEN model\_devi step, users need to customize scripts. For example, <https://github.com/deepmodeling/dpgen/tree/master/examples/run/dp-lammps-enhance_sampling> is an example script for enhanced sampling.

Parameter file param.json

When there is a "template" parameter under "model\_devi\_jobs", the model\_devi step uses the specified lmp/input.lammps as the template:

```
    "model_devi_jobs":  [          
        {   "sys_idx": [0],"traj_freq": 10,"_idx": "00",  
            "template":{ "lmp": "lmp/input.lammps", "plm": "lmp/input.plumed" },  
            "rev_mat":{ "lmp": {"V_NSTEPS": [20000], "V_TEMP": [300], "V_PRES": [1]},  
                        "plm": {"V_TEMP":  [300], "V_STRIDE": [10]}  
                      }  
        },  

```

"plm" specifies the file used for enhanced sampling. If you don't need plumed, you need to delete the "model\_devi\_plumed" parameter on line 95 of the example parameter file (it defaults to false).

LAMMPS script input.lammps

Note that the dump line needs to be modified to `dump dpgen_dump`.

```
dump           dpgen_dump  
#dump          2 all custom 100 vel.xyz id type vx vy vz  

```

When using the template, dpgen will call the revise\_lmp\_input\_dump function to write trj\_freq in input.lammps, instead of defining DUMP\_FREQ at the beginning of the file and then calling it as in the general case.

```
def revise_lmp_input_dump(lmp_lines, trj_freq):  
    idx = find_only_one_key(lmp_lines, ['dump', 'dpgen_dump'])  
    lmp_lines[idx] = "dump            dpgen_dump all custom %d traj/*.lammpstrj id type x y z\  
" % trj_freq  
    return lmp_lines  

```



