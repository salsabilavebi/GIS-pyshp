import shapefile
w=shapefile.Writer(shapeType=1)
w.shapeType
w.shapeType=3
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")

w.line([[[1,3],[2,5]]])


w.save("soal3")
