# Redundancy (engineering)

In engineering and systems theory, redundancy is the intentional duplication of critical components or functions of a system with the goal of increasing reliability of the system, usually in the form of a backup or fail-safe, or to improve actual system performance, such as in the case of GNSS receivers, or multi-threaded computer processing.
In many safety-critical systems, such as fly-by-wire and hydraulic systems in aircraft, some parts of the control system may be triplicated, which is formally termed triple modular redundancy (TMR). An error in one component may then be out-voted by the other two. In a triply redundant system, the system has three sub components, all three of which must fail before the system fails. Since each one rarely fails, and the sub components are designed to preclude common failure modes (which can then be modelled as independent failure), the probability of all three failing is calculated to be extraordinarily small; it is often outweighed by other risk factors, such as human error. Electrical surges arising from lightning strikes are an example of a failure mode which is difficult to fully isolate, unless the components are powered from independent power busses and have no direct electrical pathway in their interconnect (communication by some means is required for voting). Redundancy may also be known by the terms "majority voting systems" or "voting logic".

Redundancy sometimes produces less, instead of greater reliability –  it creates a more complex system which is prone to various issues, it may lead to human neglect of duty, and may lead to higher production demands which by overstressing the system may make it less safe.
Redundancy is one form of robustness as practiced in computer science. 
Geographic redundancy has become important in the data center industry, to safeguard data against natural disasters and political instability (see below).


== Forms of redundancy ==
In computer science, there are four major forms of redundancy:

Hardware redundancy, such as dual modular redundancy and triple modular redundancy
Information redundancy, such as error detection and correction methods
Time redundancy, performing the same operation multiple times such as multiple executions of a program or multiple copies of data transmitted
Software redundancy such as N-version programming
A modified form of software redundancy, applied to hardware may be:

Distinct functional redundancy, such as both mechanical and hydraulic braking in a car.  Applied in the case of software, code written independently and distinctly different but producing the same results for the same inputs.
Structures are usually designed with redundant parts as well, ensuring that if one part fails, the entire structure will not collapse. A structure without redundancy is called fracture-critical, meaning that a single broken component can cause the collapse of the entire structure. Bridges that failed due to lack of redundancy include the Silver Bridge and the Interstate 5 bridge over the Skagit River.
Parallel and combined systems demonstrate different level of redundancy. The models are subject of studies in reliability and safety engineering.


=== Dissimilar redundancy ===
Unlike traditional redundancy, which uses more than one of the same thing, dissimilar redundancy uses different things. The idea is that the different things are unlikely to contain identical flaws. The voting method may involve additional complexity if the two things take different amounts of time. Dissimilar redundancy is often used with software, because identical software contains identical flaws.
The chance of failure is reduced by using at least two different types of each of the following 

processors,
operating systems,
software,
sensors,
types of actuators (electric, hydraulic, pneumatic, manual mechanical, etc.)
communications protocols,
communications hardware,
communications networks,
communications paths


=== Geographic redundancy ===
Geographic redundancy corrects the vulnerabilities of redundant devices deployed by geographically separating backup devices. Geographic redundancy reduces the likelihood of events such as power outages, floods, HVAC failures, lightning strikes, tornadoes, building fires, wildfires, and mass shootings disabling most of the system if not the entirety of it.
Geographic redundancy locations can be

more than 621 miles (999 km) continental,
more than 62 miles apart and less than 93 miles (150 km) apart,
less than 62 miles apart, but not on the same campus, or
different buildings that are more than 300 feet (91 m) apart on the same campus.
The following methods can reduce the risks of damage by a fire conflagration:

large buildings at least 80 feet (24 m) to 110 feet (34 m) apart, but sometimes a minimum of 210 feet (64 m) apart.
high-rise buildings at least 82 feet (25 m) apart
open spaces clear of flammable vegetation within 200 feet (61 m) on each side of objects
different wings on the same building, in rooms that are separated by more than 300 feet (91 m)
different floors on the same wing of a building in rooms that are horizontally offset by a minimum of 70 feet (21 m) with fire walls between the rooms that are on different floors
two rooms separated by another room, leaving at least a 70-foot gap between the two rooms
there should be a minimum of two separated fire walls and on opposite sides of a corridor
Geographic redundancy is used by Amazon Web Services (AWS), Google Cloud Platform (GCP), Microsoft Azure, Netflix, Dropbox, Salesforce, LinkedIn, PayPal, Twitter, Facebook, Apple iCloud, Cisco Meraki, and many others to provide geographic redundancy, high availability, fault tolerance and to ensure availability and reliability for their cloud services.
As another example, to minimize risk of damage from severe windstorms or water damage, buildings can be located at least 2 miles (3.2 km) away from the shore, with an elevation of at least 5 feet (1.5 m) above sea level.

---
Source: https://en.wikipedia.org/wiki/Redundancy_%28engineering%29 (CC BY-SA 4.0)
