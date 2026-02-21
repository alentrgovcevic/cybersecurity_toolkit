import socket

class Scanner:
    def __init__(self, target_ip):
        self.target = target_ip
        self.results = []

    def scan_common_ports(self):
        common_ports = {21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS"}
        
        for port, service in common_ports.items():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((self.target, port))
            
            # Store data in a structured way for the "Software" to read
            self.results.append({
                "port": port,
                "service": service,
                "status": "Open" if result == 0 else "Closed"
            })
            s.close()
        
        return self.results # This list can be sent to a website frontend
