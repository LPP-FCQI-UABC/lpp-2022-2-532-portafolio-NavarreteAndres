archivo=open("grupo.txt", "r+")
archivo.write("AVALOS GODOY LEONARDO 1282003")
archivo.write("BECERRA PERAZA ERICK ARTURO 1262844")
archivo.write("BRAMBILA MOLINA LUIS ADRIAN 1264791")
archivo.write("CASTRO ANTONIO BRANDON ALBERTO 1284997")
archivo.write("CASTRO ANTONIO BRANDON ALBERTO 1284997")
archivo.write("DE LA CRUZ CHAVEZ JOSE EDUARDO 1282778")
archivo.write("ESPINO NUÑEZ SHERLYN 1281160")
archivo.write("GUERRA CERVANTES OMAR EDUARDO 1281859")
archivo.write("GUERRA HABANA JOSE GUSTAVO 1273586")
archivo.write("GUTIERREZ SANCHEZ VALERIA KAREY 1282379")
archivo.write("GUTIÉRREZ RUIZ FRANCISCO GABRIEL 1261897")
archivo.write("MACHADO MERAZ ULISES JOEL 1261836")
archivo.write("MENDOZA NAVARRO BRANDON ABRAHAM 1282292")
archivo.write("PINEDA RAMIREZ JAFET JACOB 1273987")
archivo.write("RAMIREZ SANCHEZ ANGEL ALEJANDRO 1282041")
archivo.write("RODRIGUEZ CANDIA VICTOR MANUEL 1259644")
archivo.write("RODRIGUEZ ROSAS LUIS ENRIQUE 1275919")
archivo.write("SANCHEZ ZARAGOZA EDUARDO ARTURO 1280942")
archivo.write("SEGURA SOLIS VALENTINA 1282007")
archivo.write("VELARDE MORALES LUIS EMILIO 1273159")
lista_estudiantes=archivo.readlines()
archivo.close()
print(lista_estudiantes)