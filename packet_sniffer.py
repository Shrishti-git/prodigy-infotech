from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto

        print(f"Packet: {src_ip} -> {dst_ip} | Protocol: {proto}")

        if packet.haslayer(TCP):
            print("   - TCP Packet")
        elif packet.haslayer(UDP):
            print("   - UDP Packet")

        if packet.haslayer("Raw"):
            try:
                payload = packet["Raw"].load
                print(f"   - Payload: {payload}")
            except:
                print("   - Payload: [Unreadable]")

def main():
    print("Starting packet capture (Press Ctrl+C to stop)...")
    sniff(filter="ip", prn=process_packet, store=False)

if __name__ == "__main__":
    main()
