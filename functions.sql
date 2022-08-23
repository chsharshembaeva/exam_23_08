CREATE OR REPLACE FUNCTION get_course_id_by_email() (email varchar(100))
RETURNS INTEGER AS $$
SELECT id FROM user_course
$$ LANGUAGE SQL;
