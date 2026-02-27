# quickstart > Result

**Source URL:** https://docs.bohrium.com/en/docs/quickstart/Result

---








Get job results | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/quickstart/Result)
* [English](/en/docs/quickstart/Result)
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
* Get job results
# Get job results

This article introduces how to obtain job results after the job is completed. Bohrium currently provides three ways to get results.

## Get job results from the Bohrium web interface[​](#get-job-results-from-the-bohrium-web-interface "标题的直接链接")

After the job is completed, you can download the results or save them to `/data` from the [Jobs](https://bohrium.dp.tech/jobs).

![下载结果](/en/assets/images/screenshot-20220908-021048-81779ff7290fa220ed1cabdb79b30748.png)

## Get job results from command-line interface[​](#get-job-results-from-command-line-interface "标题的直接链接")

You can use the [Bohrium CLI](/en/docs/bohrctl/about) tool to download the results of jobs:

```
bohr job download -j <JOB ID>  

```
```
bohr job_group download -j <JOB GROUP ID>  

```

Please replace the `Job_ID` in the example with the job ID you want to download.

![Download Results](/en/assets/images/result_4-eb43c8bf9566233d1b4aa52b7267659a.png)

## Automatic download of results[​](#automatic-download-of-results "标题的直接链接")

If you submit jobs on the Bohrium management node, you can add the `-r` parameter to enable the automatic download of results. In the example, the results will be automatically downloaded to the `/personal/result`.

```
bohr job submit -i job.json -p ./ -r /personal/result  

```
[PreviousTerminate jobs](/en/docs/quickstart/KillJob/)[NextIntroduction to the Bohrium CLI](/en/docs/bohrctl/about/)

* [Get job results from the Bohrium web interface](#get-job-results-from-the-bohrium-web-interface)
* [Get job results from command-line interface](#get-job-results-from-command-line-interface)
* [Automatic download of results](#automatic-download-of-results)



