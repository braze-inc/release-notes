# Debugging the Braze SDK

> Learn how to use the Braze SDK's built-in debugger, so you can troubleshoot issues for your SDK-powered channels, without needing to enable verbose logging in your app.

**Tip:**


For deeper investigation, you can also [enable verbose logging](https://www.braze.com/docs/developer_guide/sdk_integration/verbose_logging) to capture detailed SDK output and [learn how to read verbose logs](https://www.braze.com/docs/developer_guide/sdk_integration/reading_verbose_logs) for specific channels.



## Prerequisites

To use the Braze SDK debugger, you'll need the "View PII" and "View User Profiles (PII Redacted)" granular permissions (or "View User Profiles PII Compliant" legacy permissions). To download your debugging session logs, you'll also need the "Export User Data" permission. Additionally, your Braze SDK needs to meet or point to the following minimum versions: 

<div id='sdk-versions'><a href='/docs/developer_guide/platforms/swift/changelog/#1020' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa-brands fa-apple'></i> &nbsp; Swift: 10.2.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/platforms/android/changelog/#3210' class='sdk-versions--chip android-sdk' target='_blank'><i class='fa-brands fa-android'></i> &nbsp; Android: 32.1.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a></div>

## Debugging the Braze SDK

**Tip:**


To enable debugging for the Braze Web SDK, you can [use a URL parameter](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/initial_sdk_setup/#logging).



### Step 1: Close your app

Before you start your debugging session, close the app that's currently experiencing issues. You can relaunch the app at the start of your session.

### Step 2: Create a debugging session

In Braze, go to **Settings**, then under **Setup and Testing**, select **SDK Debugger**.

![The "Setup and Testing" section with "SDK Debugger" highlighted.](https://www.braze.com/docs/assets/img/sdk_debugger/select_sdk_debugger.png?2387a3520a04597abdb85a9a100baa87)

Select **Create debugging session**.

![The "SDK Debugger" page.](https://www.braze.com/docs/assets/img/sdk_debugger/select_create_debugging_session.png?b8edf96c40967f310493fcb8de32a9de)

### Step 3: Select a user

Search for a user using their email address, `external_id`, user alias, or push token. When you're ready to start your session, select **Select User**.

![The debugging page for the selected user.](https://www.braze.com/docs/assets/img/sdk_debugger/search_and_select_user.png?bab3a4f1e879e4148badff07a76a1385){: style="max-width:85%;"}

### Step 4: Relaunch the app

First, launch the app and confirm that your device is paired. If the pairing is successful, relaunch your app&#8212;this will ensure that app's initialization logs are fully captured.

### Step 5: Complete the reproduction steps

After relaunching your app, follow the steps to reproduce the error.

**Tip:**


When you're reproducing the error, be sure to follow the reproduction steps as closely as possible, so you can create [quality logs](#step-6-export-your-session-logs-optional).



### Step 6: End your session

When you're finished with your reproduction steps, select **End Session** > **Close**.

![The debugging session showing the "End Session" button.](https://www.braze.com/docs/assets/img/sdk_debugger/close_debugging_session.png?1acb6a88b82a111e7d69f7d7ccbd18b5){: style="max-width:85%;"}

**Note:**


It may take a few minutes to generate your logs depending on your session length and network connectivity.



### Step 7: Share or export your session (optional)

After your session, you can export your session logs as a CSV file. Additionally, others can use your **Session ID** to search for your debug session, so you don't need to send them your logs directly.

![The debugging page with "Export Logs" and "Copy Session ID" shown after the session.](https://www.braze.com/docs/assets/img/sdk_debugger/copy_id_and_export_logs.png?6e9b1911ea1e119ed20a667f37ab535a)
