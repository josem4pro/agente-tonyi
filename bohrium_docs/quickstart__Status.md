# quickstart > Status

**Source URL:** https://docs.bohrium.com/en/docs/quickstart/Status

---








Monitor jobs | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/quickstart/Status)
* [English](/en/docs/quickstart/Status)
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
* Monitor jobs
# Monitor jobs

This tutorial mainly introduces how to monitor job status on the Bohrium platform. Users can click on the [Jobs](https://bohrium.dp.tech/jobs) on the left side of the Bohrium homepage to display job information. According to their needs, set job filtering conditions (such as time, job group, project, etc.), as shown in the figure below:

![任务管理](/en/assets/images/task_2-d47152cb57d75f795fe7388e64b83a9d.png)

## Job Status[​](#job-status "标题的直接链接")

After the user submits a job, the job will go through three statuses in sequence: "Resource Scheduling" - "Running" - "Completed".

**Resource Scheduling:**
![等待](/en/assets/images/status_1-aeaa2e1983082992bd2e262a55313f81.png)

**Running:**
![运行中](/en/assets/images/status_2-99295ebd07ef075332194a7233424ab6.png)

**Completed:**
![已完成](/en/assets/images/status_3-aae932dd93af086e7f0d75d699807105.png)

## Job Log[​](#job-log "标题的直接链接")

Users can find the job log bottom on the right side of the [Jobs](https://bohrium.dp.tech/jobs) page (within the red box in the image below). Click on the log bottom, and the browser will pop up the log page.

![输入图片说明](/en/assets/images/log_2-eca155e211babfc80c368300364a26da.png)

You can also click on the "Job ID" in this page to enter the "Job Details" page, where you can view rich information such as the timeline of the job, real-time files, and job log.

![查看任务状态](/en/assets/images/checkjobstatus221104-99c08d34a7c1715c3511cd15bdbe39c4.png)

**Tips:**

In addition to monitoring jobs on web page, Bohrium also supports using the [Bohrium CLI](/en/docs/bohrctl/about) to directly view the status of [jobs](/en/docs/bohrctl/job)in the command line.

```
bohr job list  

```
```
bohr job_group list  

```

Alternatively, you can use the following commands:

```
bohr job describe -j  <Jobs ID>   

```
```
bohr job_group list -i  <JOB GROUP ID>   

```

Job log can also be obtained in the following ways:

```
bohr job log -j <Jobs ID>     

```
[PreviousRun your first job](/en/docs/quickstart/FirstRun/)[NextTerminate jobs](/en/docs/quickstart/KillJob/)

* [Job Status](#job-status)
* [Job Log](#job-log)



