# Traductor de Subtítulos

[![Estado del proyecto](https://img.shields.io/badge/Estado-Activo-brightgreen)](https://github.com/MartinMFM/subtitle-translator)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-blue)](https://github.com/MartinMFM/subtitle-translator/blob/main/LICENSE)

Este es un código de Python que te permite traducir subtítulos en formato SRT a otro idioma utilizando Google Translate. Puedes cambiar el idioma al que deseas traducir y el formato del archivo resultante.

## Funcionalidades

- **Traducción de subtítulos**: El código utiliza la biblioteca `googletrans` para traducir el contenido de los archivos de subtítulos al idioma especificado. Puedes proporcionar una carpeta con múltiples archivos de subtítulos y el código los traducirá por separado.

- **División automática de archivos largos**: Si un archivo supera el límite de 5000 caracteres (límite de Google Translate), se dividirá en bloques más pequeños y se traducirán individualmente para evitar exceder el límite.

- **Personalización del idioma y formato**: Puedes cambiar el idioma al que deseas traducir modificando el valor de la variable `lang` en el código. Asimismo, puedes especificar el formato del archivo resultante cambiando el valor de la variable `ext`. Por defecto, se utiliza el formato SRT.

## Requisitos

Antes de ejecutar el código, asegúrate de tener instaladas las siguientes dependencias:

- **Python**: Asegúrate de tener Python instalado en tu sistema. Puedes descargar la última versión de Python desde el sitio web oficial: [python.org](https://www.python.org).

- **googletrans**: Es una biblioteca de Python que proporciona una interfaz para la API de Google Translate. Puedes instalarlo utilizando el gestor de paquetes `pip`. Ejecuta el siguiente comando en tu terminal o línea de comandos para instalarlo:

`pip install googletrans==4.0.0-rc1`



## Uso

1. Ejecución del código:
 - Ejecuta el código en Python utilizando un entorno de desarrollo o una terminal.

2. Ruta de la carpeta con los archivos de subtítulos:
 - Se te pedirá que introduzcas la ruta de la carpeta que contiene los archivos de subtítulos a traducir. Asegúrate de proporcionar una ruta válida.

3. Especificación del idioma de traducción:
 - Elige el idioma al que deseas traducir los subtítulos. Puedes cambiar el valor de la variable `lang` en el código para especificar el idioma deseado. Por ejemplo, `lang = 'es'` para traducir al español.

4. Especificación del formato del archivo resultante:
 - Puedes especificar el formato del archivo resultante cambiando el valor de la variable `ext` en el código. Por defecto `ext = 'srt'`.

5. Inicio de la traducción de los archivos:
 - El código comenzará a traducir los archivos de subtítulos y guardará los archivos traducidos en la misma carpeta con un sufijo que indica el idioma de destino.
 
¡Disfruta traduciendo tus subtítulos con facilidad usando este código!

## Responsabilidad

Este programa se proporciona "tal cual" y sin garantía de ningún tipo. El autor no asume ninguna responsabilidad por el uso que se le dé al programa ni por cualquier consecuencia derivada de su uso. El usuario es el único responsable de verificar la legalidad y la conformidad con los derechos de autor de los archivos que se traduzcan utilizando este programa.

Se recomienda utilizar este programa de acuerdo con las leyes y regulaciones aplicables en tu jurisdicción y respetar los derechos de autor de los contenidos traducidos.

El autor no se hace responsable de ningún daño directo, indirecto, incidental, especial, ejemplar o consecuente que surja del uso de este programa.

## Licencia

Este proyecto se encuentra bajo la licencia MIT. Puedes consultar el archivo [LICENSE](./LICENSE) para obtener más información.
