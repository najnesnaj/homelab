intro
=====


Homelab
-------

A homelab is an environment where I can try things out, without upsetting a CISO, CDO, CITO ....
The system is an old HP proliant gen8, with 2TB of space and 256GB of memory, and bi-XEON with 16 cores in total. 


Virtualisation
---------------

I choose proxmox as a virtualisation platform, it runs linux containers (LXC), which are kind of cool since they are created quickly, launched quickly. Some problems arise since there are still shared resources with the host... 

Proxmox supports virtual machines (VM) as well. 

VM are used as kubernetes nodes, since using LXC was problematic.
This setup allows to run a complete kubernetes multiple node cluster on a single machine.

Containerisation
----------------

Containerization, in simple terms, is like packing a lunchbox for software. It’s a way to bundle an application with everything it needs to run—code, libraries, settings, and dependencies—into a single, portable package called a container. This makes it easy to move and run the software consistently on any computer, server, or cloud, without worrying about differences in the environment.


Kubernetes
----------

* Organizes Containers: It decides which computers (servers) should run each container, spreading them out to avoid overloading any one server. It’s like assigning chefs to different kitchen stations to keep things efficient.

* Scales Automatically: If your app gets super popular (like a sudden rush of customers), Kubernetes can add more containers to handle the demand. If things slow down, it removes extras to save resources.

* Keeps Things Running: If a container crashes (like a lunchbox spilling), Kubernetes quickly replaces it with a new one so your app stays available.

* Manages Traffic: It directs users to the right containers, ensuring everyone gets access to the app without delays, like guiding customers to the right food station.

Updates Smoothly



 


