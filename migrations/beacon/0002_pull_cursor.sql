-- Highest events.id the homelab CronJob homelab/site-beacon has already shipped to Loki,
-- so each run sends only new rows and a failed run is retried by the next one.
CREATE TABLE IF NOT EXISTS pull_cursor (
    name TEXT PRIMARY KEY,
    id   INTEGER NOT NULL
);
INSERT OR IGNORE INTO pull_cursor (name, id) VALUES ('loki', 0);
