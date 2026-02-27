# userguide > Dataset

**Source URL:** https://docs.bohrium.com/en/docs/userguide/Dataset

---








Dataset | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/userguide/Dataset)
* [English](/en/docs/userguide/Dataset)
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
* Dataset
# Dataset

This article introduces the usage of the Bohrium dataset.

## What is Dataset?[​](#what-is-dataset "标题的直接链接")

The Bohrium dataset provides capabilities for data import, download, data version management, data sharing, and dataset mounting. Have you ever encountered the following problems before:

* Most of the input files for jobs are the same, but every time you submit a job, you have to wait for the file packaging and uploading process, resulting in low job submission efficiency.
* Input files are large, and the packaging and uploading process takes a long time when submitting jobs.
* I have some files that I want to share with others, but I don't know how to share them.
* ...

Now, the dataset can solve the above problems for you, improve job submission efficiency, and address data sharing needs.

## Creating a Dataset[​](#creating-a-dataset "标题的直接链接")

### Creating a dataset on the web interface[​](#creating-a-dataset-on-the-web-interface "标题的直接链接")

Click the "[Dataset](https://bohrium.dp.tech/dataset/list)" button in the main menu to enter the dataset list page, as shown in Figure 1. Click the "New Dataset" button, as shown in Figure 2, to enter the dataset creation page.

![创建数据集](/en/assets/images/20240409-112845-228164b2f21d7836feb3929d1f104afa.png)

Fill in the basic information of the dataset and upload files. After clicking "create", the system will create the v1 version of the dataset by default. Click here to view the [Content Description](/en/docs/userguide/Dataset#dataset-content-description).

![图片](/en/assets/images/20240409-113042-60533b999d7c4f37ead0963279370a4f.png)

After the information and files are prepared, click "Create". The dataset is created successfully, and the page will automatically redirect to the details page of this dataset version.

### Creating a dataset using the command-line tool[​](#creating-a-dataset-using-the-command-line-tool "标题的直接链接")

When the dataset file is too large, the creation process might fail due to network issues or other factors, as the transfer time could be lengthy.
Therefore, you can use the [Bohrium CLI](/en/docs/bohrctl/dataset), which supports resuming from breakpoints, to create the dataset.

If an interruption occurs due to network issues or other factors, you can resume by re-executing the same command. Then, follow the prompt and enter `y` to recover the previous files, allowing the process to resume from the breakpoint.

Summary:

```
Flags:  
  -m, --comment string     dataset description  
  -h, --help               help for create  
  -l, --lp string          file local path  
  -n, --name string        dataset name  
  -p, --path string        dataset path  
  -i, --pid int            project id  

```

Parameter description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --comment | -m | Dataset Description | 否 |
| --name | -n | Dataset Name | 是 |
| --path | -p | Dataset Path | 是 |
| --pid | -i | project ID | 是 |
| --lp | -l | project id | 是 |

案例：

```
$ bohr dataset create -n bigfile -p bigfile -i 26611 -l "/Users/dp/Downloads/test"  
# Upload the test file to the bigfile dataset.  
# Interrupt the creation during the upload process.   
# Re-enter the same command and input ‘y’ to continue the upload.  

```

![dataset create](/en/assets/images/QQ20240624-190334-43989691baf9d4b777a93fd0cf4298bc.png)

## Viewing a Dataset[​](#viewing-a-dataset "标题的直接链接")

Click the "[Dataset](https://bohrium.dp.tech/dataset/list)" button in the main menu to enter the dataset list page. The list displays all the datasets you can use, including the datasets you created and the datasets others have created and shared with you.

![图片](/en/assets/images/20240409-113203-44dfca152c34a4d371182bee9a4edaf0.png)

Click on the dataset name to enter the dataset details page, where you can view the basic information of the dataset and the information of each version, obtain the file paths of each version, view and download version files.

![图片](/en/assets/images/20240409-113249-2e4e0486be39b89a434333dd7567369e.png)

You can also use the [Bohrium CLI](/en/docs/bohrctl/dataset) tool to view the dataset.

```
$ bohr dataset list # View all datasets （Press Ctrl+C to exit）  

```

![dataset list](/en/assets/images/QQ20240607-175052@2x-9c880d585ed1d276333cd8ebee630e0f.png)

## Editing and version management of a dataset.[​](#editing-and-version-management-of-a-dataset "标题的直接链接")

If you have the management permissions for the dataset, you can perform operations such as adding new versions, deleting, and editing the basic information of the created dataset.

### Version Management[​](#version-management "标题的直接链接")

If you need to make changes to the files in the current dataset, you can release a new version by using the "Create New Version" method.

1. **Creating**: Click the "New Version" button to enter the new dataset version creation page. The system will automatically import the existing files from the latest published version. You can add or delete files as needed, and click "Create" to release the new version.
   
   ![图片](/en/assets/images/20240409-113346-ea54348adc05f87cfda111b131d7c08f.png)
   
   ![图片](/en/assets/images/20240409-113426-16ee9cef1e2263f2177a86e8aa14fc1d.png)
2. **Waiting for preparation to complete**: Creating a new version requires some preparation time. During the preparation, other users cannot see or use this version. The duration of the preparation time is related to the number and size of version files. Please wait for the version to be ready before using it.
3. After a version is created, the files within the version cannot be changed. If adjustments are needed, you can create a new version.

All the versions you have released will be displayed in the dataset. You can add and delete dataset versions according to your actual needs. Other users can only see the datasets that you have successfully published.

**Notice**: Deleted versions cannot be restored and will no longer be viewable or usable.

### Editing a Dataset[​](#editing-a-dataset "标题的直接链接")

* Click the "Edit" button on the dataset list page or dataset details page to modify the dataset's name, description, and permission scope.
  
  ![图片](/en/assets/images/20240409-113530-71799ef9e21905c4448e3884a024950a.png)
* In the dataset details page, you can also modify the description of each version.
  
  ![图片](/en/assets/images/20240409-113610-6cc73cbe0c1d8429486c97905c1008d0.png)

## Using a Dataset[​](#using-a-dataset "标题的直接链接")

The dataset is currently supported in the following scenarios:

### Submitting a job[​](#submitting-a-job "标题的直接链接")

1. **Command Line Submission**: You only need to modify your `job.json`, adding a `dataset_path` field. In this field, fill in the corresponding paths of the dataset versions you need to use in an array format, as shown in the red box in the image below.

![图片](/en/assets/images/20240409-113839-668544bb27a55f840e0937d61cb0dace.png)

When submitting a job, the method of specifying the input file directory is still supported, and both can be used simultaneously.

Here is an example of how to fill in `job.json`:

```
{  
    "job_name": "DeePMD-kit test",  
    "command": " cd se_e2_a && dp train input.json > tmp_log 2>&1 && dp freeze -o graph.pb",  
    "log_file": "se_e2_a/tmp_log",  
    "backward_files": ["se_e2_a/lcurve.out","se_e2_a/graph.pb"],  
    "project_id": 0000,  
    "platform": "ali",  
    "machine_type": "c4_m15_1 * NVIDIA T4",  
    "job_type": "container",  
    "image_address": "registry.dp.tech/dptech/deepmd-kit:2.1.5-cuda11.6",  
    "dataset_path": ["/bohr/test1-51ov/v1","/bohr/test1-51ov/v2"]  
}  

```

1. **Web submission**:

When submitting a job on the graphical interface, click the 'Select Dataset' button and choose the version of dataset you wish to use.

![图片](/en/assets/images/20240409-114113-44e0990738ed2ca1669fde3572108819.png)

![图片](/en/assets/images/20240409-114205-e1c88ca015d79947765dcb9923cbb93a.png)

### Use and share datasets in Notebook[​](#use-and-share-datasets-in-notebook "标题的直接链接")

When writing and posting notebook, you can use and share the datasets required for the notebook along with it.

**Step 1: Select the dataset you want to use/share**

On the Bohrium homepage, click the 'New - Notebook' button at the top left corner to enter the Notebook editing page.

![图片](/en/assets/images/20240409-120016-472efee0b74d5c7b8e25b0bf87c9375d.png)

Click the arrow on the right side to expand the extension panel.

![图片](/en/assets/images/20240409-140453-64aa3cc54d29b4ae2d2bf26751408352.png)

Click on "Select Existing Datasets" to add the dataset version required for this notebook. You can also click on "New Dataset" to create a new dataset.

![图片](/en/assets/images/20240409-140551-9bda44d8e85592746e0e288ae56f67cc.png)

**Notice**: Please add the dataset before connecting to the node. Datasets added after the node has started will require a node restart to take effect.

**Step 2: Use the dataset in the Notebook**

Move the mouse over the selected dataset name and click the copy button to get the storage path of the dataset files. All dataset files are stored in this path.

![图片](/en/assets/images/20240409-140714-9def604698627f2d9161f7fa7304860e.png)

Simply enter this path in the Notebook to use it. The path used in the example below is: `/bohr/testdataset-6xwt/v1/`：

Example 1: Enter the dataset directory

```
cd /bohr/testdataset-6xwt/v1/  

```

Example 2: List all files under the dataset

```
ls /bohr/testdataset-6xwt/v1/  

```

**Step 3: Post the Notebook and share the dataset**

After the Notebook with the added dataset is posted, other users can view and use the corresponding dataset on the details page.

![图片](/en/assets/images/20240409-140926-fd01749643a22bc91687ea7cf523aae2.png)

### Use the dataset on the management node[​](#use-the-dataset-on-the-management-node "标题的直接链接")

When you [create container management node](https://bohrium.dp.tech/nodes/create/container), you can add the version of the dataset you need to mount, as shown in the figure below as '1'. After successful mounting and booting, you can find the dataset files on the management node at the path shown as '2'.

![图片](/en/assets/images/20240409-141708-5ff75cdc543be75f7742a01315657ca2.png)

## Dataset content description[​](#dataset-content-description "标题的直接链接")

| Field Name | Description | Example |
| --- | --- | --- |
| Dataset Name | The name of the dataset, which can be modified at any time | testdataset |
| Dataset Path | The dataset files will be uploaded to this path. Please enter the recognizable content of the dataset in the input box, and the system will automatically generate a unique path corresponding to the version**Notice**: Modifying the path after uploading files will clear the files you have already uploaded, so please modify with caution | /bohr/testdataset-b2dh/v1 |
| Files | The files included in this dataset version, support uploading local files or folders**Notice**: Please do not refresh or leave the page during file upload to avoid upload failure | -- |
| Project | The project to which the dataset belongs. Project members can use the dataset by default. | testproject |
| Permissions | Manageable: Permissions for editing, deleting, creating new versions, etc., of the dataset; the dataset creator and the creator and administrator of the project to which the dataset belongs have these permissions by default and cannot be changedUsable: The permission to view and use the dataset; project members to which the dataset belongs have this permission by default and cannot be changed. This permission can be granted to other projects or users | Manageable: the dataset creator and the creator and administrator of the project to which the dataset belongsUsable: project members to which the dataset belongs |
| Description | The description of the dataset | 该数据集用于测试 |

[PreviousFile Management](/en/docs/userguide/FileManage/)[NextNotebook](/en/docs/userguide/Notebook/)

* [What is Dataset?](#what-is-dataset)
* [Creating a Dataset](#creating-a-dataset)
  + [Creating a dataset on the web interface](#creating-a-dataset-on-the-web-interface)
  + [Creating a dataset using the command-line tool](#creating-a-dataset-using-the-command-line-tool)
* [Viewing a Dataset](#viewing-a-dataset)
* [Editing and version management of a dataset.](#editing-and-version-management-of-a-dataset)
  + [Version Management](#version-management)
  + [Editing a Dataset](#editing-a-dataset)
* [Using a Dataset](#using-a-dataset)
  + [Submitting a job](#submitting-a-job)
  + [Use and share datasets in Notebook](#use-and-share-datasets-in-notebook)
  + [Use the dataset on the management node](#use-the-dataset-on-the-management-node)
* [Dataset content description](#dataset-content-description)



