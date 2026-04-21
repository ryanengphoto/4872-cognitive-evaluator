STRUCTURE Question
    id: Integer
    question: String
    correct_answer: String
    difficulty: String
END STRUCTURE

GLOBAL knowledge_base: LIST OF Question

FUNCTION calculate_points(difficulty) RETURNS Integer
    IF difficulty == "Easy" THEN RETURN 1
    IF difficulty == "Medium" THEN RETURN 2
    IF difficulty == "Hard" THEN RETURN 3
END FUNCTION

FUNCTION get_next_difficulty(difficulty, is_correct) RETURNS String
    IF is_correct THEN
        IF difficulty == "Easy" THEN RETURN "Medium"
        IF difficulty == "Medium" THEN RETURN "Hard"
        IF difficulty == "Hard" THEN RETURN "Hard"
    ELSE
        IF difficulty == "Easy" THEN RETURN "Easy"
        IF difficulty == "Medium" THEN RETURN "Easy"
        IF difficulty == "Hard" THEN RETURN "Medium"
    END IF
END FUNCTION

FUNCTION determine_cognitive_ability(score) RETURNS String
    IF score < 3 THEN RETURN "Low cognitive ability"
    IF score < 6 THEN RETURN "Average cognitive ability"
    RETURN "High cognitive ability"
END FUNCTION


PROCEDURE start_assessment()
    SET question_pool  = knowledge_base
    SET total_score    = 0
    SET questions_done = 0
    SET max_questions  = FLOOR(SIZE(knowledge_base) / 3)
    SET difficulty     = "Medium"

    WHILE questions_done < max_questions
        SET question = PICK random question of difficulty from question_pool
        REMOVE question from question_pool

        DISPLAY question to user
        SET answer = GET answer from user

        IF answer matches question.correct_answer (case-insensitive) THEN
            SET total_score = total_score + calculate_points(difficulty)
            DISPLAY correct
        ELSE
            DISPLAY incorrect
        END IF

        SET difficulty     = get_next_difficulty(difficulty, answer == correct)
        SET questions_done = questions_done + 1
        UPDATE progress display
    END WHILE

    CALL show_final_results(total_score)
END PROCEDURE


PROCEDURE show_final_results(score)
    DISPLAY score and determine_cognitive_ability(score) to user
    DISPLAY "Play Again" and "Quit"

    IF user chooses "Play Again" THEN
        CALL start_assessment()
    ELSE
        EXIT
    END IF
END PROCEDURE


BEGIN
    CALL start_assessment()
END