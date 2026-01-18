def network_layer_checker(protocol):
    p = protocol.lower()
    if p in ['smtp', 'imap', 'https', 'http', 'ftp']:
        print("APPLICATION LAYER")
    elif p in ['tcp', 'udp']:
        print("TRANSPORT LAYER")
    elif p in ['ip', 'icmp']:
        print("NETWORK LAYER")
    elif p in ['arp', 'rarp', 'ethernet']:
        print("DATA LINK LAYER")
    else:
        print("Protocol not found")    

def network_layer_definition(protocol):
    p = protocol.lower()
    if p == 'http':
        print("HTTP is used for web pages and web communication.")
    elif p == 'https':
        print("HTTPS is secure HTTP with encryption.")
    elif p == 'ftp':
        print("FTP is used to transfer files over a network.")
    elif p == 'smtp':
        print("SMTP is used for sending emails.")
    elif p == 'imap':
        print("IMAP is used to retrieve emails from a server.")
    elif p == 'tcp':
        print("TCP provides reliable end-to-end delivery of data.")
    elif p == 'udp':
        print("UDP provides fast, connectionless delivery of data.")
    elif p == 'ip':
        print("IP handles routing and logical addressing of packets.")
    elif p == 'icmp':
        print("ICMP is used for error messages and diagnostics.")
    elif p == 'arp':
        print("ARP converts IP address to MAC address.")
    elif p == 'rarp':
        print("RARP converts MAC address to IP address.")
    elif p == 'ethernet':
        print("Ethernet handles MAC addressing and node-to-node delivery.")
    else:
        print("No description found for this protocol.")

while True:
    print("\nNETWORK LAYER ANALYSIS")
    print("*************************")
    print("1. NETWORK LAYER CHECKER")
    print("2. PROTOCOL ANALYSIS")
    print("3. EXIT")

    ch = input("Enter your choice: ")
    
    if not ch.isdigit():
        print("Please enter a valid number.")
        continue
    ch = int(ch)

    if ch == 3:
        print("Exiting program. Goodbye! ")
        break
    elif ch in [1, 2]:
        protocol = input("Enter the protocol: ")
        if ch == 1:
            network_layer_checker(protocol)
        elif ch == 2:
            network_layer_definition(protocol)
    else:
        print("Invalid choice. Try again.")
