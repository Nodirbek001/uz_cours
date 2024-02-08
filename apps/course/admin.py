from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from apps.course.models import (Certificate, Chapter, Course, CourseCategory,
                                CourseComment,
                                CourseLevel, FavouriteCourse, Payment,
                                UserCourse, VideoLesson, VideoUserView, CurseCommentComplaint)


class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "get_html_photo")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    fields = ("title", "icon", "get_html_photo", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at", "get_html_photo")
    save_on_top = True

    def get_html_photo(self, object):
        if object.icon:
            return mark_safe(f"<img src='{object.icon.url}' width=50>")

    get_html_photo.short_description = "Category_icon"


class CourseLevelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "get_html_photo")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    fields = ("title", "icon", "get_html_photo", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at", "get_html_photo")
    save_on_top = True

    def get_html_photo(self, object):
        if object.icon:
            return mark_safe(f"<img src='{object.icon.url}' width=50>")

    get_html_photo.short_description = "Level_icon"


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "lang_code",
        "price",
        "discounted_price",
        "discounted_expire_date",
        "category",
        "level",
    )
    list_display_links = ("id", "title", "author")
    search_fields = ("title", "author")
    fields = (
        "title",
        "author",
        "lang_code",
        "price",
        "discounted_price",
        "discounted_expire_date",
        "category",
        "level",
        "created_at",
        "updated_at",
    )
    readonly_fields = ("created_at", "updated_at")
    save_on_top = True


class ChapterAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "course")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    fields = ("title", "course", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    save_on_top = True


class VideoLessonAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "chapter", "video_duration", "get_html_photo")
    list_display_links = ("id", "title", "chapter")
    search_fields = ("title", "chapter")
    fields = (
        "title",
        "body_text",
        "chapter",
        "video_path",
        "video_duration",
        "video_thumbnail",
        "get_html_photo",
        "created_at",
        "updated_at",
    )
    readonly_fields = ("created_at", "updated_at", "get_html_photo")
    save_on_top = True

    def get_html_photo(self, object):
        if object.video_thumbnail:
            return mark_safe(f"<img src='{object.video_thumbnail.url}' width=50>")

    get_html_photo.short_description = "video_thumbnail"


class VideoUserViewsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "video", "last_watched_time", "is_finished")
    list_display_links = ("id", "user", "video")
    search_fields = ("user", "video")
    fields = ("user", "video", "last_watched_time", "is_finished", "progress", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    save_on_top = True


class CourseCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "rating", "status", "course")
    list_display_links = ("id", "author", "course")
    search_fields = ("author", "course")
    fields = ("author", "rating", "status", "comment_text", "course", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    save_on_top = True


class CourseCommentComplaintAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "complaint_type")
    list_display_links = ("id", "user", "complaint_type")
    search_fields = ("user", "complaint_type")
    fields = ("user", "comment", "complaint_type", "complaint_text", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    save_on_top = True


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "usercourse", "amount", "payment_type", "payment_status")
    list_display_links = ("id", "usercourse")
    search_fields = ("usercourse", "payment_type", "payment_date")
    fields = ("usercourse", "amount", "payment_type", "payment_status", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    save_on_top = True


class UserCourseAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "course", "is_finished")
    list_display_links = ("id", "user", "course")
    search_fields = ("user", "course")
    fields = ("user", "course", "is_finished", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    save_on_top = True


class CertificateAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "course", "full_name", "cid", "get_html_photo")
    list_display_links = ("id", "user", "course", "full_name")
    search_fields = ("user", "course", "full_name", "cid")
    fields = ("user", "course", "full_name", "cid", "file", "image", "get_html_photo", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at", "get_html_photo")
    save_on_top = True

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_photo.short_description = "Certificate_Image"


class FavouriteCourseAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "course")
    list_display_links = ("id", "user", "course")
    search_fields = ("user", "course")
    fields = ("user", "course", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    save_on_top = True


admin.site.register(CourseCategory, CourseCategoryAdmin)
admin.site.register(CourseLevel, CourseLevelAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(VideoLesson, VideoLessonAdmin)
admin.site.register(VideoUserView, VideoUserViewsAdmin)
admin.site.register(CourseComment, CourseCommentAdmin)
admin.site.register(CurseCommentComplaint, CourseCommentComplaintAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(UserCourse, UserCourseAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(FavouriteCourse, FavouriteCourseAdmin)
