from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from sorl.thumbnail import ImageField

from apps.common.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _

from apps.course.choices import COURSE_COMMENT_STATUS_CHOICES, PAYMENT_TYPE_CHOICES, PAYMENT_STATUS_CHOICES
from apps.course.utils import randomize_certificate_number
from apps.users.models import CustomUser


# Create your models here.
class CourseCategory(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    icon = ImageField(upload_to='categories', null=True, verbose_name=_("Icon"), blank=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class CourseLevel(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    icon = ImageField(upload_to='levels', null=True, verbose_name=_("Icon"), blank=True)

    class Meta:
        verbose_name = _("Level")
        verbose_name_plural = _("Levels")

    def __str__(self):
        return self.title


class Course(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_("Author"), related_name=_("Author"))
    lang_code = models.CharField(max_length=3, verbose_name=_("Language"), )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"), blank=True, null=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Discounted"), blank=True,
                                           null=True)
    discounted_expire_price = models.ForeignKey(
        CourseCategory, on_delete=models.CASCADE, verbose_name=_("Discounted"), related_name=_("Category")
    )
    level = models.ForeignKey(CourseLevel, on_delete=models.CASCADE, verbose_name=_("level"), related_name=_("Level"))
    is_free = models.BooleanField(default=False, verbose_name=_("Is Free"))

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return self.title


class Chapter(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("Course"), related_name="course")

    class Meta:
        verbose_name = _("Chapter")
        verbose_name_plural = _("Chapters")

    def __str__(self):
        return self.title


class Chapter(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("Course"), related_name=_("Course"))

    class Meta:
        verbose_name = _("Chapter")
        verbose_name_plural = _("Chapters")

    def __str__(self):
        return self.title


class VideoLesson(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    body_text = models.CharField(max_length=255, verbose_name=_("Body Text"))
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name=_("Chapter"), related_name="chapter")
    video_path = models.FileField(upload_to="videos", verbose_name=_("Video Path"))
    video_duration = models.DurationField(verbose_name=_("Video Duration"), blank=True, null=True)
    video_thumbnail = models.ImageField(upload_to="thumbnails", verbose_name=_("Video thumbnail"))

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    def __str__(self):
        return self.title


class VideoUserView(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_("User"),
                             related_name="user_video_view")
    video = models.ForeignKey(VideoLesson, on_delete=models.CASCADE, verbose_name=_("Video"),
                              related_name="user_video_view")
    last_watched_time = models.DurationField(verbose_name=_("Last Watched Time"), blank=True, null=True)
    is_finished = models.BooleanField(verbose_name=_("Finished"), default=False)
    progress = models.IntegerField(verbose_name=_("Progress"), blank=True, null=True)

    class Meta:
        verbose_name = _("VideoUserView")
        verbose_name_plural = _("VideoUserViews")

    def __str__(self):
        return f"{self.user}-{self.video}"


class CourseComment(TimeStampedModel):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_("Author"),
                               related_name=_("course_comment_author"))
    rating = models.PositiveSmallIntegerField(verbose_name=_("Rating"),
                                              validators=[MinValueValidator(1), MaxValueValidator(5)])
    status = models.CharField(verbose_name=_("Status"), max_length=50, choices=COURSE_COMMENT_STATUS_CHOICES)
    comment_text = models.TextField(verbose_name=_("Comment Text"))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="comments", verbose_name=_("Course"))

    class Meta:
        verbose_name = _("Course comment")
        verbose_name_plural = _("Course comments")

    def __str__(self):
        return f"{self.author}-{self.course}-{self.rating * '⭐'}"


class CurseCommentComplaint(TimeStampedModel):
    comment = models.ForeignKey(CourseComment, on_delete=models.CASCADE, verbose_name=_("Comment"),
                                related_name="comment")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_("user"),
                             related_name="coursecommentcomplaint_user")
    complaint_type = models.CharField(verbose_name=_("Complaint Type"), max_length=50,
                                      choices=COURSE_COMMENT_STATUS_CHOICES, blank=True, null=True)
    complaint_text = models.TextField(verbose_name=_("Complaint Text"))

    class Meta:
        verbose_name = _("CourseComment Complaint")
        verbose_name_plural = _("CourseComment Complaints")

    def __str__(self):
        return self.user.full_name


class UserCourse(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_("User"), related_name="user_courses")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("Course"), related_name="user_courses")
    is_finished = models.BooleanField(verbose_name=_("Finished"), default=False)

    class Meta:
        verbose_name = _("User course")
        verbose_name_plural = _("User courses")

    def __str__(self):
        return f"{self.user}-{self.course}"


class Payment(TimeStampedModel):
    usercourse = models.ForeignKey(
        UserCourse, on_delete=models.CASCADE, related_name="user_course", verbose_name=_("User Course"), null=True
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Amount"))
    payment_type = models.CharField(
        max_length=50, verbose_name=_("Payment type"), choices=PAYMENT_TYPE_CHOICES
    )  # static choice 1=card, 2=click, 3=uzcard
    payment_status = models.CharField(
        max_length=50, verbose_name=_("Payment status"), choices=PAYMENT_STATUS_CHOICES
    )  # static choice 1=success, 2=failed 3=moderating
    payment_date = models.DateTimeField(verbose_name=_("Payment date"), auto_now_add=True)

    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def __str__(self):
        return str(self.id)

class Certificate(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="certificates", verbose_name=_("User"))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="certificates", verbose_name=_("Course"))
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"), null=True)
    cid = models.CharField(max_length=255, verbose_name=_("CID"), default=randomize_certificate_number)
    file = models.FileField(upload_to="certificates", verbose_name=_("File"), null=True)
    image = models.ImageField(upload_to="certificates", verbose_name=_("Image"), null=True)

    def __str__(self):
        return f"{self.user} - {self.course} - {self.cid}"

    class Meta:
        verbose_name = _("Certificate")
        verbose_name_plural = _("Certificates")
        unique_together = ["user", "course"]


class FavouriteCourse(TimeStampedModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="favourite_courses", verbose_name=_("User")
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="favourite_courses", verbose_name=_("Favourite Course")
    )

    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = _("Favourite Course")
        verbose_name_plural = _("Favourite Courses")
        unique_together = ["user", "course"]
