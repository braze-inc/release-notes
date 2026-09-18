## Requirements

Before you start sending emails, there are some things you need. Refer to the following chart to learn more about these requirements. To find where each one lives in the dashboard and who can change it, see the [setup checklist](#setup-checklist).

| Requirement | Description |
|---|---|
| Dedicated IP (Internet Protocol) | A unique internet address provided exclusively to a single hosting account. Dedicated IPs give you control of your email sender reputation. |
| Allowlisted domains | A domain and a subdomain. Allowlisting lets your email pass DKIM and SPF authentication checks. You choose the names. |
| Subdomains | A subdivision of a domain (such as "@news.example.com") within your email address. A subdomain prevents errors that could damage your company's official email reputation. You choose the name, and you can't use a subdomain that's in use outside of Braze. |
| IP pools | A configuration that separates the reputation of different types of email (such as promotional and transactional) so that the reputation of one doesn't affect the other. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## Setup checklist

Email setup spans two areas of the dashboard: domain and IP configuration at the company level, and sending settings at the workspace level. Use this checklist to find each setting and see whether you can change it yourself.

For production email setup, go to **Settings** > **Email Self Serve** under **Company Settings**. The page uses the **Sender Verification** heading. **Settings** > **Sender Verification** is for trial email setup only, not production sending.

| Task | Where to find it | You can do this yourself | Contact Braze for this |
|---|---|---|---|
| Publish SPF and DKIM records | There's no separate SPF or DKIM settings page. Delegate your subdomain at **Settings** > **Verified Domains**, then add sending and tracking domains in **Email Self Serve**. | Add the NS records (and TXT verification record during initial setup) at your DNS provider. Braze verifies delegation automatically and manages SPF and DKIM for your sending and tracking domains. | Verification keeps failing after you confirm your DNS records are correct. |
| Find your sending IP addresses | **Settings** > **Email Self Serve** under **Company Settings**. Expand an IP pool to see the addresses assigned to it. | View your addresses. | Add or edit IP addresses, or get your first dedicated IPs. |
| Configure IP pools | Your domain setup page, listed by pool name and address count. | View your pools and attach sending and tracking domains to them. | Create a pool, or change how your domains map to your pools. |
| Add sending and tracking domains | **Verified Domains** > **Add custom domain** (then **Email Self Serve**), or **Email Self Serve** > **Start setup**. | Add and verify domains after your IP pool, IP addresses, and verified domain are in place. Requires the "Edit Domain Settings" company-level permission. | Delete a domain, raise your domain limit, or repair NS records that stopped resolving. |
| Set BCC addresses | **Settings** > **Workspace Settings** > **Email Preferences** > **Sending Configuration**. | Add BCC addresses, set a default, and require a BCC address on all email campaigns. | The **BCC Address** section doesn't appear in your workspace. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Email setup checklist" }

For the steps behind each task, see [Set up IPs and domains](https://www.braze.com/docs/user_guide/channels/email/email_setup/setting_up_ips_and_domains) and [Verified domains](https://www.braze.com/docs/user_guide/channels/email/email_setup/setting_up_ips_and_domains/verified_domains). To understand what each DNS record does, see [Email authentication](https://www.braze.com/docs/user_guide/channels/email/email_setup/authentication) and [Understanding DNS records](https://www.braze.com/docs/user_guide/channels/email/email_setup/setting_up_ips_and_domains/understanding_dns_records). For BCC behavior and billing, see [Email preferences](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/email_preferences#outbound-email-settings).

To reach Braze for the items in the last column, see [Braze Support](https://www.braze.com/docs/user_guide/administer/personal/braze_support).

## IP warming

**Important:**


IP warming is the most important step in the email setup process. Though it is not your first step (it's actually the last), we're calling it out here to let you know that you must warm up your IP address, or else any emails you send are sent to spam or are subject to other send barriers.



[IP warming](https://www.braze.com/docs/user_guide/channels/email/email_setup/ip_warming) is when you send a relatively small number of emails out in your first batch, then over time, slightly increase the volume in the following batches until you reach your typical daily volume. This is done at the very end of your email setup process.

By starting with smaller volumes of email, you are establishing a level of trust with your email provider, showing you are only sending emails to relevant users. Sending your first batch of emails to your most engaged users can help you gain trust faster with your provider.

After you're done warming up your IP, you can [start creating and sending emails](https://www.braze.com/docs/user_guide/channels/email/html_editor)!

## Legally required transactional emails







































<br><br>
