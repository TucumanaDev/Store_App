import nmap3 
import platform
import subprocess
import re

def detct_port(ip):
    nm = nmap3.NmapScanTechniques()
    results = nm.nmap_tcp_scan(ip)

    ports = results[ip]["ports"]

    open_ports = []
    for port in ports:
        open_ports.append(port.get("portid") + " : " + port["service"]["name"])
        #Nota: Poner los puertos que se iteran por el for en una lista poara luego mostrarla como lista desordenada en el template
    return open_ports


def scan_ip(ip):
    option = ""

    if platform.system().lower() == "windows":
        option = "-n"
    else:
        option = "-c"
    
    command = ["ping", option, "4", ip]
    output_ping = subprocess.run(command, capture_output=True, text=True).stdout.strip("\n")
    
    if "timed out" in output_ping:
        return("No fue posible realizar la conexión")
    else:
        return(output_ping)

    
    
def valid_ip(ip):
    validation = re.match(r'(\ d {1,3} \. \ d {1,3} \. \ d {1,3} \. \ d {1,3})', ip)
    print(validation)
    
valid_ip("8.8.8.8")