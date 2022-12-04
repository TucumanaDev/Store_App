from django.shortcuts import render
import nmap3 
import subprocess
import platform
# Create your views here.

def pingIP(request):
    scan = ""
    open_ports = []
    if request.method == "POST":
        ip = request.POST["ip"]
        scan = scan_ip(ip)
        print(scan)
        if scan != "": #redundancia con la funcion de ping
            open_ports = detct_port(ip)
        else:
            open_ports = []
    
    return render(request, "scanning/Scannig.html", {"scan" : scan, "ports": open_ports})

def detct_port(ip):
    nm = nmap3.NmapScanTechniques()
    results = nm.nmap_tcp_scan(ip)

    ports = results[ip]["ports"]
    open_ports = []
    for port in ports:
        open_ports.append(port.get("portid") + " : " + port["service"]["name"])
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
        return("No fue posible realizar la conexion")
        #puede que haya redundancia con el if del renderizado del template
    else:
        return("Conexión exitosa con la maquina")

