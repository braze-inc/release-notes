# Migrate a CNAME custom domain

> If your custom domain still uses a CNAME record, migrate it to A and AAAA records from the domain page in Braze. This update points your domain directly to Braze link infrastructure, which helps protect your shortened links from being blocked or filtered because of other senders' activity on a shared domain.

Plan for about 30 minutes of active work. You may also need to wait up to 24 hours for DNS TTL changes to take effect, and you'll likely need help from someone who manages your DNS (often IT).

**Important:**


While a migration is in progress, you can't select this domain as a subscription group's [Link Shortening Domain](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains#assign-custom-domains-to-subscription-groups) until the reassign step. During migration, you temporarily move subscription groups off the domain and can't use the domain until finishing the migration.



## Before you start

- Confirm you have the company permission ["Edit domain settings"](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions#company-permissions). If you don't see the **SMS/RCS and Messaging Apps Domains** page, contact your company administrator.
- Identify who on your team can update DNS records at your domain provider.
- Choose a temporary link shortening domain for any subscription groups that currently use the domain you're migrating (another custom domain or a Braze-managed domain).

## Start the migration

1. Go to **Company Settings** > **SMS/RCS and Messaging Apps Domains**.
2. Select the custom domain that still uses a CNAME record.
3. In the migration panel tagged **Recommended**, review the time estimate, then select **Start migration**.

Only the steps that apply to your domain are shown. For example, if no subscription groups use the domain, the steps to move and reassign them don't appear, and the migration completes on its own after Braze verifies the new records.

The domain page shows a **Migrating** tag while the migration is in progress. You can cancel the migration until you select **Generate new records**. After that, Braze updates the domain's records and the migration can't be cancelled.

## Move subscription groups off this domain

Open each subscription group that uses the domain and assign a different link shortening domain so sends keep working during the migration. Then return to the domain page and select **Next**.

If any subscription groups still use the domain, the next step is blocked and the groups that need to move are listed. Groups in workspaces you can't access appear as a count—ask a company administrator to reassign those groups.

## Lower your domain wait time

Ask your IT team to set the TTL on the domain's CNAME record to 60 seconds at your DNS provider. A lower TTL helps the later DNS swap take effect quickly.

Your current TTL and the 60-second target are shown. Use **Copy message** to send IT instructions from the domain page, then select the checkbox when IT confirms the TTL is 60 seconds and select **Next**.

Braze re-checks the TTL when you continue. If it's still above 60 seconds, or Braze can't read it, have IT set it to 60 seconds and try again.

## Generate new records

Select **Generate new records**. Braze creates the new records for your domain.

**Note:**


Braze also re-checks subscription groups at this step. If any group still uses the domain, move it off before generating records.



## Update domain settings

Use **Copy message** to send the new records to your IT team. The message tells them when they can start. After that, have them:

1. Delete only the CNAME record for this domain.
2. Add the new records shown in Braze, each with a 60-second TTL.

Make the deletion and additions back to back, ideally within a minute. The domain is unavailable between those changes, including links in messages you've already sent.

Braze verifies the new records automatically. Verification usually finishes in 30–60 minutes. Check the domain page anytime for status. If verification fails, share the error details with IT, fix the records, and Braze checks again after changes are made.

## Reassign subscription groups

After the domain is connected again, move each subscription group back to the migrated domain:

1. Open each subscription group listed on the domain page.
2. Assign the migrated domain as the **Link Shortening Domain**.
3. Return to the domain page and select **Finish migration**. You can also finish first and reassign any remaining groups later.

When the migration completes, select **Back to domain overview**. The **Migrating** tag clears, and the DNS record panel shows the new A and AAAA records.
