CREATE TABLE cliente
(
    cliente_id BIGINT,
    nombre VARCHAR NOT NULL,
    apellido VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    telefono BIGINT,
    PRIMARY KEY(cliente_id)
);

CREATE TABLE estacion
(
    estacion_id INT,
    nombre VARCHAR NOT NULL,
    pais VARCHAR NOT NULL,
    ciudad VARCHAR NOT NULL,
    PRIMARY KEY(estacion_id)
);

CREATE TABLE ruta
(
    ruta_id SERIAL,
    nombre VARCHAR NOT NULL,
    estacion_origen INT,
    estacion_destino INT,
    hora_partida TIMESTAMP,
    hora_llegada TIMESTAMP,
    monto_vip NUMERIC(10,2) NOT NULL CHECK(monto_vip > 0),
    monto_ejecutivo NUMERIC(10,2) NOT NULL CHECK(monto_ejecutivo > 0),
    monto_economico NUMERIC(10,2) NOT NULL CHECK(monto_economico > 0),
    sillas_vip INT CHECK(sillas_vip >= 0 AND sillas_vip <= 10),
    sillas_ejecutivo INT CHECK(sillas_ejecutivo >= 0 AND sillas_ejecutivo <= 20),
    sillas_economico INT CHECK(sillas_economico >= 0 AND sillas_economico <= 30),
    PRIMARY KEY(ruta_id),
    FOREIGN KEY(estacion_origen) REFERENCES estacion,
    FOREIGN KEY(estacion_destino) REFERENCES estacion
);

CREATE TABLE reserva
(
    reserva_id SERIAL,
    cliente_id INT,
    ruta_id INT,
    monto NUMERIC(10,2) CHECK(monto > 0),
    fecha TIMESTAMP NOT NULL default now(),
    medio_pago VARCHAR NOT NULL,
    tipo_silla VARCHAR NOT NULL CHECK(tipo_silla IN('vip','ejecutivo','economico')),
    PRIMARY KEY(reserva_id),
    FOREIGN KEY(cliente_id) REFERENCES cliente,
    FOREIGN KEY(ruta_id) REFERENCES ruta
)

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