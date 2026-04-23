# Dynamic SMS link preview

> With Movable Ink’s dynamic SMS link preview, you can leverage the immersiveness of MMS at the same cost of SMS. This allows you to use Braze and Movable Ink to deliver cost-effective, personalized rich messaging experiences.

## Prerequisites

| Requirement | Description |
| --- | --- |
| Movable Ink account | A Movable Ink account is required to take advantage of this partnership. |
| Data source | You need to connect a data source to Movable Ink. This can be done through CSV, website import, or API. |
| MMS sending capabilities | Confirm that you're set up for MMS through Braze.
| [Link shortening](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening/) | Confirm that link shortening is turned on. | 
| Contact card | Your brand (the sender) must be saved as a contact on the user's phone for link preview to work with iOS. This can be done with a contact card or another method. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Follow the respective steps below to send dynamic SMS links for iOS and Android operating systems.

### iOS

**Important:**


To allow link preview images for iOS, users must add your brand (the sender) as a contact.



#### Step 1: Create a contact card campaign

After users save your brand as a contact, either through a [contact card](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/create/contact_card/) or another method, they will be able to view **Tap to Load Preview** prompts and Movable Ink links.

![1]{: style="max-width:30%;"}

#### Step 2: Send Movable Ink links

1. Create an SMS campaign in Movable Ink and generate your click-through URL.
2. In the Braze dashboard, go to **Campaigns** and set up a new SMS/MMS campaign from the **Create Campaign** dropdown.
3. In the SMS campaign composer:
    - Set your subscription group.
    - Enter your message.
    - Add your Movable Ink link **last**, after all other text in the message body. <br><br>![2]{: style="max-width:50%;"}

**Tip:**


Check out [Liquid](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/) for a refresher on Liquid personalization.  



{: start="4"}
4. You’re all set to test and launch your dynamic SMS link preview campaign.

![3]{: style="max-width:70%;"}

After users load the link preview, a personalized image will render with the ability to link out to your website, app, or landing page.

![4]{: style="max-width:30%;"}

### Android (Google and Samsung devices)

Android users aren't required to save your brand as a contact in order to receive dynamic SMS link previews. However, it is still recommended so that the device can automatically load the link previews.

![5]{: style="max-width:30%;"}

Users who haven't saved your brand as a contact and have turned on automatic previews will have to select **Tap to load preview** to load the preview image.

![6]{: style="max-width:30%;"}

## Considerations

- Only include one preview link in your message. Content will not be generated with multiple links in your SMS body. 
- Don't include any characters after your preview link or the experience might break.


[1]: /docs/assets/img/movable_ink/ios_link.png?390ac9ceced88bc8189c84e15b743354
[2]: /docs/assets/img/movable_ink/ios_message.png?d70bd01c08807bf9239e2c8996906ff0
[3]: /docs/assets/img/movable_ink/ios_test_launch.png?82de7196a80bdb0aadd400052764f0ae
[4]: /docs/assets/img/movable_ink/ios_example.png?f57e0e0c67947a6affbaf62c80fb7dd6
[5]: /docs/assets/img/movable_ink/android_automatic.png?3d714108100bd5e12c39a960e5486de4
[6]: /docs/assets/img/movable_ink/android_tap.png?315729b3d6b79bbddee161654a9ddee0
