from django.utils.html import format_html

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

ICECAP_STABILITY = (
    ("4", format_html("I am able to feel settled and secure in <B>all</B> areas of my life")),
    ("3", format_html("I am able to feel settled and secure in <B>many</B> areas of my life")),
    (
        "2",
        format_html("I am able to feel settled and secure in a <B>few</B> areas of my life"),
    ),
    (
        "1",
        format_html(
            "I am <B>unable</B> to feel settled and secure in <B>any</B> areas of my life"
        ),
    ),
)


ICECAP_ATTACHMENT = (
    ("4", format_html("I can have <B>a lot</B> of love, friendship and support")),
    ("3", format_html("I can have <B>quite a lot</B> of love, friendship and support")),
    ("2", format_html("I can have <B>a little</B> love, friendship and support")),
    ("1", format_html("I <B>cannot</B> have <B>any</B> love, friendship and support")),
)


ICECAP_AUTONOMY = (
    ("4", format_html("I am able to be <B>completely</B> independent")),
    ("3", format_html("I am able to be independent in <B>many</B> things")),
    ("2", format_html("I am able to be independent in <B>a few</B> things")),
    ("1", format_html("I am <B>unable</B> to be at all independent")),
)

ICECAP_ACHIEVMENT = (
    ("4", format_html("I can achieve and progress in <B>all</B> aspects of my life")),
    ("3", format_html("I can achieve and progress in <B>many</B> aspects of my life")),
    ("2", format_html("I can achieve and progress in <B>a few</B> aspects of my life")),
    (
        "1",
        format_html("I <B>cannot</B> achieve and progress in <B>any</B> aspects of my life"),
    ),
)


ICECAP_ENJOYMENT = (
    ("4", format_html("I can have a lot of enjoyment and pleasure")),
    ("3", format_html("I can have quite a lot of enjoyment and pleasure")),
    ("2", format_html("I can have a little enjoyment and pleasure")),
    ("1", format_html("I cannot have any enjoyment and pleasure")),
)
