# mananera
¡Un archivo para webscraping de las mañaneras!

Este proyecto usa el API de YouTube para hacer webscraping de las conferencias matutinas (“mañaneras”) de Claudia Sheinbaum, recolectando datos de cada semana.

## 🎯 Objetivo principal

Analizar si las personas que comentan e interactúan con los videos se mantienen constantes durante la semana o van cambiando. Esto permite explorar:

- Patrones de participación digital
- Audiencia recurrente vs. espontánea
- Posibles indicios de comportamiento automatizado (bots)

A futuro, estos resultados también podrían utilizarse para estudiar **sentimiento**, dependiendo del tipo de audiencia y comentarios.

## ⚙️ ¿Cómo usarlo?

1. Clona el repositorio
2. Crea tu archivo .env con tu clave API de YouTube
YOUTUBE_API_KEY=tu_clave_aqui
3. Instala los paquetes necesarios desde requirements.txt
4. Ejecuta el script

📦 Salida esperada
El archivo data/comments.csv contendrá las siguientes columnas:

video_id: ID del video

author_id: ID único del autor

comment_id: ID del comentario

comment_txt: Texto del comentario

published_at: Fecha y hora de publicación



