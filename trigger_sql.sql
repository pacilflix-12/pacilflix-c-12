-- trigger biru
CREATE OR REPLACE FUNCTION check_username_uniqueness () RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM PENGGUNA WHERE username = NEW.username) THEN
        RAISE EXCEPTION 'Error: Username already exists';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
