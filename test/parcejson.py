import platform
import subprocess
import nmap3
def detct_port(ip):
    nm = nmap3.NmapScanTechniques()
    results = nm.nmap_tcp_scan(ip)

    print(results)

print(detct_port("youtube.com"))

# Parcer por la IP
# Sugerencia: Obtener la IP del dominio con el ping y esa IP tomarla como argumento para la función
