-- trigger biru
CREATE OR REPLACE FUNCTION check_username_uniqueness () RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM PENGGUNA WHERE username = NEW.username) THEN
        RAISE EXCEPTION 'Error: Username already exists';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- trigger kuning
CREATE OR REPLACE FUNCTION restrict_recent_download_deletion () RETURNS TRIGGER AS $$
BEGIN
    IF OLD.timestamp BETWEEN (CURRENT_TIMESTAMP AT TIME ZONE 'Asia/Jakarta') - INTERVAL '24 hours' AND
                               CURRENT_TIMESTAMP AT TIME ZONE 'Asia/Jakarta' THEN
        RAISE EXCEPTION 'Shows downloaded less than a day ago cannot be deleted';
    ELSE
        RETURN OLD;
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER restrict_recent_download_deletion_trigger BEFORE DELETE ON TAYANGAN_TERUNDUH FOR EACH ROW
EXECUTE FUNCTION restrict_recent_download_deletion ();