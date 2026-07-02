import subprocess

iprange = input("Enter network (Example: 192.168.1.): ")

filename = input("Enter output filename: ")

if not iprange.endswith("."):
    iprange += "."

if not filename.endswith(".txt"):
    filename += ".txt"

active_ips = []

for i in range(1,225):
    ip = iprange + str(i)

    result = subprocess.run(
        ["ping", "-n", "1", "-w", "20", ip],
        stdout=subprocess.DEVNULL
    )

    if result.returncode == 0:
        print(ip)
        active_ips.append(ip)

with open(filename, "w") as file:
    for ip in active_ips:
        file.write(ip + "\n")

print(f"\nDone >> {len(active_ips)} IPs saved to {filename}")