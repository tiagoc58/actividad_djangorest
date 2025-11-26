# poblar_datos.py
# Ejecutar con: python3 manage.py shell < poblar_datos.py

from biblioteca.models import Autor, Libro, Resena

# Crear autores
autor1 = Autor.objects.create(nombre="Gabriel Garcia Marquez", nacionalidad="Colombiana", edad="87")
autor2 = Autor.objects.create(nombre="Isabel Allende", nacionalidad="Chilena", edad="73")
autor3 = Autor.objects.create(nombre="Jorge Luis Borges", nacionalidad="Argentina", edad="86")
autor4 = Autor.objects.create(nombre="Mario Vargas Llosa", nacionalidad="Peruana", edad="88")
autor5 = Autor.objects.create(nombre="Gabriela Mistral", nacionalidad="Chilena", edad="80")

# Crear libros para autor1 (Gabriel Garcia Marquez)
libro1_1 = Libro.objects.create(titulo="Cien años de soledad", autor=autor1, fecha_publicacion="1967-06-05", resumen="Novela emblemática del realismo mágico.")
libro1_2 = Libro.objects.create(titulo="El amor en los tiempos del cólera", autor=autor1, fecha_publicacion="1985-09-05", resumen="Historia de amor a lo largo de décadas.")
libro1_3 = Libro.objects.create(titulo="Crónica de una muerte anunciada", autor=autor1, fecha_publicacion="1981-05-01", resumen="Relato breve sobre honor y destino.")
libro1_4 = Libro.objects.create(titulo="El coronel no tiene quien le escriba", autor=autor1, fecha_publicacion="1961-03-01", resumen="Retrato de la espera y la dignidad.")
libro1_5 = Libro.objects.create(titulo="Del amor y otros demonios", autor=autor1, fecha_publicacion="1994-01-01", resumen="Novela sobre lo profano y lo sagrado.")

# Crear libros para autor2 (Isabel Allende)
libro2_1 = Libro.objects.create(titulo="La casa de los espíritus", autor=autor2, fecha_publicacion="1982-01-01", resumen="Saga familiar con toques de realismo mágico.")
libro2_2 = Libro.objects.create(titulo="Eva Luna", autor=autor2, fecha_publicacion="1987-01-01", resumen="Historias contadas por una narradora excepcional.")
libro2_3 = Libro.objects.create(titulo="Paula", autor=autor2, fecha_publicacion="1994-01-01", resumen="Memorias íntimas y dolorosas.")
libro2_4 = Libro.objects.create(titulo="Hija de la fortuna", autor=autor2, fecha_publicacion="1999-01-01", resumen="Aventura y búsqueda personal.")
libro2_5 = Libro.objects.create(titulo="Inés del alma mía", autor=autor2, fecha_publicacion="2006-01-01", resumen="Novela histórica basada en hechos reales.")

# Crear libros para autor3 (Jorge Luis Borges)
libro3_1 = Libro.objects.create(titulo="Ficciones", autor=autor3, fecha_publicacion="1944-01-01", resumen="Colección de relatos cortos laberínticos.")
libro3_2 = Libro.objects.create(titulo="El Aleph", autor=autor3, fecha_publicacion="1949-01-01", resumen="Relatos que exploran el infinito y la memoria.")
libro3_3 = Libro.objects.create(titulo="El hacedor", autor=autor3, fecha_publicacion="1960-01-01", resumen="Antología de poemas y relatos breves.")
libro3_4 = Libro.objects.create(titulo="Historia universal de la infamia", autor=autor3, fecha_publicacion="1935-01-01", resumen="Relatos basados en hechos o leyendas.")
libro3_5 = Libro.objects.create(titulo="Otras inquisiciones", autor=autor3, fecha_publicacion="1952-01-01", resumen="Ensayos y críticas literarias.")

# Crear libros para autor4 (Mario Vargas Llosa)
libro4_1 = Libro.objects.create(titulo="La ciudad y los perros", autor=autor4, fecha_publicacion="1963-01-01", resumen="Novela sobre la vida en una academia militar.")
libro4_2 = Libro.objects.create(titulo="Conversación en La Catedral", autor=autor4, fecha_publicacion="1969-01-01", resumen="Novela sobre política y memoria.")
libro4_3 = Libro.objects.create(titulo="La casa verde", autor=autor4, fecha_publicacion="1966-01-01", resumen="Relatos que entrelazan personajes y destinos.")
libro4_4 = Libro.objects.create(titulo="El héroe discreto", autor=autor4, fecha_publicacion="2013-01-01", resumen="Comedia y tragedia en el Perú contemporáneo.")
libro4_5 = Libro.objects.create(titulo="El sueño del celta", autor=autor4, fecha_publicacion="2010-01-01", resumen="Biografía novelada de un personaje histórico.")

# Crear libros para autor5 (Gabriela Mistral)
libro5_1 = Libro.objects.create(titulo="Desolación", autor=autor5, fecha_publicacion="1922-01-01", resumen="Poemario sobre pérdida y duelo.")
libro5_2 = Libro.objects.create(titulo="Ternura", autor=autor5, fecha_publicacion="1924-01-01", resumen="Poesía breve y emotiva.")
libro5_3 = Libro.objects.create(titulo="Lagar", autor=autor5, fecha_publicacion="1954-01-01", resumen="Poesía adulta y reflexiva.")
libro5_4 = Libro.objects.create(titulo="Poema de Chile", autor=autor5, fecha_publicacion="1967-01-01", resumen="Himno poético a la nación.")
libro5_5 = Libro.objects.create(titulo="Lecturas para Mujeres", autor=autor5, fecha_publicacion="1934-01-01", resumen="Textos y ensayos.")

# Crear 2 reseñas por libro (autor1 libros)
resena1_1_1 = Resena.objects.create(libro=libro1_1, texto="Magnífica, un clásico que no envejece.", calificacion=5)
resena1_1_2 = Resena.objects.create(libro=libro1_1, texto="Me costó al principio pero valió la pena.", calificacion=4)

resena1_2_1 = Resena.objects.create(libro=libro1_2, texto="Romántica y profunda.", calificacion=5)
resena1_2_2 = Resena.objects.create(libro=libro1_2, texto="No es mi favorita pero reconocible.", calificacion=3)

resena1_3_1 = Resena.objects.create(libro=libro1_3, texto="Corta y absorbente.", calificacion=5)
resena1_3_2 = Resena.objects.create(libro=libro1_3, texto="Muy bien escrita, recomendable.", calificacion=4)

resena1_4_1 = Resena.objects.create(libro=libro1_4, texto="Intensa y conmovedora.", calificacion=4)
resena1_4_2 = Resena.objects.create(libro=libro1_4, texto="El lenguaje es impecable.", calificacion=5)

resena1_5_1 = Resena.objects.create(libro=libro1_5, texto="Interesante mezcla de temas.", calificacion=4)
resena1_5_2 = Resena.objects.create(libro=libro1_5, texto="Un estilo particular y rico.", calificacion=4)

# Reseñas autor2
resena2_1_1 = Resena.objects.create(libro=libro2_1, texto="Saga familiar inolvidable.", calificacion=5)
resena2_1_2 = Resena.objects.create(libro=libro2_1, texto="Me emocionó profundamente.", calificacion=5)

resena2_2_1 = Resena.objects.create(libro=libro2_2, texto="Narración cautivadora.", calificacion=4)
resena2_2_2 = Resena.objects.create(libro=libro2_2, texto="Personajes memorables.", calificacion=4)

resena2_3_1 = Resena.objects.create(libro=libro2_3, texto="Muy personal y sentido.", calificacion=4)
resena2_3_2 = Resena.objects.create(libro=libro2_3, texto="Duro pero hermoso.", calificacion=5)

resena2_4_1 = Resena.objects.create(libro=libro2_4, texto="Aventura y crecimiento.", calificacion=4)
resena2_4_2 = Resena.objects.create(libro=libro2_4, texto="Bien documentado.", calificacion=3)

resena2_5_1 = Resena.objects.create(libro=libro2_5, texto="Historia bien reconstruida.", calificacion=4)
resena2_5_2 = Resena.objects.create(libro=libro2_5, texto="Muy recomendable para amantes de la historia.", calificacion=5)

# Reseñas autor3
resena3_1_1 = Resena.objects.create(libro=libro3_1, texto="Relatos que desafían la lógica.", calificacion=5)
resena3_1_2 = Resena.objects.create(libro=libro3_1, texto="Brillante y enigmático.", calificacion=5)

resena3_2_1 = Resena.objects.create(libro=libro3_2, texto="Impresionante manejo de la imaginación.", calificacion=5)
resena3_2_2 = Resena.objects.create(libro=libro3_2, texto="Cargado de símbolos y sentido.", calificacion=4)

resena3_3_1 = Resena.objects.create(libro=libro3_3, texto="Breves y profundos.", calificacion=4)
resena3_3_2 = Resena.objects.create(libro=libro3_3, texto="Para releer varias veces.", calificacion=5)

resena3_4_1 = Resena.objects.create(libro=libro3_4, texto="Historias curiosas y oscuras.", calificacion=4)
resena3_4_2 = Resena.objects.create(libro=libro3_4, texto="Muy original.", calificacion=4)

resena3_5_1 = Resena.objects.create(libro=libro3_5, texto="Ensayos que invitan a la reflexión.", calificacion=4)
resena3_5_2 = Resena.objects.create(libro=libro3_5, texto="Lectura densa pero valiosa.", calificacion=3)

# Reseñas autor4
resena4_1_1 = Resena.objects.create(libro=libro4_1, texto="Cruda y realista.", calificacion=5)
resena4_1_2 = Resena.objects.create(libro=libro4_1, texto="Un inicio potente de su obra.", calificacion=4)

resena4_2_1 = Resena.objects.create(libro=libro4_2, texto="Compleja y profunda.", calificacion=5)
resena4_2_2 = Resena.objects.create(libro=libro4_2, texto="Requiere paciencia pero recompensa.", calificacion=4)

resena4_3_1 = Resena.objects.create(libro=libro4_3, texto="Tramas bien entrelazadas.", calificacion=4)
resena4_3_2 = Resena.objects.create(libro=libro4_3, texto="Personajes inolvidables.", calificacion=5)

resena4_4_1 = Resena.objects.create(libro=libro4_4, texto="Divertida y crítica.", calificacion=4)
resena4_4_2 = Resena.objects.create(libro=libro4_4, texto="Buena prosa y ritmo.", calificacion=4)

resena4_5_1 = Resena.objects.create(libro=libro4_5, texto="Interesante reconstrucción histórica.", calificacion=4)
resena4_5_2 = Resena.objects.create(libro=libro4_5, texto="Bien documentada.", calificacion=3)

# Reseñas autor5
resena5_1_1 = Resena.objects.create(libro=libro5_1, texto="Poesía que toca el alma.", calificacion=5)
resena5_1_2 = Resena.objects.create(libro=libro5_1, texto="Profunda y conmovedora.", calificacion=5)

resena5_2_1 = Resena.objects.create(libro=libro5_2, texto="Sencilla y poderosa.", calificacion=4)
resena5_2_2 = Resena.objects.create(libro=libro5_2, texto="Versos que perduran.", calificacion=4)

resena5_3_1 = Resena.objects.create(libro=libro5_3, texto="Madura y reflexiva.", calificacion=4)
resena5_3_2 = Resena.objects.create(libro=libro5_3, texto="Una voz única.", calificacion=5)

resena5_4_1 = Resena.objects.create(libro=libro5_4, texto="Patriótico y poético.", calificacion=4)
resena5_4_2 = Resena.objects.create(libro=libro5_4, texto="Evoca paisajes y recuerdos.", calificacion=4)

resena5_5_1 = Resena.objects.create(libro=libro5_5, texto="Interesantes reflexiones.", calificacion=3)
resena5_5_2 = Resena.objects.create(libro=libro5_5, texto="Útil y evocador.", calificacion=3)