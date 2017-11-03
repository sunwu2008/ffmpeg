from __future__ import unicode_literals

from .nodes import (
    filter_operator,
    InputNode,
    MergeOutputsNode,
    OutputNode,
    output_operator,
)


def input(filename, **kwargs):
    """Input file URL (ffmpeg ``-i`` option)

    Official documentation: `Main options <https://ffmpeg.org/ffmpeg.html#Main-options>`__
    """
    kwargs['filename'] = filename
    fmt = kwargs.pop('f', None)
    if fmt:
        if 'format' in kwargs:
            raise ValueError("Can't specify both `format` and `f` kwargs")
        kwargs['format'] = fmt
    return InputNode(input.__name__, kwargs=kwargs).stream()


@output_operator()
def overwrite_output(stream):
    """No longer supported; see ``overwrite_output`` parameter of ``get_args`` function instead.
    """
    raise NameError('`overwrite_output` operator is no longer supported; see `overwrite_output` parameter of '
        '`get_args` function instead')


@output_operator()
def merge_outputs(*streams):
    """Include all given outputs in one ffmpeg command line
    """
    return MergeOutputsNode(streams, merge_outputs.__name__).stream()


@filter_operator()
def output(stream, filename, **kwargs):
    """Output file URL

    Official documentation: `Synopsis <https://ffmpeg.org/ffmpeg.html#Synopsis>`__
    """
    kwargs['filename'] = filename
    fmt = kwargs.pop('f', None)
    if fmt:
        if 'format' in kwargs:
            raise ValueError("Can't specify both `format` and `f` kwargs")
        kwargs['format'] = fmt
    return OutputNode(stream, output.__name__, kwargs=kwargs).stream()



__all__ = [
    'input',
    'merge_outputs',
    'output',
    'overwrite_output',
]
