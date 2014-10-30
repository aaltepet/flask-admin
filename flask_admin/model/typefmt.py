from jinja2 import Markup
from datetime import datetime
from dateutil.tz import tzlocal,tzfile
from flask.ext.admin._compat import text_type


def null_formatter(view, value):
    """
        Return `NULL` as the string for `None` value

        :param value:
            Value to check
    """
    return Markup('<i>NULL</i>')


def empty_formatter(view, value):
    """
        Return empty string for `None` value

        :param value:
            Value to check
    """
    return ''


def bool_formatter(view, value):
    """
        Return check icon if value is `True` or empty string otherwise.

        :param value:
            Value to check
    """
    glyph = 'ok-circle' if value else 'minus-sign'
    return Markup('<span class="glyphicon glyphicon-%s icon-%s"></span>' % (glyph, glyph))


def list_formatter(view, values):
    """
        Return string with comma separated values

        :param values:
            Value to check
    """
    return u', '.join(text_type(v) for v in values)

try:
    TZ = tzfile('/etc/localtime')
except:
    TZ = tzlocal()

def localizing_datetime_formatter(view, value):
    """
    Converts a tz-aware datetime to local timezone, returning a string
    representation like MM/DD/YY HH:MM TZ.
    """
    if value.tzinfo:
        value = value.astimezone(TZ)
    return value.strftime("%I:%M %p %x %Z")


BASE_FORMATTERS = {
    type(None): empty_formatter,
    bool: bool_formatter,
    list: list_formatter,
    datetime: localizing_datetime_formatter
}
