# CoderForo

## El foro de Coderhouse

### ¿Qué vamos a hacer?
Vamos a crear un foro. Nuestra página va a tener **profesores** y **alumnos** de cada **comisión** que van a poder crear **hilos** en su comisión y **comentar** en los hilos creados. Los profesores funcionarían como moderadores de su comisión, pudiendo editar y borrar todos los posts y comentarios, mientras que los alumnos solo pueden tocar los propios.

## Primera parte

### Apps
Crearemos nuestras apps, ¿qué apps necesitamos? Hay que separar bien las diferentes características de la página en diferentes aplicaciones.

### Modelos
Armaremos los modelos para poder guardar la siguiente información:  
**Profesor**

| Nombre | Apellido | Email | Pagina Web | Descripción | Comisión |
|--------|----------|-------|------------|-------------|----------|
| Texto  | Texto    | Email | Texto      | Texto largo | Número   |

**Estudiante**

| Nombre | Apellido | Email | Cursos completados | Descripción | Comisión |
|--------|----------|-------|--------------------|-------------|----------|
| Texto  | Texto    | Email | Número             | Texto largo | Número   |

**Hilo**

| Titulo | Tema  | Contenido   | Comisión | Posteador |
|--------|-------|-------------|----------|-----------|
| Texto  | Texto | Texto largo | Número   | Texto?    |

### Para ir pensando...
¿Cómo armaría un comentario?  
**Comentario**

| Comentador | Hilo | Contenido | 
|------------|------|-----------|
| ?????????? | ???? | Texto     |

### Objetivo
La idea de esta **primera parte** es llegar a tener las siguientes páginas funcionando:
- ***/usuarios/nuevo_estudiante/***: formulario para crear un estudiante.
- ***/usuarios/nuevo_profesor/***: formulario para crear un profesor.
- ***/paginas/nuevo_hilo/\<comision\>***: formulaio para crear un hilo (en una comisión).
- ***/paginas/busar_hilo/\<comision\>/\<tiutulo\>***: página para buscar hilo por título (en una comisión).
  
Si llegamos...
- ***/paginas/\<comision\>***: mostrar todos los hilos del foro de la comisión.
- ***/paginas/borrar/\<hilo\>***: eliminar un hilo.
- ***/paginas/editar/\<hilo\>***: formulario editar un hilo.