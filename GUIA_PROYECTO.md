## Material del proyecto
- Módulos propios en `custom_addons/`.
- Guía del entorno en `GUIA_PROYECTO.md`.
 - Versión de Odoo.
 - Comando de arranque.
## Comprobación de una mejora
1. Guarda los archivos.
2. Revisa las diferencias.
3. Prueba el comportamiento.
4. Prepara y confirma los cambios.

## Verificaciones
- [x] Comprobar la rama activa.
- [ ] Revisar el contenido preparado.
- [ ] Crear el commit de documentación.
> Nota: la base de datos se respalda por separado.
Texto del apartado anterior.
---
Texto de un bloque distinto.


| Archivo | Función | Se versiona |
| --- | --- | :---: |
| `GUIA_PROYECTO.md` | Instrucciones propias | Sí |
| `.venv/` | Entorno local | No |
| `*.local.conf` | Configuración privada | No |

Escribe \*texto\* para mostrar los asteriscos.
| Expresión | Significado |
| --- | --- |
| `a \| b` | Una barra vertical dentro de la celda |
```text
On branch main
nothing to commit, working tree clean
```

# Proyecto de prácticas de Odoo 19
## Objetivo
PENDIENTE: explica el proceso empresarial que resuelve
el proyecto y qué podrá hacer la persona que lo utilice.
## Índice
- [Requisitos](#requisitos)
- [Estructura](#estructura)
- [Entorno de trabajo](#entorno-de-trabajo)
- [Arranque](#arranque)
- [Comprobaciones](#comprobaciones)
- [Incidencias](#incidencias)
## Requisitos
| Elemento | Versión utilizada o procedencia |
| --- | --- |
| Odoo | 19.0 y PENDIENTE: paquete o revisión exacta |
| Python | PENDIENTE: versión comprobada |
| PostgreSQL | PENDIENTE: versión comprobada |
| Sistema | PENDIENTE: distribución y versión de WSL |
## Estructura
- `custom_addons/`: módulos desarrollados en clase.
- `docs/img/`: capturas de documentación sin datos privados.
- `requirements.txt`: dependencias de Python de referencia.
- `GUIA_PROYECTO.md`: instrucciones de este proyecto.
El código base de Odoo y `.venv/` no se incluyen en Git.
El README original de Odoo se conserva en la instalación.
El repositorio no contiene la base de datos ni el filestore.