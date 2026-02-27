# bohrctl > project

**Source URL:** https://docs.bohrium.com/en/docs/bohrctl/project

---








Project Management Command：project | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/bohrctl/project)
* [English](/en/docs/bohrctl/project)
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
* Project management
# Project Management Command：project

## List all projects：list[​](#list-all-projectslist "标题的直接链接")

Command Entry:

`bohr project list`

Summary:

```
Usage:  
  bohr project list [flags]  
  
Aliases:  
  list, -ls  
  
Flags:  
      --csv    Output in CSV format  
  -h, --help   help for list  
      --json   Output in JSON format  
      --yaml   Output in YAML format  

```

Example:

```
bohr project list --csv   
# View all projects in CSV format  
bohr project list   
# View all projects （Press Ctrl+C to exit）.  

```

![bohr project list](/en/assets/images/QQ20240607-184521@2x-67b911c9111b18dcac208ea44ea683df.png)

## Delete project：delete[​](#delete-projectdelete "标题的直接链接")

Command Entry:

`bohr project delete`

Summary:

```
Usage:  
  bohr project delete <project_id> [flags]  
  
Aliases:  
  delete, -d  
  
Flags:  
  -h, --help             help for delete  
  -p, --project_id int   project id  

```

Parameter description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --project\_id | -p | Project ID | Yes |

Example:

```
bohr project delete 123   
# Delete the project with ID 123  

```
## Create project：create[​](#create-projectcreate "标题的直接链接")

Command Entry:

`bohr project create`

Summary:

```
Usage:  
  bohr project create [flags]  
  
Flags:  
  -h, --help                   help for create  
  -m, --month_cost_limit int   month cost limit, [optional]  
  -n, --name string            project name (default "default")  
  -t, --total_cost_limit int   total cost limit, [optional]  

```

Parameter description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --month\_cost\_limit | -m | Monthly cost limit | No |
| --name | -n | Project name (default is 'default') | Yes |
| --total\_cost\_limit | -t | Total cost limit | No |

Example:

```
bohr project create -n "bohrctl-test" # Create a project named bohrctl-test  

```
[PreviousImage Management Command：image](/en/docs/bohrctl/image/)[NextInstall Lebesgue Utility](/en/docs/commandline/about/)

* [List all projects：list](#list-all-projectslist)
* [Delete project：delete](#delete-projectdelete)
* [Create project：create](#create-projectcreate)



