# userguide > WebShell

**Source URL:** https://docs.bohrium.com/en/docs/userguide/WebShell

---








Bohrium Web Shell | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/userguide/WebShell)
* [English](/en/docs/userguide/WebShell)
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
* Web Shell
# Bohrium Web Shell

Bohrium Web Shell is a web-based SSH connection tool provided by Bohrium.

## Use Web Shell to connect to the management node[​](#use-web-shell-to-connect-to-the-management-node "标题的直接链接")

Click the `Connect` button on the node card, select `Open Web Shell` in the pop-up window, and you will automatically log in to the management node as **root**:

![Web Shell入口](/en/assets/images/entrance-a06e167c19d2f4766f917bd95cd2aa4f.png)

For each project, there is a default **1TB (1024 GB)** shared space for project members (i.e., the /share directory), which can store your data and files persistently without being deleted when the node is released. All nodes under the same project share this storage space.

> **Note**: When converting a node into a mirror, only the data on the system disk will be saved in the mirror. Therefore, it is recommended to store the data that needs to be mirrored on the system disk.

## Use Web Shell to connect to compute nodes[​](#use-web-shell-to-connect-to-compute-nodes "标题的直接链接")

When the task (Job) is running and the remote compute node has not been released, you can use the Web Shell to log in to the compute node and view related files.

Click the `SSH` button on the right side of the task to connect to the compute node running the task through the Web Shell:

![连接计算节点](/en/assets/images/connect_compute-91c2909f914ebbd12b519914768fd3ae.png)

Additionally, clicking the `SSH` button on the task details page can also establish a connection to the computing node:

![任务详情页连接计算节点](/en/assets/images/connect_compute_job-674de13f9c55f859944f65c6fa2f683a.png)

## Other features of Web Shell[​](#other-features-of-web-shell "标题的直接链接")

### Switch shell[​](#switch-shell "标题的直接链接")

The Bohrium Web Shell features two built-in shells, `zsh` and `bash`, on the management node for you to choose from. You can switch between them as needed (please note that this feature is not available on the compute node):

**Switch from zsh to bash**

```
bash  

```

**Switch from bash to zsh**

```
zsh  

```
### Minimize and adjust windows[​](#minimize-and-adjust-windows "标题的直接链接")

Click the **Minimize** button to hide the Web Shell. To reopen it, click the **Web Shell** button on the upper navigation bar:

![Web Shell按钮](/en/assets/images/window_minimum-d26c50932c6fc7a8297b2f8a3e7bd0bb.png)

You can adjust the window size by **dragging the top of the Web Shell**; additionally, by clicking the **Top** or **Full Screen** button, you can either fill the Web Shell window in the working area or maximize the Web Shell window.

### Open multiple windows[​](#open-multiple-windows "标题的直接链接")

Click the **+** button at the top of the Web Shell to open multiple windows:

![打开多个窗口](/en/assets/images/window_multi-b1ec4ed274894865c558e948ed4344f3.png)

[PreviousSubmit jobs on Bohrium](/en/docs/userguide/submitjob/)[NextFile Management](/en/docs/userguide/FileManage/)

* [Use Web Shell to connect to the management node](#use-web-shell-to-connect-to-the-management-node)
* [Use Web Shell to connect to compute nodes](#use-web-shell-to-connect-to-compute-nodes)
* [Other features of Web Shell](#other-features-of-web-shell)
  + [Switch shell](#switch-shell)
  + [Minimize and adjust windows](#minimize-and-adjust-windows)
  + [Open multiple windows](#open-multiple-windows)



