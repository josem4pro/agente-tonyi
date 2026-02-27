# bestpractice > DP-Dispatcher

**Source URL:** https://docs.bohrium.com/en/docs/bestpractice/DP-Dispatcher

---








Submit Jobs to Bohrium with dpdispatcher | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/bestpractice/DP-Dispatcher)
* [English](/en/docs/bestpractice/DP-Dispatcher)
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
* Use DP-Dispatcher
# Submit Jobs to Bohrium with dpdispatcher

## Introduction[​](#introduction "标题的直接链接")

DP-Dispatcher allows you to declare high-performance computing jobs, computing environments, and computing resources, and automatically completes the entire process of job generation, submission, polling, and recycling.

[Project Documentation](https://docs.deepmodeling.com/projects/dpdispatcher/en/latest/getting-started.html)

[Chinese Introduction](https://mp.weixin.qq.com/s/4i-yOVcuUGHu5JSbOk4XPA)

dpdispatcher provides the following abstractions:

1. Task class: defines a computing command and its dependent files.
2. Resources class: defines the computing resources required during computation.
3. Machine class: defines the batch processing system used for computation, remote machine IP, working path, etc. Currently supports Slurm, PBS, LSF, DpCloudserver, and other systems.

## Prepare Input Files[​](#prepare-input-files "标题的直接链接")

```
mkdir -p dp_dispatcher/test && cd dp_dispatcher  
  
echo "hello world" > example.txt  
  
for i in {1..4}  
do  
    mkdir test/dir${i}  
    cp example.txt test/dir${i}/  
done  

```

In the dp\_dpdispather folder, create run.py, machine.json, and resource.json files, with examples as follows:

**run.py**

* task\_work\_path: defines the working directory
* forward\_files: defines the files to be uploaded, here the example.txt files under dir1-4/ will be uploaded
* backward\_files: defines the files to be downloaded, namely out.txt

```
from dpdispatcher import Machine, Resources, Task, Submission  
  
machine = Machine.load_from_json('machine.json')  
resources = Resources.load_from_json('resource.json')  
  
task1 = Task(command='cat example.txt', task_work_path='dir1/', forward_files=['example.txt'], backward_files=['out.txt'], outlog='out.txt')  
task2 = Task(command='cat example.txt', task_work_path='dir2/', forward_files=['example.txt'], backward_files=['out.txt'], outlog='out.txt')  
task3 = Task(command='cat example.txt', task_work_path='dir3/', forward_files=['example.txt'], backward_files=['out.txt'], outlog='out.txt')  
task4 = Task(command='cat example.txt', task_work_path='dir4/', forward_files=['example.txt'], backward_files=['out.txt'], outlog='out.txt')  
  
task_list = [task1, task2, task3, task4]  
  
submission = Submission(work_base='test/',  
    machine=machine,  
    resources=resources,  
    task_list=task_list,  
    forward_common_files=[],  
    backward_common_files=[]  
)  
  
submission.run_submission()  

```

**machine.json**

```
{  
        "batch_type": "Lebesgue",  
        "context_type": "LebesgueContext",  
        "local_root" : "./",  
        "remote_profile":{  
          "email": "Bohrium registration email",  
          "password": "password",  
          "project_id": 0000,  
            "input_data":{  
              "job_type": "indicate",  
              "log_file": "log",  
              "job_name": "dpdispather_test",  
              "disk_size": 100,  
              "scass_type":"c16_m32_cpu",  
              "platform": "ali",  
              "image_name":"Image name for the job, can be found in the 'Images' page",  
              "on_demand":0  
            }  
        }  
}  

```

**Note1**: Replace the `0000` after `"project_id":` with your own project ID, which can be found on the "[Projects](https://bohrium.dp.tech/projects)" page.

**Note2**：In some scenarios that support tickets, add environment variables as follows.

```
import os  
os.environ["BOHR_TICKET"] = ""  
os.environ.get("BOHR_TICKET", None)  

```

**resource.json**

```
{  
    "number_node": 1,  
    "cpu_per_node": 32,  
    "gpu_per_node": 0,  
    "queue_name": "LBG_CPU",  
    "group_size": 4  
}  

```
## Submit Job[​](#submit-job "标题的直接链接")

```
python3 run.py  

```
## View Results[​](#view-results "标题的直接链接")

You can find the corresponding job in [Bohrium's My Jobs](https://bohrium.dp.tech/jobs).

## Download Results[​](#download-results "标题的直接链接")

`bohr job download -j <Job ID\>` or directly click the download option in the web job bar.

![Download Results](/en/assets/images/result_4-eb43c8bf9566233d1b4aa52b7267659a.png)

[PreviousRunning Container Jobs](/en/docs/bestpractice/Docker/)[NextSubmit jobs on Bohrium](/en/docs/userguide/submitjob/)

* [Introduction](#introduction)
* [Prepare Input Files](#prepare-input-files)
* [Submit Job](#submit-job)
* [View Results](#view-results)
* [Download Results](#download-results)



