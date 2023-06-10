def file_upload(instance, filename):

    """
    Return a path for uploading image attchments.
    Adapted from netbox/extras/utils.py
    """
    path = 'netbox-floorplan/'

    if hasattr(instance, 'site'):
        path_prepend = instance.site.id
    # if hasattr(instance, 'floorplan'):
    #     path_prepend = instance.floorplan.id

    # Rename the file to the provided name, if any. Attempt to preserve the file extension.
    # extension = filename.rsplit('.')[-1].lower()
    # # if instance.id and extension in ['bmp', 'gif', 'jpeg', 'jpg', 'png', 'tif', 'tiff', 'svg']:
    # #     filename = '.'.join([instance.id, extension])
    # # elif instance.id:
    # #     filename = instance.id

    return f'{path}{path_prepend}_{filename}'