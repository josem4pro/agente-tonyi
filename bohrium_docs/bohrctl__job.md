# bohrctl > job

**Source URL:** https://docs.bohrium.com/en/docs/bohrctl/job

---








Job Management Commands：job | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/bohrctl/job)
* [English](/en/docs/bohrctl/job)
[Console](https://bohrium.dp.tech/home)

* [Homepage](/en/docs/)
* [Quick Start](#)
* [Command Line（New）](#)
  + [Bohrium CLI](/en/docs/bohrctl/about)
  + [Install Bohrium CLI](/en/docs/bohrctl/install)
  + [Job](/en/docs/bohrctl/job)
  + [Job group management](/en/docs/bohrctl/job_group)
  + [Node management](/en/docs/bohrctl/node)
  + [Machine configuration](/en/docs/bohrctl/machine)
  + [Dataset management](/en/docs/bohrctl/dataset)
  + [Image management](/en/docs/bohrctl/image)
  + [Project management](/en/docs/bohrctl/project)
* [Command Line](#)
* [Best Practice](#)
* [User Guide](#)
* [Softwares](#)
* [FAQ](#)
* [More Help](/en/docs/MoreHelp)
* [Extensions](#)


* Command Line（New）
* Job
# Job Management Commands：job

## Query：list[​](#querylist "标题的直接链接")

Command Entry:
`bohr job list`

Summary:

```
Usage:  
  bohr job list [flags]  
  
Aliases:  
  list, -ls  
  
Flags:  
      --csv                output with CSV format  
  -f, --fail               only show failed job  
  -i, --finish             only show finished job  
  -h, --help               help for list  
  -j, --job_group_id int   job group id  
      --json               output with JSON format  
      --noheader           does not print header information  
  -n, --number int         number of results to be displayed(default 10)  
  -p, --pending            only show pending job  
  -q, --quiet              only show job id  
  -r, --running            only show running job  
  -s, --scheduling         only show scheduling job  
  -d, --stopped            only show stopped job  
  -t, --stopping           only show stopping job  
      --yaml               output in YAML format  

```

Parameter description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --job\_group\_id | -j | Show tasks under job group id | N o |
| --fail | -f | Only show failed tasks | No |
| --pending | -p | Only show pending tasks | No |
| --running | -r | Only show running tasks | No |
| --finish | -i | Only show finished tasks | No |
| --scheduling | -s | Only show scheduling tasks | No |
| --stopping | -t | Only show stopping tasks | No |
| --stopped | -d | Only show stopped tasks | No |
| --quiet | -q | Only show Job ID | No |
| --number | -n | Number of jobs to display | No |

Example：

```
bohr job list -n 20 --yaml  
# Display the most recent 20 job details in YAML format  
bohr job list -j 1022 -f  
# View all failed jobs under Job Group ID 1022  

```

![bohr job list](/en/assets/images/QQ20240607-182427@2x-827935d55f73a940286d1b6872e06525.png)

## Submit：submit[​](#submitsubmit "标题的直接链接")

Command Entry:
`bohr job submit`

Summary:

```
Usage:  
  bohr job submit [flags]  
  
Examples:  
$ bohr job submit  
  
  
Flags:  
  -c, --command string             command  
  -i, --config_file string         config file  
  -h, --help                       help for submit  
  -m, --image_address string       image name  
  -p, --input_directory string     input directory path (default "./")  
  -g, --job_group_id int           job group id  
  -n, --job_name string            job name  
  -l, --log_file string            log file  
  -t, --machine_type string        machine type  
      --max_reschedule_times int   max reschedule times  
      --max_run_time int           max run time(measured in minutes)  
      --nnode int                  nnode (default 1)  
      --project_id int             project id  
  -r, --result_path string         result path  

```

Parameter description:

| Parameter | Abbreviation | Required | Description |
| --- | --- | --- | --- |
| --command | -c | Yes | Task execution command |
| --config\_file | -i | No | Predefined configuration file; fields declared in the command line will replace those in the file |
| --image\_address | -m | Yes | Image address; select different image addresses based on task type |
| --input\_directory | -p | No | Input files, e.g., -p ./ means current directory (default is ./) |
| --job\_group\_id | -g | No | Job group id (obtained from bohr job\_group create) |
| --job\_name | -n | No | Job name |
| --log\_file | -l | No | Log file |
| --machine\_type | -t | Yes | Machine configuration |
| --max\_reschedule\_times |  | No | Maximum reschedule times |
| --max\_run\_time |  | No | Maximum runtime (in minutes)） |
| --nnode |  | No | Number of compute nodes to run in parallel |
| --project\_id |  | Yes | Project ID, which you can view in project management |
| --result\_path | -r | No | Automatically download result files to specified directory; data can be downloaded to personal or share disk, with parameter `-r` followed by a path starting with `/share` or `/personal` |

Attention

The `job_group_id` used here is different from the `JobGroupId` obtained after creating a task. The `job_group_id` needs to be created through [bohr job\_group create](/en/docs/bohrctl/job_group) to meet the requirement of submitting multiple tasks into the same job group.

Example：

```
bohr job submit -i job.json -p ./input   
# Use the files in job.json and treat the files in the input directory as input.  

```

--config\_file -i JSON file example

```
{  
    "job_name": "DeePMD-kit test",  
    "command": "cd se_e2_a && dp train input.json > tmp_log 2>&1 && dp freeze -o graph.pb",  
    "log_file": "se_e2_a/tmp_log",  
    "backward_files": ["se_e2_a/lcurve.out","se_e2_a/graph.pb"],  
    "project_id": 0000,  
    "machine_type": "c32_m64_cpu",  
    "image_address": "registry.dp.tech/dptech/lammps:29Sep2021",  
    "input_directory": "./Bohrium_LAMMPS_example",  
    "job_group_id": 0000,  
    "result_path": "/personal",   
    "dataset_path": ["/bohr/test-rihu/v1"],  
    "max_reschedule_times": 2,  
    "max_run_time": 12,  
    "nnode": 1  
}  

```
## Delete：delete[​](#deletedelete "标题的直接链接")

Command Entry:

`bohr job delete`

Summary:

```
Usage:  
  bohr job delete <job_id>... [flags]  
  
Flags:  
  -h, --help          help for delete  
      --job_id ints   Job ID(s) (can be used multiple times)  

```

Parameter description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --job\_id |  | Deleted job ID | Yes |

Example：

```
bohr job delete  1234  2345   
# Delete the task with IDs 1234 and 2345  

```
## Terminate early：terminate[​](#terminate-earlyterminate "标题的直接链接")

Command Entry:

`bohr job terminate`

Summary:

```
Usage:  
  bohr job terminate <job_id>... [flags]  
  
Flags:  
  -h, --help          help for terminate  
      --job_id ints   Job ID(s)  (can be used multiple times)  

```

Parameter description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --job\_id | - | Job ID for early termination | Yes |

Example：

```
bohr job terminate  1234 2345  
# Terminate the task with IDs 1234 and 2345 early  

```
## Kill：kill[​](#killkill "标题的直接链接")

Command Entry:

`bohr job kill`

Summary:

```
Usage:  
  bohr job kill <job_id>... [flags]  
  
Flags:  
  -h, --help          help for kill  
      --job_id ints   Job ID(s) (can be used multiple times)  

```

Parameter description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --job\_id |  | kill job ID | Yes |

Example：

```
bohr job kill  1234 2345  
# Kill the task with IDs 1234 and 2345  

```
# Download log：log

Command Entry:

`bohr job log`

Summary:

```
Usage:  
  bohr job log [flags]  
  
Flags:  
  -h, --help              help for log  
  -j, --job_id ints       Job ID(s) (can be used multiple times)  
  -o, --out string   specify the directory to save downloaded files (default "./")  

```

Parameter description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --job\_id | -j | jobs id | Yes |
| --out | -o | Save the logs to a local path for example: -o ./ indicates the current directory (default is ./) | No |

案例：

```
bohr job log -j 1234 -j 2345 -o /opt  
# Download the log files for Job IDs 1234 and 2345 and save them to the local /opt directory  

```
## Download：download[​](#downloaddownload "标题的直接链接")

Command Entry:

`bohr job download`

Summary:

```
Usage:  
  bohr job download [flags]  
  
Aliases:  
  download, -d  
  
Flags:  
  -h, --help              help for download  
  -j, --job_id ints       Job ID(s) (can be used multiple times)  
  -o, --out string   specify the directory to save downloaded files (default "./")  

```

Parameter description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --job\_id | -j | Downloaded job ID | Yes |
| --out | -o | Save the outs to a local path for example: -o ./ indicates the current directory (default is ./) | No |

Example：

```
bohr job download -j 1234 -j 2345 -o /opt  
# Download the out files for Job IDs 1234 and 2345 and save them to the local /opt directory  

```
## Describe：describe[​](#describedescribe "标题的直接链接")

Command Entry:

`bohr job describe`

Summary:

```
Usage:  
  bohr job describe [flags]  
  
Flags:  
      --csv           output with csv format  
  -h, --help          help for describe  
  -j, --job_id ints   Job ID(s) (can be used multiple times)  
      --json          output with json format  
  -l, --long          Long listing format  
      --noheader      does not print header information  
      --yaml          output with yaml format  

```

Parameter description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --job\_id | -j | Jobs ID | Yes |
| --long | -l | Whether to display all the task information in detail | No |

Example：

```
bohr job describe -j 1234 -j 2345 --json   
# Display the task details of Job IDs 1234 and 2345 in JSON format  
bohr job describe -j 1234 -l   
# View the task with Job ID 1234 and display all its information in detail  

```
[PreviousInstall Bohrium CLI](/en/docs/bohrctl/install/)[NextJob Group Management Command：job\_group](/en/docs/bohrctl/job_group/)

* [Query：list](#querylist)
* [Submit：submit](#submitsubmit)
* [Delete：delete](#deletedelete)
* [Terminate early：terminate](#terminate-earlyterminate)
* [Kill：kill](#killkill)
* [Download：download](#downloaddownload)
* [Describe：describe](#describedescribe)



