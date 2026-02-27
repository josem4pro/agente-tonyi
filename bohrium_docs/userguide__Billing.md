# userguide > Billing

**Source URL:** https://docs.bohrium.com/en/docs/userguide/Billing

---








Top-up and Billing | Bohrium Docs


[跳到主要内容](#)Documentation[![Bohrium docs Logo](https://cdn1.deepmd.net/bohrium/web/images/8c4ab8c9/home-nav-en.png)](https://www.bohrium.com/)[Documentation](/en/docs)[English](#)

* [简体中文](/docs/userguide/Billing)
* [English](/en/docs/userguide/Billing)
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
* Billing
# Top-up and Billing

This article introduces the top-up, refund process, how to check the bill, billing items, and arrears instructions for Bohrium.

## How to top-up an account?[​](#how-to-top-up-an-account "标题的直接链接")

Bohrium currently supports small amount self-service top-up, the top-up amount is less than or equal to 20000 yuan, you can top-up in the system. For amounts over 20000 yuan, you need to top-up through a public transfer. Please contact the sales or send an email to bohrium. Click on the account name at the top of the page to enter the [Expenses](https://bohrium.dp.tech/consume) page, and you can see the "Top-up" entrance in the figure.

![top-up Entrance](/en/assets/images/screenshot-20240409-185830-cd9e625498eeb8d10e418c5ccbd99e6d.png)

1. Click "Top-up" to enter the top-up page, enter the amount you want to top-up and select the corresponding top-up channel (currently supports Alipay \ WeChat \ PayPal) to submit.

![top-up Page](/en/assets/images/screenshot-20240409-192844-63d610568c153c64e8ef50056ccf83b5.png)

1. Scan the QR code displayed on the page with your mobile phone to complete the top-up. Subsequently, you can check your account balance in the "Expenses" page.

**Note**: If there is an arrears in your account, the top-up will be used to deduct the arrears amount first.

1. After the balance is consumed, an invoice can be issued for the actual amount. If you need an invoice, please contact the sales staff or send an email to bohrium.

## How to request an Invoice?[​](#how-to-request-an-invoice "标题的直接链接")

After consuming the balance of your recharge, you can request an invoice based on the actual amount spent. Simply click the "Apply for Invoice" button on the Expenses page, select the consumption record you wish to invoice, and fill in the invoice information. Then, submit your invoice request. We will process your request and issue the invoice within 15 working days of receiving your application (there may be delays in special circumstances).

![Apply for Invoice](/en/assets/images/screenshot-20240409-194917-8255f5100e08e6bd2cb964992945ffeb.png)

For overseas (including Hong Kong, Macao, Taiwan, and other countries) paper invoice mailing, please contact us via email: [zhangxiaonan@dp.tech](mailto:zhangxiaonan@dp.tech).

## How to refund?[​](#how-to-refund "标题的直接链接")

If there is an unconsumed balance in your account that needs to be refunded, please contact us via WeChat Work at 17710231129, and we will process it as soon as possible.

**Note**: If the balance includes experience card given by Bohrium, it cannot be withdrawn.

## How to check the bill[​](#how-to-check-the-bill "标题的直接链接")

Click the "Bill" button on the page to view your bill details:

![Billing Statement Page](/en/assets/images/screenshot-20240409-195251-f4f26d2dbc437d3bd45649b40f7841bc.png)

You can filter your bills by date range, consumption type, project, user, and more. For more detailed information such as job IDs and specific start and end times, you can click the "Download Detailed Bill" button in the top right corner of the table, and we will send the more detailed bill information to your email.

**Note**:

1. The consumption of **projects you created** and **projects you only participate in** are listed under two separate tabs, which you can switch to view.
2. The account balance is deducted **every 5 minutes**, which means that even if you have incurred expenses within 5 minutes between two deductions, the account balance will not change temporarily.

## Billing Items and Prices[​](#billing-items-and-prices "标题的直接链接")

| Billing Item | Price |
| --- | --- |
| Computing Resources | Charged based on the duration of computing resources used by the job, the price changes dynamically, subject to the price displayed when selecting the configuration |
| Management Node | The node used to run DP-GEN or create images will be billed based on duration, subject to the price displayed when activating the node |
| Personal Storage Space (/personal) | By default, each user gets 500GB of free storage space, and additional capacity can be purchased if needed. |
| Project Storage Space (/share) | By default, each project comes with 1TB of free storage space, and additional capacity can be purchased for individual projects if needed. |

Different hardware configurations have different unit prices. You can view the latest price information on the "Pricing" page and estimate the total cost of your computing jobs:

![Pricing](/en/assets/images/screenshot-20240409-195656-6fd56ed064da251ed407f11935a55355.png)

**Note**: Nodes will continue to charge after being activated. If not in use, please click the "Stop" or "Delete" button in time to save costs.

## What happens when the purchased storage space expires?[​](#what-happens-when-the-purchased-storage-space-expires "标题的直接链接")

1. If I had previously purchased storage space and later canceled the automatic renewal, how will my purchased storage space be handled after it expires?
   
   After the expiration, the purchased storage capacity will be reclaimed, and the available storage space will revert to the system's default size (500GB for personal storage and 1TB for shared project storage).
   
   * If you have deleted some files within the paid storage space before its expiration, making the total occupied capacity smaller than the free space provided by Bohrium, your files will not be affected.
   * If you have not deleted any files within the paid storage space before its expiration, and the total occupied capacity exceeds the free space provided by Bohrium, **you will have a 30-day grace period to purchase more storage capacity or delete files. If after the 30-day grace period, the total occupied capacity still exceeds the free space provided by Bohrium, all files in that storage space will be deleted.**
     
     + During the grace period, we will periodically send you email or message to remind you to promptly manage your data.
     + During the grace period, you will not be able to write new data to the storage space until you delete enough files to bring the total occupied capacity below the free space provided by Bohrium.
     + To ensure the safety of your data, please promptly manage the files exceeding the capacity after canceling the automatic renewal.
2. If I had previously purchased storage space, but the automatic renewal payment failed, how will my purchased storage space be handled?
   
   In case of a payment failure, you will receive a notification from the system. Please make sure to top-up your account with a sufficient balance within the grace period (30 days) to ensure a successful payment when the system attempts to deduct the fee again.
   
   If you do not recharge your account within the grace period:
   
   * If the total occupied capacity smaller than the free space provided by Bohrium, your files will not be affected.
   * If the total occupied capacity exceeds the free space provided by Bohrium, **all files in that storage space will be deleted.**
     
     + During the grace period, we will periodically send you email or message to remind you to promptly manage your data.
     + During the grace period, you will not be able to write new data to the storage space until you delete enough files to bring the total occupied capacity below the free space provided by Bohrium.
     + To ensure the safety of your data, please promptly manage the files exceeding the capacity after canceling the automatic renewal.

## Arrears Instructions[​](#arrears-instructions "标题的直接链接")

When the balance of your Bohrium account falls below the alert threshold you have set (the default threshold is ￥100 ), we will send a reminder email to your registered email address, reminding you to top-up in time. When your account balance is zero, you will not be able to submit new jobs.

[PreviousImages](/en/docs/userguide/image/)[NextQuota Limits](/en/docs/userguide/QuataLlimit/)

* [How to top-up an account?](#how-to-top-up-an-account)
* [How to request an Invoice?](#how-to-request-an-invoice)
* [How to refund?](#how-to-refund)
* [How to check the bill](#how-to-check-the-bill)
* [Billing Items and Prices](#billing-items-and-prices)
* [What happens when the purchased storage space expires?](#what-happens-when-the-purchased-storage-space-expires)
* [Arrears Instructions](#arrears-instructions)



