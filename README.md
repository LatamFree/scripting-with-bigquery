## Actividad I: Repaso de Joins

### Inner joins
Revisaremos el primer tipo de JOIN o INNER JOIN

```sql
WITH from_item_a AS (
  SELECT 'Dalles' as city, 'OR' as state
  UNION ALL SELECT 'Tokyo', 'Tokyo'
  UNION ALL SELECT 'Mumbai', 'Maharashtra'
),
from_item_b AS (
  SELECT 'OR' as state, 'USA' as country
  UNION ALL SELECT 'Tokyo', 'Japan'
  UNION ALL SELECT 'Maharashtra', 'India'
)
SELECT from_item_a.*, country
FROM from_item_a
JOIN from_item_b
ON from_item_a.state = from_item_b.state
```

No necesariamente debe ser una igualdad en el JOIN!

```sql
SELECT from_item_a.*, country AS surcharge
FROM from_item_a
JOIN from_item_b
ON from_item_a.state != from_item_b.state
```

### Cross JOIN

Este JOIN no necesita condición

```sql
WITH winners AS (
  SELECT 'John' as person, '100m' as event
  UNION ALL SELECT 'Hiroshi', '200m'
  UNION ALL SELECT 'Sita', '400m'
),
gifts AS (
  SELECT 'Google Home' as gift
  UNION ALL SELECT 'Google Hub'
  UNION ALL SELECT 'Pixel3'
)
SELECT person, gift
FROM winners
CROSS JOIN gifts
```

### Others JOINS

```sql
SELECT person, gift
FROM winners
FULL OUTER JOIN gifts
ON winners.event = gifts.event

SELECT person, gift
FROM winners
LEFT OUTER JOIN gifts
ON winners.event = gifts.event

SELECT person, gift
FROM winners
RIGHT OUTER JOIN gifts
ON winners.event = gifts.event
```

## Actividad 2: Scripting BigQuery

Crearemos un dataset, cargaremos la información en la tabla, validaremos y correremos Queries utilizando la metodología de cambios discretos en archivos ejecutables. Al terminar limpiaremos todos los recursos utilizados

```json
[
  {
    "mode": "REQUIRED",
    "name": "Fecha-I",
    "type": "DATETIME"
  },
  {
    "mode": "REQUIRED",
    "name": "Vlo-I",
    "type": "STRING"
  },
  {
    "mode": "REQUIRED",
    "name": "Ori-I",
    "type": "STRING"
  },
  {
    "mode": "REQUIRED",
    "name": "Des-I",
    "type": "STRING"
  },
  {
    "mode": "REQUIRED",
    "name": "Emp-I",
    "type": "STRING"
  },
  {
    "mode": "REQUIRED",
    "name": "Fecha-O",
    "type": "DATETIME"
  },
  {
    "mode": "NULLABLE",
    "name": "Vlo-O",
    "type": "STRING"
  },
  {
    "mode": "REQUIRED",
    "name": "Ori-O",
    "type": "STRING"
  },
  {
    "mode": "REQUIRED",
    "name": "Des-O",
    "type": "STRING"
  },
  {
    "mode": "REQUIRED",
    "name": "Emp-O",
    "type": "STRING"
  },
  {
    "mode": "REQUIRED",
    "name": "DIA",
    "type": "INTEGER"
  },
  {
    "mode": "REQUIRED",
    "name": "MES",
    "type": "INTEGER"
  },
  {
    "mode": "REQUIRED",
    "name": "AÑO",
    "type": "INTEGER"
  },
  {
    "mode": "REQUIRED",
    "name": "DIANOM",
    "type": "STRING"
  },
  {
    "mode": "REQUIRED",
    "name": "TIPOVUELO",
    "type": "STRING"
  },
  {
    "mode": "REQUIRED",
    "name": "OPERA",
    "type": "STRING"
  },
  {
    "mode": "REQUIRED",
    "name": "SIGLAORI",
    "type": "STRING"
  },
  {
    "mode": "REQUIRED",
    "name": "SIGLADES",
    "type": "STRING"
  }
]
```

| Campo | Descripción |
|---|---|
|Fecha-I | Fecha y hora programada del vuelo.|
|Vlo-I | Número de vuelo programado.|
|Ori-I | Código de ciudad de origen programado.|
|Des-I | Código de ciudad de destino programado.|
|Emp-I | Código aerolínea de vuelo programado.|
|Fecha-O | Fecha y hora de operación del vuelo.|
|Vlo-O | Número de vuelo de operación del vuelo.|
|Ori-O | Código de ciudad de origen de operación|
|Des-O | Código de ciudad de destino de operación.|
|Emp-O | Código aerolínea de vuelo operado.|
|DIA | Día del mes de operación del vuelo.|
|MES | Número de mes de operación del vuelo.|
|AÑO | Año de operación del vuelo.|
|DIANOM | Día de la semana de operación del vuelo.|
|TIPOVUELO | Tipo de vuelo, I =Internacional, N =Nacional.|
|OPERA | Nombre de aerolínea que opera.|
|SIGLAORI | Nombre ciudad origen.|
|SIGLADES | Nombre ciudad destino.|
