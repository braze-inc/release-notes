# Send to Destination step

> The Send to Destination step allows you to send users from one Canvas to another. For example, if you have two Canvases that share messaging for promotional offers, you can use Send to Destination to connect these Canvases.

## How it works

![A Send to Destination step to send users to a new Canvas.](https://www.braze.com/docs/assets/img/send_to_destination1.png?fe2eea5457018add9a41076d8483eb24){: style="float:right;max-width:35%;margin-left:15px;"}

Your current Canvas with the Send to Destination step is the source. Within the step, you can choose the destination Canvas. From here, users are sent to the destination Canvas. They will proceed down that Canvas if they meet the entry criteria there and will also continue to flow through the source Canvas.

## Create a Send to Destination step

### Step 1: Add a step

Drag and drop the **Send to Destination** component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Send to Destination**.

### Step 2: Choose your destination

Select the dropdown or enter the Canvas name in the **Destination** field. Then, select **Done**.

![A Send to Destination step set up to send users from the a Canvas named "Feature Adoption" to "New Canvas".](https://www.braze.com/docs/assets/img/send_to_destination2.png?319d903f29526f93b190c30c4306f05a)

### Step 3: Preview your destination

You can select **Preview destination** to see the journey for users who meet the entry criteria for the destination Canvas.

After setting up this Canvas step, you can [preview the user path](https://www.braze.com/docs/user_guide/messaging/canvas/testing_canvases/preview_user_paths) to see if a user proceeds to the next step in the current Canvas and if they also proceed to the destination Canvas.

## Frequently asked questions

### Can I set the destination to a draft Canvas?

Yes. The destination Canvas can have a draft or idle status.

### Are context variables preserved?

Yes. The [context](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/context_variables) of the source Canvas is always passed to the destination Canvas.