import subprocess

# subprocess.run(
#     ['ifconfig', 'eth0'],shell=True)

# if __name__ == "__main__":
#     print("Shutting down the interface")

if __name__ == "__main__":
    interface = "eth0"
    new_mac = "00:44:55:66:77:88"
    # print("Shutting down the interface")
    subprocess.run(['ifconfig', 'eth0', 'down'])
    # print("Changing the interface hw address of ",interface, " to ", new_mac)
    subprocess.run(['ifconfig',interface, "hw", "ether", new_mac])
    # print("MAC address changed to ", new_mac)
    subprocess.run(["ifconfig", interface, "up"])

    # print("Network interface turned on")