Conversor de Video a Audio en Python
Este programa en Python utiliza la biblioteca pydub y la interfaz gráfica de usuario tkinter para convertir archivos de video a archivos de audio .mp3.

Instalación
Antes de ejecutar el programa, asegúrate de tener instaladas las bibliotecas pydub y tkinter. Si no las tienes instaladas, puedes instalarlas usando pip:

sh
Copy code
pip install pydub
pip install tkinter
Además, debes tener instalado ffmpeg, que es utilizado por pydub para trabajar con archivos de audio y video. Puedes descargar ffmpeg de su sitio oficial: https://ffmpeg.org/download.html

Uso
Para ejecutar el programa, sigue los siguientes pasos:

Ejecuta el archivo video_to_audio.py con Python.

Se abrirá una ventana de diálogo para que selecciones la carpeta donde se encuentran los archivos de video que deseas convertir.

El programa buscará en la carpeta seleccionada todos los archivos de video con las extensiones .3gpp, .flv, .webm y .mp4, y los convertirá en archivos de audio .mp3.

Los archivos de audio convertidos se guardarán en la misma carpeta que los archivos de video originales, con el mismo nombre pero con la extensión .mp3.

Cuando el proceso de conversión haya finalizado, se mostrará un mensaje indicando que la conversión ha sido completada.

Contribución
Si deseas contribuir al programa, siéntete libre de crear una solicitud de extracción (pull request) o abrir un problema (issue) en el repositorio.
