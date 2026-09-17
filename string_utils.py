"""Small string utility used for the code-review workshop demo."""


def slugify(text, separator="-"):
    """Turn an arbitrary string into a lowercase, separator-joined slug."""
    parts = text.strip().lower().split()
    return separator.join(parts)


def truncate(text, limit):
    """Shorten text to `limit` characters, appending an ellipsis if cut."""
    if limit is None or limit <= 0:
        return text
    if len(text) <= limit:
        return text
    return text[:limit] + "..."
