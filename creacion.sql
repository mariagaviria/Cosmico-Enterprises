CREATE TABLE cliente(
    cliente_id INT,
    nombre VARCHAR NOT NULL,
    apellido VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    telefono INT,
    PRIMARY KEY(cliente_id)
);

CREATE TABLE estacion(
    estacion_id INT,
    nombre VARCHAR NOT NULL,
    pais VARCHAR NOT NULL,
    ciudad VARCHAR NOT NULL,
    PRIMARY KEY(estacion_id)
);

CREATE TABLE reserva(
    reserva_id SERIAL,
    cliente_id INT,
    ruta_id INT,
    monto NUMERIC(10,2),
    tipo_silla VARCHAR NOT NULL CHECK(tipo_silla IN('vip','ejecutivo','economico')),
    fecha TIMESTAMP NOT NULL,
    medio_pago VARCHAR NOT NULL,
    PRIMARY KEY(reserva_id),
    FOREIGN KEY(cliente_id) REFERENCES cliente,
    FOREIGN KEY(ruta_id) REFERENCES ruta
);

CREATE TABLE ruta(
    ruta_id SERIAL,
    nombre VARCHAR NOT NULL,
    estacion_origen INT,
    estacion_destino INT,
    hora_partida TIMESTAMP,
    hora_llegada TIMESTAMP,
    sillas_vip INT CHECK(sillas_vip >= 0 AND sillas_vip <= 10),
    sillas_ejecutiva INT CHECK(sillas_ejecutiva >= 0 AND sillas_ejecutiva <= 20),
    sillas_economica INT CHECK(sillas_economica >= 0 AND sillas_economica <= 30),
    PRIMARY KEY(ruta_id),
    FOREIGN KEY(estacion_origen) REFERENCES estacion,
    FOREIGN KEY(estacion_destino) REFERENCES estacion,
);

CREATE OR REPLACE FUNCTION idDeEstacion(ciudad VARCHAR) RETURNS INTEGER AS $$
BEGIN
    RETURN estacion.estacion_id 
    FROM estacion
    WHERE estacion.ciudad=ciudad;
END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION ciudadDeIdEstacion(id INTEGER) RETURNS VARCHAR AS $$
BEGIN
    RETURN estacion.ciudad 
    FROM estacion
    WHERE estacion.estacion_id=id;
END;
$$
LANGUAGE plpgsql;