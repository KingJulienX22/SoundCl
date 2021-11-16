from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):

    return f'avatar/{instance.id}/{file}'


def validate_size_image(file_obj):
    mb_limit = 2
    if file_obj.size > mb_limit * 1024 * 1024:
        raise ValidationError(f"Максимальний розмір файла {mb_limit}MB")
    return