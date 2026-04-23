# Set user attributes

> Learn how to set user attributes through the Braze SDK.

**Note:**


For wrapper SDKs not listed, use the relevant native Android or Swift method instead.





## Prerequisites

Before you can use this feature, you'll need to [integrate the Web Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=web).

## Default user attributes

### Predefined methods

Braze provides predefined methods for setting the following user attributes within the [`User` class](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html):

- First Name
- Last Name
- Language
- Country
- Date of Birth
- Email
- Gender
- Home City
- Phone Number

### Setting default attributes



To set a default attribute for a user, call the `getUser()` method on your Braze instance to get a reference to the current user of your app. Then you can call methods to set a user attribute.



```javascript
braze.getUser().setFirstName("SomeFirstName");
```


```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```


```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```





Using Google Tag Manager, standard user attributes (such as a user's first name), should be logged in the same manner as custom user attributes. Ensure the values you're passing in for standard attributes match the expected format specified in the [User class](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) documentation.

For example, the gender attribute can accept any of the following as values: `"m" | "f" | "o" | "u" | "n" | "p"`. Therefore to set a user's gender as female, create a Custom HTML tag with the following content:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```



### Unsetting default attributes

To unset a default user attribute, pass `null` to the related method. For example:



```javascript
braze.getUser().setFirstName(null);
```


```javascript
braze.getUser().setGender(null);
```


```javascript
braze.getUser().setDateOfBirth(null, null, null);
```



## Custom user attributes

### Setting custom attributes



In addition to the default user attribute methods, you can also set [custom attributes](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) for your users. Full method specifications, see [our JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).



To set a custom attribute with a `string` value:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```



To set a custom attribute with a `integer` value:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_INT_VALUE
);

// Integer attributes may also be incremented using code like the following
braze.getUser().incrementCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  THE_INTEGER_VALUE_BY_WHICH_YOU_WANT_TO_INCREMENT_THE_ATTRIBUTE
);
```



To set a custom attribute with a `date` value:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_DATE_VALUE
);

// This method will assign the current time to a custom attribute at the time the method is called
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date()
);

// This method will assign the date specified by secondsFromEpoch to a custom attribute
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date(secondsFromEpoch * 1000)
);
```




The default and maximum number of elements in an array is 500. You can update the maximum number of arrays in the Braze dashboard, under **Data Settings** > **Custom Attributes**. Arrays exceeding the maximum number of elements are truncated to contain the maximum number of elements.


To set a custom attribute with an `array` value:

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

**Important:**


Dates passed to Braze with this method must be JavaScript Date objects.





**Important:**


Custom attribute keys and values can only have a maximum of 255 characters. For more information about valid custom attribute values, refer to the [reference documentation](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).





Custom user attributes are not available due to a limitation in Google Tag Manager's scripting language. To log custom attributes, create a Custom HTML tag with the following content:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

**Important:**


The GTM template does not support nested properties on events or purchases. You can use the preceding HTML to log any events or purchases that require nested properties.





### Unsetting custom attributes

To unset a custom attribute, pass `null` to the related method.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Nesting custom attributes

You can also nest properties within custom attributes. In the following example, a `favorite_book` object with nested properties is set as a custom attribute on the user profile. For more details, refer to [Nested Custom Attributes](https://www.braze.com/docs/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).

```javascript
import * as braze from "@braze/web-sdk";

const favoriteBook = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  publishing_date: "1937"
};

braze.getUser().setCustomUserAttribute("favorite_book", favoriteBook);
```

### Using the REST API

You can also use our REST API to set or unset user attributes. For more information, refer to [User Data Endpoints](https://www.braze.com/docs/developer_guide/rest_api/user_data/#user-data).

## Setting user subscriptions

To set up a subscription for your users (either email or push), call the functions `setEmailNotificationSubscriptionType()`  or `setPushNotificationSubscriptionType()`, respectively. Both functions take the `enum` type `braze.User.NotificationSubscriptionTypes` as arguments. This type has three different states:

| Subscription Status | Definition |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Subscribed, and explicitly opted in |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Subscribed, but not explicitly opted in |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | Unsubscribed and/or explicitly opted out |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

When a user is registered for push, the browser forces them to choose to allow or block notifications, and if they choose to allow push, they are set `OPTED_IN` by default. 

Visit [Managing user subscriptions](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) for more information on implementing subscriptions and explicit opt-ins.

### Unsubscribing a user from email

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### Unsubscribing a user from push

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```




## Prerequisites

Before you can use this feature, you'll need to [integrate the Android Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=android).

## Default user attributes

### Predefined methods

Braze provides predefined methods for setting the following user attributes within the [`BrazeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html) class. For method specifications, refer to [our KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html).

- First name
- Last name
- Country
- Language
- Date of birth
- Email
- Gender
- Home city
- Phone number

**Note:**


All string values such as first name, last name, country, and home city are limited to 255 characters.



### Setting default attributes

To set a default attribute for a user, call the `getCurrentUser()` method on your Braze instance to get a reference to the current user of your app. Then you can call methods to set a user attribute.




```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setFirstName("first_name");
  }
}
```




```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setFirstName("first_name")
}
```




### Unsetting default attributes

To unset a user attribute, pass `null` to the relevant method.




```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setFirstName(null);
  }
}
```




```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setFirstName(null)
}
```




## Custom user attributes

In addition to the default user attributes, Braze also allows you to define custom attributes using several different data types. For more information on each attribute's segmentation option, see [User data collection](https://www.braze.com/docs/developer_guide/analytics).

### Setting custom attributes



To set a custom attribute with a `string` value:




```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", "your_attribute_value");
  }
}
```




```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", "your_attribute_value")
}
```





To set a custom attribute with an `int` value:




```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE);
    
    // Integer attributes may also be incremented using code like the following:
    brazeUser.incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE);
  }
}
```




```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE)

  // Integer attributes may also be incremented using code like the following:
  brazeUser.incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE)
}
```




To set a custom attribute with a `long` integer value:




```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE);
  }
});
```




```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE)
}
```





To set a custom attribute with a `float` value:




```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE);
  }
});
```




```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE)
}
```




To set a custom attribute with a `double` value:




```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE);
  }
});
```




```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE)
}
```






To set a custom attribute with a `boolean` value:




```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE);
  }
});
```




```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE)
}
```









```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE);
    // This method will assign the current time to a custom attribute at the time the method is called:
    brazeUser.setCustomUserAttributeToNow("your_attribute_key");
    // This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
    brazeUser.setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH);
  }
});
```




```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE)
  // This method will assign the current time to a custom attribute at the time the method is called:
  brazeUser.setCustomUserAttributeToNow("your_attribute_key")
  // This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
  brazeUser.setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH)
}
```




**Warning:**


Dates passed to Braze with this method must either be in the [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format (e.g `2013-07-16T19:20:30+01:00`) or in the `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format (e.g `2016-12-14T13:32:31.601-0800`).






The default and maximum number of elements in an array is 500. You can update the maximum number of arrays in the Braze dashboard, under **Data Settings** > **Custom Attributes**. Arrays exceeding the maximum number of elements are truncated to contain the maximum number of elements. For more information on custom attribute arrays and their behavior, see [Arrays](https://www.braze.com/docs/developer_guide/analytics/#arrays).




```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    // Setting a custom attribute with an array value
    brazeUser.setCustomAttributeArray("your_attribute_key", testSetArray);
    // Adding to a custom attribute with an array value
    brazeUser.addToCustomAttributeArray("your_attribute_key", "value_to_add");
    // Removing a value from an array type custom attribute
    brazeUser.removeFromCustomAttributeArray("your_attribute_key", "value_to_remove");
  }
});
```



```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  // Setting a custom attribute with an array value
  brazeUser.setCustomAttributeArray("your_attribute_key", testSetArray)
  // Adding to a custom attribute with an array value
  brazeUser.addToCustomAttributeArray("your_attribute_key", "value_to_add")
  // Removing a value from an array type custom attribute
  brazeUser.removeFromCustomAttributeArray("your_attribute_key", "value_to_remove")
}
```






### Unsetting custom attributes

To unset a custom attribute, pass the relevant attribute key to the `unsetCustomUserAttribute` method.




```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.unsetCustomUserAttribute("your_attribute_key");
  }
});
```




```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.unsetCustomUserAttribute("your_attribute_key")
}
```




### Nesting custom attributes

You can also nest properties within custom attributes. In the following example, a `favorite_book` object with nested properties is set as a custom attribute on the user profile. For more details, refer to [Nested Custom Attributes](https://www.braze.com/docs/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).



```java
JSONObject favoriteBook = new JSONObject();
try {
  favoriteBook.put("title", "The Hobbit");
  favoriteBook.put("author", "J.R.R. Tolkien");
  favoriteBook.put("publishing_date", "1937");
} catch (JSONException e) {
  e.printStackTrace();
}

braze.getCurrentUser(user -> {
  user.setCustomUserAttribute("favorite_book", favoriteBook);
  return null;
});
```



```kotlin
val favoriteBook = JSONObject()
  .put("title", "The Hobbit")
  .put("author", "J.R.R. Tolkien")
  .put("publishing_date", "1937")

braze.getCurrentUser { user ->
  user.setCustomUserAttribute("favorite_book", favoriteBook)
}
```



### Using the REST API

You can also use our REST API to set or unset user attributes. For more information, refer to [User Data Endpoints](https://www.braze.com/docs/developer_guide/rest_api/user_data/#user-data).

## Setting user subscriptions

To set up a subscription for your users (either email or push), call the functions `setEmailNotificationSubscriptionType()`  or `setPushNotificationSubscriptionType()`, respectively. Both of these functions take the enum type `NotificationSubscriptionType` as arguments. This type has three different states:

| Subscription status | Definition |
| ------------------- | ---------- |
| `OPTED_IN` | Subscribed, and explicitly opted in |
| `SUBSCRIBED` | Subscribed, but not explicitly opted in |
| `UNSUBSCRIBED` | Unsubscribed and/or explicitly opted out |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**Important:**


No explicit opt-in is required by Android to send users push notifications. When a user is registered for push, they are set to `SUBSCRIBED` rather than `OPTED_IN` by default. Refer to [managing user subscriptions](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) for more information on implementing subscriptions and explicit opt-ins.



### Setting email subscriptions




```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType);
  }
});
```




```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType)
}
```




### Setting push notification subscription




```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setPushNotificationSubscriptionType(pushNotificationSubscriptionType);
  }
});
```




```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setPushNotificationSubscriptionType(pushNotificationSubscriptionType)
}
```








## Prerequisites

Before you can use this feature, you'll need to [integrate the Swift Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift).

## Default user attributes

### Supported attributes

The following attributes should be set on the `Braze.User` object:

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `gender`

### Setting default attributes

To set a default user attribute, set the appropriate field on the shared `Braze.User` object. The following is an example of setting the first name attribute:




```swift
AppDelegate.braze?.user.set(firstName: "Alex")
```




```objc
[AppDelegate.braze.user setFirstName:@"Alex"];
```




### Unsetting default attributes

To unset a default user attribute, pass `nil` to the relevant method.




```swift
AppDelegate.braze?.user.set(firstName: nil)
```




```objc
[AppDelegate.braze.user setFirstName:nil];
```




## Custom user attributes

In addition to the default user attributes, Braze also allows you to define custom attributes using several different data types. For more information on each attribute's segmentation option, see [User data collection](https://www.braze.com/docs/developer_guide/analytics/).

**Important:**


Custom attribute values have a maximum length of 255 characters; longer values will be truncated. For more information, refer to [`Braze.User`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class).



### Setting custom attributes



To set a custom attribute with a `string` value:



```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```



```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```





To set a custom attribute with an `integer` value:



```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```



```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```





Braze treats `float` and `double` values the same within our database. To set a custom attribute with a double value:



```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```



```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```





To set a custom attribute with a `boolean` value:



```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```



```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```





To set a custom attribute with a `date` value:



```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```



```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```





The default and maximum number of elements in an array is 500. You can update the maximum number of arrays in the Braze dashboard, under **Data Settings** > **Custom Attributes**. Arrays exceeding the maximum number of elements are truncated to contain the maximum number of elements.

To set a custom attribute with an `array` value:



```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```



```objc
// Setting a custom attribute with an array value
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[AppDelegate.braze.user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[AppDelegate.braze.user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```





### Incrementing or decrementing custom attributes

This code is an example of an incrementing custom attribute. You may increment the value of a custom attribute by any `integer` or `long` value:




```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```




```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```




### Unsetting custom attributes



To unset a custom attribute, pass the relevant attribute key to the `unsetCustomAttribute` method.

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```



To unset a custom attribute, pass the relevant attribute key to the `unsetCustomAttributeWithKey` method.

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```




### Nesting custom attributes

You can also nest properties within custom attributes. In the following example, a `favorite_book` object with nested properties is set as a custom attribute on the user profile. For more details, refer to [Nested Custom Attributes](https://www.braze.com/docs/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).



```swift
let favoriteBook: [String: Any?] = [
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
]

braze.user.setCustomAttribute(key: "favorite_book", dictionary: favoriteBook)
```



```objc
NSDictionary *favoriteBook = @{
  @"title": @"The Hobbit",
  @"author": @"J.R.R. Tolkien",
  @"publishing_date": @"1937"
};

[AppDelegate.braze.user setCustomAttributeWithKey:@"favorite_book" dictionary:favoriteBook];
```



### Using the REST API

You can also use our REST API to set or unset user attributes. For more information, refer to [User Data Endpoints](https://www.braze.com/docs/developer_guide/rest_api/user_data/#user-data).

## Setting user subscriptions

To set up a subscription for your users (either email or push), call the functions `set(emailSubscriptionState:)` or `set(pushNotificationSubscriptionState:)`, respectively. Both of these functions take the enum type `Braze.User.SubscriptionState` as arguments. This type has three different states:

| Subscription Status | Definition |
| ------------------- | ---------- |
| `optedIn` | Subscribed, and explicitly opted in |
| `subscribed` | Subscribed, but not explicitly opted in |
| `unsubscribed` | Unsubscribed and/or explicitly opted out |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Users who grant permission for an app to send them push notifications default to the status of `optedIn` as iOS requires an explicit opt-in.

Users will be set to `subscribed` automatically upon receipt of a valid email address; however, we suggest that you establish an explicit opt-in process and set this value to `optedIn` upon receipt of explicit consent from your user. Refer to [Managing user subscriptions](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/) for more details.

### Setting email subscriptions




```swift
AppDelegate.braze?.user.set(emailSubscriptionState: Braze.User.SubscriptionState)
```




```objc
[AppDelegate.braze.user setEmailSubscriptionState: BRZUserSubscriptionState]
```




### Setting push notification subscriptions




```swift
AppDelegate.braze?.user.set(pushNotificationSubscriptionState: Braze.User.SubscriptionState)
```




```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```




Refer to [Managing user subscriptions](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/) for more details.




## Prerequisites

Before you can use this feature, you'll need to [integrate the Flutter Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=flutter).

## Default user attributes

### Supported attributes

The following attributes are supported:

- First Name
- Last Name
- Gender
- Date of Birth
- Home City
- Country
- Phone Number
- Language
- Email

**Important:**


All string values such as first name, last name, country, and home city are limited to 255 characters.



### Setting default attributes 

To set user attributes automatically collected by Braze, you can use the setter methods included with the SDK.

```dart
braze.setFirstName('Name');
```

## Custom user attributes

### Setting custom attributes

In addition to the default user attributes, Braze also allows you to define custom attributes using a number of different data types:



To set a custom attribute with a `string` value:

```dart
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");
```



To set a custom attribute with an `integer` value:

```dart
// Set Integer Attribute
braze.setIntCustomUserAttribute("custom int attribute key", integer);
// Increment Integer Attribute
braze.incrementCustomUserAttribute("key", integer);
```



To set a custom attribute with a `double` value:

```dart
braze.setDoubleCustomUserAttribute("custom double attribute key", double);
```



To set a custom attribute with a `boolean` value:

```dart
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);
```



To set a custom attribute with a `date` value:

```dart
braze.setDateCustomUserAttribute("custom date attribute key", date);
```


To set a custom attribute with an `array` value:

```dart
// Adding to an Array
braze.addToCustomAttributeArray("key", "attribute");
// Removing an item from an Array
braze.removeFromCustomAttributeArray("key", "attribute");
```



**Important:**


Custom attribute values have a maximum length of 255 characters; longer values will be truncated.



### Unsetting custom attributes

To unset a custom attribute, pass the relevant attribute key to the `unsetCustomUserAttribute` method.

```dart
braze.unsetCustomUserAttribute('attribute_key');
```




## Prerequisites

Before you can use this feature, you'll need to [integrate the Roku Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=roku).


## Default user attributes

### Predefined methods

Braze provides predefined methods for setting the following user attributes using the `m.Braze` object.

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `Language`
- `HomeCity`
- `PhoneNumber`

### Setting default attributes

To set a default attribute, call the relevant method on the `m.Braze` object.



```brightscript
m.Braze.setFirstName("Alex")
```


```brightscript
m.Braze.setLastName("Smith")
```


```brightscript
m.Braze.setEmail("alex@example.com")
```


```brightscript
m.Braze.setGender("m") ' Accepts: "m", "f", "o", "n", "u", "p"
```


```brightscript
m.Braze.setDateOfBirth(1990, 5, 15) ' Year, month, day
```


```brightscript
m.Braze.setCountry("United States")
```


```brightscript
m.Braze.setLanguage("en")
```


```brightscript
m.Braze.setHomeCity("New York")
```


```brightscript
m.Braze.setPhoneNumber("+1234567890")
```



## Custom user attributes

In addition to the default user attributes, Braze also allows you to define custom attributes using several different data types.

### Settings custom attributes



To set a custom attribute a `string` value:

```brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```



To set a custom attribute with an `integer` value:

```brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```



Braze treats `float` and `double` values exactly the same. To set a custom attribute with either value:

```brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```



To set a custom attribute with a `boolean` value:

```brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```



To set a custom attribute with a `date` value:

```brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```



To set a custom attribute with an `array` value:

```brightscript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```



**Important:**


Custom attribute values have a maximum length of 255 characters; longer values will be truncated.



### Incrementing and decrementing custom attributes

This code is an example of an incrementing custom attribute. You may increment the value of a custom attribute by any positive or negative integer value.

```brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### Unsetting custom attributes

To unset a custom attribute, pass the relevant attribute key to the `unsetCustomAttribute` method.

```brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### Using the REST API

You can also use our REST API to set or unset user attributes. For more information, refer to [User Data Endpoints](https://www.braze.com/docs/developer_guide/rest_api/user_data/#user-data).

## Setting email subscriptions

You can set the following email subscription statuses for your users programmatically through the SDK.

| Subscription Status | Definition |
| ------------------- | ---------- |
| `OptedIn` | Subscribed, and explicitly opted in |
| `Subscribed` | Subscribed, but not explicitly opted in |
| `UnSubscribed` | Unsubscribed and/or explicitly opted out |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**Note:**


These types fall under `BrazeConstants().SUBSCRIPTION_STATES`.



The method for setting email subscription status is `setEmailSubscriptionState()`. Users will be set to `Subscribed` automatically upon receipt of a valid email address, however, we suggest that you establish an explicit opt-in process and set this value to `OptedIn` upon receipt of explicit consent from your user. For more details, visit [Managing user subscriptions](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

```brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```




## Prerequisites

Before you can use this feature, you'll need to [integrate the Unity Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=unity).

## Default user attributes

### Predefined methods

Braze provides predefined methods for setting the following user attributes using the `BrazeBinding` object. For more information, see [Braze Unity declaration file](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs).

- First name
- Last name
- User email
- Gender
- Birth date
- User country
- User home city
- User email subscription
- User push subscription
- User phone number

### Setting default attributes

To set a default attribute, call the relevant method on the `BrazeBinding` object.



```csharp
BrazeBinding.SetUserFirstName("first name");
```


```csharp
BrazeBinding.SetUserLastName("last name");
```


```csharp
BrazeBinding.SetUserEmail("email@email.com");
```


```csharp
BrazeBinding.SetUserGender(Appboy.Models.Gender);
```


```csharp
BrazeBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");
```


```csharp
BrazeBinding.SetUserCountry("country name");
```


```csharp
BrazeBinding.SetUserHomeCity("city name");
```


```csharp
BrazeBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```


```csharp
BrazeBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```


```csharp
BrazeBinding.SetUserPhoneNumber("phone number");
```



### Unsetting default attributes

To unset a default user attribute, pass `null` to the relevant method.

```csharp
BrazeBinding.SetUserFirstName(null);
```

## Custom user attributes

In addition to the default user attributes, Braze also allows you to define custom attributes using several different data types. For more information on each attribute's segmentation option, see [User data collection](https://www.braze.com/docs/developer_guide/analytics).

### Setting custom attributes

To set a custom attribute, use the corresponding method for the attribute type: 




```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```





```csharp
// Set Integer Attribute
AppboyBinding.SetCustomUserAttribute("custom int attribute key", 'integer value');
// Increment Integer Attribute
AppboyBinding.IncrementCustomUserAttribute("key", increment(int))
```




```csharp
AppboyBinding.SetCustomUserAttribute("custom float attribute key", 'float value');
```





```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
```




```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

**Note:**


Dates passed to Braze must either be in the [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format (such as `2013-07-16T19:20:30+01:00`) or in the `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format (such as`2016-12-14T13:32:31.601-0800`).







```csharp
// Setting An Array
AppboyBinding.SetCustomUserAttributeArray("key", array(List), sizeOfTheArray(int))
// Adding to an Array
AppboyBinding.AddToCustomUserAttributeArray("key", "Attribute")
// Removing an item from an Array
AppboyBinding.RemoveFromCustomUserAttributeArray("key", "Attribute")
```



**Important:**


Custom attribute values have a maximum length of 255 characters; longer values will be truncated.



### Unsetting custom attributes

To unset a custom attribute, pass the relevant attribute key to the `UnsetCustomUserAttribute` method. 

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### Using the REST API

You can also use our REST API to set or unset user attributes. For more information, refer to [User Data Endpoints](https://www.braze.com/docs/developer_guide/rest_api/user_data/#user-data).

## Setting user subscriptions

To set up an email or push subscription for your users, call one of the following functions.

```csharp
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`
```

Both functions take `Appboy.Models.AppboyNotificationSubscriptionType` as arguments, which has three different states:

| Subscription Status | Definition |
| ------------------- | ---------- |
| `OPTED_IN` | Subscribed, and explicitly opted in |
| `SUBSCRIBED` | Subscribed, but not explicitly opted in |
| `UNSUBSCRIBED` | Unsubscribed and/or explicitly opted out |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**Note:**


No explicit opt-in is required by Windows to send users push notifications. When a user is registered for push, they are set to `SUBSCRIBED` rather than `OPTED_IN` by default. To learn more, check out our documentation on [implementing subscriptions and explicit opt-ins](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).



| Subscription Type                        | Description |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType`      | Users will be set to `SUBSCRIBED` automatically upon receipt of a valid email address. However, we suggest that you establish an explicit opt-in process and set this value to `OPTED_IN` upon receipt of explicit consent from your user. Visit our [Changing User Subscriptions](https://www.braze.com/docs/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions) doc for more details. |
| `PushNotificationSubscriptionType`       | Users will be set to `SUBSCRIBED` automatically upon valid push registration. However, we suggest that you establish an explicit opt-in process and set this value to `OPTED_IN` upon receipt of explicit consent from your user. Visit our [Changing User Subscriptions](https://www.braze.com/docs/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions) doc for more details. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**Note:**


These types fall under `Appboy.Models.AppboyNotificationSubscriptionType`.



### Setting email subscriptions

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Setting push notification subscriptions

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```




## Prerequisites

Before you can use this feature, you'll need to [integrate the React Native Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native).

## Logging custom attributes

Braze provides methods for assigning attributes to users. You'll be able to filter and segment your users according to these attributes on the dashboard.

### Default user attributes

To set user attributes automatically collected by Braze, you can use setter methods that come with the SDK.

```javascript
Braze.setFirstName("Name");
```

The following attributes are supported:

- First Name
- Last Name
- Gender
- Date of Birth
- Home City
- Country
- Phone Number
- Language
- Email

All string values such as first name, last name, country, and home city are limited to 255 characters.

### Custom user attributes

In addition to our predefined user attribute methods, Braze also provides [custom attributes](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) to track data from your applications. 

```javascript
Braze.setCustomUserAttribute("attribute_key", "attribute_value", function(){
    // optional onResult callback
});
```

#### Unsetting custom attributes

```javascript
Braze.unsetCustomUserAttribute("attribute_key", function(){
    // optional onResult callback
});
```

#### Custom Attribute Arrays

```javascript

// Adds a string to a custom attribute string array, or creates that array if one doesn't exist.
Braze.addToCustomUserAttributeArray("my-attribute-array", "new or existing value", optionalCallback);

// Removes a string from a custom attribute string array.


Braze.removeFromCustomUserAttributeArray("my-attribute-array", "existing value", optionalCallback);
```




