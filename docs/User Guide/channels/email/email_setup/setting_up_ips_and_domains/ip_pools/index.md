# Set up IP pools and IP addresses

> This page covers how to create your own dedicated IP pools and add IP addresses to them in Braze. Use the sender profile questionnaire to get a recommended setup based on your sending volume, or set up your IP pools manually.

An IP pool is a group of dedicated IP addresses that you send email from. Separating your email into IP pools, such as one for marketing email and one for transactional email, protects the sending reputation of each type of email. For example, a spike in marketing volume doesn't affect the deliverability of your password reset emails. Domains that send from the same IP pool share its sending reputation.

## Prerequisites

To set up IP pools and IP addresses, you need:

- Amazon SES as your email service provider (ESP)
- Verified domains in your Braze contract
- Dedicated IP addresses in your Braze contract
- The "Edit Domain Settings" company-level permission

Users without the "Edit Domain Settings" permission can view IP pools and IP addresses, but can't create IP pools, add IP addresses, or delete IP pools.

If your company doesn't have an Amazon SES email sending account yet, the **Sender Verification** page shows **Set up account** instead of the questionnaire or your IP pools. Select **Set up account** to create your sending account, then continue with the steps on this page.

### How your IP address limit works

The number of dedicated IP addresses you can use is set by your contract and applies across your company, including all workspaces. Every IP address you add to any IP pool counts toward this limit. When you reach it, you can't create new IP pools or add IP addresses. To request more IP addresses, contact [Braze Support](https://www.braze.com/docs/user_guide/administer/personal/braze_support).

If Braze set up IP pools for your company before you had access to this feature, you see your existing IP pools and IP addresses on the **Sender Verification** page. You can create more IP pools or add IP addresses as long as IP addresses remain on your contract.

## Option 1: Use the sender profile questionnaire (recommended)

The sender profile questionnaire asks about how you send email and recommends how many IP pools and IP addresses to set up. If you don't have any IP pools yet, the questionnaire appears when you open the **Sender Verification** page.

### Step 1: Choose your use case

1. Go to **Settings** > **Email Self Serve** under **Company Settings**.
2. For **What's your primary email use case?**, select one of the following:

| Use case | Select this if | IP pools created |
| --- | --- | --- |
| **Marketing and Transactional** | You want to separate your marketing and transactional email. | One marketing IP pool and one transactional IP pool. |
| **Sending different business units** | You send on behalf of different brands, business units, or regions, and want to manage the sending reputation of each one separately. | One marketing IP pool for each business unit. You can also add transactional IP pools in the next step. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="IP pool use cases" }

If both use cases apply, select the one that represents most of your sending volume.

### Step 2: Name your IP pools and enter your sending volume

The questions you answer depend on the use case you selected.




1. Enter a name for your marketing IP pool and your transactional IP pool. The default names are `marketing` and `transactional`.
2. Under **Marketing**, answer whether you expect to send more than 2 million marketing emails per day on peak days, such as Black Friday. If you select **Yes**, enter your expected peak daily sending volume in millions as a whole number, such as `5` for 5 million.
3. Under **Transactional**, answer the same question for your transactional email.




1. Enter a name for each business unit. To add another business unit, select **Add**. You can add up to 10 business units.
2. Answer whether you expect to send more than 2 million marketing emails per day for each business unit on peak days, such as Black Friday. If you select **Yes**, enter your expected peak daily sending volume for each business unit in millions.
3. For **Do you have any transactional emails?**, select **Yes** or **No**.
4. If you send transactional email, select whether you separate your transactional email for each business unit:
    - **Yes:** Each business unit gets its own transactional IP pool. Answer the peak volume questions for each business unit's transactional email.
    - **No:** All business units share one transactional IP pool. Answer the peak volume questions for your overall transactional email.

Braze names each IP pool after its business unit. For example, a business unit named `brand_a` gets an IP pool named `brand_a_marketing`, plus `brand_a_transactional` if each business unit has its own transactional IP pool. A shared transactional IP pool is named `transactional`.




After you've answered every question, select **Get results**. Name each IP pool according to the [IP pool naming rules](#ip-pool-naming-rules).

### Step 3: Review the recommendation

The **Sender profile recommendation** shows the IP pools Braze recommends and the number of IP addresses in each one. Braze calculates the number of IP addresses for each IP pool as follows:

| Your answer for the IP pool | Recommended IP addresses |
| --- | --- |
| No peak days over 2 million emails | 1 |
| Peak days over 2 million emails | Your peak daily volume in millions, divided by 2 and rounded up |
{: .reset-td-br-1 .reset-td-br-2 aria-label="IP addresses recommended per IP pool" }

As a best practice, Braze recommends sending no more than 2 million emails per day from each IP address to protect its sending reputation. The recommendation follows this guideline and rounds up so your IP pools can handle peak days. If you add IP addresses later, you need to [warm](https://www.braze.com/docs/user_guide/channels/email/email_setup/ip_warming) the new IP addresses before they can send at full volume.

For example:

| Answers | Recommendation |
| --- | --- |
| Marketing and Transactional. Marketing peaks at 5 million emails per day. Transactional doesn't exceed 2 million per day. | 2 IP pools with 4 IP addresses: 3 in `marketing` and 1 in `transactional` |
| Three business units, each peaking at 4 million marketing emails per day. One shared transactional IP pool that doesn't exceed 2 million per day. | 4 IP pools with 7 IP addresses: 2 in each business unit's marketing IP pool and 1 in `transactional` |
| The same three business units, each with its own transactional IP pool that doesn't exceed 2 million per day | 6 IP pools with 9 IP addresses |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Example recommendations" }

From the recommendation, you can:

- Select **Apply recommendation** to create the recommended IP pools and IP addresses.
- Select **Edit responses** to change your answers. Your previous answers are kept.
- Select **Set up manually** to [create IP pools yourself](#option-2-set-up-ip-pools-manually). The recommendation is discarded.

#### If your contract doesn't have enough IP addresses

If the recommendation needs more IP addresses than remain on your contract, Braze tells you how many it needs and how many remain. You can contact [Braze Support](https://www.braze.com/docs/user_guide/administer/personal/braze_support) to request more IP addresses, or [set up your IP pools manually](#option-2-set-up-ip-pools-manually) within your current limit.

### Step 4: Apply the recommendation

Before you apply, review the IP pool names and the number of IP addresses in each IP pool. You can't rename an IP pool, and after IP addresses are added to an IP pool, you can't remove them.

Select **Apply recommendation**. Braze creates your IP pools and adds IP addresses to them, which can take a few minutes. You can leave the page while setup runs. When setup finishes, your IP pools appear on the **Sender Verification** page.

If Braze can't finish setting up some of your IP pools, a message lists which IP pools need attention and what to do next, such as creating an IP pool manually, choosing a different name, or adding IP addresses. For more information, see [Troubleshooting](#troubleshooting).

**Note:**


The questionnaire doesn't save your answers until you select **Apply recommendation**. If you refresh or leave the page before then, you need to answer the questions again.



## Option 2: Set up IP pools manually

If you already know the IP pool setup you want, you can skip the questionnaire.

1. Go to **Settings** > **Email Self Serve** under **Company Settings**.
2. Select **Skip questionnaire**, then select **Proceed**.

### Step 1: Create an IP pool

1. Select **Add IP pool**.
2. Enter an IP pool name that follows the [IP pool naming rules](#ip-pool-naming-rules). Name the IP pool after the type of email it sends, such as `marketing` or `transactional`.
3. Select **Save IP pool**.

You can only create an IP pool when IP addresses remain on your contract. If none remain, **Add IP pool** is unavailable.

### Step 2: Add IP addresses

1. On the IP pool, select **Add IP addresses**. The **Add IP addresses** window shows how many of your contract's IP addresses are assigned.
2. Enter the number of IP addresses to add. As a best practice, plan for no more than 2 million emails per day for each IP address, and account for seasonal peaks.
3. Select **Add**, then select **Confirm**.

Braze assigns IP addresses from its available dedicated IP addresses. You can't choose specific IP addresses.

**Important:**


After you add IP addresses to an IP pool, you can't remove them or move them to another IP pool. Before you confirm, check that you're adding the correct number of IP addresses to the correct IP pool.



## Manage IP pools and IP addresses

### View IP addresses

To see the IP addresses in an IP pool, select **View IP addresses** on that IP pool. From this list, you can also select **Add IP addresses** to add more.

### Delete an IP pool

To delete an IP pool, select <i class="fas fa-trash-can" title="Delete"></i> on the IP pool. You can only delete an IP pool that has no IP addresses and no domains, such as an IP pool you created by mistake before adding IP addresses.

## Considerations

- You can't rename an IP pool after you create it.
- You can't remove an IP address from an IP pool or move it to another IP pool. Because of this, you can't delete an IP pool that has IP addresses. If you added IP addresses by mistake, contact [Braze Support](https://www.braze.com/docs/user_guide/administer/personal/braze_support).
- This feature is available for Amazon SES only. If you use SendGrid or SparkPost, contact [Braze Support](https://www.braze.com/docs/user_guide/administer/personal/braze_support) to set up IP pools and IP addresses.

### IP pool naming rules

IP pool names can contain only lowercase letters, numbers, hyphens (`-`), and underscores (`_`). Each name must be unique across your company. Names have a maximum length, and Braze shows an error if a name is too long.

## Next steps

After your IP pools have IP addresses:

1. If you haven't already, [add a verified domain](https://www.braze.com/docs/user_guide/channels/email/email_setup/setting_up_ips_and_domains/verified_domains). The **Sender Verification** page shows a reminder until you have one.
2. [Add sending and tracking domains](https://www.braze.com/docs/user_guide/channels/email/email_setup/setting_up_ips_and_domains/email_self_serve) to each IP pool.
3. [Warm your IP addresses](https://www.braze.com/docs/user_guide/channels/email/email_setup/ip_warming) so mailbox providers learn to trust them.

## Troubleshooting

| Message | What it means | What to do |
| --- | --- | --- |
| Only _N_ dedicated IP addresses are left on your contract. | Your request uses more IP addresses than remain on your contract. | Request fewer IP addresses, or contact Braze Support to request more. |
| Some IP pools couldn't be created. | Braze created some of your IP pools but couldn't finish others. | Follow the instructions in the message to create the remaining IP pools manually, rename them, or add their IP addresses. |
| Your IP pools are already being set up. | A previous setup is still running. | Wait a few minutes, then refresh the page. |
| We couldn't set up your IP pools. | Setup failed before any IP pools were created. | Try again later. If the problem continues, contact Braze Support. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="IP provisioning error messages" }

### Add IP pool is unavailable

**Add IP pool** is unavailable when your company has no dedicated IP addresses left. Either your contract doesn't include dedicated IP addresses, or every IP address on your contract is in use. To request more IP addresses, contact [Braze Support](https://www.braze.com/docs/user_guide/administer/personal/braze_support).

If you don't see **Add IP pool** at all, your company might not have an Amazon SES sending account yet. In that case, the page shows **Set up account** instead. For more information, see [Prerequisites](#prerequisites).

## Frequently asked questions

### How many IP addresses do I need?

As a best practice, Braze recommends sending no more than 2 million emails per day from each IP address, based on your busiest day. Size your IP pools for peak days, such as Black Friday, instead of your average day. Every IP address you add later needs to be warmed. The sender profile questionnaire applies this guideline for you.

### Why can't I remove an IP address from an IP pool?

An IP address's sending reputation stays with it. To protect that reputation, IP addresses stay in the IP pool you add them to. If you need an IP address moved or removed, contact [Braze Support](https://www.braze.com/docs/user_guide/administer/personal/braze_support).

### Can I choose which IP addresses I get?

No. Braze assigns IP addresses from its available dedicated IP addresses.

### Do IP pools apply to all my workspaces?

Yes. IP pools and your IP address limit apply across your company. You choose which workspaces can use each sending domain when you [add your domains](https://www.braze.com/docs/user_guide/channels/email/email_setup/setting_up_ips_and_domains/email_self_serve).
