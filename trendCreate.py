
import rrdtool
def create_rrdtool():
    ret = rrdtool.create("/home/koryto/Documentos/escom/redes3/Practica 3/RDD/trend.rrd",
                        "--start",'N',
                        "--step",'60',
                        "DS:CPUload:GAUGE:60:0:100",
                        "DS:RAMload:GAUGE:60:0:100",
                        "RRA:AVERAGE:0.5:1:2400")
    if ret:
        print (rrdtool.error())