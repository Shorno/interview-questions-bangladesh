---
description: Therap Software Engineer interview questions, Therap System Adminstrator interview stages, Therap System Adminstrator interview details, Therap System Adminstrator interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/therap/sys
---
# Associate System Adminstrator

## Interview Stages

The selection process has multiple stages,

1. **Initial screening:** This round is taken in written format
2. **1st technical round** The first round is taken by the BD team
3. **2nd technical round** The second round is taken by both the BD and USA teams
4. **HR Round:** This is the final stage before onboarding and typically deals with salary negotiation. 

## Written test Questions for Associate System Adminstrator

### Operating System (OS)
<article>

What is a kernel? What is the difference between a monolithic kernel and a microkernel?

<details><summary>Theory and explanation</summary>

The **kernel** is the core of an OS: manages CPU, memory, devices, and system calls. User programs request services via **syscalls**.

**Monolithic kernel** — drivers, FS, scheduler in one address space (Linux). Fast syscall path; bug in driver can crash kernel.

**Microkernel** — minimal kernel (IPC, scheduling); drivers/services in user space (Minix, seL4). Better isolation; more IPC overhead.

**Hybrid** — macOS/Windows blend both (e.g. Windows kernel + user-mode drivers).

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides

</details>

<details><summary>Solution (JavaScript)</summary>

```bash
# Example: inspect Linux kernel version
uname -r
```

#### Code walkthrough
Apply commands in a lab VM; explain output.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Permission denied — use sudo appropriately.

</details>

</article>
<article>

What is a process?

<details><summary>Theory and explanation</summary>

A **process** is a running program instance: own virtual address space, file descriptors, PID, credentials. OS schedules processes/threads on CPUs.

**Process vs thread** — threads share address space; processes are isolated. Creation: `fork()` + `exec()` on Linux.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// Conceptual: process has PID, memory, open files
// Node.js child_process spawns a new OS process
const { spawn } = require('child_process');
const child = spawn('echo', ['hello']);
```

#### Code walkthrough
Apply commands in a lab VM; explain output.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Permission denied — use sudo appropriately.

</details>

</article>
<article>

What is the difference between virtualization and containers?

<details><summary>Theory and explanation</summary>

**Virtualization (VMs)** — hypervisor emulates hardware; each VM runs full guest OS. Strong isolation; higher overhead.

**Containers** — share host kernel; isolated via namespaces (pid, net, mount, user) + cgroups for limits. Images bundle app + deps (Docker/OCI).

Use VMs for multi-tenant strong isolation; containers for dense microservice deployment.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides

</details>

<details><summary>Solution (JavaScript)</summary>

```bash
docker run --rm hello-world   # container
# vs VirtualBox/VMware full VM
```

#### Code walkthrough
Apply commands in a lab VM; explain output.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Permission denied — use sudo appropriately.

</details>

</article>
<article>

What are the advantages of cloud storage over local storage?

<details><summary>Theory and explanation</summary>

**Cloud storage** (S3, Azure Blob): durability (replication), elasticity, off-site backup, pay-as-you-go, global CDN integration, managed encryption.

**Local** — lower latency for on-prem apps, no egress fees, full control, air-gapped compliance.

Trade-off: cloud ops cost vs capex hardware; network dependency.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides

</details>

<details><summary>Solution (JavaScript)</summary>

N/A — discuss trade-offs verbally with SLA, RPO/RTO examples.

#### Code walkthrough
Apply commands in a lab VM; explain output.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Permission denied — use sudo appropriately.

</details>

</article>
<article>

Provide an example where multithreading is a better approach than multiprocessing.

<details><summary>Theory and explanation</summary>

**Multithreading** when tasks share large in-memory state and are **I/O-bound** — web server handling many connections, GUI app, parallel reads from disk where GIL/release GIL matters less in native code.

Example: thread pool serving HTTP — threads block on I/O while others run; sharing connection cache avoids serializing data across processes.

**Multiprocessing** better for CPU-bound Python due to GIL, or when crash isolation needed.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// Node.js: single-threaded event loop + worker threads for CPU work
const { Worker } = require('worker_threads');
```

#### Code walkthrough
Apply commands in a lab VM; explain output.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Permission denied — use sudo appropriately.

</details>

</article>
<article>

What is a context switch in Linux

<details><summary>Theory and explanation</summary>

**Context switch** — CPU saves state of current thread/process (registers, program counter, kernel stack) and loads another's so it can run.

Triggered by: timer interrupt, blocking syscall, preemption. Cost: flush TLB/cache, scheduler overhead — why too many threads hurt performance.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides

</details>

<details><summary>Solution (JavaScript)</summary>

N/A — mention `vmstat 1` / `pidstat -w` for switch rates.

#### Code walkthrough
Apply commands in a lab VM; explain output.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Permission denied — use sudo appropriately.

</details>

</article>
<article>

What's the Difference between Hard Links vs Soft Links in Linux? What will happen if soft link is broken?

<details><summary>Theory and explanation</summary>

**Hard link** — another directory entry pointing to same **inode** (same file data). Cannot cross filesystems; cannot link directories usually.

**Soft link (symlink)** — special file containing path to target. Can cross FS; can point to directories.

**Broken symlink** — target deleted/moved; `readlink` still shows path but open/read fails with ENOENT until relinked. Hard links keep data until all links removed.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides

</details>

<details><summary>Solution (JavaScript)</summary>

```bash
ln file.txt hardlink.txt
ln -s file.txt softlink.txt
rm file.txt   # softlink now broken; hardlink still works
```

#### Code walkthrough
Apply commands in a lab VM; explain output.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Permission denied — use sudo appropriately.

</details>

</article>

### Networking
<article>

What is the difference between HTTP and HTTPS?

<details><summary>Theory and explanation</summary>

**HTTP** — plaintext application protocol (default port 80). **HTTPS** — HTTP over **TLS**: encryption, integrity, server authentication (certificates). Port 443.

TLS handshake negotiates cipher, verifies cert chain, establishes session keys. Protects against eavesdropping and MITM (with valid PKI).

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides
- [Cloudflare Learning](https://www.cloudflare.com/learning/) — networking primers

</details>

<details><summary>Solution (JavaScript)</summary>

N/A — mention HSTS, cert expiry, Let's Encrypt.

#### Code walkthrough
Demonstrate troubleshooting sequence.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
IPv6-only vs IPv4 — clarify environment.

</details>

</article>
<article>

Define the following terms:

`CIDR` (Classless Inter-Domain Routing), `Gateway`, `NAT` (Network Address Translation)

<details><summary>Theory and explanation</summary>

**CIDR** — `192.168.1.0/24` notation; prefix length defines network/host bits; replaces classful A/B/C.

**Gateway** — router IP where host sends traffic for destinations outside local subnet (default route).

**NAT** — maps private IPs to public IP(s) on edge router; enables RFC1918 networks to reach internet; breaks end-to-end inbound unless port forwarding.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides
- [Cloudflare Learning](https://www.cloudflare.com/learning/) — networking primers

</details>

<details><summary>Solution (JavaScript)</summary>

```bash
ip route show default   # gateway
```

#### Code walkthrough
Demonstrate troubleshooting sequence.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
IPv6-only vs IPv4 — clarify environment.

</details>

</article>
<article>

What is an IP address? Why is it necessary?

<details><summary>Theory and explanation</summary>

**IP address** uniquely identifies a host on a network layer (IPv4 32-bit, IPv6 128-bit). Required for routing packets source→destination across interconnected networks.

Without IP (or equivalent), routers cannot forward datagrams between subnets/internet.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides
- [Cloudflare Learning](https://www.cloudflare.com/learning/) — networking primers

</details>

<details><summary>Solution (JavaScript)</summary>

N/A

#### Code walkthrough
Demonstrate troubleshooting sequence.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
IPv6-only vs IPv4 — clarify environment.

</details>

</article>
<article>

What is a firewall?

<details><summary>Theory and explanation</summary>

**Firewall** filters traffic by rules (IP, port, protocol, state). **Network firewall** at perimeter; **host firewall** (`iptables`, `ufw`, Windows Defender Firewall).

Stateful inspection tracks connections; default-deny inbound is best practice.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides
- [Cloudflare Learning](https://www.cloudflare.com/learning/) — networking primers

</details>

<details><summary>Solution (JavaScript)</summary>

```bash
sudo ufw status
sudo ufw allow 22/tcp
```

#### Code walkthrough
Demonstrate troubleshooting sequence.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
IPv6-only vs IPv4 — clarify environment.

</details>

</article>
<article>

What is a port? Name some commonly used service ports.

<details><summary>Theory and explanation</summary>

A **port** (16-bit) multiplexes services on one IP. Well-known: **22** SSH, **80** HTTP, **443** HTTPS, **53** DNS, **25** SMTP, **3306** MySQL, **5432** PostgreSQL.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides
- [Cloudflare Learning](https://www.cloudflare.com/learning/) — networking primers

</details>

<details><summary>Solution (JavaScript)</summary>

```bash
ss -tlnp   # listening TCP ports
```

#### Code walkthrough
Demonstrate troubleshooting sequence.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
IPv6-only vs IPv4 — clarify environment.

</details>

</article>
<article>

Define the following networking tools/commands:

`ping`, `traceroute`, `nslookup`

<details><summary>Theory and explanation</summary>

**ping** — ICMP echo request/reply; tests reachability and RTT.

**traceroute** (tracert) — maps path hops using TTL expiry.

**nslookup/dig** — DNS queries (A, AAAA, MX, PTR records).

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides
- [Cloudflare Learning](https://www.cloudflare.com/learning/) — networking primers

</details>

<details><summary>Solution (JavaScript)</summary>

```bash
ping -c 4 8.8.8.8
traceroute google.com
dig google.com A
```

#### Code walkthrough
Demonstrate troubleshooting sequence.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
IPv6-only vs IPv4 — clarify environment.

</details>

</article>
<article>

What is the difference between TCP and UDP?

<details><summary>Theory and explanation</summary>

**TCP** — connection-oriented, reliable, ordered, congestion control; overhead for handshake/retransmits. HTTP, SSH, DB.

**UDP** — datagrams, no guarantee of delivery/order; low latency. DNS, VoIP, QUIC (over UDP).

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides
- [Cloudflare Learning](https://www.cloudflare.com/learning/) — networking primers

</details>

<details><summary>Solution (JavaScript)</summary>

N/A

#### Code walkthrough
Demonstrate troubleshooting sequence.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
IPv6-only vs IPv4 — clarify environment.

</details>

</article>
<article>

A user says they can ping `8.8.8.8` but not `google.com`. What might be the problem? How can you resolve it?

<details><summary>Theory and explanation</summary>

IP works but **name resolution fails** — DNS misconfiguration, down resolver, `/etc/resolv.conf` wrong, corporate DNS block, local hosts file typo.

**Fix**: check `dig google.com`, verify DNS servers, flush cache (`systemd-resolve --flush-caches`), try alternate DNS (8.8.8.8).

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides
- [Cloudflare Learning](https://www.cloudflare.com/learning/) — networking primers

</details>

<details><summary>Solution (JavaScript)</summary>

```bash
ping 8.8.8.8
ping google.com
cat /etc/resolv.conf
dig google.com
```

#### Code walkthrough
Demonstrate troubleshooting sequence.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
IPv6-only vs IPv4 — clarify environment.

</details>

</article>
<article>

In a local network, there is no packet loss in communication. However, after connecting it to the external network and accessing it from outside, there is packet loss. What could be the possible reasons? How can this be resolved?

<details><summary>Theory and explanation</summary>

Common causes: **MTU/MSS mismatch** (fragmentation black hole), **asymmetric routing**, **NAT/firewall** dropping, **ISP congestion**, **QoS**, **DDoS mitigation** false positives.

**Fix**: lower MTU test (`ping -M do -s 1472`), check firewall/NAT timeouts, tcpdump on edge, verify port forwarding and reverse path.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides
- [Cloudflare Learning](https://www.cloudflare.com/learning/) — networking primers

</details>

<details><summary>Solution (JavaScript)</summary>

```bash
ping -M do -s 1472 remote.host
mtr remote.host
```

#### Code walkthrough
Demonstrate troubleshooting sequence.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
IPv6-only vs IPv4 — clarify environment.

</details>

</article>

### Linux
<article>

How can you create a user in Linux? Provide a command-line example.

<details><summary>Theory and explanation</summary>

User management via **useradd/usermod** or **adduser** (Debian interactive). Sets UID, home dir, shell, groups.

`useradd -m -s /bin/bash alice` then `passwd alice`. `/etc/passwd`, `/etc/shadow` store account metadata.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides

</details>

<details><summary>Solution (JavaScript)</summary>

```bash
sudo useradd -m -s /bin/bash alice
sudo passwd alice
id alice
```

#### Code walkthrough
Run examples on Ubuntu VM.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Distro differences — Debian vs RHEL package names.

</details>

</article>
<article>

How can you create a file in Linux? Provide a command-line example.

<details><summary>Theory and explanation</summary>

`touch file` creates empty or updates mtime. `echo 'hi' > file` writes content. `nano/vim` editors. Redirect `>` overwrite, `>>` append.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides

</details>

<details><summary>Solution (JavaScript)</summary>

```bash
touch notes.txt
echo 'Hello' > notes.txt
```

#### Code walkthrough
Run examples on Ubuntu VM.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Distro differences — Debian vs RHEL package names.

</details>

</article>
<article>

What is a shell? Provide some examples of common shells.

<details><summary>Theory and explanation</summary>

**Shell** — CLI interpreter executing commands, scripts, pipelines. Examples: **bash** (default Linux), **zsh**, **sh**, **fish**, **PowerShell** (cross-platform).

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides

</details>

<details><summary>Solution (JavaScript)</summary>

```bash
echo $SHELL
bash --version
```

#### Code walkthrough
Run examples on Ubuntu VM.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Distro differences — Debian vs RHEL package names.

</details>

</article>
<article>

What is the Linux file system hierarchy? Describe the purpose of the following directories:

`/`,  `/home`, `/var`, `/bin`, `/etc`, `/opt`, `/tmp`, `/usr`

<details><summary>Theory and explanation</summary>

**/** — root of hierarchy. **/home** — user home dirs. **/var** — variable data (logs, spool, cache). **/bin** — essential user binaries. **/etc** — config files. **/opt** — optional third-party software. **/tmp** — temp files (often cleared on reboot). **/usr** — read-only user programs, libraries, docs.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides

</details>

<details><summary>Solution (JavaScript)</summary>

```bash
ls -la / /home /var /etc
```

#### Code walkthrough
Run examples on Ubuntu VM.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Distro differences — Debian vs RHEL package names.

</details>

</article>
<article>

How can you find help in the Linux command line? Provide example commands.

<details><summary>Theory and explanation</summary>

**man** pages (`man ls`), **--help** flag, **info**, **apropos**/ **whatis** for keyword search, distribution docs (`/usr/share/doc`).

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides

</details>

<details><summary>Solution (JavaScript)</summary>

```bash
man grep
grep --help
apropos password
```

#### Code walkthrough
Run examples on Ubuntu VM.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Distro differences — Debian vs RHEL package names.

</details>

</article>
<article>

Provide example commands for the following:

`cd`, `cp`, `ls`, `grep`, `mv`

<details><summary>Theory and explanation</summary>

**cd** — change directory. **cp** — copy. **ls** — list. **grep** — search text patterns. **mv** — move/rename.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides

</details>

<details><summary>Solution (JavaScript)</summary>

```bash
cd /var/log
ls -lah
cp file.txt backup.txt
mv old.txt new.txt
grep -r ERROR /var/log/syslog
```

#### Code walkthrough
Run examples on Ubuntu VM.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Distro differences — Debian vs RHEL package names.

</details>

</article>
<article>

What are file permissions in Linux?

<details><summary>Theory and explanation</summary>

Unix **rwx** for owner, group, others (octal 755 etc.). **chmod** changes mode; **chown** owner/group. Special bits: setuid, setgid, sticky (e.g. /tmp).

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides

</details>

<details><summary>Solution (JavaScript)</summary>

```bash
ls -l file.txt
chmod 644 file.txt
chmod u+x script.sh
```

#### Code walkthrough
Run examples on Ubuntu VM.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Distro differences — Debian vs RHEL package names.

</details>

</article>
<article>

How can you monitor a process? Suppose you have a program and you need to check its status and restart it if it crashes. How can you do that?

<details><summary>Theory and explanation</summary>

**Monitor**: `ps`, `top`/`htop`, `systemctl status`, `journalctl`. **Auto-restart**: **systemd** unit with `Restart=on-failure`, or **supervisord**, **monit**, Kubernetes liveness probes.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides

</details>

<details><summary>Solution (JavaScript)</summary>

```ini
# /etc/systemd/system/myapp.service
[Service]
ExecStart=/usr/local/bin/myapp
Restart=on-failure
```

#### Code walkthrough
Run examples on Ubuntu VM.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Distro differences — Debian vs RHEL package names.

</details>

</article>
<article>

You have a file where you applied `chmod 777`, but still cannot modify it. What could be the possible reason?

<details><summary>Theory and explanation</summary>

**Immutable flag** (`chattr +i`), **SELinux/AppArmor** context, **read-only mount**, **NFS root squash**, file owned by different user (777 still allows all but immutable wins), **disk full**, editing via wrong user over SSH force command.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides

</details>

<details><summary>Solution (JavaScript)</summary>

```bash
lsattr file.txt
mount | grep 'ro,'
getenforce   # SELinux
```

#### Code walkthrough
Run examples on Ubuntu VM.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Distro differences — Debian vs RHEL package names.

</details>

</article>

### Other
<article>

What is the biggest accomplishment in your educational life? Explain why.

<details><summary>Theory and explanation</summary>

Behavioral question — STAR format: **Situation**, **Task**, **Action**, **Result**. Pick achievement showing leadership, persistence, or technical depth relevant to sysadmin (e.g. lab setup, competition, research). Tie to reliability and learning mindset Therap expects.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [Arch Linux Wiki](https://wiki.archlinux.org/) — Linux admin guides

</details>

<details><summary>Solution (JavaScript)</summary>

N/A — behavioral; no code.

#### Code walkthrough
Prepare 2-minute spoken answer.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Keep answer authentic and specific.

</details>

</article>


## 1st technical round

This interview was taken in therap office. Basic questions like what do you understand about system operations and why do want to join were asked. Some hands on tasks on ubuntu command line were also given

## 2nd technical round

This part was taken online. Both Bangladesh and USA team were presents. This round was also similar like the previous round.