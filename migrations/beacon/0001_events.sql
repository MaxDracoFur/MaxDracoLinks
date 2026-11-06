-- First-party beacon rows (functions/api/b.js). No IP, no user agent, no visitor ID.
-- kind: view | notfound (a 404 page view) | out (outbound link click) | err (own-script JS error)
-- cont: 0 for the first send of a page view, 1+ when the reader came back to the tab
--       (count views with cont = 0; sum engaged_ms over all rows).
CREATE TABLE IF NOT EXISTS events (
    id           INTEGER PRIMARY KEY,
    at           INTEGER NOT NULL,   -- unix seconds, server clock
    kind         TEXT    NOT NULL,
    cont         INTEGER NOT NULL DEFAULT 0,
    host         TEXT    NOT NULL,
    path         TEXT    NOT NULL,
    ref_host     TEXT,
    ref_path     TEXT,
    tag_ref      TEXT,
    utm_source   TEXT,
    utm_medium   TEXT,
    utm_campaign TEXT,
    country      TEXT,
    device       TEXT,
    engaged_ms   INTEGER,
    scroll_pct   INTEGER,
    target       TEXT,               -- out: host+path clicked; err: file:line
    detail       TEXT                -- err: message
);
CREATE INDEX IF NOT EXISTS events_at ON events (at);

-- Rows refused by the per-minute cap, so a flood shows up as a number instead of silence.
CREATE TABLE IF NOT EXISTS dropped (
    id INTEGER PRIMARY KEY,
    n  INTEGER NOT NULL DEFAULT 0
);
INSERT OR IGNORE INTO dropped (id, n) VALUES (1, 0);
