# Prueba Técnica — Desarrollador Senior Python

Tiempo total: **40 minutos**

Esta prueba evalúa cuatro áreas clave de un desarrollador Python senior. Cada ejercicio tiene un tiempo sugerido; adminístralo según tu criterio.

---

## Ejercicios

| # | Tema | Archivo principal | Tiempo |
|---|------|-------------------|--------|
| 1 | Estructuras de datos — LRU Cache en contexto real | `ejercicio1/` | 15 min |
| 2 | Python idiomático — Decorador `@retry` | `ejercicio2/` | 12 min |
| 3 | OOP y diseño — Jerarquía de figuras geométricas | `ejercicio3/` | 8 min |
| 4 | Git — Escenarios y preguntas conceptuales | `ejercicio4/` | 5 min |

---

## Requisitos

- Python 3.10 o superior
- pytest

```bash
pip install pytest
```

---

## Cómo ejecutar los tests

```bash
# Todos los ejercicios de una vez
pytest ejercicio1/ ejercicio2/ ejercicio3/ -v

# Un ejercicio individual
pytest ejercicio1/ -v
pytest ejercicio2/ -v
pytest ejercicio3/ -v
```

Al comenzar, **todos los tests fallarán** porque los archivos de implementación están vacíos. El objetivo es que todos pasen al terminar.

---

## Reglas

1. **No modificar** los archivos `test_*.py` ni los `conftest.py`.
2. Implementar únicamente en los archivos indicados en cada ejercicio.
3. No usar las librerías o funciones explícitamente prohibidas en cada ejercicio.
4. Se permite usar la librería estándar de Python salvo las excepciones indicadas.
5. No se permiten librerías externas (salvo `pytest` para correr los tests).
6. **Todo el código debe estar escrito en inglés**: nombres de variables, funciones, clases, comentarios y docstrings.

---

## Ejercicio 1 — LRU Cache en contexto real (15 min)

**Archivos a modificar:** `ejercicio1/lru_cache.py` y `ejercicio1/product_service.py`

Un servicio de catálogo consulta datos de productos desde una base de datos costosa. Para evitar consultas redundantes, el servicio debe usar un caché LRU.

**Tu tarea:**
1. Implementar la clase `LRUCache` en `lru_cache.py`.
2. Completar `ProductService.__init__` y `ProductService.get_product` en `product_service.py`.

**Restricciones obligatorias:**
- ❌ No usar `collections.OrderedDict`
- ❌ No usar `functools.lru_cache` ni `@cache`
- ✅ `get()` y `put()` deben ser **O(1)** en tiempo promedio

**Criterios de evaluación:**
- Correctitud de la lógica de evicción LRU
- Complejidad temporal O(1)
- Integración correcta con `ProductService`

---

## Ejercicio 2 — Decorador `@retry` (12 min)

**Archivo a modificar:** `ejercicio2/retry.py`

Implementar un decorador de fábrica que reintente automáticamente una función cuando lanza ciertos tipos de excepción.

```python
@retry(times=3, exceptions=(ValueError, ConnectionError))
def consultar_api():
    ...
```

**Requisitos:**
- `times`: número máximo de intentos (incluye el primero).
- `exceptions`: solo reintentar para los tipos listados; otros se propagan de inmediato.
- Usar `functools.wraps` para preservar `__name__` y `__doc__`.
- Si se agotan los intentos, relanzar la última excepción.

**Criterios de evaluación:**
- Lógica correcta de reintentos y conteo
- Manejo selectivo de excepciones
- Preservación de metadatos de la función

---

## Ejercicio 3 — OOP y diseño (8 min)

**Archivo a modificar:** `ejercicio3/shapes.py`

Implementar una jerarquía de figuras geométricas usando clases abstractas.

**Clases a implementar:**
- `Shape` (ABC): base con `area()`, `perimeter()`, `__eq__` (por área), `__lt__` (por área), `__repr__`.
- `Circle(Shape)`: definido por `radius`. Lanzar `ValueError` si `radius <= 0`.
- `Rectangle(Shape)`: definido por `width` y `height`. Lanzar `ValueError` si alguno `<= 0`.

**Criterios de evaluación:**
- Uso correcto de `ABC` y `@abstractmethod`
- Implementación de `__eq__` y `__lt__` (que habilitan `sorted()` y comparaciones)
- Validación de parámetros con `ValueError`
- Fórmulas correctas para área y perímetro

---

## Ejercicio 4 — Git (5 min)

**Archivo a completar:** `ejercicio4/respuestas.md`

Lee los escenarios en `ejercicio4/preguntas.md` y escribe tus respuestas en `ejercicio4/respuestas.md`.

**Criterios de evaluación:**
- Comandos exactos y correctos para cada escenario
- Comprensión de merge vs rebase y sus casos de uso
- Conocimiento de cómo operar de forma segura sobre historia compartida

---

## Criterios generales de evaluación

| Criterio | Descripción |
|----------|-------------|
| Correctitud | Los tests pasan; la lógica es correcta |
| Conocimiento de Python | Uso idiomático, tipos de datos adecuados |
| Diseño | Responsabilidades claras, código legible |
| Git | Comandos precisos, comprensión de flujos |
