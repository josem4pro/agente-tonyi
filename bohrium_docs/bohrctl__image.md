# bohrctl > image

**Source URL:** https://docs.bohrium.com/en/docs/bohrctl/image

---








Image Management Command：image | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/bohrctl/image)
* [English](/en/docs/bohrctl/image)
[Console](https://bohrium.dp.tech/home)

* [Homepage](/en/docs/)
* [Quick Start](#)
* [Command Line（New）](#)
  + [Bohrium CLI](/en/docs/bohrctl/about)
  + [Install Bohrium CLI](/en/docs/bohrctl/install)
  + [Job](/en/docs/bohrctl/job)
  + [Job group management](/en/docs/bohrctl/job_group)
  + [Node management](/en/docs/bohrctl/node)
  + [Machine configuration](/en/docs/bohrctl/machine)
  + [Dataset management](/en/docs/bohrctl/dataset)
  + [Image management](/en/docs/bohrctl/image)
  + [Project management](/en/docs/bohrctl/project)
* [Command Line](#)
* [Best Practice](#)
* [User Guide](#)
* [Softwares](#)
* [FAQ](#)
* [More Help](/en/docs/MoreHelp)
* [Extensions](#)


* Command Line（New）
* Image management
# Image Management Command：image

## List all images：list[​](#list-all-imageslist "标题的直接链接")

Command Entry:

`bohr image list`

Summary:

```
Usage:  
  bohr image list [flags]  
  
Aliases:  
  list, -ls  
  
Flags:  
      --csv           output with CSV format  
  -h, --help          help for list  
      --json          output with JSON format  
      --noheader      does not print header information  
  -t, --type string   type of the image.eg: bohr image list -t "DeePMD-kit" (default: custom image)  
      --yaml          output in YAML format  
  

```

Parameter description:

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --type | -t | specify the image type (default: custom image) | 否 |

--type -t Example of image types."

```
bohr image list -t "Basic Image"  
bohr image list -t "DeePMD-kit"  
bohr image list -t "DPGEN"  
bohr image list -t "ABACUS"  
bohr image list -t "CP2K"  
bohr image list -t "LAMMPS"  
bohr image list -t "GROMACS"  
bohr image list -t "CALYPSO"  
bohr image list -t "Quantum Espresso"  
bohr image list -t "Uni-Mol"  
bohr image list -t "TBPLaS"  
bohr image list -t "DPEM"  
bohr image list -t "FEALPy"  
bohr image list -t "Amber"  
bohr image list -t "Third-party software"  

```

Example:

```
bohr image list --json   
# View all custom images in JSON format.  
bohr image list -t "DeePMD-kit"  
# Display all public images under DeePMD-kit (press Ctrl+C to exit).  

```

![image list](/en/assets/images/WX20240925-180213-9fff15b516a13e74bb13d94aa12f74d5.png)

## Pull the image to local.： pull[​](#pull-the-image-to-local-pull "标题的直接链接")

Only Bohrium’s public and your own custom images can be pulled (shared images from others are not supported).

Command Entry：

`bohr image pull`

Summary：

```
Usage:  
  bohr image pull [flags]  
  
Aliases:  
  pull, -pull  
  
Flags:  
  -h, --help                   help for pull  
  -i, --image_address string   image_address of Bohrium  

```

Parameter description：

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --image\_address | -i | image\_address of Bohrium | yes |

案例：

```
bohr image pull  registry.dp.tech/dptech/deepmd-kit:3.0.0b3-cuda12.1  
# Pull the public image deepmd-kit:3.0.0b3-cuda12.1 to the local Docker  

```
Attention

Before running the `bohr image pull` command, you need to start the Docker daemon. The simplest way is to open the Docker client (such as Docker Desktop).

![image pull](/en/assets/images/WX20240926-162934-a5d2d422ba0552012427df87a546d1af.png)

## Delete the private image.：delete[​](#delete-the-private-imagedelete "标题的直接链接")

Command Entry:

`bohr image delete`

Summary:

```
Usage:  
  bohr image delete <imageId>... [flags]  
  
Flags:  
  -h, --help           help for delete  
      --imageId ints   imageId(s) (can be used multiple times)  

```

Parameter description：

| Parameter | Abbreviation | Description | Required |
| --- | --- | --- | --- |
| --imageId | - | imageId | yes |

Example:

```
bohr image delete 123 234  
# Delete the private images with IDs 123 and 234.  

```
[PreviousDataset Management Command：dataset](/en/docs/bohrctl/dataset/)[NextProject Management Command：project](/en/docs/bohrctl/project/)

* [List all images：list](#list-all-imageslist)
* [Pull the image to local.： pull](#pull-the-image-to-local-pull)
* [Delete the private image.：delete](#delete-the-private-imagedelete)



