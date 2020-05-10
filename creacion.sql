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
    monto_vip NUMERIC(10,2),
    monto_ejecutivo NUMERIC(10,2),
    monto_economico NUMERIC(10,2),
    tipo_silla VARCHAR NOT NULL CHECK(tipo_silla IN('vip','ejecutivo','economico')),
    fecha TIMESTAMP NOT NULL,
    medio_pago VARCHAR NOT NULL,
    PRIMARY KEY(reserva_id),
    FOREIGN KEY(cliente_id) REFERENCES cliente,
    FOREIGN KEY(ruta_id) REFERENCES ruta,
    FOREIGN KEY(monto_vip) REFERENCES ruta,
    FOREIGN KEY(monto_ejecutivo) REFERENCES ruta,
    FOREIGN KEY(monto_economico) REFERENCES ruta
);

CREATE TABLE ruta(
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
    sillas_ejecutiva INT CHECK(sillas_ejecutiva >= 0 AND sillas_ejecutiva <= 20),
    sillas_economica INT CHECK(sillas_economica >= 0 AND sillas_economica <= 30),
    PRIMARY KEY(ruta_id),
    FOREIGN KEY(estacion_origen) REFERENCES estacion,
    FOREIGN KEY(estacion_destino) REFERENCES estacion,
);
