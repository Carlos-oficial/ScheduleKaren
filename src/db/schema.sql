CREATE TABLE IF NOT EXISTS event (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  time TIMESTAMP NOT NULL,
  remind INT DEFAULT 15 -- lembrar n minutos antes do evento
);