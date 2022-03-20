# Module7
## Run `python restoreData.py` then `pytest testModule.py`

### 1. login - System.py
  - PASSES TEST
  
### 2. check_password - System.py
  - PASSES TEST

### 3. change_grade - Staff.py
  - PASSES TEST

### 4. create_assignment Staff.py
  - PASSES TEST

### 5. add_student - Professor.py
  - FAILS TEST
    - Type Error

### 6. drop_student Professor.py
  - FAILS TEST
    - Because student is not enrolled in the specified course

### 7. submit_assignment - Student.py
  - PASSES TEST

### 8. check_ontime - Student.py
  - PASSES TEST

### 9. check_grades - Student.py
  - PASSES TEST

### 10. view_assignments - Student.py
  - PASSES TEST

**For the last five tests, you will choose what to test for on your own.**

### 11. drop_course - Student.py
  - FAILS TEST
    - Because student is not enrolled in the specified course.

### 12. remove_assignment - Staff.py
  - PASSES TEST
    - Because assignment exists for the specified course

### 13. check_student - Staff.py
  - PASSES TEST
    - Because student is enrolled in specified course

### 14. extend_deadline - Staff.py
  - FAILS TEST
    - Because the function is attempting to look for course that does not exist

### 15. search_course - Student.py
  - FAILS TEST
    - Because the function is attempting to look for course user is not enrolled in
