#pgzero

"""
Version actual: [M7.L1: Actividad #1]

Kodland: https://kenney.nl/assets/roguelike-caves-dungeons
packs de assets: https://kenney.nl/assets/series:Tiny?sort=update
"""

# Ventana de juego hecha de celdas
celda = Actor('border') # Celda que voy a utilizar como referencia para mi mapa

cant_celdas_ancho = 5 # Ancho del mapa (en celdas)
cant_celdas_alto = 5 # Altura del mapa (en celdas)

WIDTH =  celda.width  * cant_celdas_ancho # Ancho de la ventana (en píxeles)
HEIGHT = celda.height * cant_celdas_alto  # Alto de la ventana (en píxeles)

TITLE = "Rogue-like: Mazmorras" # Título de la ventana de juego
FPS = 30 # Número de fotogramas por segundo