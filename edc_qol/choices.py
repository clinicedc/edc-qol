from django.utils.functional import lazy
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

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

format_html_lazy = lazy(format_html, str)
DESCRIBE_HEALTH_CHOICES = (
    ("excellent", _("Excellent")),
    ("very_good", _("Very good")),
    ("good", _("Good")),
    ("fair", _("Fair")),
    ("poor", _("Poor")),
)

FEELING_DURATION_CHOICES = (
    (ALL_OF_THE_TIME, _("All of the time")),
    (MOST_OF_THE_TIME, _("Most of the time")),
    (GOOD_BIT_OF_THE_TIME, _("A good bit of the time")),
    (SOME_OF_THE_TIME, _("Some of the time")),
    (LITTLE_OF_THE_TIME, _("A little of the time")),
    (NONE_OF_THE_TIME, _("None of the time")),
)

HEALTH_LIMITED_CHOICES = (
    ("limited_a_lot", _("YES, limited a lot")),
    ("limited_a_little", _("YES, limited a little")),
    ("not_limited_at_all", _("NO, not at all limited")),
)

INTERFERENCE_DURATION_CHOICES = (
    (ALL_OF_THE_TIME, _("All of the time")),
    (MOST_OF_THE_TIME, _("Most of the time")),
    (SOME_OF_THE_TIME, _("Some of the time")),
    (LITTLE_OF_THE_TIME, _("A little of the time")),
    (NONE_OF_THE_TIME, _("None of the time")),
)

MOBILITY = (
    (NO_PROBLEM_WALKING, _("I have no problems in walking about")),
    (SOME_PROBLEM_WALKING, _("I have some problems in walking about")),
    (CONFINED_TO_BED, _("I am confined to bed")),
)

SELF_CARE = (
    (NO_PROBLEM_SELF_CARE, _("I have no problems with self-care")),
    (PROBLEM_WASHING_DRESSING, _("I have some problems washing or dressing myself")),
    (UNABLE_WASH_DRESS, _("I am unable to wash or dress myself")),
)

USUAL_ACTIVITIES = (
    (NO_PROBLEM_USUAL_ACTIVITIES, _("I have no problems with performing my usual activities")),
    (
        SOME_PROBLEM_USUAL_ACTIVITIES,
        _("I have some problems with performing my usual activities"),
    ),
    (UNABLE_PERFORM_USUAL_ACTIVITIES, _("I am unable to perform my usual activities")),
)

PAIN_DISCOMFORT = (
    (NO_PAIN_DISCOMFORT, _("I have no pain or discomfort")),
    (MODERATE_PAIN_DISCOMFORT, _("I have moderate pain or discomfort")),
    (EXTREME_PAIN_DISCOMFORT, _("I have extreme pain or discomfort")),
)

ANXIETY_DEPRESSION = (
    (NOT_ANXIOUS_DEPRESSED, _("I am not anxious or depressed")),
    (MODERATE_ANXIOUS_DEPRESSED, _("I am moderately anxious or depressed")),
    (EXTREME_ANXIOUS_DEPRESSED, _("I am extremely anxious or depressed")),
)

WORK_PAIN_INTERFERENCE_CHOICES = (
    ("not_at_all", _("Not at all")),
    ("a_little_bit", _("A little bit")),
    ("moderately", _("Moderately")),
    ("quite_a-bit", _("Quite a bit")),
    ("extremely", _("Extremely")),
)

ICECAP_STABILITY = (
    (
        "4",
        format_html_lazy(
            _("I am able to feel settled and secure in <B>all</B> areas of my life")
        ),
    ),
    (
        "3",
        format_html_lazy(
            _("I am able to feel settled and secure in <B>many</B> areas of my life")
        ),
    ),
    (
        "2",
        format_html_lazy(
            _("I am able to feel settled and secure in a <B>few</B> areas of my life")
        ),
    ),
    (
        "1",
        format_html_lazy(
            _("I am <B>unable</B> to feel settled and secure in <B>any</B> areas of my life")
        ),
    ),
)


ICECAP_ATTACHMENT = (
    ("4", format_html_lazy(_("I can have <B>a lot</B> of love, friendship and support"))),
    (
        "3",
        format_html_lazy(_("I can have <B>quite a lot</B> of love, friendship and support")),
    ),
    ("2", format_html_lazy(_("I can have <B>a little</B> love, friendship and support"))),
    ("1", format_html_lazy(_("I <B>cannot</B> have <B>any</B> love, friendship and support"))),
)


ICECAP_AUTONOMY = (
    ("4", format_html_lazy(_("I am able to be <B>completely</B> independent"))),
    ("3", format_html_lazy(_("I am able to be independent in <B>many</B> things"))),
    ("2", format_html_lazy(_("I am able to be independent in <B>a few</B> things"))),
    ("1", format_html_lazy(_("I am <B>unable</B> to be at all independent"))),
)

ICECAP_ACHIEVMENT = (
    ("4", format_html_lazy(_("I can achieve and progress in <B>all</B> aspects of my life"))),
    ("3", format_html_lazy(_("I can achieve and progress in <B>many</B> aspects of my life"))),
    (
        "2",
        format_html_lazy(_("I can achieve and progress in <B>a few</B> aspects of my life")),
    ),
    (
        "1",
        format_html_lazy(
            _("I <B>cannot</B> achieve and progress in <B>any</B> aspects of my life")
        ),
    ),
)


ICECAP_ENJOYMENT = (
    ("4", format_html_lazy(_("I can have <B>a lot</B> of enjoyment and pleasure"))),
    ("3", format_html_lazy(_("I can have <B>quite a lot</B> of enjoyment and pleasure"))),
    ("2", format_html_lazy(_("I can have <B>a little</B> enjoyment and pleasure"))),
    ("1", format_html_lazy(_("I <B>cannot</B> have <B>any</B> enjoyment and pleasure"))),
)
