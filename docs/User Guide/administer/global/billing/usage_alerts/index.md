# Usage alerts

> When usage alerts are enabled for your company, dashboard users are alerted through banners, emails, or both when Action Credit consumption crosses fixed thresholds during your current credits period. Alerts use the same usage data as the [Credits Usage dashboard](https://www.braze.com/docs/user_guide/administer/global/billing/credits_usage).




**Important:**


 is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.





## About usage alerts

Usage alerts are proactive emails and banners about total Action Credit consumption across channels and products that draw from your contract allotment. They don't pause messaging, change limits, or replace the [Credits Usage dashboard](https://www.braze.com/docs/user_guide/administer/global/billing/credits_usage).

### Emails

Each email shows:

- The threshold you've reached (50%, 75%, 90%, or 100% of your allotment for the current credits period)
- Your credits allotment for that period
- A channel-level breakdown (channel name, credits used, and percent of allotment used per channel)
- A **View usage** link to the Credits Usage dashboard in the dashboard

Below 100%, the email states that messaging continues as normal and no action is required. At 100%, the email still confirms that messaging continues; additional usage through the end of the period may be billed as overage according to your contract.

### Banners

The Credits Usage **Overview** tab shows a banner at 90% or higher usage.

## Who receives alerts

Alerts go to dashboard users who have the workspace-level "View Billing Details" permission. Braze doesn't maintain a separate billing contact list for these emails.

Grant or revoke the "View Billing Details" permission in [Company Users](https://www.braze.com/docs/user_guide/administer/global/user_management/manage_company_users) to add or remove alert recipients. For what the permission includes, see [permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions).

Your Braze account team may receive a copy of the email when Braze has account team contact information on file.

## When alerts send

| Topic | Behavior |
| --- | --- |
| **Thresholds** | 50%, 75%, 90%, and 100% of total Action Credit consumption for the current credits period |
| **Frequency** | At most one email per threshold per credits period (not repeated daily at the same tier) |
| **Scope** | Total consumption across channels and products on your credits contract, not per channel |
| **Measurement** | Usage, not pacing. Alerts report how much of the allotment you've consumed; they don't forecast whether you'll stay on track for the full contract term |
| **Credits period** | Evaluated against the allotment for your active **Credits period** (shown in **Credits contract overview** on the Credits Usage dashboard), not a manual date range you select in the dashboard |
| **Multi-workspace accounts** | One alert per Salesforce account per threshold, even if your organization uses multiple Braze clusters or workspaces |
| **Opt out** | Threshold values aren't configurable in the dashboard |
| **Evaluation** | Braze checks usage daily and sends when a threshold is newly reached |
{: .reset-td-br-1 .reset-td-br-2 aria-label="When usage alerts send" }

If your allotment increases during the credits period (for example, after a contract change), usage is measured against the updated allotment. You don't receive another alert for a threshold your usage has already fallen under after a recalculation.

## In-dashboard usage warnings

On the Credits Usage dashboard **Overview** tab, a banner appears when usage is at or above 90% of your credit allotment for the selected period. This in-product warning is separate from email alerts and prompts you to contact your account manager. It isn't tied to the same company enablement as threshold emails.

## Frequently asked questions

### Why am I getting this email? Did something change?

These emails are a new automated status update from Braze. They fire at four consumption thresholds during your credits period. Nothing about your account settings has changed, and you don't need to take action unless you want to review usage on the Credits Usage dashboard.

### Will my sends stop at 100%?

No. Messaging continues at every threshold, including 100%.

### Is this different from API usage alerts?

Yes. [API usage alerts](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts) monitor API request volumes. Usage alerts monitor Action Credit consumption against your contract allotment.

### Can I set different alert thresholds?

Not in this release.

### Where can I see what's driving consumption?

Use the [Credits Usage dashboard](https://www.braze.com/docs/user_guide/administer/global/billing/credits_usage). The **Overview** tab and channel tabs show consumption over time. When available for your account, **Usage by campaign / Canvas** lists volume metrics (such as sends or impressions) per campaign or Canvas for the date range you select.

### My billing contact is wrong. How do I fix it?

Update **View Billing Details** permissions for the users who should (or shouldn't) receive billing-related emails. Braze sends alerts to everyone with that permission, not to a separate billing distribution list.
