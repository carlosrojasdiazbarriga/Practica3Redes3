
import time
import rrdtool
from getSNMP import consultaSNMP
import sys

comunidad = sys.argv[1]
host = sys.argv[2]


def updateSNMP(comunidad,host):
    rrdpath = '/home/koryto/Documentos/escom/redes3/Practica 3/RDD/'
    carga_CPU = 0

    while 1:
        carga_CPU = float(consultaSNMP(comunidad,host,'1.3.6.1.4.1.2021.11.9.0'))
        mem_total = int(consultaSNMP(comunidad,host,'1.3.6.1.4.1.2021.4.5.0'))
        mem_free = int(consultaSNMP(comunidad,host,'1.3.6.1.4.1.2021.4.11.0'))

        porcentaje = (1-(mem_free)/(mem_total))*100

        valor = "N:" + str(carga_CPU) + ':' + str(porcentaje)
        print (valor)
        rrdtool.update(rrdpath+'trend.rrd', valor)
        time.sleep(5)

updateSNMP(comunidad,host)