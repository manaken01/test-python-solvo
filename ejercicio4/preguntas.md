# Ejercicio 4 — Git (5 minutos)

Escribe tus respuestas en el archivo `respuestas.md`.

---

## Escenarios (escribe los comandos exactos)

### Escenario 1 — Commit en la rama equivocada

Trabajabas en una nueva funcionalidad y sin querer hiciste el commit en `main` en lugar de en una rama nueva.

**Situación actual:**
```
main: A -- B -- C   ← el commit C es el que hiciste por error
```

**Situación deseada:**
```
main:        A -- B
feature/nueva-func: A -- B -- C
```

> Escribe la secuencia de comandos git para llegar al estado deseado sin perder el commit C.

---

### Escenario 2 — Limpiar historial antes del merge

Tu rama `feature/pago` tiene 6 commits con mensajes poco claros:

```
abc1234 wip
def5678 fix
ghi9012 fix2
jkl3456 another fix
mno7890 almost done
pqr1234 done for real
```

Antes de hacer el merge a `main` quieres aplastar los 6 commits en uno solo con el mensaje `"feat: implementar módulo de pago"`.

> Escribe el comando (o secuencia de comandos) para lograrlo.

---

### Escenario 3 — Cherry-pick

La rama `hotfix/ssl` tiene varios commits, pero solo necesitas traer el commit `a3f9c21` a tu rama actual (`feature/auth`) sin hacer un merge completo.

> Escribe el comando exacto.

---

## Preguntas conceptuales

### Pregunta 4 — merge vs rebase

¿Cuál es la diferencia entre `git merge` y `git rebase`?  
¿En qué situaciones preferirías usar cada uno? Da un ejemplo concreto de cada caso.

---

### Pregunta 5 — Revertir un commit pusheado

Un commit con un bug ya está en `main` y otros desarrolladores ya hicieron pull.  
¿Cómo lo revertirías de forma segura sin reescribir la historia del repositorio compartido?

> Explica el enfoque y escribe el comando.
