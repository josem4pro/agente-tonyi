# userguide > Notebook

**Source URL:** https://docs.bohrium.com/en/docs/userguide/Notebook

---








Notebook | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/userguide/Notebook)
* [English](/en/docs/userguide/Notebook)
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
* Notebook
# Notebook

This article introduces how to use Notebook on Bohrium.

## What is Notebook?[​](#what-is-notebook "标题的直接链接")

Notebook on Bohrium provides an interactive environment for writing and running code, allowing you to create documents with executable code, LaTeX, rich text, images, HTML, etc. It comes with pre-installed software like DeePMD-kit and frameworks such as PyTorch and TensorFlow. You can easily connect to vast CPU and GPU resources and share the Notebook for collaboration.

The interactive development environment is provided by the open-source project Jupyter. For more information, visit the [Jupyter homepage](https://jupyter.org/).

## Creating a Notebook[​](#creating-a-notebook "标题的直接链接")

Click the "**New**" button on the [Bohrium](https://bohrium.dp.tech/home) main navigation to create a new Notebook draft and start editing:

![Write Notebook](/en/assets/images/screenshot-20240408-204345-884167e15010e444ee3dfc433ecc79ee.png)

To import a pre-existing Notebook, click the button in the top right corner, and choose "Upload from Local" or "Select Files":

![Import](/en/assets/images/screenshot-20240408-204512-4ca2b88486779c2c30b30e6e4d8257db.png)

## Editing a Notebook[​](#editing-a-notebook "标题的直接链接")

In the Notebook editing page, you can perform various actions:

![Editing Page](/en/assets/images/screenshot-20240408-204704-d89820a82163ca89291e2fc1b43c3564.png)

On the main edit area, you can write the Notebook title and content.

The text cells support common Markdown syntax, such as headings, bold/italic, ordered/unordered lists, code blocks, links, tables, images, and more. Double-click on the cell to utilize Bohrium's provided visual editing capabilities:

![](/en/assets/images/20240410-190717-5c2d5114279d8f2848612e18eeb2784a.gif)

Code cells support Python code and Shell commands. You can click the Run button to run the code cells. When code execution encounters errors, Bohrium's built-in AI assistant intelligently identifies the reasons for the errors and provides correct examples:

![](/en/assets/images/20240410-194740-f83c7c6e45fb84be6798533fde6bfe2e.gif)

Notebook automatically saves while editing. When the indicator light turns green, it means the autosave is complete:

![](/en/assets/images/screenshot-20240408-204727-a77cf1c00ce3e4f5e23b75c0194d4553.png)

You can find all your Notebooks or Notebooks shared by others in the "Notebooks" page of your profile page. Click the red circle button to continue editing:

![](/en/assets/images/screenshot-20240408-204901-7dc0a76e84037cb5b5e4cf5a867d1639.png)

For more detailed editing techniques, you can read the article [A Guide to Using Bohrium Notebook](https://bohrium.dp.tech/notebooks/8149821500) written by Bohrium's product manager. It provides detailed methods for markdown editing, practical examples of data visualization using Notebook, and helpful shortcut key usage to enhance editing efficiency.

For more Notebook writing tips, read [NBHub | Notebook Writing Help](https://bohrium.dp.tech/notebooks/3613346219) and [8 Hidden Notebook Usage Tips](https://bohrium.dp.tech/notebooks/3814348933), or search online for more methods. Additionally, Bohrium has numerous high-quality Notebooks created by users, which you can explore at the [Notebooks](https://bohrium.dp.tech/notebooks) page.

## Running Notebooks[​](#running-notebooks "标题的直接链接")

To run a Notebook, click the "Connect" button as shown in the picture:

![](/en/assets/images/screenshot-20240408-204934-f0e112c97df6ce9ca29289898d52f20a.png)

Clicking "New node for Notebook" will launch a new Notebook-specific node with the specified configuration. If you already have a running node with the necessary Notebook environment, you can choose "Connect to existing node".

Bohrium offers a variety of CPU and GPU models to choose from, with the 2-core 4G CPU being completely free:

![](/en/assets/images/screenshot-20240408-205008-3e031e2faefcd927a7a23537a7342be1.png)

After making your selection, click "Connect" and wait about 10 seconds for the node to start. When the button shows a green "Connected" status, you can start running your Notebook.

Note: If you choose to run a Notebook with a custom image, make sure it has JupyterLab version 3.0 or above installed, preferably the **latest version**. Install it using the official recommended method to ensure the `jupyter lab` command works correctly. If the image does not meet the launch requirements, the connection will fail, so please try another image.

To save costs, Bohrium will automatically release the node if the Notebook is **idle for more than 120 minutes** (no code has been run and the page is not active). Releasing the node will not affect your saved Notebook files or any files saved in the /personal disk, but changes made to the node's system disk (e.g., newly installed software) will be lost.

If you don't want to lose these changes, keep your Notebook active or save the environment as a custom image in the node list [here](/en/docs/software/OtherSoftwares). The next time you connect, use that image to start the node.

You can also manually disconnect when you don't need computing resources:

![Release Node](/en/assets/images/screenshot-20240408-205212-912590c4fbdd106926ba436450f4c71a.png)

### Configure Notebook with Multiple Kernels[​](#configure-notebook-with-multiple-kernels "标题的直接链接")

#### Install Multiple Kernels[​](#install-multiple-kernels "标题的直接链接")

If you want to install multiple Notebook kernels in the image for switching, you can follow these steps:

1. Select the node you want to configure multiple kernels from the node list and [connect using WebShell](/en/docs/userguide/WebShell#use-web-shell-to-connect-to-the-management-node);
2. Use conda to create a new Python virtual environment

```
conda create --name myenv python=3.8  

```

3. Activate the newly created virtual environment

```
conda activate myenv  

```

4. Install IPython

```
conda install ipython  

```

5. Install the required kernel (e.g., python3 kernel)

```
python -m pip install ipykernel  

```

You can also use this command to install other kernels, such as the R kernel or Julia kernel.

6. Register the installed kernel

```
python -m ipykernel install --user --name=myenv --display-name "Python (myenv)"  

```

Where,

* The `--user` option means that the kernel is registered to the current user's directory instead of the system-wide directory, which avoids permission issues.
* The `--name=myenv` option is for naming the kernel, where myenv is your environment name, and you can change this name as needed.
* The `--display-name` option is for the kernel name displayed in the Notebook interface, and you can change this name as needed.

7. Verify if the kernel configuration is successful

```
jupyter kernelspec list  

```

Note: After configuring multiple kernels, remember to [save the environment as a custom image](/en/docs/software/OtherSoftwares) and connect using the new image, otherwise the configuration will not take effect.

#### Change the default kernel[​](#change-the-default-kernel "标题的直接链接")

If you have multiple Notebook kernels installed in your image environment, you can use the following steps to change the default startup kernel using WebShell:

1. Generate the default configuration file using generate-config

```
jupyter lab --generate-config  

```

2. Locate the configuration directory of Notebook

```
jupyter --config-dir  

```

3. Check the installed Notebook multi-kernels

```
jupyter kernelspec list  

```

4. Switch to the configuration directory and add the following configuration to the end of the `jupyter_lab_config.py` file

```
c.NotebookApp.kernel_spec_manager.default_kernel_name = 'ir'  

```

In this case, `ir` is the name of the installed R kernel, which can be replaced with any installed kernel.

Note: After changing the default kernel, you also need to [save the environment as a custom image](/en/docs/software/OtherSoftwares) and connect using the new image, otherwise the configuration will not take effect.

## Sharing Notebooks[​](#sharing-notebooks "标题的直接链接")

Newly created Notebooks are visible only to you by default. To invite others to read or edit, click the "Permissions" button in the top-right corner and share the Notebook with specific users:

![](/en/assets/images/screenshot-20240408-205146-2dd306b0b7c248ccaea3b8a9c2c29368.png)

You can invite specific Bohrium users or all members of a project. When inviting collaborators, you can specify their permission levels, with Bohrium offering **read, edit, and manage** access types.

If you're unsure of the invitee's Bohrium account (e.g., for open lectures or courses) or if they don't have one, enable "**Link Sharing**" so that anyone with the link can read your Notebook.

To share your Notebook with all Bohrium Notebooks users, choose "Public". This makes it searchable by all users and visible on your personal homepage. If your Notebook receives many likes, it may appear on the [Bohrium Notebooks homepage](https://bohrium.dp.tech/notebooks).

When publicly releasing a Notebook, you can:

* **Add Authors**: Add other contributors and determine their ranking by the order added;
* **Add Tags**: Make it easier for users to search and for the platform to recommend related content;
* **Recommend Image and Machine**: Specify an image and machine, and the system will automatically use them when readers run your Notebook. If you recommend a custom image, ensure it doesn't contain private data and is functional;
* **Share Datasets**: If your Notebook references other data or files, create datasets and share them when publishing so readers can access these files when running your Notebook.

![](/en/assets/images/screenshot-20240408-205249-75451b9abb4c920134b8b0f401f3eb28.png)

You can continue to modify publicly released Notebooks, but don't forget to click the "Republish" button to sync the latest content:

![](/en/assets/images/screenshot-20240408-205401-7ec8fce1ec25a68be9650564aa38262d.png)

Note: Only publicly released notebooks need to be republished. Private notebooks don't require this action, as collaborators will always see the latest version after any user edits.

[PreviousDataset](/en/docs/userguide/Dataset/)[NextImages](/en/docs/userguide/image/)

* [What is Notebook?](#what-is-notebook)
* [Creating a Notebook](#creating-a-notebook)
* [Editing a Notebook](#editing-a-notebook)
* [Running Notebooks](#running-notebooks)
  + [Configure Notebook with Multiple Kernels](#configure-notebook-with-multiple-kernels)
* [Sharing Notebooks](#sharing-notebooks)



