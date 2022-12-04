from django.shortcuts import render

# Create your views here.

def detct_port():
    import nmap3 
    nm = nmap3.Nmap()
    results = nm.scan_top_ports('186.121.249.109')
    print(results)

def 