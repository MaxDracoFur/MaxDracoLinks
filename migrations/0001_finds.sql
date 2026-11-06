-- One row per gem found. No visitor data: which gem, and when (unix seconds).
CREATE TABLE IF NOT EXISTS finds (
    id  INTEGER PRIMARY KEY,
    egg TEXT    NOT NULL,
    at  INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS finds_at ON finds (at);
