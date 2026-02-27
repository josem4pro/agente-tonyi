# userguide > FileManage

**Source URL:** https://docs.bohrium.com/en/docs/userguide/FileManage

---








File Management | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/userguide/FileManage)
* [English](/en/docs/userguide/FileManage)
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
* File Management
# File Management

This article introduces how to manage files on Bohrium.

Click the `Files` button on the left sidebar of Bohrium to enter the **File Management** interface:

![文件管理](/en/assets/images/file-f6f81e7a539778d0a2ad2d01f9fd52d0.png)

On this page, you can perform basic operations such as **uploading, downloading, moving, copying, renaming, and deleting** files in the `/personal` disk of the node. Additionally, you can **preview and edit online** both **text files** and **structured files**.

The file types and operations supported by Bohrium are detailed in the table below:

| **File Types** | **File Formats** | **Supported Operations** |
| --- | --- | --- |
| Structured Files | POSCAR, CONTCAR, CIF, XYZ | Online preview and edit |
| dump, lammpstrj, pdb, sdf, mol, mol2 | Online preview |
| Text Files | PY, CPP, JSON, LOG, XML, TXT and most other text formats | Online preview and edit |
| Image Files | JPEG, PNG, BMP, GIF, SVG | Online preview |

The recognition rules adopted by Bohrium for identifying structural files are as follows:

* VASP Structure File Recognition
  
  + Files with the uppercase **POSCAR** or **CONTCAR** in the filename.
  + Files with the suffixes **poscar**, **contcar**, or **vasp**.
* LAMMPS Trajectory File Recognition
  
  + Files with the suffixes **dump** or **lammpstrj**.
  + Files with the prefix **lammpstrj**.
* Recognition of Other Structural Files
  
  + Files with the suffixes **cif**, **pdb**, **sdf**, **mol**, **mol2**, or **xyz**.

## File download and upload[​](#file-download-and-upload "标题的直接链接")

### Download[​](#download "标题的直接链接")

**Select the file** in the Bohrium directory tree, and right-click `Download` to download the file from the `/personal` disk to your local computer.

![文件下载](/en/assets/images/file_download-d898c5798d28d96ec512fb5c1dbbf6e4.png)

### Upload[​](#upload "标题的直接链接")

On Bohrium, you can upload local files or folders to the `/personal` disk using three methods:

1. Click the `Upload` button to upload files and folders

![按钮](/en/assets/images/file_upload_button-8bba1dcb51f4d2f952be2f1d7145853b.png)

2. **Select the folder** in the directory tree and right-click `Upload`

![文件上传](/en/assets/images/file_upload-6b5faa369ea17ba69cc6731094bde541.png)

3. Drag and drop files or folders directly to the **/personal directory tree** to upload

![拖拽上传](/en/assets/images/file_upload_drag-1b78f03308128d9516ed8cd65123359a.png)

## Structured file visualization[​](#structured-file-visualization "标题的直接链接")

### Online preview[​](#online-preview "标题的直接链接")

For structural files such as POSCAR, dump, xyz, and mol2, double-click the desired file in the directory tree on the left side of the Bohrium file management page to conveniently and quickly preview the structure.

![结构文件预览](/en/assets/images/structure_preview-ec1ff242d438d1737e0b4ab1acea9e9e.png)

In preview mode, you can view the lattice information of the structure. Additionally, you can **translate** and **rotate** the structure by **holding Ctrl while dragging the mouse** and **simply dragging the mouse**, respectively.

When the **mouse hovers** over an atom, the **element name and coordinates** of the atom will be displayed. After **clicking** to select the atom, its information will also be displayed in the structure information column on the right.

![选中原子后的结构预览](/en/assets/images/atom_select-18df9cfef00cd7b4e334645e77fd951b.png)

### Online edit[​](#online-edit "标题的直接链接")

Specifically, for **POSCAR, CONTCAR, CIF, and single-frame structured XYZ format files**, Bohrium now supports online editing of these structured files.

Click the slider on the left side of `Start editing` to enter editing mode, and then you can edit the structure file online. After editing, click the slider again to `Save the file and finish editing`.

In edit mode, you can modify the lattice size, add atom, edit atom and delete atom in the structure file.

#### Edit lattice[​](#edit-lattice "标题的直接链接")

In edit mode, click the edit icon located to the right of **Lattice** to modify the size of the lattice.

![编辑晶格](/en/assets/images/edit_lattice-784f59428bd145d4740d941c322e71fc.png)

> Note: When editing the lattice, the distance between atoms will also be scaled proportionally.

#### Add atom[​](#add-atom "标题的直接链接")

In edit mode, click **Add Atom** in the structure information column on the right. Select an atom from the periodic table and enter its Cartesian or fractional coordinates to add the atom to the structure file.

![增加原子](/en/assets/images/add_atom-05efa8b0a3c0fb93792e35d32a80246e.png)

#### Edit Atom[​](#edit-atom "标题的直接链接")

In edit mode, after selecting an atom to be edited, click the **Edit** icon in the atom information column to modify the atom type and coordinates.

![编辑原子](/en/assets/images/edit_atom-901f600ff7af477637bf0ccdece0588f.png)

#### Delete atom[​](#delete-atom "标题的直接链接")

In edit mode, after selecting an atom to be edited, click the **Delete** icon in the atom information column or press the **Del** key to delete the atom.

[PreviousBohrium Web Shell](/en/docs/userguide/WebShell/)[NextDataset](/en/docs/userguide/Dataset/)

* [File download and upload](#file-download-and-upload)
  + [Download](#download)
  + [Upload](#upload)
* [Structured file visualization](#structured-file-visualization)
  + [Online preview](#online-preview)
  + [Online edit](#online-edit)



