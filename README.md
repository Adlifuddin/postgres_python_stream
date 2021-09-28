## create a function in postgres

CREATE OR REPLACE FUNCTION PUBLIC.NOTIFY()
  RETURNS TRIGGER AS $$
DECLARE
BEGIN
  PERFORM pg_notify('notify', row_to_json(NEW)::text);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

## create trigger for a table

CREATE TRIGGER notification_after
AFTER INSERT ON PUBLIC.notification
FOR EACH ROW EXECUTE PROCEDURE PUBLIC.NOTIFY();

## run the test.py script

## every new insert data will be shown