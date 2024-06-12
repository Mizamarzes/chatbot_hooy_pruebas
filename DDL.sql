-- #########################################################################
-- #### COMANDOS DDL CREACION DE TABLAS | Juan Diego Contreras ##################
-- ######################################################################
-- Este archivo realiza la creacion de las tablas necesarias 
-- para el funcionamiento de la base de datos

-- Creacion de base de datos
DROP DATABASE IF EXISTS hooy_database_pruebas;
CREATE DATABASE hooy_database_pruebas;

-- Seleccion de base de datos
USE hooy_database_pruebas;

-- Crear la tabla usuarios
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT NOT NULL,
    fecha_ultimo_pedido DATE,
    numero_celular VARCHAR(15) NOT NULL
);


-- ################ PROCEDIMIENTOS #####################

-- Este procedimiento muestra los clientes que no han hecho
-- compras dependiendo de la cantidad de meses que le ingreses,
-- si le ingresas 3 meses te mostrara los que no han comprado en 3 meses
DELIMITER $$

DROP PROCEDURE IF EXISTS clientes_sin_pedidos_recientes;
CREATE PROCEDURE clientes_sin_pedidos_recientes(
    IN meses INT
)
BEGIN
    DECLARE cutoff_date DATE;
    SET cutoff_date = DATE_SUB(CURDATE(), INTERVAL meses MONTH);

    CREATE TEMPORARY TABLE IF NOT EXISTS temp_clientes_sin_pedidos AS
    SELECT
        u.id,
        u.nombre,
        u.edad,
        u.fecha_ultimo_pedido,
        u.numero_celular
    FROM usuario AS u
    WHERE u.fecha_ultimo_pedido IS NULL OR u.fecha_ultimo_pedido < cutoff_date;
END $$

DELIMITER ;



-- Este procedimiento filtra los usuarios por edades, dependiendo del numero que 
-- ingreses, si ingresas el numero 25 de listar los usuarios con una edad menor o igual
-- a 25 años
DELIMITER $$

DROP PROCEDURE IF EXISTS filtrar_rangos_edad;
CREATE PROCEDURE filtrar_rangos_edad(
    IN edad_maxima_filtrar INT
)
BEGIN
    CREATE TEMPORARY TABLE IF NOT EXISTS temp_clientes_por_edad AS
    SELECT
        u.id,
        u.nombre,
        u.edad,
        u.fecha_ultimo_pedido,
        u.numero_celular
    FROM usuario AS u
    WHERE u.edad <= edad_maxima_filtrar;
END $$

DELIMITER ;



-- Este procedimiento utiliza los otros procedimientos para crear
-- consultas temporales y utilizarlas y imprimir una consulta final
DELIMITER $$

DROP PROCEDURE IF EXISTS filtrar_usuarios;
CREATE PROCEDURE filtrar_usuarios(
    IN meses INT,
    IN edad_maxima_filtrar INT
)
BEGIN
    -- Drop temporary tables if they exist
    DROP TEMPORARY TABLE IF EXISTS temp_clientes_sin_pedidos;
    DROP TEMPORARY TABLE IF EXISTS temp_clientes_por_edad;
    DROP TEMPORARY TABLE IF EXISTS temp_result;

    -- Call individual procedures based on the input parameters
    IF meses IS NOT NULL THEN
        CALL clientes_sin_pedidos_recientes(meses);
    END IF;

    IF edad_maxima_filtrar IS NOT NULL THEN
        CALL filtrar_rangos_edad(edad_maxima_filtrar);
    END IF;

    -- Combine results if both filters are applied
    IF meses IS NOT NULL AND edad_maxima_filtrar IS NOT NULL THEN
        CREATE TEMPORARY TABLE temp_result AS
        SELECT * FROM temp_clientes_sin_pedidos
        WHERE id IN (SELECT id FROM temp_clientes_por_edad);
    ELSEIF meses IS NOT NULL THEN
        CREATE TEMPORARY TABLE temp_result AS
        SELECT * FROM temp_clientes_sin_pedidos;
    ELSEIF edad_maxima_filtrar IS NOT NULL THEN
        CREATE TEMPORARY TABLE temp_result AS
        SELECT * FROM temp_clientes_por_edad;
    END IF;

    -- Select final result
    SELECT * FROM temp_result;

    -- Drop temporary tables
    DROP TEMPORARY TABLE IF EXISTS temp_clientes_sin_pedidos;
    DROP TEMPORARY TABLE IF EXISTS temp_clientes_por_edad;
    DROP TEMPORARY TABLE IF EXISTS temp_result;
END $$

DELIMITER ;




-- Juan Diego Contreras - C.C: 1.***.***.782