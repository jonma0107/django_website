<!-- <div align="center">
  
![image](https://github.com/user-attachments/assets/7ec5b32a-6592-4485-b7f6-f8ee7c4e9285)

</div> -->

## Uso de Amazon S3 para Almacenamiento de Archivos no Cargados en Vercel
Vercel tiene limitaciones en el almacenamiento y manejo de archivos grandes, especialmente para cargas dinámicas y almacenamiento persistente.
Usar Amazon S3 para almacenar archivos que Vercel no puede manejar garantiza una solución confiable y eficiente
para aplicaciones que requieren manejo de archivos estáticos y dinámicos.

![image](https://github.com/user-attachments/assets/5873f0ca-f560-46b8-bf68-7b98a68ce106)

Me gustaría recomendar una plataforma que también es adecuada para implementar servicios Python: Leapcell

Puede implementar una aplicación Django Python en Leapcell con solo unos pocos clics.

1. Cree un servicio en el panel de Leapcell y conecte su nuevo repositorio

Vaya al panel de Leapcell y haga clic en el botón `New Service`.

![image](https://docs.leapcell.io/assets/images/create-service-9a71984444806ed95e71e603c6e12484.png)

Para acceder a sus repositorios, deberá conectar Leapcell a su cuenta de GitHub.

Cuando estés en la página "Crear servicio" , hay un botón "Conectarse a Github".

Al hacer clic aquí, se abrirá una ventana emergente de autorización de GitHub.

![image](https://docs.leapcell.io/assets/images/connect-btn-3264f1a3fc61d0e28235200359e117ce.png)

Una vez conectado, sus repositorios aparecerán en la lista.


En la página "Nuevo servicio", seleccione el repositorio que acaba de bifurcar.

![image](https://docs.leapcell.io/assets/images/select-repo-e7109782f416e2b04a85f97cebb16fc8.png)

2. Proporcione los siguientes valores durante la creación

> [!NOTE]
> Usaremos Gunicorn para ejecutar la aplicación Django, así que asegúrese de agregarlo gunicorna su requirements.txt.

A continuación se muestran los detalles de configuración básicos para configurar un servicio Django en Leapcell:

| CAMPO | VALOR |
| --- | --- |
| Runtime | Python (cualquier versión) |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn myproject.wsgi --bind 0.0.0.0:8080` |
| Port | `8080` |

<!-- Fuente para hacer TABLAS : https://docs.github.com/es/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables -->

Introduzca estos valores en los campos correspondientes.

![image](https://docs.leapcell.io/assets/images/deploy-config-2ce58d877e45de905804178899f73bc7.png)

3. Accede a tu aplicación

Una vez implementado, debería ver una URL como la que aparece foo-bar.leapcell.deven la página de Implementación. Visite el dominio que se muestra en la página de servicio.

![image](https://docs.leapcell.io/assets/images/deploy-result-e5fd0fd191a1a02b0155d428daad52ea.png)

El Resultado:

https://jonathameza.leapcell.app/en/

Link de Leapcell:

https://leapcell.io/
