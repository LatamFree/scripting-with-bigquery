import bq import bq 
bq.cmd
query = """
SELECT
    COUNT(*) AS vuelos_totales,
    OPERA AS aerolinea,
    SUM(atraso_15) AS vuelos_atrasados,
    AVG(atraso_15) AS porcentaje_atraso,
FROM
    `ado-boolean.scripting_druminot.scripting_test`
WHERE
    temporada_alta = 1
GROUP BY
    OPERA
ORDER BY
    porcentaje_atraso desc
"""
