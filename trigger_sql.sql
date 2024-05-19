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

-- trigger hijau
CREATE OR REPLACE FUNCTION validate_user_review_submission () RETURNS TRIGGER AS $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM ULASAN WHERE id_tayangan = NEW.id_tayangan AND username = NEW.username) THEN
        RETURN NEW;
    ELSE
        RAISE EXCEPTION 'Failed to submit review. You have already reviewed this show.';
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER validate_user_review_submission_trigger BEFORE INSERT ON ULASAN FOR EACH ROW
EXECUTE FUNCTION validate_user_review_submission ();

-- trigger merah 
CREATE OR REPLACE FUNCTION handle_subscription_purchase () RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM transaction t WHERE t.username = NEW.username AND t.end_date_time >= CURRENT_DATE) THEN
        UPDATE transaction
        SET end_date_time = NEW.end_date_time,
            start_date_time = NEW.start_date_time,
            nama_paket = NEW.nama_paket,
            metode_pembayaran = NEW.metode_pembayaran,
            timestamp_pembayaran = NEW.timestamp_pembayaran
        WHERE username = NEW.username AND end_date_time = (SELECT MAX(end_date_time) FROM transaction WHERE username = NEW.username);
        RETURN NULL;
    ELSE
        RETURN NEW;
    END IF;
END
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS handle_subscription_purchase ON TRANSACTION;

CREATE TRIGGER handle_subscription_purchase BEFORE INSERT ON TRANSACTION FOR EACH ROW
EXECUTE FUNCTION handle_subscription_purchase ();