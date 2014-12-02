import os
import posixpath
from cStringIO import StringIO

import logging
import requests
from PIL import Image, ImageSequence
from paste.httpheaders import CONTENT_DISPOSITION
from pyramid.response import FileIter, FileResponse
from pyramid.view import view_config
from pyramid_duh import argify


LOG = logging.getLogger(__name__)


@view_config(
    route_name='root',
    renderer='index.jinja2')
@argify
def index_view(request, url=None):
    """ Root view '/' """
    if url:
        filename, ext = posixpath.splitext(posixpath.basename(url))
        ext = ext.lower()
        filename = filename + "_sprite" + ext
        if ext == '.gif':
            img_format = 'GIF'
        elif ext == '.png':
            img_format = 'PNG'
        else:
            img_format = None
        stream = download_gif(url)
        sprite = convert_gif(stream)
        data = StringIO()
        sprite.save(data, format=img_format)
        data.seek(0)
        disp = CONTENT_DISPOSITION.tuples(filename=filename)
        request.response.headers.update(disp)
        request.response.app_iter = FileIter(data)
        return request.response
    else:
        return {}


def download_gif(url):
    return StringIO(requests.get(url).content)


def convert_gif(stream):
    image = Image.open(stream)
    frames = ImageSequence.Iterator(image)
    frame_width, frame_height = 0, 0
    frame_width, frame_height = frames[0].size

    width = frame_width*len(list(frames))
    height = frame_height
    out = Image.new('RGBA', (width, height))

    stream.seek(0)
    image = Image.open(stream)
    for i, frame in enumerate(ImageSequence.Iterator(image)):
        out.paste(frame, (frame_width*i, 0))
    return out
