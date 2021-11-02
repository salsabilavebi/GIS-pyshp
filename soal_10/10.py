import shapefile
w=shapefile.Writer()
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")


w.record("pati","satu")
w.record("crot","dua")
w.record("crek","tiga")
w.record("cfot","empat")
w.record("crat","lima")
w.record("crit","enam")

w.poly(parts=[[[1,6],[5.5,6], [5.5,10],[1,10], [1,6]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[1,5],[5.5,5], [5.5,1],[1,1], [1,5]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[11,6],[6.5,6], [6.5,10],[11,10], [11,6]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[16,6],[12,6], [12,9],[16,9], [16,6]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[16,1],[12,1], [12,5],[16,5], [16,1]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[21,5],[17,5], [17,9],[21,9], [21,5]]],shapeType=shapefile.POLYLINE)
 
w.save("soal10")