# bohrctl > install

**Source URL:** https://docs.bohrium.com/en/docs/bohrctl/install

---








Install Bohrium CLI | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/bohrctl/install)
* [English](/en/docs/bohrctl/install)
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
* Install Bohrium CLI
# Install Bohrium CLI

## Preparation[​](#preparation "标题的直接链接")

Before you begin, please make sure you have registered a Bohrium account. If you have not registered yet, please visit the [Bohrium official website](https://bohrium.dp.tech/) to sign up.

## Install[​](#install "标题的直接链接")

### linux Version[​](#linux-version "标题的直接链接")

Use **curl** to download:

```
/bin/bash -c "$(curl -fsSL https://dp-public.oss-cn-beijing.aliyuncs.com/bohrctl/1.0.0/install_bohr_linux_curl.sh)"  

```
### macOS Version[​](#macos-version "标题的直接链接")

Use **curl** to download:

```
/bin/bash -c "$(curl -fsSL https://dp-public.oss-cn-beijing.aliyuncs.com/bohrctl/1.0.0/install_bohr_mac_curl.sh)"  

```
### Windows Version[​](#windows-version "标题的直接链接")

Use **curl** to download:

```
curl -o install_bohr_windows_wget.bat https://dp-public.oss-cn-beijing.aliyuncs.com/bohrctl/1.0.0/install_bohr_windows_curl.bat && install_bohr_windows_wget.bat  

```
Attention

Since the environment variables have been set, you need to reopen the command prompt for the changes to take effect.

## Configure Account Information[​](#configure-account-information "标题的直接链接")

Please visit [Bohrium-AccessKey](https://bohrium.dp.tech/settings/user/) to generate an AccessKey （**Recreating the AccessKey will cause the original one to become invalid.**）

![ACCESS_KEY值](/en/assets/images/20240605-112347-5909c8064c9851ad1616d71fd74f43a1.png)

After obtaining the ACCESS\_KEY value, configure the environment variables for ACCESS\_KEY as follows:

> Note: Please replace the `XXXX` after `ACCESS_KEY` with your own AccessKey.

**ZSH**

If you are using ZSH, use the following command to write the `ACCESS_KEY` into `~/.zshrc`.

```
echo 'export ACCESS_KEY=XXXX' >> ~/.zshrc  
source ~/.zshrc  

```

**BASH**

If you are using ZSH, use the following command to write the `ACCESS_KEY` into `~/.bashrc`.

```
echo 'export ACCESS_KEY=XXXX' >> ~/.bashrc  
source ~/.bashrc  

```

**Windows**

Open Command Prompt (CMD) and run the following commands (note that the setx command requires reopening the Command Prompt to take effect):

```
setx ACCESS_KEY XXXX  

```

Alternatively, you can manually add these variables through the system settings.

[PreviousIntroduction to the Bohrium CLI](/en/docs/bohrctl/about/)[NextJob Management Commands：job](/en/docs/bohrctl/job/)

* [Preparation](#preparation)
* [Install](#install)
  + [linux Version](#linux-version)
  + [macOS Version](#macos-version)
  + [Windows Version](#windows-version)
* [Configure Account Information](#configure-account-information)



