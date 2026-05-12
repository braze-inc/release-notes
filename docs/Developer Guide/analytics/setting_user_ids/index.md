# Set user IDs

> Learn how to set user IDs through the Braze SDK. These are unique identifiers that let you track users across devices and platforms, import their data through the [user data API](https://www.braze.com/docs/developer_guide/rest_api/user_data/#user-data), and send targeted messages through the [messaging API](https://www.braze.com/docs/api/endpoints/messaging/). If you don't assign a unique ID to a user, Braze assigns them an anonymous ID instead; however, you can't use these features until you do.

**Note:**


For wrapper SDKs not listed, use the relevant native Android or Swift method instead.



## About anonymous users

After you [integrate the Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/), users who launch your app for the first time will be considered "anonymous" until you call the `changeUser` method and assign them an `external_id`. Once assigned, you can't make them anonymous again. However, if they uninstall and reinstall your app, they will become anonymous again until `changeUser` is called.

If a previously-identified user starts a session on a new device, all of their anonymous activity will automatically sync to their existing profile after you call `changeUser` on that device using their `external_id`. This includes any attributes, events, or history collected during the session on the new device.



### Preventing anonymous user tracking

If your use case requires that no data is collected before a user is identified, you can delay initializing the Braze SDK until the user logs in and an `external_id` is available. Set a flag in your code that flips to `true` when the user signs in, and only initialize the SDK when that flag is set.

**Warning:**


Only delay initialization the **first time** a user downloads your app (before an `external_id` is set). If you prevent the SDK from initializing every time a user signs out or starts a new session, it will interfere with prefetching in-app message and Content Card assets, which can lead to deliverability errors for those campaigns.



## Setting a user ID

To set a user ID, call the `changeUser()` method after the user initially logs in. IDs should be unique and follow our [naming best practices](#naming-best-practices).

If you're hashing a unique identifier instead, be sure to normalize the input of your hashing function. For example, when hashing an email address, remove any leading or trailing spaces and account for localization.



For a standard Web SDK implementation, you can use the following method:

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

If you'd like to use Google Tag Manager instead, you can use the **Change User** tag type to call the [`changeUser` method](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser). Use it whenever a user logs in or is otherwise identified with their unique `external_id` identifier.

Be sure to enter the current user's unique ID in the **External User ID** field, typically populated using a data layer variable sent by your website.

![A dialog box showing the Braze Action Tag configuration settings. Settings included are "tag type" and "external user ID".](https://www.braze.com/docs/assets/img/web-gtm/gtm-change-user.png?a4edbf312c5ba1fa6d32ecdd559361b0)





```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```


```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```







```swift
AppDelegate.braze?.changeUser(userId: "YOUR_USER_ID")
```


```objc
[AppDelegate.braze changeUser:@"YOUR_USER_ID_STRING"];
```





```javascript
BrazePlugin.changeUser("YOUR_USER_ID");
```



```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```



```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```



```javascript
Braze.changeUser("YOUR_USER_ID_STRING");
```



### How `changeUser()` works

When you call `changeUser()`, the following behaviors apply:

- Calling `changeUser()` with the **same** user ID that's already set has no effect on session count.
- Calling `changeUser()` with a **different** user ID automatically ends the current session and starts a new one.
- When an anonymous user calls `changeUser()` with a **new** user ID (one that doesn't exist in Braze yet), the anonymous profile's data is merged into the new identified profile.
- When an anonymous user calls `changeUser()` with an **existing** user ID, the anonymous profile's data is not merged into the identified profile.

**Note:**


Calling `changeUser()` triggers a data flush as part of closing the current user's session. The SDK automatically flushes any pending data for the previous user before switching to the new user, so you don't need to manually request a data flush before calling `changeUser()`.



**Warning:**


Do not assign a single, shared user ID (for example, a static default external ID) or call `changeUser()` when a user logs out. Doing so prevents you from re-engaging any previously logged-in users on shared devices and causes all data to be logged against a single user ID, which can cause other features to not behave as expected. Instead, keep track of all user IDs separately and ensure your app's logout process allows for switching back to a previously logged-in user. When a new session starts, Braze automatically refreshes the data for the newly-active profile.



## User aliases

### How they work

Although anonymous users don’t have `external_ids`, you can assign them a [user alias](https://www.braze.com/docs/user_guide/data/user_data_collection/user_profile_lifecycle/#user-aliases) instead. You should assign a user alias when you want to add other identifiers to the user but don't know what their `external_id` is (for example, they aren't logged in). With user aliases, you also can:

- Use the Braze API to log events and attributes associated with anonymous users
- Use the [External User ID is blank](https://www.braze.com/docs/user_guide/engagement_tools/segments/segmentation_filters#external-user-id) segmentation filter to target anonymous users in your messaging



### Setting a user alias

A user alias consists of two parts: a name and a label. The name refers to the identifier itself, while the label refers to the type of identifier it belongs to. For example, if you have a user in a third-party customer support platform with the external ID `987654`, you can assign them an alias in Braze with the name `987654` and the label `support_id`, so you can track them across platforms.



```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```





```java
Braze.getInstance(context).getCurrentUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```



```kotlin
Braze.getInstance(context).currentUser?.addAlias(ALIAS_NAME, ALIAS_LABEL)
```







```swift
Appboy.sharedInstance()?.user.addAlias(ALIAS_NAME, ALIAS_LABEL)
```



```objc
 [[Appboy sharedInstance].user addAlias:ALIAS_NAME withLabel:ALIAS_LABEL];
```





```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```



```javascript
Braze.addAlias("ALIAS_NAME", "ALIAS_LABEL");
```



## ID Naming best practices {#naming-best-practices}

We recommend that you create user IDs using the [Universally Unique Identifier (UUID)](https://en.wikipedia.org/wiki/Universally_unique_identifier) standard, meaning they are 128-bit strings that are random and well distributed.

Alternatively, you can hash an existing unique identifier (such as a name or email address) to generate your user IDs instead. If you do so, be sure to implement [SDK authentication](https://www.braze.com/docs/developer_guide/sdk_integration/authentication/), so you can prevent user impersonation.

**Warning:**


Do not use a guessable value or incrementing number for your user ID. This may expose your organization to malicious attacks or data exfiltration.

For added security, use [SDK Authentication](https://www.braze.com/docs/developer_guide/sdk_integration/authentication/).



While it's essential that you correctly name your user IDs from the start, you can always rename them in the future using the [`/users/external_ids/rename`](https://www.braze.com/docs/api/endpoints/user_data/external_id_migration/) endpoint.

| ID types not recommended | Example not recommended |
| ------------ | ----------- |
| User's visible profile ID or username | JonDoe829525552 |
| Email Address | Anna@email.com |
| Auto-incrementing user ID | 123 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ID Naming best practices" }

**Warning:**


Avoid sharing details about how you create user IDs, as this may expose your organization to malicious attacks or data exfiltration.


