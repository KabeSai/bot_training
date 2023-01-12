CREATE TABLE  IF NOT EXISTS  places (
    id     serial  PRIMARY KEY
                   UNIQUE
                   NOT NULL,
    name   TEXT    NOT NULL

);

CREATE TABLE  IF NOT EXISTS  users (
    id     integer  PRIMARY KEY
                   UNIQUE
                   NOT NULL,
    name   TEXT    NOT NULL,
    age integer,
    weight real,
    gender varchar,
    lvl integer,
    training_goal varchar,
    place_id integer references places (id) ON DELETE SET NULL
);



CREATE TABLE  IF NOT EXISTS  trainings (
    id     serial     PRIMARY KEY
                   UNIQUE
                   NOT NULL,
    name   TEXT    NOT NULL,
    lvl integer DEFAULT(0),
    gender varchar,
    type varchar,
    description text,
    muscle_group text


);