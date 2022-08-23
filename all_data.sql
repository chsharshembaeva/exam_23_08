SELECT c.name, c.date_started, l.name, s.name FROM user_course as c
join user_language as l
on c.language_id= l.id
join user_student as s
on c.student_id= s.id
join user_mentor as m
on c.mentor_id= m.id




