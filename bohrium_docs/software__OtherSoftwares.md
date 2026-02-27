# software > OtherSoftwares

**Source URL:** https://docs.bohrium.com/en/docs/software/OtherSoftwares

---








Custom Software | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/software/OtherSoftwares)
* [English](/en/docs/software/OtherSoftwares)
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
* Custom Software
# Custom Software

Bohrium has already pre-installed some commonly used software. You can view the provided container images and virtual machine images in the "[Images - Public Images](https://bohrium.dp.tech/web-images/public)". If the existing software does not include the software you need, or you have customization requirements for some software, you can create your own custom software in the "[Images - Custom Images - Create Image](https://bohrium.dp.tech/web-images/public)".

**Three ways to create custom software:**

1. Built based on Dockerfile.
2. Pull images from the public repository.
3. Create a management node, install and compile the software you need, and then save it as custom software.

## Create Custom Software Based on Dockerfile[​](#create-custom-software-based-on-dockerfile "标题的直接链接")

### Step 1: Fill in the Basic Information[​](#step-1-fill-in-the-basic-information "标题的直接链接")

* Select the project: Required, all members of this project will have access to use this image.
* Fill in the image name and Tag: Required, the image name and Tag must not be duplicated with existing images in the project.
* Description: Optional, for the convenience of others to understand the software information included in the image.

### Step 2: Enter the Dockerfile[​](#step-2-enter-the-dockerfile "标题的直接链接")

As shown below, select the build method as "Based on Dockerfile" and enter the Dockerfile used to build the image.

![基于 dockerfile](/en/assets/images/screenshot-20240409-201230-1f60e7c713bdcce8c492cdedfbe91126.png)

See [Docker Official Docs](https://docs.docker.com/engine/reference/builder/) for standard Dockerfile usage.

**Some Notes on Using Dockerfile on This Platform:**

* When downloading foreign packages via pip, use [domestic mirrors](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/) to avoid download failures. For example:
  
  ```
  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package  
  
  ```
* When downloading software via apt-get, use [domestic mirrors](https://developer.aliyun.com/mirror/ubuntu/) to avoid download failures. For example:
  
  ```
  RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list  
  RUN apt-get update  
  RUN apt-get install -y some-package  
  
  ```
* When downloading software via yum, use [domestic mirrors](https://developer.aliyun.com/mirror/centos). For example:
  
  ```
  RUN yum install -y some-package  
  
  ```
* When downloading software via conda, use [domestic mirrors](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/). For example:
  
  ```
  RUN conda install -y some-package  
  
  ```
* Copying local files into image is not supported for now. For example:
  
  ```
  COPY ./some-file /some-path   
  
  ```
* The image you pull needs to install the relevant components for **SSH Login**. Otherwise it may cause the image to fail to use on the management node. It does not affect using this image to submit jobs. The required software is as follows:
  
  + openssh-server
  + supervisor
  + net-tools
  
  If you are unsure how to install the above software, you can download the script below for one-click installation. After the installation is successful, try pulling the image again.
  
  + For Ubuntu image, [Click here](https://dp-public.oss-cn-beijing.aliyuncs.com/k8s/ubuntu_machine_init.sh) to download the corresponding script.
  + For Centos image, [Click here](https://dp-public.oss-cn-beijing.aliyuncs.com/k8s/centos_machine_init.sh) to download the corresponding script.

### Step 3: View, use, and share the created images[​](#step-3-view-use-and-share-the-created-images "标题的直接链接")

After the image is created, you can go to "[Images - Custom Images - Container Image](https://bohrium.dp.tech/web-images/private)" to view the creation progress and basic information of the image. You can view the build log in the image details to understand the progress and failure reasons of the build.

![基于 dockerfile](/en/assets/images/screenshot-20240409-201404-3cebbfb31b0730022f86b45a7bbd9a5a.png)

You can use the image for [job submission](/en/docs/bestpractice/Docker) without waiting for the image creation to be completed.

Of course, you can also share the custom images you've created with others.

![共享自定义镜像](/en/assets/images/screenshot-20240409-201500-f6f710be5d40b2bd04eb527201361815.png)

## Create Custom Software by Pulling Images from a Public Repository[​](#create-custom-software-by-pulling-images-from-a-public-repository "标题的直接链接")

Bohrium supports pull images from the DockerHub public repository and automatically converts them into custom images that can be used within Bohrium for development, debugging, and job computing.

### Step 1: Fill in the Basic Information[​](#step-1-fill-in-the-basic-information-1 "标题的直接链接")

* Select the project: Required, all members of this project will have access to use this image.
* Fill in the image name and Tag: Required, the image name and Tag must not be duplicated with existing images in the project.
* Description: Optional, for the convenience of others to understand the software information included in the image.

### Step 2: Fill in the public repository address[​](#step-2-fill-in-the-public-repository-address "标题的直接链接")

As shown below, select the build method as "Based on Public Repository Image", and fill in the public image address to be pulled, such as: nvcr.io/nvidia/pytorch:23.09-py3.

![基于 dockerfile](/en/assets/images/screenshot-20240409-201303-006c6515a449287c10cf520e7e353767.png)

**Notice:**

1. The image you pull needs to install the relevant components for **SSH Login**. Otherwise it may cause the image to fail to use on the management node. It does not affect using this image to submit jobs. The required software is as follows:

* openssh-server
* supervisor
* net-tools

If you are unsure how to install the above software, you can download the script below for one-click installation. After the installation is successful, try pulling the image again.

* For Ubuntu image, [Click here](https://dp-public.oss-cn-beijing.aliyuncs.com/k8s/ubuntu_machine_init.sh) to download the corresponding script.
* For Centos image, [Click here](https://dp-public.oss-cn-beijing.aliyuncs.com/k8s/centos_machine_init.sh) to download the corresponding script.

2. Image larger than 40GB or having an unstable public network may result in slow pulling or failure to pull.

### Step 3: View, use, and share the created images[​](#step-3-view-use-and-share-the-created-images-1 "标题的直接链接")

After the image is created, you can go to "[Images - Custom Images - Container Image](https://bohrium.dp.tech/web-images/private)" to view the creation progress and basic information of the image. You can view the build log in the image details to understand the progress and failure reasons of the build.

![基于 dockerfile](/en/assets/images/screenshot-20240409-201404-3cebbfb31b0730022f86b45a7bbd9a5a.png)

You can use the image for [job submission](/en/docs/bestpractice/Docker) without waiting for the image creation to be completed.

Of course, you can also share the custom images you've created with others.

![共享自定义镜像](/en/assets/images/screenshot-20240409-201500-f6f710be5d40b2bd04eb527201361815.png)

## Create Custom Software Based on Management Node[​](#create-custom-software-based-on-management-node "标题的直接链接")

### Step 1: Fill in the Basic Information[​](#step-1-fill-in-the-basic-information-2 "标题的直接链接")

* Select the project: Required, all members of this project will have access to use this image.
* Fill in the image name and Tag: Required, the image name and Tag must not be duplicated with existing images in the project.
* Description: Optional, for the convenience of others to understand the software information included in the image.

### Step 2：Select an existing node or start a new node[​](#step-2select-an-existing-node-or-start-a-new-node "标题的直接链接")

Select "Based on Existing Node" for image building within Bohrium "[Image Center - Custom Images - Create Image](https://bohrium.dp.tech/web-images/private/create)".

* You can choose any running node to build its environment directly into a custom image.
* You can also click on "Start a New Node" to start a new node for the installation and compilation of custom software. Once the installation is complete, go to the corresponding node card in the "Node Management" page and select "Create Image" (as shown in the red circle below) to save the software environment.

![](/en/assets/images/screenshot-20240409-201545-550cd4a49f2c7ef51fb5499019affeaa.png)

**Notice:**

Images larger than 40GB will fail to build. Please exclude paths that do not need to be built into the image before building.

![](/en/assets/images/screenshot-20240409-201324-bb597d945587d0aeb0a06c28e5363099.png)

### Step 3: View, use, and share the created images[​](#step-3-view-use-and-share-the-created-images-2 "标题的直接链接")

After the image is created, you can go to "[Images - Custom Images - Container Image](https://bohrium.dp.tech/web-images/private)" to view the creation progress and basic information of the image.

![](/en/assets/images/screenshot-20240409-201404-3cebbfb31b0730022f86b45a7bbd9a5a.png)

You can use the image for [job submission](/en/docs/bestpractice/Docker) without waiting for the image creation to be completed.

Of course, you can also share the custom images you've created with others.

![](/en/assets/images/screenshot-20240409-201500-f6f710be5d40b2bd04eb527201361815.png)

[PreviousVASP](/en/docs/software/VASP/)[NextBohrium CLI Frequently Asked Questions](/en/docs/faq/UtilityFaq/)

* [Create Custom Software Based on Dockerfile](#create-custom-software-based-on-dockerfile)
  + [Step 1: Fill in the Basic Information](#step-1-fill-in-the-basic-information)
  + [Step 2: Enter the Dockerfile](#step-2-enter-the-dockerfile)
  + [Step 3: View, use, and share the created images](#step-3-view-use-and-share-the-created-images)
* [Create Custom Software by Pulling Images from a Public Repository](#create-custom-software-by-pulling-images-from-a-public-repository)
  + [Step 1: Fill in the Basic Information](#step-1-fill-in-the-basic-information-1)
  + [Step 2: Fill in the public repository address](#step-2-fill-in-the-public-repository-address)
  + [Step 3: View, use, and share the created images](#step-3-view-use-and-share-the-created-images-1)
* [Create Custom Software Based on Management Node](#create-custom-software-based-on-management-node)
  + [Step 1: Fill in the Basic Information](#step-1-fill-in-the-basic-information-2)
  + [Step 2：Select an existing node or start a new node](#step-2select-an-existing-node-or-start-a-new-node)
  + [Step 3: View, use, and share the created images](#step-3-view-use-and-share-the-created-images-2)



