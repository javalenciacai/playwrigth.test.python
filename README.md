# TestBoost

[![CI](https://github.com/javalenciacai/playwrigth.test.python/actions/workflows/main.yml/badge.svg)](https://github.com/javalenciacai/playwrigth.test.python/actions/workflows/main.yml)

[![Python unittest](https://github.com/javalenciacai/playwrigth.test.python/actions/workflows/python-unitest.yml/badge.svg)](https://github.com/javalenciacai/playwrigth.test.python/actions/workflows/python-unitest.yml)

### [Report](https://javalenciacai.github.io/playwrigth.test.python/report.html)

### [ReportAPI](https://javalenciacai.github.io/playwrigth.test.python/reportAPI.html)


## Inicio rápido

* instalar dependencias

        pip install -r requirements.txt

 * Instalar navegadores

        playwright install


* Ejecutar todos los test

        ptest

* Ejecutar con formato html basico

        pytest --html=src/report/report.html --self-contained-html

#### para correr los test con otro formato html
    pip install pytest-reporter-html1
    pytest --template=html1/index.html --report=report.htm 

#### para correr los unittest
    python -m unittest discover \src
____________________________

# Documentación

## ¡Con TestBoost, tus pruebas nunca volverán a ser las mismas!

### I. Introducción
####   - ¿Qué es el proyecto de pruebas automatizadas con Playwright y ptest?

* ¿Quieres ahorrar tiempo y esfuerzo al realizar pruebas de interfaz de usuario y API? 

    ¡Nuestro proyecto de pruebas automatizadas con Playwright y ptest es lo que necesitas! Incluso si no tienes experiencia en programación, podrás agregar nuevos tests y organizar las ejecuciones de estos de manera sencilla. Además, nuestro reporte amigable te permitirá detectar fácilmente cualquier falla que se produzca y te dará confianza en que lo que estás ejecutando es lo que esperabas que se ejecutara. ¡Con nuestro proyecto, podrás simplificar el proceso de pruebas y aumentar tu eficiencia como QA!

### II. Instalación

#### - ¿Cómo clonar el repositorio de Git para crear tu propio proyecto?

* Verifica que en tu equipo tengas instalado git de no ser asi sigue esta guía:

    https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git

* Luego ejecuta este comando en tu cli 

        git clone https://github.com/javalenciacai/playwrigth.test.python.git

* Ahora que ya tu proyecto esta en tu maquina puedes subirlo a tu propio repositorio

    * Primero crea tu un repositorio en git siguiente esta documentación quickstart

        https://docs.github.com/es/get-started/quickstart/create-a-repo
    * Luego en el repositorio clonado del proyecto **TestBoost** borra la carpeta .git
                
            rm -rf .git
    
    * Luego inicializa el repositorio y envía tu primer commit a tu proyecto asi:

            git init
            git add .
            git commit -m 'mensaje a enviar'
            git push /Reemplace aquí URL del repositorio donde va ha enviar el commit/

#### - ¿Cómo instalar las dependencias necesarias?

* Primero debes tener python instalado sigue esta documentación:

    * Windows https://docs.python.org/es/3/using/windows.html

    * Linux

        * Linux normalmente viene con python 2.7 pero debemos tener  una version 3.7 o superior:
            
            * En tipos Debian, como Ubuntu, use APT

                    sudo apt-get install python3.7

            * En tipos Red Hat, use yum

                    sudo yum install python37

            * En tipos SUSE, use zypper

                    sudo zypper install python3-3.7
            
            * Para confirmar la version de python use:

                    python3 --version
            

* Es tiempo de activar el entorno virtual, normalmente se activa automáticamente porque ya esta configurado en el proyecto ejecuta este comando para activar el entorno virtual

        source venv/bin/activate

* Sigue instalar las dependencia del archivo requirements.txt esto para verificar que funcionen correctamente

        pip install -r requirements.txt

* A continuación instalaremos el navegador o los navegadores que necesites para probar tu aplicación 

    * Instalar todos los navegadores

            playwright install

    * Instalar un navegador especifico

            playwright install chromium

        Puedes reemplazar chromium por firefox, msedge, chrome, chrome-beta, msedge-beta, etc

### III. Ejecución de los test unitarios

#### - ¿Cómo ejecutar los test unitarios?

   Asi como suena este proyecto de pruebas tiene pruebas, ya que es un proyecto de desarrollo normal le puedes agregas pruebas unitarias a tu código y verificar que no afectaste nada cada vez que realizas cambios

* Las pruebas unitarias o unittest deben ir dentro de la carpeta src y deben estar en la raíz de la carpeta 

* Los nombres de los archivos .py deben estar escritos en **snake_case** ejemplo:

        test_unittest_base_test.py

* Para ejecutar los test unitario usas el siguiente comando:

        python -m unittest discover \src

#### - ¿Qué significa que los test unitarios se hayan ejecutado correctamente?

* Cuando los test unitarios se han ejecutado correctamente, significa que todos los test han pasado y que no han encontrado ningún error en el código que están probando. Esto indica que el código cumple con lo que se espera que haga y esta listo para ejecutar tus pruebas de ui o api que implementaste

### IV. Ejecución de los test por defecto

#### - ¿Cómo ejecutar los test por defecto?

* Este proyecto viene con dos pruebas por defecto una de UI y otra de API
* Ten presente que puedes en un mismo test usar API y UI para hacer una prueba
* Para ejecutar un un test puede usar el siguiente comando

        pytest src/test_suites/api --html=src/report/reportAPI.html --self-contained-html --numprocesses auto

    o

        pytest src/test_suites/ui --html=src/report/report.html --self-contained-html --numprocesses 4 -k "alguna palabra dentro del nombre del test"


* Explicare cada parte de estos comandos

    * Primero esta:

            pytest

        Palabra reservada para ejecutar todas las funciones que inicien por ***test_***

    * Segunda parte luego de pytest la ruta de los test, si no se indica ejecuta todos los test en todas las rutas en este caso es ***src/test_suites/api***

            pytest src/test_suites/api

    * Tercera parte es la llamada a la libreria pytest-html la cual crea un reporte en formato html en la ruta especificada y con el nombre especificado en este caso es ***--html=src/report/report.html***

            pytest src/test_suites/ui --html=src/report/report.html

    * Cuarta parte option de la libreria que une todos los archivos css, javascript y html en un solo archivo ***--self-contained-html*** para mas informacion consultar https://pypi.org/project/pytest-reporter-html1/

            pytest src/test_suites/api --html=src/report/reportAPI.html --self-contained-html

    * Quinta parte y muy importante es el comando ***--numprocesses*** de la libreria ***pytest-xdist*** que ayuda a ejecutar test en paralelo, tienen dos formas de hacerlo 

        * En automatico: Esto le indica a la librería que use la cantidad de hilos necesarios para ejecutar el test teniendo en cuenta la capacidad de la maquina o el pipeline

                pytest --numprocesses auto

        * Manual: Puedo indicarle cuantos hilos debería usar en la ejecución, en el ejemplo siguiente le indico 4 hilos

                pytest --numprocesses 4

            otra forma abreviada de usar el numprocesses es:

                pytest -n 4

    * Sexta parte es cuando queremos ejecutar un test especifico o un grupo de test que comparten una palabra en común ejemplo:

        Digamos que todos los test de ambiente QA tiene la palabra **QA** en alguna parte de el nombre del test ***test_login_qa***, ***test_invoce_qa***, etc.

        usamos **-k** + la palabra clave **qa** para ejecutar todos los test que tengan esta palabra

                pytest -k "qa"


#### - ¿Qué incluye el reporte generado por los test por defecto?

* Este reporte incluye información sobre cuántos test se han ejecutado, cuántos han pasado y cuántos han fallado, así como detalles sobre los errores que se han encontrado.

    Para explicar el reporte generado por pytest con ptest-html, es importante mencionar las siguientes secciones:

    Resumen: esta sección muestra un resumen de los resultados de las pruebas. Incluye el número total de test ejecutados, el número de test que han pasado y el número de test que han fallado.

    Test que han fallado: esta sección muestra una lista de los test que han fallado, junto con información sobre el error que se ha encontrado. Por cada test fallido, se incluye el nombre del test, la ubicación del código del test y un mensaje de error que describe el problema encontrado.

    Test que han pasado: esta sección muestra una lista de los test que han pasado, junto con la ubicación del código de cada test.

    Detalles: esta sección muestra información adicional sobre los resultados de las pruebas. Puede incluir información sobre la versión de pytest y de la librería ptest-html que se están utilizando, así como sobre la plataforma y el entorno en el que se están ejecutando las pruebas.

    Dentro encontraras un video de la ejecución para el caso de la **UI**

    Para el **API** encontraras un detalle del error y puedes configurar un ***print*** para mostrar cuando pasa el detalle de la petición

### V. Agregar nuevos tests

#### - ¿Cómo agregar un test de API?

* Aqui un video corte de como agregar un nuevo test

#### - ¿Cómo agregar un test de interfaz de usuario

* Aquí un video corte de como agregar un nuevo test

### VI. Conclusión

#### - ¿Qué has aprendido al leer esta documentación?

* Déjame tu comentario

#### - ¿Cómo puedes comenzar a utilizar el proyecto de pruebas automatizadas con Playwright y ptest en tu equipo de trabajo?

* Para comenzar a utilizar el proyecto de pruebas automatizadas con Playwright y ptest en tu equipo de trabajo, puedes seguir los siguientes pasos:

    - Clona el repositorio del proyecto de pruebas automatizadas en tu equipo de trabajo. Esto te permitirá tener una copia local del código del proyecto y podrás realizar cambios o agregar nuevas pruebas.

    - Instala las dependencias necesarias para el proyecto. Esto incluye las librerías de Python que se utilizan en el proyecto, como Playwright y ptest. Puedes hacerlo ejecutando el comando "pip install -r requirements.txt" en la consola.

    - Ejecuta los test unitarios para verificar que el proyecto esté correctamente instalado y configurado. Esto se puede hacer ejecutando el comando "pytest" en la consola.

    - Ejecuta los test por defecto para verificar el funcionamiento del proyecto. Esto se puede hacer ejecutando el comando "pytest -s" en la consola.

    - Comienza a agregar nuevas pruebas al proyecto. Puedes hacerlo creando nuevos archivos de test en la carpeta "tests" y escribiendo el código de las pruebas en ellos. Asegúrate de seguir la estructura y el formato de los test existentes para que puedan ser ejecutados correctamente.

    - Ejecuta las pruebas de manera periódica para verificar el funcionamiento del código y para detectar errores o problemas. Puedes hacerlo ejecutando el comando "pytest" o "pytest -s" en la consola.

    Espero que estos pasos te sean útiles para comenzar a utilizar el proyecto de pruebas automatizadas con Playwright y ptest llamado **TestBoost** en tu equipo de trabajo. Si tienes alguna otra duda o necesitas más ayuda, no dudes en preguntar.
