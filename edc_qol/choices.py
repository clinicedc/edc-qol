from .constants import (
    ALL_OF_THE_TIME,
    CONFINED_TO_BED,
    EXTREME_ANXIOUS_DEPRESSED,
    EXTREME_PAIN_DISCOMFORT,
    GOOD_BIT_OF_THE_TIME,
    LITTLE_OF_THE_TIME,
    MODERATE_ANXIOUS_DEPRESSED,
    MODERATE_PAIN_DISCOMFORT,
    MOST_OF_THE_TIME,
    NO_PAIN_DISCOMFORT,
    NO_PROBLEM_SELF_CARE,
    NO_PROBLEM_USUAL_ACTIVITIES,
    NO_PROBLEM_WALKING,
    NONE_OF_THE_TIME,
    NOT_ANXIOUS_DEPRESSED,
    PROBLEM_WASHING_DRESSING,
    SOME_OF_THE_TIME,
    SOME_PROBLEM_USUAL_ACTIVITIES,
    SOME_PROBLEM_WALKING,
    UNABLE_PERFORM_USUAL_ACTIVITIES,
    UNABLE_WASH_DRESS,
)

DESCRIBE_HEALTH_CHOICES = (
    ("excellent", "Excellent"),
    ("very_good", "Very good"),
    ("good", "Good"),
    ("fair", "Fair"),
    ("poor", "Poor"),
)

FEELING_DURATION_CHOICES = (
    (ALL_OF_THE_TIME, "All of the time"),
    (MOST_OF_THE_TIME, "Most of the time"),
    (GOOD_BIT_OF_THE_TIME, " A good bit of the time"),
    (SOME_OF_THE_TIME, "Some of the time"),
    (LITTLE_OF_THE_TIME, "A little of the time"),
    (NONE_OF_THE_TIME, "None of the time"),
)

HEALTH_LIMITED_CHOICES = (
    ("limited_a_lot", "YES, limited a lot"),
    ("limited_a_little", "YES, limited a little"),
    ("not_limited_at_all", "NO, not at all limited"),
)

INTERFERENCE_DURATION_CHOICES = (
    (ALL_OF_THE_TIME, "All of the time"),
    (MOST_OF_THE_TIME, "Most of the time"),
    (SOME_OF_THE_TIME, "Some of the time"),
    (LITTLE_OF_THE_TIME, "A little of the time"),
    (NONE_OF_THE_TIME, "None of the time"),
)

MOBILITY = (
    (NO_PROBLEM_WALKING, "I have no problems in walking about"),
    (SOME_PROBLEM_WALKING, "I have some problems in walking about"),
    (CONFINED_TO_BED, "I am confined to bed"),
)

SELF_CARE = (
    (NO_PROBLEM_SELF_CARE, "I have no problems with self-care"),
    (PROBLEM_WASHING_DRESSING, "I have some problems washing or dressing myself"),
    (UNABLE_WASH_DRESS, "I am unable to wash or dress myself"),
)

USUAL_ACTIVITIES = (
    (NO_PROBLEM_USUAL_ACTIVITIES, "I have no problems with performing my usual activities"),
    (
        SOME_PROBLEM_USUAL_ACTIVITIES,
        "I have some problems with performing my usual activities",
    ),
    (UNABLE_PERFORM_USUAL_ACTIVITIES, "I am unable to perform my usual activities"),
)

PAIN_DISCOMFORT = (
    (NO_PAIN_DISCOMFORT, "I have no pain or discomfort"),
    (MODERATE_PAIN_DISCOMFORT, "I have moderate pain or discomfort"),
    (EXTREME_PAIN_DISCOMFORT, "I have extreme pain or discomfort"),
)

ANXIETY_DEPRESSION = (
    (NOT_ANXIOUS_DEPRESSED, "I am not anxious or depressed"),
    (MODERATE_ANXIOUS_DEPRESSED, "I am moderately anxious or depressed"),
    (EXTREME_ANXIOUS_DEPRESSED, "I am extremely anxious or depressed"),
)

WORK_PAIN_INTERFERENCE_CHOICES = (
    ("not_at_all", "Not at all"),
    ("a_little_bit", "A little bit"),
    ("moderately", "Moderately"),
    ("quite_a-bit", "Quite a bit"),
    ("extremely", "Extremely"),
)
