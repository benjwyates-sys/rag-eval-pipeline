# Geofence

A geofence is a virtual "perimeter" or "fence" around a given geographic feature. A geofence can be dynamically generated (as in a radius around a point location) or match a predefined set of boundaries (such as school zones or neighborhood boundaries).
The use of a geofence is called geofencing, and one example of use involves a location-aware device of a location-based service (LBS) user entering or exiting a geofence. This method combines awareness of the user's current location with awareness of the user's proximity to locations that may be of interest. This activity could trigger an alert to the device's user as well as messaging to the geofence operator. This info, which could contain vehicle location data, could be sent to a mobile telephone or an email account.
Geofencing is a critical technology in many fields. In fleet management, it is used to automate timekeeping at job sites and to alert managers of unauthorized vehicle use. It is also used in marketing, smart home automation, and public transport information systems. However, the technology has also raised significant privacy concerns, particularly regarding its use by law enforcement to issue geofence warrants to collect data on all individuals within a specific area.


== History ==
Geofencing was invented in the early 1990s and patented in 1995 by American inventor Michael Dimino, using the first-of-its-kind GPS and GSM technology for a tracking system to locate objects anywhere on the globe from a remote location.
Cellular geofencing for global tracking is cited in the United States Patent Office over 240 times by major companies such as IBM and Microsoft since 1995 and is first mentioned as:

A global tracking system (GTS) for monitoring an alarm condition associated with and locating a movable object, the GTS comprising:

a cellular telephone located with the movable object;
a GPS (global positioning system) receiver located with the movable object, the GPS receiver being effective for providing data reflecting a present spacial position of the movable object, in terms of spacial latitude/longitude coordinates;
an interface between the GPS receiver and the cellular telephone, the interface being connected between the GPS receiver and the cellular telephone and including circuitry for transmitting the spacial coordinates from the GPS receiver through the telephone, wirelessly to a remote location; and
an alarm for detecting that the object has been moved, by calculating a spatial movement of the object which exceeds a predetermined distance based on information supplied by the GPS receiver, and the alarm initiating the transmission to the remote location the spatial coordinates from the GPS receiver when said movement of predetermined distance has been detected.

In April 2026, the Supreme Court heard arguments about whether police use of geofences violates the Fourth Amendment's ban on unreasonable searches and seizures. Police have obtained "geofence warrants" to identify people who were in a given area, such as those near the January 6, 2021 Capitol attack, the person who planted pipe bombs outside the Democratic and Republican party headquarters the night before, and after killings in several states.


== Working ==
Geofencing uses technologies like GPS, or even IP address ranges, to build its virtual fence. In most cases, mobile phones are using combinations of positioning methods, e.g., Assisted GPS (A-GPS). "A-GPS uses assistance data received from the network to obtain a faster location calculation compared with GPS alone." The global system of tracking and geofencing is supported by a group of subsystems based on global navigation satellite system (GNSS) services. Both horizontal and vertical accuracy of GNSS is just a few centimetres for baseline ≤ 5 km. The Wide Area Augmentation System (WAAS) is used by devices equipped and used in North America—the accuracy is considered to be within 3 m at least 95% of the time. These virtual fences can be used to track the physical location of the device active in the particular region or the fence area. The location of the person using the device is taken as geocoding data and can be used further for advertising purposes.
It is possible to monitor several geofences at once (multiple active geofences). The number of active geofences on Android devices is limited to 100 per app and per user. It is possible to monitor different type of triggering activity for each geofence separately—entrance, exit, or dwell in the monitored area.


== Types ==
There are two types of geofencing—choice of type depends on the purpose of using geofencing in a given situation.


=== Active ===
It uses GPS services for the entire time when the application is running and therefore consumes more battery as a result. The reason for the higher battery consumption is the fact that the service requires running in the foreground throughout the time of usage.


=== Passive ===
This type does not require a constantly active state of the application and is able to run in the background. It is rather suitable for the process of data collection.

---
Source: https://en.wikipedia.org/wiki/Geofence (CC BY-SA 4.0)
