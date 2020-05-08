CREATE TABLE cliente(
    cliente_id INT,
    nombre VARCHAR NOT NULL,
    apellido VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    telefono INT,
    PRIMARY KEY(cliente_id)
);

CREATE TABLE tren(
    tren_id SERIAL,
    num_sillas_vip INT NOT NULL CHECK(num_sillas_vip = 10),
    num_sillas_ejecutiva INT NOT NULL CHECK(num_sillas_ejecutiva = 20),
    num_sillas_economica INT NOT NULL CHECK(num_sillas_economica = 30),
    PRIMARY KEY (tren_id)
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
    tren_id INT,
    monto NUMERIC(10,2),
    silla INT NOT NULL,
    fecha TIMESTAMP NOT NULL,
    medio_pago VARCHAR NOT NULL,
    PRIMARY KEY(reserva_id),
    FOREIGN KEY(cliente_id) REFERENCES cliente,
    FOREIGN KEY(tren_id) REFERENCES tren
);

CREATE TABLE ruta(
    nombre VARCHAR NOT NULL,
    estacion_id INT,
    tren_id INT,
    hora_llegada TIMESTAMP,
    hora_salida TIMESTAMP,
    FOREIGN KEY(estacion_id) REFERENCES estacion,
    FOREIGN KEY(tren_id) REFERENCES tren
);