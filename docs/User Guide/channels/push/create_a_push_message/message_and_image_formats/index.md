# Push message and image formats

> This reference article describes message and image formats for push notifications.

For best results, refer to the following image size and message length guidelines when crafting your push messages. There may be some variance depending on the presence of an image, the notification state (iOS) and display setting of the user's device, as well as the size of the device. When in doubt, keep your copy short and sweet.

## iOS and Android push




**Image Type** | **Recommended Image Size** | **Max Image Size** | **File Types**
--- | --- | --- | ---
(iOS) 2:1 *Recommended* | 500&nbsp;KB | 5&nbsp;MB | PNG, JPEG, GIF
(Android) Push icon | 500&nbsp;KB | 5&nbsp;MB | PNG, JPEG
(Android) Expanded notification | 500&nbsp;KB | 5&nbsp;MB | PNG, JPEG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

**Note:**


GIFs are not supported in Android push notifications. This is an Android platform limitation, not a Braze limitation.

For in-app messages and Content Cards on Android, you can support GIFs by integrating a third-party image library, such as [Glide](https://bumptech.github.io/glide/) or [Fresco](https://frescolib.org/).

On iOS, push notifications support GIFs. In-app messages and Content Cards require a custom GIF image provider.






| Message Type | Recommended Message Length (Text only) | Recommended Message Length (Rich)
--- | ---
(iOS) Lock Screen | 160 characters | 130 characters
(iOS) Notification Center | 160 characters | 130 characters
(iOS) Banner Alert | 80 characters | 65 characters
(Android) Lock Screen | 49 characters | N/A
(Android) Notification Drawer | 597 characters | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

Wondering how many characters you can use in an iOS push notification without it being truncated? Check out our [iOS character count guidelines](https://www.braze.com/docs/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/#character-count).




**Platform** | **Size**
--- | ---
pre iOS 8 | 0.256 KB
post iOS 8 | 2 KB
Android (FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }






![iOS push notification with text that reads: "Hi! This is an iOS Push with an image" with an emoji. There is a small image beside the text.](https://www.braze.com/docs/assets/img_archive/braze_richpush1.png?ef4e0bdea0cc8bad17fcdd73d3217f6e){: style="max-width:50%;"}
![iOS push notification on a hard push with the same text as the previous message with an expanded image preceding the text.](https://www.braze.com/docs/assets/img_archive/braze_richpush2.png?d084b6ecdf38632d542b0312de9ef22a){: style="max-width:50%;"}




![Android push notification with a large image under the message text.](https://www.braze.com/docs/assets/img_archive/android_push_img2.png?e3ea367aa6289702384fd3d9bbc4df0b)

**Note:**


Large image notifications display best when using an image of at least 600x300 pixels.










![iOS push notification with text that reads: "Hi! This is an iOS Push".](https://www.braze.com/docs/assets/img_archive/iOS_push_notification_small.png?3cb03d1af1f40aa294bc9c9bcc893603)



![Android push notification displayed on the home screen.](https://www.braze.com/docs/assets/img_archive/Push_Android_2.png?1dc8a0d31e842142c9476b7131136313)





## Web push




| **Browser** | **Recommended Icon Size**
| --- | ---
Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | 192 x 192 ≥ (Icons are configurable on a per-campaign basis with Safari 16+ on macOS 13+)
Opera | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

| **Browser** | **Platform** | **Large Image Size**
| --- | --- | ---
Chrome | Android | 2:1 aspect ratio
Firefox | Android | N/A
Chrome | Windows | 2:1 aspect ratio
Edge | Windows | 2:1 aspect ratio
Firefox | Windows | N/A
Firefox | Windows | 2:1 aspect ratio
Safari | macOS | N/A
Chrome | macOS | N/A
Firefox | macOS | N/A
Opera | macOS | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }




| **Browser** | **Platform** | **Maximum Title Length**  | **Maximum Message Body Length**
| --- | --- | --- | ---
Chrome | Android | 35 | 50
Firefox | Android | 35 | 50
Chrome | Windows | 50 | 120
Edge | Windows | 50 | 120
Firefox | Windows | 54 | 200
Opera | Windows | 50 | 120
Chrome | macOS | 35 | 50
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opera | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }



