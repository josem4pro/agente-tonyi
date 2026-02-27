# bohrctl > node

**Source URL:** https://docs.bohrium.com/en/docs/bohrctl/node

---








Node Management Commands：node | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/bohrctl/node)
* [English](/en/docs/bohrctl/node)
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
* Node management
# Node Management Commands：node

## List all nodes：list[​](#list-all-nodeslist "标题的直接链接")

Command Entry:

`bohr node list`

Summary:

```
Usage:  
  bohr node list [flags]  
  
Aliases:  
  list, -ls  
  
Flags:  
      --csv        output with CSV format  
  -h, --help       Display help information for list  
      --json       output with JSON format  
      --noheader   does not print header information  
  -p, --paused     only show paused nodes  
  -d, --pending    only show pending nodes  
  -q, --quiet      only show node id and node name  
  -s, --started    only show started nodes  
  -w, --waiting    only show waiting nodes  
      --yaml       output in YAML format  

```

Example:

```
bohr node list --json -p    
# View all nodes in paused state in JSON format  
bohr node list -q   
# View all nodes' IDs and names (ctrl+c to exit)  

```

![node list](/en/assets/images/QQ20240607-183240@2x-2d9058c0b6aa5bbfa4ce10c330ee3744.png)

## Create Node: create[​](#create-node-create "标题的直接链接")

Command Entry:

`bohr node create`

Summary:

```
Usage:  
  bohr node create [flags]  
  
Flags:  
  -h, --help                  help for create  

```

Example:

```
bohr node create # Create a node   

```

![bohr node create4](/en/assets/images/imageonline-co-gifimage-e121bdf2a57528bedcbdfd879f42f49f.gif)

## Connect Node：connect[​](#connect-nodeconnect "标题的直接链接")

Command Entry:

`bohr node connect`

Summary:

```
Usage:  
  bohr node connect <node_id> [flags]  
  
Flags:  
  -h, --help          help for connect  
  -n, --node_id int   node id to connect  
  

```

Parameter description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --node\_id | -n | Node id | Yes |

Example:

```
bohr node connect  12345   
# connect nodes 12345  

```
## Stop node: stop[​](#stop-node-stop "标题的直接链接")

Command Entry:

`bohr node stop`

Summary:

```
Usage:  
  bohr node stop <node_id> [flags]  
  
Aliases:  
  stop, -s  
  
Flags:  
  -h, --help          help for stop  
  -n, --node_id int   node id  

```

Parameter description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --node\_id | -n | Node id | Yes |

Example:

```
bohr node stop 12345   
# Stop node with ID 12345  

```
## Delete note：delete[​](#delete-notedelete "标题的直接链接")

Command Entry:

`bohr node delete`

Summary:

```
Usage:  
  bohr node delete <node_id> [flags]  
  
Aliases:  
  delete, -d  
  
Flags:  
  -h, --help          help for delete  
  -n, --node_id int   node id  

```

Parameter description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --node\_id | -n | Node id | Yes |

Example:

```
bohr node delete  12345   
# delete nodes 12345  

```
[PreviousJob Group Management Command：job\_group](/en/docs/bohrctl/job_group/)[NextMachine Configuration Command: machine](/en/docs/bohrctl/machine/)

* [List all nodes：list](#list-all-nodeslist)
* [Create Node: create](#create-node-create)
* [Connect Node：connect](#connect-nodeconnect)
* [Stop node: stop](#stop-node-stop)
* [Delete note：delete](#delete-notedelete)



