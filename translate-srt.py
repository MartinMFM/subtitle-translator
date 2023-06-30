import os
from googletrans import Translator

def traducir_archivo(archivo_entrada, lang, ext):
    translator = Translator()
    nombre_archivo = os.path.basename(archivo_entrada)
    nombre_archivo_sin_extension = os.path.splitext(nombre_archivo)[0]
    carpeta_destino = os.path.dirname(archivo_entrada)
    archivo_destino = os.path.join(carpeta_destino, f"{nombre_archivo_sin_extension}_{lang}.{ext}")

    with open(archivo_entrada, 'r', encoding='utf-8') as archivo_entrada:
        texto = archivo_entrada.read()

    print("== Traducción de Archivo ==")
    print(f"Archivo de origen: {nombre_archivo}")
    print(f"Número de caracteres del archivo: {len(texto)}")
    print("")

    if len(texto) > 5000:
        print("El archivo supera el límite de caracteres. Dividiendo en bloques.")
        bloques = [texto[i:i+5000] for i in range(0, len(texto), 5000)]
        traducciones = [translator.translate(bloque, dest=lang).text for bloque in bloques]
        texto_traducido = ' '.join(traducciones)
    else:
        texto_traducido = translator.translate(texto, dest=lang).text

    texto_traducido = texto_traducido.replace("->", "-->")
    texto_traducido = texto_traducido.replace(": ", ":")
    texto_traducido = texto_traducido.replace("--->", "-->")

    with open(archivo_destino, 'w', encoding='utf-8') as archivo_destino:
        archivo_destino.write(texto_traducido)

    print(f"El archivo traducido ha sido guardado como:\n{nombre_archivo_sin_extension}_{lang}.{ext}")
    print("=============================")
    print("")

# Solicitar la ruta de la carpeta con los archivos de origen al usuario
carpeta_origen = input("Introduce la ruta de la carpeta con los archivos de origen: ")

# Verificar si la ruta es válida
if not os.path.isdir(carpeta_origen):
    print("La ruta proporcionada no es una carpeta válida.")
    exit()

archivos_a_traducir = [archivo for archivo in os.listdir(carpeta_origen) if archivo.lower().endswith('.srt')]

lang = 'es'  # Cambia 'es' por el idioma deseado
ext = 'srt'  # Cambia 'srt' por el tipo de formato deseado

print("=============================")
print("Iniciando Traducción de Archivos")
print("=============================")
print("")

for archivo in archivos_a_traducir:
    archivo_entrada = os.path.join(carpeta_origen, archivo)
    traducir_archivo(archivo_entrada, lang, ext)
