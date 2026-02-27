# bohrctl > job group

**Source URL:** https://docs.bohrium.com/en/docs/bohrctl/job_group

---








Job Group Management Command：job\_group | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/bohrctl/job_group)
* [English](/en/docs/bohrctl/job_group)
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
* Job group management
# Job Group Management Command：job\_group

## List all Job Group：list[​](#list-all-job-grouplist "标题的直接链接")

Command Entry:

`bohr job_group list`

Summary:

```
Usage:  
  bohr job_group list [flags]  
  
Aliases:  
  list, -ls  
  
Flags:  
  -a, --asce            list by ascending, default descending  
      --csv             output with CSV format  
  -e, --end string      end date. format is yyyy-mm-dd (must be used together with --start)  
  -h, --help            help for list  
  -j, --job_group int   Specify Job group ID to filter results  
      --json            output with JSON format  
      --noheader        does not print header information  
  -n, --number int      number of results to be displayed (default 50)  
  -p, --projectId int   project Id of Bohrium  
  -q, --quiet           only show job group id  
  -o, --sortby string   sort by id/createTime(default "id")  
  -s, --start string    start date. format is yyyy-mm-dd (must be used together with --end)  
      --yaml            output in YAML format  

```

Parameter Description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --asce | -a | Sort in reverse order | No |
| --end | -e | End date, format is yyyy-mm-dd (must be used together with --start) | No |
| --job\_group | -j | Search by job\_group | No |
| --number | -n | Number of job groups to display, default is 50 | No |
| --projectId | -p | Search by project ID | No |
| --quiet | -q | Only show job group ID | No |
| --sortby | -o | Sort by createTime/id, default is id | No |
| --start | -s | Start date, format is yyyy-mm-dd (must be used together with --end) | No |

Example:

```
bohr job_group list -n 10 --yaml  
# Display the first 10 job groups in YAML format  
bohr job_group list -s 2024-03-05 -e 2024-07-08   
# Display job groups from March 5, 2024, to July 8  

```
## Terminate：terminate[​](#terminateterminate "标题的直接链接")

Command Entry:

`bohr job_group terminate`

Summary:

```
Usage:  
  bohr job_group terminate <job_group_id>... [flags]  
  
Flags:  
  -h, --help                help for terminate  
      --job_group_id ints   Job group ID(s) to terminate (can be used multiple times)  

```

Parameter Description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --job\_group\_id | - | Job Group ID to terminate | yes |

Example:

```
bohr job_group terminate  123 456  
# Terminate the job groups with IDs 123 and 456  

```
## Delete：delete[​](#deletedelete "标题的直接链接")

Command Entry:

`bohr job_group delete`

Summary:

```
Usage:  
  bohr job_group delete <job_group_id>... [flags]  
  
Flags:  
  -h, --help                help for delete  
      --job_group_id ints   Job group ID(s) (can be used multiple times)  

```

Parameter Description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --job\_group\_id | - | Job group id to be deleted | Yes |

Example:

```
bohr job_group delete 123 345  
#Delete job groups with ID 123 and 345  

```
## Download：download[​](#downloaddownload "标题的直接链接")

Command Entry:

`bohr job_group download`

Summary:

```
Usage:  
  bohr job_group download [flags]  
  
Aliases:  
  download, -d  
  
Flags:  
  -h, --help               help for download  
  -j, --job_group_id int   job group id  
  -n, --number int         number of results to be displayed (default 50)  
  -o, --out_path string    specify the directory to save downloaded files (default "./")  

```

Parameter description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --job\_group\_id | -i | Job group ID to download | Yes |
| --number | -n | Number of jobs to download (default is 50) | No |
| --out\_path | -o | Save results to a specified local path, e.g., -o ./ means current directory (default is ./) | No |

Example:

```
bohr job_group download 123 654   
# Download files of job groups with IDs 123 and 654  

```
## Create：create[​](#createcreate "标题的直接链接")

Command Entry:

`bohr job_group create`

Summary:

```
Usage:  
  bohr job_group create [flags]  
  
Flags:  
  -h, --help              help for create  
  -n, --job_name string   job name  
  -p, --project_id int    project id  

```

Parameter Description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --job\_name | -n | the name of job group | Yes |
| --project\_id | -p | the project id of job group | Yes |

Example:

```
bohr job_group create  -n test -p 123   
# Create a job group named test under Project ID 123  

```
Attention

The `job_group_id` created here is different from the `JOB GROUP ID` obtained after creating a job. The task group ID generated through `bohr job_group create` is used to submit multiple tasks to the same task group. It is only applicable when submitting tasks via the Bohrium CLI and is set in the `job_group_id` field in the JSON configuration file.
。

```
{  
    "job_group_id":0000   
}  

```
[PreviousJob Management Commands：job](/en/docs/bohrctl/job/)[NextNode Management Commands：node](/en/docs/bohrctl/node/)

* [List all Job Group：list](#list-all-job-grouplist)
* [Terminate：terminate](#terminateterminate)
* [Delete：delete](#deletedelete)
* [Download：download](#downloaddownload)
* [Create：create](#createcreate)



