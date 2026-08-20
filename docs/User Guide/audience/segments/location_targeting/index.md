# Location targeting

> This article covers how to set up location targeting so you can segment users by their most recent location.

## Step 1: Create your segment

Navigate to the **Segments** page, under **Audience**, to view all of your current user segments. On this page, you can create and name new segments. To get started, select **Create Segment** and give your segment a name.

![Modal to create a segment.](https://www.braze.com/docs/assets/img_archive/createsegment2.png?61188dcd6d179f63f346b1bd93ef3557){: style="max-width:70%;"}

## Step 2: Customize your location

After you've created your segment, add a `Most Recent Location` filter to highlight users by the last place that they used your app. You have the option of highlighting users within or outside of a standard circular region or customizable polygonal region.

![Filter for a most recent location within a circle.](https://www.braze.com/docs/assets/img_archive/filter_recent_location.png?974a24c25731dcbd42ae48472595ea6f)

### Users without location data

Users without location data—including users whose location was previously recorded and later cleared—match filters for `most recent location outside of circle` and `most recent location outside of polygon`. To exclude users without location data, combine the `Most Recent Location` filter with a `Location Available` filter.




### Circular regions

For circular regions, you can move the origin and adjust the location radius for your segmentation.

![A circular outline of cities between New Jersey and New York.](https://www.braze.com/docs/assets/img_archive/location_circle.png?0cb3994392e4f8c92e795b2969d01720){: style="max-width:70%;"}




### Polygonal regions

For polygonal regions, you can more specifically designate which areas you wish to be included in your segment.

![An outline of New York state as the selected polygonal region.](https://www.braze.com/docs/assets/img_archive/create_polygon.png?f614b6152440f32dfa7030e6fb716de7){: style="max-width:70%;"}




## Partnership support for beacon and geofence

Combining existing beacon or geofence support with our targeting and messaging features gives you more information about your users' physical actions so you can message them accordingly. You can leverage location tracking with some of our partners: 

- [Radar](https://www.braze.com/docs/partners/message_personalization/location/radar)
- [Infillion](https://www.braze.com/docs/partners/message_personalization/location/infillion)
- [Foursquare](https://www.braze.com/docs/partners/message_personalization/location/foursquare)

