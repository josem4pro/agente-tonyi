# userguide > submitjob

**Source URL:** https://docs.bohrium.com/en/docs/userguide/submitjob

---








Submit jobs on Bohrium | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/userguide/submitjob)
* [English](/en/docs/userguide/submitjob)
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
* Submit Jobs
# Submit jobs on Bohrium

Currently, Bohrium offers two different job submission methods for different user scenarios, with the following usage scenarios:

| Usage Scenarios | Suggested Submission Method |
| --- | --- |
| Not familiar with Linux commands or software usage parameters | [Web submission](/en/docs/userguide/submitjob#web-submission) |
| First-time using Bohrium, not familiar with Bohrium CLI, and not able to write `job.json` etc. | [Web submission](/en/docs/userguide/submitjob#web-submission) |
| Advanced users who are familiar with Linux commands and Bohrium job submission commands. | [Command Line Submission](/en/docs/userguide/submitjob#command-line-submission) |

## Web Submission[​](#web-submission "标题的直接链接")

Bohrium has pre-installed commonly used scientific computing software for users. You only need to prepare the input files, and you can quickly submit a job within 1 minute.

### Basic process[​](#basic-process "标题的直接链接")

1. In the left menu bar of Bohrium, select "New Job";
2. Choose the software you need, follow the steps to upload files and set parameters;
3. After submission, you can view the calculation process and results for the corresponding job.

### Specific operations[​](#specific-operations "标题的直接链接")

#### 1. Set basic job information[​](#1-set-basic-job-information "标题的直接链接")

Click the "New-Job" button on the left menu bar of Bohrium to enter the Web Submission page, as shown in the red box in the following image:

![网页提交入口](/en/assets/images/webjob-ee44a5675ae58588ca37f18d37b431b0.png)

The basic job information includes the job name and the project which the job belongs：

* The job name has been filled with a default value, you can change it according to your actual needs；
* In the "Project" field, you need to select the project to which the job belongs. The job will directly use the project creator's balance. If you do not have a project, you can create one here by clicking "New Project" and entering the project name.

![webcreateproject](/en/assets/images/webcreateproject-e94298f9a44906eb6ff2bbf6a803db81.png)

#### 2. Software and Parameters Settings[​](#2-software-and-parameters-settings "标题的直接链接")

You can choose the software you need to use from the software list. If the list does not have the software you need, you can contact WeChat Work at 17710231129 for help. Click on the software you need to use to enter its specific settings. This tutorial takes ABACUS as an example:

![selectsoftware](/en/assets/images/selectsoftware-c7502b6e709877bf7594d8e7a4eeab1d.png)

* Click "Upload" to upload the input files you need for calculation, as shown in icon number 1 in the image below；
* Select the specific version of the software you need, as shown in icon number 2 in the image below. If the version you need is not available, please contact WeChat Work at 17710231129 for assistance；
* The system will automatically fill in the command required to run the software based on the software version you have selected, as shown in icon number 3 in the image below.

**Notice** For some software, the command requires an `input_file` to be filled in. You can select the corresponding file from the list of uploaded input files, and the system will automatically fill it in.

![setsoftware](/en/assets/images/setsoftware-327cd5191f101a866fc2ef46e57324d2.png)

#### 3. Hardware Settings[​](#3-hardware-settings "标题的直接链接")

After completing the software settings, click "Next" to enter the hardware settings. Here, you can choose the computer configuration you need for the calculations. If you are unsure about which configuration to choose, simply use the recommended values that the system has pre-filled by default.

![sethardware](/en/assets/images/sethardware-1040a0433f4bb8babd097a0abe4b7f06.png)

#### 4. Review and Submit Job[​](#4-review-and-submit-job "标题的直接链接")

After both the software and hardware settings are completed, you can proceed to "Review". If there are no issues, you can submit the job.

**Notice** The "Submit" button will only be highlighted when all the required fields are filled in correctly.

![jobcheck](/en/assets/images/jobcheck-e903b6597acdd18cbeca1cab6589031b.png)

## Command Line Submission[​](#command-line-submission "标题的直接链接")

You can learn how to use command line to submit jobs on the Bohrium platform in the [Command Line Submission Documentation](/en/docs/quickstart/FirstRun).

## View Jobs[​](#view-jobs "标题的直接链接")

You can learn how to view job status on the Bohrium platform in the [Monitoring Jobs Documentation](/en/docs/quickstart/Status).

## Download Results[​](#download-results "标题的直接链接")

You can learn how to download job results on the Bohrium platform in the [Result Download Documentation](/en/docs/quickstart/Result).

[PreviousSubmit Jobs to Bohrium with dpdispatcher](/en/docs/bestpractice/DP-Dispatcher/)[NextBohrium Web Shell](/en/docs/userguide/WebShell/)

* [Web Submission](#web-submission)
  + [Basic process](#basic-process)
  + [Specific operations](#specific-operations)
* [Command Line Submission](#command-line-submission)
* [View Jobs](#view-jobs)
* [Download Results](#download-results)



