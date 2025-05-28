.. _kubernetes_architecture:

Kubernetes Architecture  MetalLB, Traefik
===========================================

To make ``www.example.com`` accessible from my laptop. 

Overview of  Setup
------------------

 running a Kubernetes cluster on Talos Linux nodes, hosted on a Proxmox virtualization platform. The setup includes:

- **MetalLB** for load balancing
- **Traefik** as an ingress controller
- An **Ingress** resource to route traffic to a service for ``www.example.com``
-  **laptop** resolves ``www.example.com`` to ``10.10.10.10`` via ``/etc/hosts``
- A **Proxmox LXC container** acts as a router/DHCP server (``192.168.1.200``) on a network bridge (``vmbr1``)
- a router assigns IPs to three Talos nodes and one Talos client

Below, each part is explained in detail.

1. Proxmox and Networking Setup
-------------------------------

Proxmox is the virtualization platform hosting your infrastructure, including the Talos VMs and the router container.

**Proxmox Network Bridge (vmbr1)**

- Acts as a virtual switch that connects VMs and containers.
- Configured to handle networking for Talos nodes and the client.
- Devices on this bridge typically reside in the ``192.168.1.0/24`` subnet.

**LXC Container (Router/DHCP Server at 192.168.1.200)**

- Provides dynamic IP assignment via DHCP.
- Routes traffic between the ``vmbr1`` subnet and external networks.
- May also offer NAT, DNS, or firewall services.

**Network Flow**

- Talos nodes and the client receive IPs (e.g., ``192.168.1.201-204``) from this container.
- The container enables traffic to flow between your laptop’s network and the Kubernetes cluster.

2. Talos Linux Kubernetes Cluster
----------------------------------


**Three Talos Cluster Nodes**

- VMs on Proxmox configured as Kubernetes nodes.
- a control plane 2 worker nodes
- IPs assigned by DHCP from the LXC router.

**One Talos Client**

- a LXC device used for managing the cluster using ``talosctl``.
- Communicates with the control plane via the Talos API.

**Talos Networking**

- Nodes are assigned IPs via ``vmbr1``.
- Kubernetes networking handles intra-cluster communication.

3. Kubernetes Networking with MetalLB and Traefik
--------------------------------------------------

**MetalLB**

- Provides load balancing by assigning external IPs (e.g., ``10.10.10.10``) to LoadBalancer services.
- Operates in Layer 2 (ARP) or BGP mode.
- A node "owns" the external IP and routes traffic to the appropriate pod.

**How MetalLB Works**

- Configured with a pool like ``10.10.10.0/24``.
- Ensures external traffic is routed to the correct service or pod via ARP.

**Traefik as Ingress Controller**

- A reverse proxy and ingress controller running in the cluster.
- Exposed via a LoadBalancer service assigned the IP ``10.10.10.10``.
- Handles HTTP/S requests and routes them according to Ingress rules.

**Ingress Resource Example**

.. code-block:: yaml

    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: example-ingress
      annotations:
        traefik.ingress.kubernetes.io/router.entrypoints: web, websecure
    spec:
      rules:
      - host: www.example.com
        http:
          paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: example-service
                port:
                  number: 80

This configuration tells Traefik to forward traffic for ``www.example.com`` to the ``example-service`` on port ``80``.

4. Laptop Configuration
------------------------

**/etc/hosts Entry**

Your laptop uses the following line in ``/etc/hosts``:

.. code-block:: text

    10.10.10.10 www.example.com

This resolves ``www.example.com`` locally without DNS.

**Routing to the Cluster**

- The LXC router at ``192.168.1.200`` forwards traffic to ``10.10.10.10``.
- Routing may involve NAT or static rules to ensure reachability.

5. How It All Ties Together
----------------------------

The full path of a request to ``www.example.com`` is:

1. **Laptop Resolution**
   - The browser looks up ``www.example.com`` and resolves it to ``10.10.10.10`` using ``/etc/hosts``.

2. **Network Routing**
   - Traffic is sent to ``10.10.10.10`` and routed by the LXC container to the Talos node that owns this IP.

3. **MetalLB**
   - Owns the ``10.10.10.10`` IP and ensures the request reaches the correct node.

4. **Traefik**
   - Receives the HTTP/S request on port 80/443.
   - Uses the Ingress resource to determine routing.

5. **Kubernetes Service and Pods**
   - ``example-service`` forwards the request to one of your pods (e.g., Nginx).
   - The response is returned back through Traefik and MetalLB.

6. **Response**
   - Your browser displays the resulting web page from ``www.example.com``.


