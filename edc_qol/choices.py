from .constants import (
    CONFINED_TO_BED,
    EXTREME_ANXIOUS_DEPRESSED,
    EXTREME_PAIN_DISCOMFORT,
    MODERATE_ANXIOUS_DEPRESSED,
    MODERATE_PAIN_DISCOMFORT,
    NO_PAIN_DISCOMFORT,
    NO_PROBLEM_SELF_CARE,
    NO_PROBLEM_USUAL_ACTIVITIES,
    NO_PROBLEM_WALKING,
    NOT_ANXIOUS_DEPRESSED,
    PROBLEM_WASHING_DRESSING,
    SOME_PROBLEM_USUAL_ACTIVITIES,
    SOME_PROBLEM_WALKING,
    UNABLE_PERFORM_USUAL_ACTIVITIES,
    UNABLE_WASH_DRESS,
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
