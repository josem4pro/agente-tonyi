# userguide > coorperation

**Source URL:** https://docs.bohrium.com/en/docs/userguide/coorperation

---








Project Management and Collaboration | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/userguide/coorperation)
* [English](/en/docs/userguide/coorperation)
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
* Collaboration
# Project Management and Collaboration

## Introduction[​](#introduction "标题的直接链接")

In daily scientific research and teaching, teachers/students often have the following needs:

1. How to centrally manage the funds of several people and set budgets: for example, members of the same research group, students participating in a course or workshop together, they need to use the funds of a project together;
2. How can members involved in the same research topic conveniently and "painlessly" use the code developed by other members;
3. It would be so much more convenient for the members of a research group if there was a place to share files instead of constantly sending them back and forth;
4. It would be great if the teacher could log in directly to check the problem when their own code doesn't work.

To meet these needs, Bohrium provides a series of tools to help you complete project collaboration and improve team efficiency. All team collaborations are based on projects, and we first need to create a project.

## Creating a Project[​](#creating-a-project "标题的直接链接")

After completing Bohrium account registration and top-up, click on "Projects" in the navigation bar on the Bohrium homepage (red box 1 in the picture), and select "New Project" in the upper right corner of the page (red box 2 in the picture).

![createproject](/en/assets/images/20240410-163838-7ac079a8c336405adce735540aaf90be.png)

In the pop-up window, give the project a name that is easy for you to recognize (such as the name of your research group, course or project), and click "OK".

![new project](/en/assets/images/20240410-172846-b145ae42885d4e8d7c38a6b3d23a99ea.png)

## Project Roles and Permissions Description[​](#project-roles-and-permissions-description "标题的直接链接")

There are currently 3 roles in the project:

1. Creator: The user who creates the project is the creator of the project. A project must have and only have one creator, and this role cannot be transferred to others or deleted.
2. Administrator: Appointed by the creator, a project can have multiple administrators, which is not a mandatory role and can be appointed or removed at any time.
3. Member: Users added to the project are by default in this role.

The specific permissions of each role are as follows:

> Symbol explanation: √ means that the role has this permission; X means that the role does not have this permission.

| Function Module | Permission Content | Creator | Administrator | Member |
| --- | --- | --- | --- | --- |
| Project Management | Modify project name | √ | √ | X |
| Project Management | Delete project | √ | X | X |
| Project Member Management | Add or delete project members | √ | √ | X |
| Project Member Management | Appoint or cancel project administrators | √ | X | X |
| Project Budget Management | View the overall and individual consumption of the projectAdjust the overall and individual budget amounts of the project | √ | √ | X |
| Project Node Management | View and operate all management nodes within the project: such as logging into management nodes, shutting down, deleting, etc. | √ | √ | X |
| Project Job Management | View and operate all jobs within the project: such as logging into computing nodes, viewing logs, downloading files, etc. | √ | √ | X |
| Project Image Management | View and operate all images within the project: such as sharing, deleting | √ | √ | X |
| Project Expense Bill | View and download the project's consumption bill | √ | √ | X |

## Add/Remove Members[​](#addremove-members "标题的直接链接")

If the project has other collaborators (such as course assistants, team members, or students in a course or workshop), you can click on the "Project Member Management" button (circled in red in the figure) to enter the member management page for operations.

![Enter image description](/en/assets/images/20240410-173011-5f768b3d9b21d839c3b6c40225964f51.png)

On the member management page, you can add project members in bulk, delete them in bulk, set administrators, and view the budget and expenses of each member within the organization. For differences between roles, please check the [role permission description](/en/docs/userguide/coorperation#project-roles-and-permissions-description).

![Enter image description](/en/assets/images/20240410-173105-d8f3451aa34c34476da336927c5e1d51.png)

**Special Note**: The expenses incurred by members within the project directly consume the balance in the project creator's wallet. It is recommended that you set up a budget for the project and its members.

## Project and Member Budget[​](#project-and-member-budget "标题的直接链接")

1. Project Budget

The project creator and administrators can set a budget for the project (not mandatory) to control the total expenses of the project. If you do not set a budget, the default project budget will be "unlimited". Click the "Project Budget" button (circled in red in the image) to enter the budget management page.

![输入图片说明](/en/assets/images/20240410-173152-f05471755de331e1c24461e5bfa34c0f.png)

![输入图片说明](/en/assets/images/20240410-173252-abc0117bca6e8e8b25accec0b484a618.png)

The expenses of all members within the project will be recorded in this budget. When the total expenses of the project exceed the budget, project members will be unable to submit new jobs or start new nodes.

You can set a reminder threshold in [Notification Management](https://bohrium.dp.tech/settings/notice). When the remaining project budget falls below the threshold, you will receive a message reminder.

![输入图片说明](/en/assets/images/20240410-173413-244b2348f21a7a9b0c1c942381198608.png)

2. Member Budget

The creator and administrators of the project can allocate the consumable budget for the project members, so as to control the overall spending.

In the "Project Budget" settings window, click the "Divide evenly" button to evenly distribute the total project budget among all members. You can also click "Unified Configuration" to allocate the same budget for each member. Of course, you can also set individual budget amounts for each member separately.

Distribute the budget evenly to all members:

![Enter image description](/en/assets/images/20240410-173530-adb0cba2c893b141b1c9a76f394ca778.png)

Set different budgets for different members:

![Enter image description](/en/assets/images/20240410-173755-6701c3bae32e987eec0f02e483cc962c.png)

## Shared Files[​](#shared-files "标题的直接链接")

Each project has a /share drive available for file sharing, with a default free space of 1024GB. All members within the project have read and write access to the files in this drive. Click the "View Files" button (circled in red in the image) to view the shared drive files for the project.

![输入图片说明](/en/assets/images/20240410-173951-4768ff1cfac295f6ba063e0a6f49fe74.png)

![输入图片说明](/en/assets/images/20240410-174112-e42c8a75497d84f14d20cc6929705241.png)

## Shared Images[​](#shared-images "标题的直接链接")

All members within the project can view and use the images created by other teammates in the same project in the Bohrium ["Images" - "Custom Images"](https://bohrium.dp.tech/web-images/private). This allows for a more convenient way to set up a consistent working environment, debug code, or directly deploy in a production environment.

![Image description](/en/assets/images/20240410-174210-79ff086790e9cfc6c1c1a89abce3a95a.png)

## Delete Project[​](#delete-project "标题的直接链接")

When you finish a project, you can click the "Delete" button (the red circle in the picture) to delete the project and disband the members within the project. However, after the project is deleted, all jobs and images within the project will be permanently deleted and cannot be viewed. The deletion operation is irreversible, so please be cautious.

![Image description](/en/assets/images/20240410-174256-d457d33d2eb029a03b64674077106d10.png)

[PreviousQuota Limits](/en/docs/userguide/QuataLlimit/)[NextABACUS](/en/docs/software/ABACUS/)

* [Introduction](#introduction)
* [Creating a Project](#creating-a-project)
* [Project Roles and Permissions Description](#project-roles-and-permissions-description)
* [Add/Remove Members](#addremove-members)
* [Project and Member Budget](#project-and-member-budget)
* [Shared Files](#shared-files)
* [Shared Images](#shared-images)
* [Delete Project](#delete-project)



