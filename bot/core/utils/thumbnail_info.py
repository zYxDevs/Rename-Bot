# (c) @AbirHasan2005

from hachoir.parser import createParser
from hachoir.metadata import extractMetadata


async def get_thumbnail_info(thumb_path: str):
    try:
        metadata = extractMetadata(createParser(thumb_path))
    except: return 0, 0
    try:
        height = metadata.get("height") if metadata.has("height") else 0
    except:
        height = 0
    try:
        width = metadata.get("width") if metadata.has("width") else 0
    except:
        width = 0

    return height, width
