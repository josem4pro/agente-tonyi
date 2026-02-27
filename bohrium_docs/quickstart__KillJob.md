# quickstart > KillJob

**Source URL:** https://docs.bohrium.com/en/docs/quickstart/KillJob

---








Terminate jobs | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/quickstart/KillJob)
* [English](/en/docs/quickstart/KillJob)
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
* Terminate Jobs
# Terminate jobs

This article introduces how to terminate jobs or job groups on the Bohrium platform. You can choose between `terminate` and `delete` operations according to the scenario.

* Terminate
  
  **To end running jobs/job groups in advance, save the generated result files,** and the status of the terminated jobs will be changed to "completed."
* Delete
  
  **To end running jobs/job groups,** the status of the jobs will be changed to "failed." Job result files will be deleted, and the jobs/job groups disappear from the list. The delete operation cannot be undone, so please use it with caution.

## Terminate jobs on the Jobs page[​](#terminate-jobs-on-the-jobs-page "标题的直接链接")

The [Jobs](https://bohrium.dp.tech/jobs) page provides buttons to end and delete (jobs/job groups):

* Job Groups:
  
  ![输入图片说明](/en/assets/images/jobgroup-d76b39c954c4d6d1bb1c1a70fa79cd2f.png)
* Job:
  
  ![输入图片说明](/en/assets/images/job-c36fd98f0dfe1259d6b57358dbe1fe30.png)
  
  This operation can also be performed on the Job Details page.
  
  ![输入图片说明](/en/assets/images/screenshot-20220909-164304-1301a7a048ad8316a7b0ff9eeb3f5312.png)

## Terminate jobs in the command-line[​](#terminate-jobs-in-the-command-line "标题的直接链接")

You can also use the [Bohrium CLI](/en/docs/bohrctl/job) tool in the command-line to end jobs.

* Terminate the job/job groups(It has the same effect as the terminate button on the page.)

```
bohr job terminate -j <JOB ID>  

```
```
bohr job_group terminate -j <Job_Group_ID>  

```

Please replace the `Job_Group_ID` or `Job_ID` in the example with the job group ID or job ID you want to terminate.

* Delete job/job groups(It has the same effect as the delete button on the page.)

```
bohr job delete -j <JOB ID>  

```
```
bohr job_group delete -j <<Job_Group_ID>  

```

Please replace the `Job_Group_ID` or `Job_ID` in the example with the job group ID or job ID you want to delete.

* Terminate the job (stop operation provided by Bohrium CLI)
  
  ```
  bohr job kill -j <JOB ID>  
  
  ```
  
  Please replace the `Job_ID` in the example with the job ID you want to delete.

Compared to the `terminate` operation, `kill` interrupts the job **without saving the result files**.
Compared to the `delete` operation, `kill` interrupts the job **without deleting the job**.

[PreviousMonitor jobs](/en/docs/quickstart/Status/)[NextGet job results](/en/docs/quickstart/Result/)

* [Terminate jobs on the Jobs page](#terminate-jobs-on-the-jobs-page)
* [Terminate jobs in the command-line](#terminate-jobs-in-the-command-line)



