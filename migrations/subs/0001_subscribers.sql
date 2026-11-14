-- Blog email subscribers (functions/api/subscribe.js), card blog-email-subscription.
--
-- One row per address, ever. A row is never deleted on unsubscribe: the token has to keep
-- working (CAN-SPAM: the opt-out mechanism works for at least 30 days after a message is
-- sent, and we keep it indefinitely), and the record is what proves the person opted in.
--
-- Stored: the address, which page they signed up from, and three timestamps. NOT stored:
-- IP address, user agent, name, or anything else. Same rule as the page beacon.
--
-- status:
--   pending      signed up, confirmation email not yet confirmed. Never mailed anything else.
--   confirmed    clicked the link in the confirmation email. Only these get sent posts.
--   unsubscribed asked to stop. Never mailed again; the row stays as the record.
CREATE TABLE IF NOT EXISTS subscribers (
    id              INTEGER PRIMARY KEY,
    email           TEXT    NOT NULL UNIQUE,  -- trimmed and lower-cased before it gets here
    status          TEXT    NOT NULL DEFAULT 'pending',
    token           TEXT    NOT NULL UNIQUE,  -- confirm AND unsubscribe link; never reused
    created_at      INTEGER NOT NULL,         -- unix seconds: when they asked
    confirmed_at    INTEGER,                  -- unix seconds: proof of double opt-in
    unsubscribed_at INTEGER,
    confirm_sent_at INTEGER,                  -- set by the homelab puller once it has mailed them
    source_path     TEXT                      -- the page the form was on, no query string
);

CREATE INDEX IF NOT EXISTS subscribers_status ON subscribers (status, created_at);

-- Per-minute flood cap, same idea as the beacon's: anyone can POST to the form.
CREATE TABLE IF NOT EXISTS signup_rate (
    minute INTEGER PRIMARY KEY,
    n      INTEGER NOT NULL
);
