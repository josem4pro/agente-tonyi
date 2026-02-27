# bestpractice > Docker

**Source URL:** https://docs.bohrium.com/en/docs/bestpractice/Docker

---








Running Container Jobs | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/bestpractice/Docker)
* [English](/en/docs/bestpractice/Docker)
[Console](https://bohrium.dp.tech/home)

* [Homepage](/en/docs/)
* [Quick Start](#)
* [Command Line（New）](#)
* [Command Line](#)
* [Best Practice](#)
  + [Run a container job](/en/docs/bestpractice/Docker)
  + [Use DP-Dispatcher](/en/docs/bestpractice/DP-Dispatcher)
* [User Guide](#)
* [Softwares](#)
* [FAQ](#)
* [More Help](/en/docs/MoreHelp)
* [Extensions](#)


* Best Practice
* Run a container job
# Running Container Jobs

## What is a Container[​](#what-is-a-container "标题的直接链接")

A container is a lightweight virtualization technology used to encapsulate and isolate the runtime environment of an application or service. Compared to traditional virtualization technologies, containers eliminate the need for operating system virtualization and directly encapsulate the environment and dependencies required by the application or service on the host operating system. As a result, containers are very lightweight, allowing a new container instance to be started in seconds, while traditional virtualization technologies take minutes. At the same time, containers have higher resource utilization because they avoid the additional resource consumption brought by operating system virtualization.

Running computing jobs using container technology can solve environmental dependency problems on the one hand, and a container image that can run in a development environment can be safely submitted to any resource for production; on the other hand, isolation and standardization ensure the repeatability of computing to a large extent.

## When to Use Containers[​](#when-to-use-containers "标题的直接链接")

The most popular container technology in the industry today is Docker. Docker not only has a rich public image repository (Docker Hub) but also provides a complete set of interfaces. Therefore, we can not only build our own image repository to ensure the security and isolation of user images but also easily convert Docker images into other container image formats such as Singularity and Podman. The advantages of containers are reflected in many aspects:

* If you need to update your code frequently, using Docker images can save you the trouble of repeatedly creating Bohrium virtual machine images, with incremental pulling and extremely fast speeds;
* If you need to manage multiple versions of your code, Docker images can help you achieve this easily, and you no longer have to worry about not having enough images;
* If you need to replicate the environment on Bohrium for testing elsewhere, we strongly recommend Docker images, which break the strong environmental dependency of traditional cloud providers and supercomputers, allowing users to compile once and run anywhere;
* If you need to share an image with a friend without letting them damage the original environment, give Docker a try;
* ...

As you can see, container technology helps us solve the problems of environment migration, sharing, and deployment. It is very lightweight and does an excellent job of resource isolation at the system level, meeting our usage scenarios in multiple aspects and all-around.

## How to Run Container Jobs on Bohrium[​](#how-to-run-container-jobs-on-bohrium "标题的直接链接")

Bohrium currently supports Docker containers and provides Docker images. You can visit Bohrium's [Image Center-Container Image](https://bohrium.dp.tech/web-images?tab=public&publicTab=container&privateTab=vm) to view the public container images we provide.

Here we take DeePMD-kit as an example to introduce how to submit container jobs on Bohrium:

### Step 1: Prepare Input Data[​](#step-1-prepare-input-data "标题的直接链接")

The input files of DeePMD-kit are all stored in the `Bohrium_DeePMD-kit_example` folder. After entering the data disk with the `cd /personal` command, execute the following commands in sequence to download and unzip the input files:

```
wget https://bohrium-example.oss-cn-zhangjiakou.aliyuncs.com/Bohrium_DeePMD-kit_example.zip  

```
```
unzip Bohrium_DeePMD-kit_example.zip  

```
```
cd Bohrium_DeePMD-kit_example  

```
### Step 2, Prepare job.json[​](#step-2-prepare-jobjson "标题的直接链接")

To use the container image and submit the container job, you only need to modify two places in the original job configuration file job.json:

`job_type` field: Must be set to `"container"` ;

`image_address` field: Fill in the Bohrium [public container image address](https://bohrium.dp.tech/web-images?tab=public&publicTab=container&privateTab=vm) you need to use, that is, the "image address" at the number 3 in the figure below. You can also quickly query the image address in the "[Container Image and Virtual Machine Image Mapping Table](/en/docs/bestpractice/Docker#%E5%AE%B9%E5%99%A8%E9%95%9C%E5%83%8F%E4%B8%8E%E8%99%9A%E6%8B%9F%E6%9C%BA%E9%95%9C%E5%83%8F%E6%98%A0%E5%B0%84%E5%85%B3%E7%B3%BB%E8%A1%A8)" at the end of this article.

**Note**:

1. This field also supports filling in public image addresses in Docker Hub, without the need to fill in the domain name, for example: `"tensorflow/tensorflow-gpu:latest"`.
2. If you need to submit container jobs in parallel, you currently do not support using images other than public container images. If you have any requirements, you can send an email to bohrium. The job.json is as follows:

![Container Image Repository](/en/assets/images/image221116-f475ec2320516f16c1eee54f9e7751cb.png)
![Container Image Repository](/en/assets/images/image221117-c2ed50cfdcc4e2f798316039cac891e5.png)
The modified job.json is as follows:

> Note: Replace the `0000` after `project_id` with your own project ID

```
{  
    "job_name": "DeePMD-kit test",  
    "command": " cd se_e2_a && dp train input.json > tmp_log 2>&1 && dp freeze -o graph.pb",  
    "log_file": "se_e2_a/tmp_log",  
    "backward_files": ["se_e2_a/lcurve.out","se_e2_a/graph.pb"],  
    "project_id": 0000,  
    "platform": "ali",  
    "machine_type": "c4_m15_1 * NVIDIA T4",  
    "job_type": "container",  
    "image_address": "registry.dp.tech/dptech/deepmd-kit:2.1.5-cuda11.6"  
}  

```
### Step 3, Submit container jobs using Lebesgue Utility[​](#step-3-submit-container-jobs-using-lebesgue-utility "标题的直接链接")

After preparing the job.json, you can use [Bohrium CLI](/en/docs/bohrctl/install)to submit DeePMD-kit jobs:

```
bohr job submit -i job.json -p ./  

```
## Container Image and Virtual Machine Image Mapping Table[​](#container-image-and-virtual-machine-image-mapping-table "标题的直接链接")

If you are currently using the virtual machine images provided by Bohrium to submit jobs, you can query their corresponding container image addresses in the table below and replace the `image_name` field in job.json:

| Pre-installed Software | Virtual Machine Image | Container Image Address |
| --- | --- | --- |
| DeePMD-kit | LBG\_DeePMD-kit\_2.1.4\_v1 and previous DeePMD-kit versions | registry.dp.tech/dptech/deepmd-kit:2.1.5-cuda11.6 |
| DPGEN | LBG\_DP-GEN\_0.10.6\_v3 and previous DP-GEN versions | registry.dp.tech/dptech/dpgen:0.10.6 |
| LAMMPS | LBG\_LAMMPS\_stable\_23Jun2022\_v1 | registry.dp.tech/dptech/lammps:29Sep2021 |
| GROMACS | gromacs-dp:2020.2 | registry.dp.tech/dptech/gromacs:2022.2 |
| Quantum-Espresso | LBG\_Quantum-Espresso\_7.1 | registry.dp.tech/dptech/quantum-espresso:7.1 |
| VASP | -- | Requires VASP authorization, please send your VASP authorization certificate to borirum email |
| Common basic software | LBG\_Common\_v1LBG\_Common\_v2LBG\_base\_image\_ubun20.04LBG\_base\_image\_ubun22.04 | registry.dp.tech/dptech/ubuntu:20.04-py3.10-cuda11.6 |
| intel oneapi | LBG\_oneapi\_2021\_v1 | registry.dp.tech/dptech/ubuntu:20.04-py3.10-intel2022-cuda11.6 |

[PreviousProject Management Command: project](/en/docs/commandline/project/)[NextSubmit Jobs to Bohrium with dpdispatcher](/en/docs/bestpractice/DP-Dispatcher/)

* [What is a Container](#what-is-a-container)
* [When to Use Containers](#when-to-use-containers)
* [How to Run Container Jobs on Bohrium](#how-to-run-container-jobs-on-bohrium)
  + [Step 1: Prepare Input Data](#step-1-prepare-input-data)
  + [Step 2, Prepare job.json](#step-2-prepare-jobjson)
  + [Step 3, Submit container jobs using Lebesgue Utility](#step-3-submit-container-jobs-using-lebesgue-utility)
* [Container Image and Virtual Machine Image Mapping Table](#container-image-and-virtual-machine-image-mapping-table)



