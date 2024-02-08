# PAYMENT TYPE CHOICES:
PAYME = "uzcard"
PAYLOV = "paylov"
UZUM_BANK = "uzum bank"
CLICK = "click"

PAYMENT_TYPE_CHOICES = (
    (PAYME, "payme"),
    (CLICK, "click"),
    (PAYLOV, "paylov"),
    (UZUM_BANK, "uzum bank"),
)

# PAYMENT STATUS CHOICES:
SUCCESS = "success"
FAILED = "failed"
PENDING = "pending"

PAYMENT_STATUS_CHOICES = (
    (SUCCESS, "success"),
    (FAILED, "failed"),
    (PENDING, "pending"),
)

# LANGUAGE CODE CHOICES:
RUSSIAN = "ru"
ENGLISH = "en"
UZBEK = "uz"

LANGUAGE_CODE_CHOICES = (
    (RUSSIAN, "Russian"),
    (ENGLISH, "English"),
    (UZBEK, "Uzbek"),
)

# COURSE COMMENT STATUS CHOICES:
ACCEPTED = "accepted"
REJECTED = "rejected"
PENDING = "pending"
COMPLAINT = "complaint"

COURSE_COMMENT_STATUS_CHOICES = (
    (ACCEPTED, "accepted"),
    (REJECTED, "rejected"),
    (PENDING, "pending"),
    (COMPLAINT, "complaint"),
)

# COMPLAINT TYPE CHOICES:

DECEPTION = "deception"
OFFENSIVE = "offensive"
SUICIDE = "suicide"
OTHER = "other"

COMPLAINT_TYPE_CHOICES = (
    (DECEPTION, "deception"),
    (OFFENSIVE, "offensive"),
    (SUICIDE, "suicide"),
    (OTHER, "other"),
)
