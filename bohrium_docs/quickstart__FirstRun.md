# quickstart > FirstRun

**Source URL:** https://docs.bohrium.com/en/docs/quickstart/FirstRun

---








Run your first job | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/quickstart/FirstRun)
* [English](/en/docs/quickstart/FirstRun)
[Console](https://bohrium.dp.tech/home)

* [Homepage](/en/docs/)
* [Quick Start](#)
  + [Run your first job](/en/docs/quickstart/FirstRun)
  + [Monitor jobs](/en/docs/quickstart/Status)
  + [Terminate Jobs](/en/docs/quickstart/KillJob)
  + [Get job results](/en/docs/quickstart/Result)
* [Command Line（New）](#)
* [Command Line](#)
* [Best Practice](#)
* [User Guide](#)
* [Softwares](#)
* [FAQ](#)
* [More Help](/en/docs/MoreHelp)
* [Extensions](#)


* Quick Start
* Run your first job
# Run your first job

In this tutorial, we will use the DeePMD-kit software as an example to introduce how to run a job on the Bohrium platform.

## 1. Registration[​](#1-registration "标题的直接链接")

[Click here](https://bohrium.dp.tech/home) to go to the Bohrium homepage. In the top right corner of the page, click the "Log in/Register" button to register a Bohrium account using your mobile number. If you already have an account for other DP products, you can skip this step and log in directly.

![login](/en/assets/images/login-f0c3f1a45dd830fd9151f046001f0e37.png)

## 2. Top-up and create a project[​](#2-top-up-and-create-a-project "标题的直接链接")

Bohrium supports online top-up. You can click on the "User Center" on the top right avatar to recharge by yourself.

![充值入口](/en/assets/images/rechargeentrance-8ac2d3130aefa3f7d8ab30a03ad5afdf.png)

After completing the top-up, click on the navigation bar - "[Projects](https://bohrium.dp.tech/projects)" (red box 1 in the image), and then click "New Project" in the upper right corner of the page (red box 2 in the image).

Give the project a name that is easy for you to recognize and click "OK". If the project has other collaborators, you can click on "Members" (red box 3 in the image) to add project members.

![添加成员](/en/assets/images/project-c6ce3a85ec059e5df19919700c794767.png)

The creator of the project can allocate budgets, add or remove members, view the bills of each member, etc. Project members can directly spend the creator's balance when submitting jobs, and members can also share images to each other. For more information on project collaboration, please refer to [Project Collaboration](/en/docs/userguide/coorperation).

If your funds come from other people's accounts, such as your tutor or a company, you can ask the provider of the funds to create a project and add you as a project member.

## 3. Create the management node (optional)[​](#3-create-the-management-node-optional "标题的直接链接")

The management node is used for data preparation, compilation debugging, result processing, and other scenarios.

Bohrium provides a [visual file management capability](/en/docs/userguide/FileManage) in the management node, with online previews of structure files, trajectories, scripts, and images.

In this tutorial, the management node is used for preparing DeePMD-kit input files and job submission. You can also choose to perform related operations on your local machine or other machines.

1. On the [Nodes](https://bohrium.dp.tech/nodes) page, click "Create Container" in the upper right corner. In this tutorial, choose the image `ubuntu:20.04-py3.10`, and select the corresponding project for the "Project" field. There is no need to modify the machine, disk, and automatic stop options, keep the default values.
2. It usually takes about 10 second to start. When the node status changes from "Preparing" to "Running", you can connect it.
3. Bohrium provides a web-based SSH tool called [Web Shell](/en/docs/userguide/WebShell) and also supports logging into the management node through your local terminal. In this tutorial, we will demonstrate using the Web Shell. Click the button indicated by the red box 2 in the image and select Web Shell:

![FirstRunwebshell](/en/assets/images/FirstRunwebshell-16e76718807249c9c0c17fc017e3a76e.png)

If you choose to submit the job on your local machine, you can skip this step and proceed with the following operations.

## 4. Run DeePMD-kit job[​](#4-run-deepmd-kit-job "标题的直接链接")

In this tutorial, we will demonstrate using [DeePMD-kit](/en/docs/software/DeePMD-kit) to train a deep potential model of water. The job will take approximately 10 minutes to run.

### 1. Prepare the input files[​](#1-prepare-the-input-files "标题的直接链接")

Open the [Bohrium Workspace](https://bohrium.dp.tech/workspace) page and use the `cd /personal` command to enter the personal data disk. You can transfer data to the data disk by dragging and uploading files.

In this tutorial, we will use `wget` to download the DeePMD-kit input files. The input files are stored in the `Bohrium_DeePMD-kit_example` folder. You can execute the following two commands to download and unzip them:

```
wget https://bohrium-example.oss-cn-zhangjiakou.aliyuncs.com/Bohrium_DeePMD-kit_example.zip  

```
```
unzip Bohrium_DeePMD-kit_example.zip  

```

Refresh and expand the directory tree on the left side, as shown in the following image, which indicates that the data has been successfully prepared.

![输入图片说明](/en/assets/images/dpmdfiles-8ef1d63b87b80ef278d5153ca7a9734f.png)

### 2. Configure Bohrium CLI[​](#2-configure-bohrium-cli "标题的直接链接")

We will use `bohr` to submit jobs. If you are using the Bohrium management node to submit jobs, the selected image `ubuntu:20.04-py3.10` already has Bohrium CLI pre-installed. If you are using your local machine to submit jobs, you can install it with the following command:

#### linux Version[​](#linux-version "标题的直接链接")

Use **curl** to download:

```
/bin/bash -c "$(curl -fsSL https://dp-public.oss-cn-beijing.aliyuncs.com/bohrctl/1.0.0/install_bohr_linux_curl.sh)"  

```
#### macOS Version[​](#macos-version "标题的直接链接")

Use **curl** to download:

```
/bin/bash -c "$(curl -fsSL https://dp-public.oss-cn-beijing.aliyuncs.com/bohrctl/1.0.0/install_bohr_mac_curl.sh)"  

```
#### Windows Version[​](#windows-version "标题的直接链接")

Use **curl** to download:

```
curl -o install_bohr_windows_wget.bat https://dp-public.oss-cn-beijing.aliyuncs.com/bohrctl/1.0.0/install_bohr_windows_curl.bat && install_bohr_windows_wget.bat  

```

When using the Bohrium CLI for the first time, you need to bind an AccessKey. Please ensure that the bound AccessKey is correct.

Please visit [Bohrium-AccessKey](https://bohrium.dp.tech/settings/user/) to generate an AccessKey （**Recreating the AccessKey will cause the original one to become invalid.**）

![ACCESS_KEY值](/en/assets/images/20240605-112347-5909c8064c9851ad1616d71fd74f43a1.png)

After obtaining the ACCESS\_KEY value, configure the environment variables for ACCESS\_KEY as follows:

> Note: Please replace the `XXXX` after `ACCESS_KEY` with your own AccessKey.

**ZSH**

If you are using ZSH, use the following command to write the `ACCESS_KEY` into `~/.zshrc`.

```
echo 'export ACCESS_KEY=XXXX' >> ~/.zshrc  
source ~/.zshrc  

```

**BASH**

If you are using ZSH, use the following command to write the `ACCESS_KEY` into `~/.bashrc`.

```
echo 'export ACCESS_KEY=XXXX' >> ~/.bashrc  
source ~/.bashrc  

```

**Windows**

Open Command Prompt (CMD) and run the following commands (note that the setx command requires reopening the Command Prompt to take effect):

```
setx ACCESS_KEY XXXX  

```

Alternatively, you can manually add these variables through the system settings.

### 3. Prepare the configuration file[​](#3-prepare-the-configuration-file "标题的直接链接")

The configuration file `job.json` has already been preloaded in the input folder, we only need to modify some of the parameters in it. Run the following command to enter the input folder:

```
cd Bohrium_DeePMD-kit_example  

```

In the Web Shell, you can double-click the `job.json` file in the left-side file tree to edit and save it online, or you can edit it in the command-line window:

```
vi job.json  

```

Enter `i` to enter edit mode, after completing the modifications, press `esc` to exit edit mode and then enter `:` to enter the command mode. Next, enter `wq` to save and exit. The content of the configuration file is as follows:

**Notice**：All `0000` after `"project_id"` need to be replaced with your own project ID, which can be viewed on the "[Projects](https://bohrium.dp.tech/projects)" page. Also, the JSON file format requires that no commas be added after the last field within the `{}`, otherwise, there will be a syntax error.

```
{  
  "job_name": "DeePMD-kit test",  
  "command": " cd se_e2_a && dp train input.json > tmp_log 2>&1 && dp freeze -o graph.pb",  
  "log_file": "se_e2_a/tmp_log",  
  "backward_files": ["se_e2_a/lcurve.out", "se_e2_a/graph.pb"],  
  "project_id": 0000,  
  "platform": "ali",  
  "machine_type": "c4_m15_1 * NVIDIA T4",  
  "job_type": "container",  
  "image_address": "registry.dp.tech/dptech/deepmd-kit:2.1.5-cuda11.6"  
}  

```

`job.json` field description

| Field Name | Description | Example |
| --- | --- | --- |
| job\_name | The name of your computing job, which can be named freely. | DeePMD-kit test |
| command | The command to be executed on the computing node. Enter the folder where the script for this tutorial is located, execute the `dp train` command, and print the screen output to the `tmp_log` file, execute the `dp freeze` command, and save the result to the `graph.pb` file. | cd se\_e2\_a && dp train input.json > tmp\_log 2>&1 && dp freeze -o graph.pb |
| log\_file | The log file that can be viewed at any time during the calculation process, which can be viewed on the Bohrium "[Jobs](https://bohrium.dp.tech/jobs)" page. | se\_e2\_a/tmp\_log |
| backward\_files | The result files that need to be downloaded after the calculation is finished. If the field is empty, all files in the working directory of the computing node will be retained. | se\_e2\_a/lcurve.out,se\_e2\_a/graph.pb |
| project\_id | The project ID to which the job belongs. It can be viewed on the "[Projects](https://bohrium.dp.tech/projects)" page. | 0000 |
| machine\_type | The machine type used for this job, which can be viewed on the "[Pricing](https://bohrium.dp.tech/profiler)" page. In this tutorial, we use a 4 core 15G memory NVIDIA T4 GPU machine to accelerate the training process of DeePMD-kit. If you need faster speed, you can choose the A100 or V100 machine. | c4\_m15\_1 \* NVIDIA T4 |
| image\_address | The image address for the computing node, which can be viewed on the "[Images](https://bohrium.dp.tech/web-images)" page. The software used in this tutorial is DeePMD-kit version 2.1.5. | registry.dp.tech/dptech/deepmd-kit:2.1.5-cuda11.6 |

At this point, we have completed the preparation of all the necessary documents for the case.

### 4. Submit job[​](#4-submit-job "标题的直接链接")

Using Bohrium CLI to submit the job:

```
bohr job submit -i job.json -p ./  

```

Where:

* `-i` specifies the configuration file for the job, which is `job.json` in this tutorial.
* `-p` specifies the directory where the input files are located. Bohrium will package and upload the specified directory, and after decompressing it on the computing node, it will switch the working directory to that directory. In this tutorial, it is `./`.

As shown below, the job is submitted successfully:

![提交任务](/en/assets/images/screenshot-20220908-015826-acd1838b551c64b8c1efc9f9d539abee.png)

### 5. Check job status[​](#5-check-job-status "标题的直接链接")

After successfully submitting the job, you can view the progress and related logs of the submitted jobs on the "[Jobs](https://bohrium.dp.tech/jobs)" page.

![查看任务状态](/en/assets/images/checkjobstatus221104-99c08d34a7c1715c3511cd15bdbe39c4.png)

### 6. Download Results[​](#6-download-results "标题的直接链接")

After the job calculation is completed, you can download the results on the "[Jobs](https://bohrium.dp.tech/jobs)" page, or save them to the data disk.

![下载结果](/en/assets/images/downloadresult221104-bb4cac8f6e8e337d4b1b10ec5f69ca8a.png)

You can also download it using the commands of Bohrium CLI

```
bohr job download -j <JOB ID>  

```

or

```
bohr job_group download -j <JOB GROUP ID>  

```

So far, we have completed the running of a DeePMD-kit training job on Bohrium.

Finally, don't forget to stop or delete the node after finishing your work on the "[Nodes](https://bohrium.dp.tech/nodes)" page to avoid wasting resources.

![关机节点](/en/assets/images/pausenode221104-e70f545ce1e6e8e60ee42ef7414d987e.png)

[PreviousBohrium®️ Space Station](/en/docs//)[NextMonitor jobs](/en/docs/quickstart/Status/)

* [1. Registration](#1-registration)
* [2. Top-up and create a project](#2-top-up-and-create-a-project)
* [3. Create the management node (optional)](#3-create-the-management-node-optional)
* [4. Run DeePMD-kit job](#4-run-deepmd-kit-job)
  + [1. Prepare the input files](#1-prepare-the-input-files)
  + [2. Configure Bohrium CLI](#2-configure-bohrium-cli)
  + [3. Prepare the configuration file](#3-prepare-the-configuration-file)
  + [4. Submit job](#4-submit-job)
  + [5. Check job status](#5-check-job-status)
  + [6. Download Results](#6-download-results)



