## How to export a list of users with dashboard access

Use this workflow to audit users who have access to your Braze dashboard.

1. Download the Security Event report from **Settings** > **Admin Settings** > **Security Settings** > **Security Event Download**.
2. Extract the user emails from the report.
3. For each email, use [GET: Search Existing Dashboard User Account by Email](https://www.braze.com/docs/api/endpoints/scim/get_search_existing_dashboard_user/) to retrieve the user details.
4. If needed, use the returned resource `id` with [GET: Look Up an Existing Dashboard User Account by Resource ID](https://www.braze.com/docs/api/endpoints/scim/get_see_user_account_information/) for additional user details.

For the full SCIM endpoint list, see [SCIM Endpoints](https://www.braze.com/docs/api/endpoints/scim/). For more information about the report source, see [Downloading a security event report](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings/#security-event-report).
