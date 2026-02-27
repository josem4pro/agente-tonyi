# userguide > image

**Source URL:** https://docs.bohrium.com/en/docs/userguide/image

---








Images | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/userguide/image)
* [English](/en/docs/userguide/image)
[Console](https://bohrium.dp.tech/home)

* [Homepage](/en/docs/)
* [Quick Start](#)
* [Command Line（New）](#)
* [Command Line](#)
* [Best Practice](#)
* [User Guide](#)
  + [Submit Jobs](/en/docs/userguide/submitjob)
  + [Web Shell](/en/docs/userguide/WebShell)
  + [File Management](/en/docs/userguide/FileManage)
  + [Dataset](/en/docs/userguide/Dataset)
  + [Notebook](/en/docs/userguide/Notebook)
  + [Images](/en/docs/userguide/image)
  + [Billing](/en/docs/userguide/Billing)
  + [Quota Limit](/en/docs/userguide/QuataLlimit)
  + [Collaboration](/en/docs/userguide/coorperation)
* [Softwares](#)
* [FAQ](#)
* [More Help](/en/docs/MoreHelp)
* [Extensions](#)


* User Guide
* Images
# Images

This article introduces the use of Bohrium images and the software content included in the official images.

## What is image？[​](#what-is-image "标题的直接链接")

Image is a file storage format that contains the basic environment and other information required for running an application. Bohrium has created images suitable for different development scenarios and computing jobs according to user needs.

## How to use image?[​](#how-to-use-image "标题的直接链接")

### Submit computing job[​](#submit-computing-job "标题的直接链接")

When you [submitting a job](/en/docs/bestpractice/Docker) with Bohrium CLI , please enter the container image address corresponding to the software you need to use in the `image_address` field of the `job.json`. The image address can be viewed in the [Images](https://bohrium.dp.tech/web-images).

If the software we provide does not meet your requirements, you can refer to [how to create a custom image](/en/docs/software/OtherSoftwares) for custom software installation or contact WeChat Work at 17710231129 for assistance..

![镜像地址](/en/assets/images/20240409-155114-114018c653a114931e95a6c647b5357d.png)

**Notice:** Starting from January 1, 2023, Bohrium will no longer support submitting virtual machine jobs using virtual machine images. To ensure that your job can be successfully submitted, please use the container image when submitting the job and configure the `job_type` field in `job.json` as `container`.

### Software development/debugging[​](#software-developmentdebugging "标题的直接链接")

Bohrium supports starting container nodes. Compared to traditional virtualization technology, containers eliminate the need for operating system virtualization and directly encapsulate the environment and dependencies required for applications or services on the host operating system. It only takes a few seconds to start a new container instance, while traditional virtualization technologies require several minutes.

We recommend that you start a container node for software development, debugging, etc. You can select the corresponding container image when [starting the container management node](/en/docs/quickstart/FirstRun), as shown in Figure 2 below. You can view the official container images and virtual machine images provided in the [Images](https://bohrium.dp.tech/web-images).

![图片](/en/assets/images/20240409-155009-40c3dcec28b5c44956061a9bc3eb4bd7.png)

* If you want a blank machine with a pre-installed basic environment, we recommend that you use the following container images based on your requirements for resource types and whether to run MPI or not:

| Resource type | Image Address |
| --- | --- |
| CPU | registry.dp.tech/dptech/ubuntu:20.04-py3.10registry.dp.tech/dptech/ubuntu:20.04-py3.10-intel2022 |
| GPU | registry.dp.tech/dptech/ubuntu:20.04-py3.10-cuda11.6registry.dp.tech/dptech/ubuntu:20.04-py3.10-intel2022-cuda11.6 |

* If you want to customize existing scientific computing software on Bohrium or run DPGEN jobs, you can start the management node using the corresponding container image.
* Since the container node itself is already a docker environment, it does not support creating another docker environment on top of it. If you have requirements for docker development, such as needing to build your own docker images. Please use the virtual machine image `LBG_Common_v2` to start a virtual machine management node for development.

## Images provided by Bohrium[​](#images-provided-by-bohrium "标题的直接链接")

### Images for submitting jobs[​](#images-for-submitting-jobs "标题的直接链接")

The following is a list of some of the pre-installed scientific computing software on Bohrium. For more software, please visit the [Images](https://bohrium.dp.tech/web-images):

* DeePMD-kit
* DPGEN
* VASP: To obtain VASP authorization, please send your VASP authorization certificate via WeChat Work at 17710231129.
* LAMMPS
* GROMACS
* Quantum-Espresso
* ...

### Images for software development[​](#images-for-software-development "标题的直接链接")

For more flexible job such as software development, compilation, debugging. You can use the basic public container image when starting the management node, which already includes commonly used development software:

| Resource type | Image Address |
| --- | --- |
| CPU | registry.dp.tech/dptech/ubuntu:20.04-py3.10registry.dp.tech/dptech/ubuntu:20.04-py3.10-intel2022 |
| GPU | registry.dp.tech/dptech/ubuntu:20.04-py3.10-cuda11.6registry.dp.tech/dptech/ubuntu:20.04-py3.10-intel2022-cuda11.6 |

**All images provided by Bohrium come with the following pre-installed software:**

| Software categories | Pre-installed software |
| --- | --- |
| Python-related | python3.10pip AnacondaJupyter Lab：Powerful Notebook tool |
| File management | wget, curl: file download toolunzip: file decompression toolemacs, vim: file editing toolrsync: file synchronization tooltree: directory structure viewing toolgit: version control tool |
| Compilation tool | cmakebuild-essential: gnu compilation tool |
| System monitoring | htop: monitoring toolncdu: used for viewing directory sizenet-tools: network tools |
| DP series | Lebesgue Utility: Bohrium-developed command-line interactive tool for resource management, job management, project monitoring, and other functionsDp-Dispatcher: Declare high-performance computing jobs, computing environments, and computing resources, automatically completing the entire process of job generation, submission, polling, and recyclingDpdata: scientific computing format conversion tool |

Some images come with specific pre-installed software, such as Intel-oneapi, Pytorch, TensorFlow, etc. It is reflected in the image address, you can choose based on your actual needs. For example, `registry.dp.tech/dptech/ubuntu:20.04-py3.10-intel2022` comes with Intel-oneapi pre-installed.

## How to create a custom image[​](#how-to-create-a-custom-image "标题的直接链接")

If the software we provide does not meet your requirements, you can refer to [how to create a custom image](/en/docs/software/OtherSoftwares) for custom software installation or contact WeChat Work at 17710231129 for assistance.

## How to Pull an Image to Local Docker[​](#how-to-pull-an-image-to-local-docker "标题的直接链接")

Currently, you can use the Docker CLI to pull Bohrium's public images and your own custom images (shared images from others are not supported).

### Access Address[​](#access-address "标题的直接链接")

registry.bohrium.dp.tech (Please manually replace the copied registry.dp.tech domain from the Bohrium image menu, as it is not supported!)

### Usage[​](#usage "标题的直接链接")

1. Docker login: Use your Bohrium account username and password to log in

```
docker login registry.bohrium.dp.tech  
Username: xxx@dp.tech  
Password:  
Login Succeeded  

```

2. Docker pull: Pull the Bohrium public image

```
docker pull registry.bohrium.dp.tech/dptech/ubuntu:22.04-py3.10-intel2022  

```

![image pull](/en/assets/images/dockerpull-e70cef82c677b3cc470b38f2750beea0.png)

3. Push operations are not currently supported
[PreviousNotebook](/en/docs/userguide/Notebook/)[NextTop-up and Billing](/en/docs/userguide/Billing/)

* [What is image？](#what-is-image)
* [How to use image?](#how-to-use-image)
  + [Submit computing job](#submit-computing-job)
  + [Software development/debugging](#software-developmentdebugging)
* [Images provided by Bohrium](#images-provided-by-bohrium)
  + [Images for submitting jobs](#images-for-submitting-jobs)
  + [Images for software development](#images-for-software-development)
* [How to create a custom image](#how-to-create-a-custom-image)
* [How to Pull an Image to Local Docker](#how-to-pull-an-image-to-local-docker)
  + [Access Address](#access-address)
  + [Usage](#usage)



