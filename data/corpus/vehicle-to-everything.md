# Vehicle-to-everything

Vehicle-to-everything (V2X) may be used in regard to communication of a vehicle, or to energy transfer from a battery electric vehicle used to power a local load (V2L, V2V if another vehicle), a house (V2H "off-grid"), or the grid (V2G).
In case of wireless communication, V2X describes communication between a vehicle and any entity that may affect, or may be affected by, the vehicle. Sometimes called C-V2X, it is a vehicular communication system that is intended to improve road safety and traffic efficiency while reducing pollution and saving energy.  
The automotive and communications industries, along with the U.S. government, European Union and South Korea are actively promoting V2X and C-V2X as potentially life-saving, pollution-reducing technologies. The U.S. Department of Transport has said V2X technologies offer significant transportation safety and mobility benefits. The U.S. NHTSA estimates a minimum of 13% reduction in traffic accidents if a V2V system were implemented, resulting in 439,000 fewer crashes per year. V2X technology is already being used in Europe and China.
There are two standards for dedicated V2X communications depending on the underlying wireless technology being used: (1) WLAN-based, and (2) cellular-based. V2X also incorporates various more specific types of communication including:

Vehicle-to-device (V2D) - Bluetooth / WiFi-Direct, e.g. Apple's CarPlay and Google's Android Auto.
Vehicle-to-grid (V2G) - information exchange with the smart grid to balance loads more efficiently.
Vehicle-to-building (V2B), also known as vehicle-to-home (V2H)
Vehicle-to-load (V2L)
Vehicle-to-network (V2N) - communication between a vehicle and a wider network, such as a cellular network. This category includes telematics, where a vehicle communicates with a fleet management platform or a cloud server.
Vehicle-to-cloud (V2C) - e.g. OTA updates, remote vehicle diagnostics (DoIP).
Vehicle-to-infrastructure (V2I) - e.g. traffic lights, lane markers and parking meters.
Vehicle-to-pedestrian (V2P) - e.g. wheelchairs and bicycles, commonly also used to designate vulnerable road users (VRUs).
Vehicle-to-vehicle (V2V) - real-time data exchange with nearby vehicles.


== History ==
The history of working on vehicle-to-vehicle communication projects to increase safety, reduce accidents and driver assistance can be traced back to the 1970s with projects such as the US Electronic Road Guidance System (ERGS) and Japan's CACS. Most milestones in the history of vehicle networks originate from the United States, Europe, and Japan.
Standardization of WLAN-based V2X supersedes that of cellular-based V2X systems. IEEE first published the specification of WLAN-based V2X (IEEE 802.11p) in 2010. It supports direct communication between vehicles (V2V) and between vehicles and infrastructure (V2I).  This technology is referred to as dedicated short-range communication (DSRC).  DSRC uses the underlying radio communication provided by 802.11p.
In 2016, Toyota became the first automaker globally to introduce automobiles equipped with V2X.  These vehicles use DSRC technology and are only for sale in Japan.  In 2017, GM became the second automaker to introduce V2X.  GM sells a Cadillac model in the United States that also is equipped with DSRC V2X.
In 2016, 3GPP published V2X specifications based on LTE as the underlying technology. It is generally referred to as "cellular V2X" (C-V2X) to differentiate itself from the 802.11p based V2X technology.  In addition to the direct communication (V2V, V2I), C-V2X also supports wide area communication over a cellular network (V2N).
As of December 2017, a European automotive manufacturer has announced to deploy V2X technology based on 802.11p from 2019. While some studies and analysis in 2017 and 2018, all performed by the 5G Automotive Association (5GAA) – the industry organisation supporting and developing the C-V2X technology – indicate that cellular-based C-V2X technology in direct communication mode is superior to 802.11p in multiple aspects, such as performance, communication range, and reliability, many of these claims are disputed, e.g. in a whitepaper published by NXP, one of the companies active in the 802.11p based V2X technology,
but also published by peer-reviewed journals.
This technology can be misused to remotely control the vehicle. The Police of the Czech Republic in cooperation with universities has developed a system for remote stopping of vehicles with reference to the fact that such a procedure is legal even under the current legislation.


== Technology overview ==


=== 802.11p (DSRC) ===
The original V2X communication uses WLAN technology and works directly between vehicles (V2V) as well as vehicles and traffic infrastructure (V2I), which form a vehicular ad-hoc network as two V2X senders come within each other's range. Hence it does not require any communication infrastructure for vehicles to communicate, which is key to ensure safety in remote or little-developed areas.
WLAN is particularly well-suited for V2X communication, due to its low latency. It transmits messages known as Cooperative Awareness Messages (CAM)  or Basic Safety Message (BSM), and Decentralised Environmental Notification Messages (DENM).
Other roadside infrastructure related messages are Signal Phase and Timing Message (SPaT), In Vehicle Information Message (IVI), and Service Request Message (SRM). The data volume of these messages is very low. The radio technology is part of the WLAN IEEE 802.11 family of standards and known in the US as Wireless Access in Vehicular Environments (WAVE) and in Europe as ITS-G5. To complement the direct communication mode, vehicles can be equipped with traditional cellular communication technologies, supporting V2N based services.

---
Source: https://en.wikipedia.org/wiki/Vehicle-to-everything (CC BY-SA 4.0)
