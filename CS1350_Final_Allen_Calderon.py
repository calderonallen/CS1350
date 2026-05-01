problem 1 - Dictionary: Gradebook Summary
def gradebook_summary(grades):
    student_averages = {}
    course_totals = {}
    course_counts = {}
    course_student_avgs = {}

    # --- Process each student ---
    for student, courses in grades.items():
        total = 0
        count = 0

        for course, scores in courses.items():
            # Student total
            total += sum(scores)
            count += len(scores)

            # Course totals using .get()
            course_totals[course] = course_totals.get(course, 0) + sum(scores)
            course_counts[course] = course_counts.get(course, 0) + len(scores)

            # Track student average per course
            avg = sum(scores) / len(scores)
            if course not in course_student_avgs:
                course_student_avgs[course] = {}
            course_student_avgs[course][student] = avg

        # Store student average
        student_averages[student] = total / count if count > 0 else 0

    # --- Compute course averages ---
    course_averages = {}
    for course in course_totals:
        course_averages[course] = course_totals[course] / course_counts[course]

    # --- Find top student per course ---
    top_per_course = {}
    for course, students in course_student_avgs.items():
        # Sort by (-avg, name) to break ties alphabetically
        top_student = sorted(students.items(), key=lambda x: (-x[1], x[0]))[0][0]
        top_per_course[course] = top_student

    return {
        "student_averages": student_averages,
        "course_averages": course_averages,
        "top_per_course": top_per_course
    }
  problem 2 -sets:candidate skill matcher
def skill_analysis(candidates, required):
    # --- fully qualified ---
    fully_qualified = sorted([
        name for name, skills in candidates.items()
        if required <= skills   # subset check
    ])

    # --- best match ---
    best_match = None
    best_count = -1

    for name, skills in candidates.items():
        match_count = len(skills & required)  # intersection

        if (match_count > best_count) or (
            match_count == best_count and name < best_match
        ):
            best_match = name
            best_count = match_count

    # --- unique skills ---
    unique_skills = {}

    for name, skills in candidates.items():
        other_skills = set()

        for other_name, other in candidates.items():
            if other_name != name:
                other_skills |= other   # union of others

        unique = skills - other_skills

        if unique:  # only include if not empty
            unique_skills[name] = sorted(list(unique))

    return {
        "fully_qualified": fully_qualified,
        "best_match": best_match,
        "unique_skills": unique_skills
    }
  problem 5 - recursion:subset sum
def subset_sum(nums, target):
    # Base case: if target is 0, an empty subset or chosen numbers worked
    if target == 0:
        return True

    # Base case: no numbers left and target was not reached
    if len(nums) == 0:
        return False

    first = nums[0]
    rest = nums[1:]

    # Recursive choice:
    # include the first number OR exclude the first number
    return subset_sum(rest, target - first) or subset_sum(rest, target)
