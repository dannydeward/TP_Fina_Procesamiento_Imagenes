# TP Final — Procesamiento de Imágenes

Aplicación de línea de comandos para aplicar operaciones de procesamiento de
imágenes (rotar, brillo, blanco y negro, desenfoque, quitar fondo, mejora
automática, etc.) usando [Pillow](https://python-pillow.org/) y
[rembg](https://github.com/danielgatis/rembg).

El proyecto está diseñado con principios **SOLID** y patrones de diseño para que
agregar una operación nueva no requiera modificar el código existente: alcanza
con crear una clase y registrarla con un decorador.

---

## Índice

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Operaciones disponibles](#operaciones-disponibles)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Arquitectura y patrones de diseño](#arquitectura-y-patrones-de-diseño)
- [Cómo agregar una operación nueva](#cómo-agregar-una-operación-nueva)
- [Detalles internos](#detalles-internos)

---

## Requisitos

- Python 3.10 o superior.
- Las dependencias listadas en [`requirements.txt`](requirements.txt):
  - `Pillow` — manipulación de imágenes.
  - `rembg[cpu]` — eliminación de fondo (incluye el backend `onnxruntime`).

> **Nota:** las operaciones `fondo` y `sin_fondo` necesitan el backend
> `onnxruntime` de rembg. El resto de las operaciones funciona sin él, porque
> rembg se importa de forma diferida (solo cuando se ejecuta una operación de
> fondo).

---

## Instalación

```bash
# 1. (opcional pero recomendado) crear un entorno virtual
python -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate

# 2. instalar dependencias
pip install -r requirements.txt
```

---

## Uso

1. Colocá las imágenes a procesar dentro de la carpeta `imagenes/`.
2. Ejecutá la aplicación:

```bash
python app.py
```

3. El programa pide el nombre de la operación y el nombre del archivo:

```text
Operaciones disponibles: blur, brillo, byn, contraste, flip, fondo, mejora, rotar, sin_fondo
Función: rotar
Imagen (dentro de la carpeta 'imagenes/'): foto.jpg
✅ Guardado en: resultados/resultado_rotar.jpg
```

El resultado se guarda en la carpeta `resultados/` (se crea automáticamente) con
el nombre `resultado_<operacion>.<extension>`.

Si se ingresa una operación que no existe, el programa lo informa sin romperse:

```text
Función: noexiste
❌ Operación 'noexiste' no reconocida. Opciones disponibles: blur, brillo, byn, ...
```

---

## Operaciones disponibles

| Nombre      | Qué hace                                             | Salida | Parámetro por defecto |
|-------------|------------------------------------------------------|:------:|-----------------------|
| `rotar`     | Rota la imagen.                                      | `jpg`  | ángulo = 90°          |
| `flip`      | Espejo horizontal.                                   | `jpg`  | —                     |
| `byn`       | Convierte a blanco y negro.                          | `jpg`  | —                     |
| `brillo`    | Ajusta el brillo.                                    | `jpg`  | factor = 1.5          |
| `contraste` | Ajusta el contraste.                                 | `jpg`  | factor = 2.0          |
| `blur`      | Desenfoque gaussiano.                                | `jpg`  | radio = 8             |
| `fondo`     | Desenfoca el fondo y mantiene a la persona nítida.   | `png`  | radio fondo = 10      |
| `sin_fondo` | Elimina el fondo (PNG con transparencia).            | `png`  | —                     |
| `mejora`    | Mejora automática de brillo y contraste + nitidez.   | `jpg`  | automático            |

---

## Estructura del proyecto

```
TP_Fina_Procesamiento_Imagenes/
├── app.py                      # Punto de entrada: arranca el CLI
├── requirements.txt            # Dependencias
├── imagenes/                   # Imágenes de entrada (poné las tuyas acá)
├── resultados/                 # Imágenes procesadas (se crea sola)
└── src/                        # Código fuente
    ├── __init__.py
    ├── cargador.py             # CargadorImagenes: abrir y guardar
    ├── registro.py             # Registry + decorador @registrar
    ├── app_cli.py              # Orquestador del programa (sin if/elif)
    └── operaciones/
        ├── __init__.py         # Importa los módulos -> registra todo
        ├── base.py             # Operacion: interfaz abstracta común
        ├── transformaciones.py # rotar, flip
        ├── color.py            # byn, brillo, contraste
        ├── filtros.py          # blur
        ├── fondo.py            # fondo, sin_fondo (rembg)
        ├── mejora.py           # mejora automática
        └── desconocida.py      # Null Object para nombres inválidos
```

---

## Arquitectura y patrones de diseño

El programa **no usa cadenas de `if/elif`** para elegir la operación. En su
lugar combina tres patrones:

### 1. Registry (registro de operaciones)

`src/registro.py` mantiene un diccionario `nombre -> operación`. Cada operación
se da de alta con el decorador `@registrar`:

```python
@registrar
class Rotar(Operacion):
    nombre = "rotar"
    ...
```

Para invocar una operación, el CLI solo la busca por su nombre:

```python
operacion = registro.obtener(nombre_operacion)
resultado = operacion.aplicar(imagen)
```

### 2. Command (cada operación es una clase)

Todas las operaciones implementan la misma interfaz `Operacion` (`src/operaciones/base.py`):

```python
class Operacion(ABC):
    nombre: str = ""
    extension: str = "jpg"

    @abstractmethod
    def aplicar(self, img: Image.Image) -> Image.Image: ...
```

Esto permite tratarlas a todas de forma uniforme (todas se aplican con
`.aplicar(img)`), sin importar qué hagan por dentro.

### 3. Null Object (operación desconocida)

Si el nombre pedido no existe, en vez de un `if operacion is None` se usa un
objeto que respeta la misma interfaz y, al aplicarse, informa el error
(`src/operaciones/desconocida.py`):

```python
operacion = registro.obtener(nombre) or OperacionDesconocida(nombre, registro.nombres())
```

### Principios SOLID aplicados

- **S — Single Responsibility:** cargar/guardar imágenes (`CargadorImagenes`),
  registrar operaciones (`RegistroOperaciones`) y orquestar el flujo
  (`app_cli`) están en módulos separados.
- **O — Open/Closed:** se agregan operaciones nuevas sin tocar el registro ni el
  CLI, solo creando una clase con `@registrar`.
- **L — Liskov Substitution:** cualquier `Operacion` (incluido el Null Object)
  puede usarse de forma intercambiable.
- **I — Interface Segregation:** la interfaz `Operacion` es mínima (`aplicar`).
- **D — Dependency Inversion:** el CLI depende de la abstracción `Operacion`,
  no de funciones concretas.

---

## Cómo agregar una operación nueva

Por ejemplo, una operación que voltea la imagen verticalmente:

1. Creá la clase en el módulo que corresponda (ej. `src/operaciones/transformaciones.py`):

```python
@registrar
class FlipVertical(Operacion):
    nombre = "flip_v"
    extension = "jpg"

    def aplicar(self, img: Image.Image) -> Image.Image:
        return img.transpose(Image.FLIP_TOP_BOTTOM)
```

2. Si la creaste en un módulo nuevo, importalo en `src/operaciones/__init__.py`
   para que el decorador se ejecute.

¡Listo! La operación ya aparece en el menú y se puede invocar como `flip_v`. No
hubo que modificar el registro ni el CLI.

---

## Detalles internos

### Mejora automática

`MejoraAutomatica` (`src/operaciones/mejora.py`) mide la imagen y ajusta brillo y
contraste según rangos definidos en tablas, evitando cadenas de `if/elif`:

```python
RANGOS_BRILLO = [
    (0, 60, 1.4),       # muy oscura  -> subir brillo
    (60, 100, 1.2),     # algo oscura -> subir un poco
    (190, 256, 0.8),    # muy clara   -> bajar brillo
]
```

Se elige el primer rango `(mínimo, máximo, factor)` que contiene al valor
medido; si no entra en ninguno, el factor por defecto es `1.0` (no cambia nada).
Luego se aplica un filtro de mediana (reduce ruido) y un realce de nitidez.

### Carga diferida de rembg

En `src/operaciones/fondo.py`, `rembg` se importa **dentro** de cada método
`aplicar`, no al inicio del módulo. Esto evita que la falta del backend
`onnxruntime` rompa el resto de las operaciones, que no dependen de rembg.
