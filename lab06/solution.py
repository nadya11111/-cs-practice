def count_by_extension(paths):
    result = {}
    for path in paths:
        parts = path.split('/')
        filename = parts[-1]


        if '.' in filename:
            dot_index = filename.rfind('.')
            ext = filename[dot_index + 1:].lower()
        else:
            ext = ""


        if ext in result:
            result[ext] = result[ext] + 1
        else:
            result[ext] = 1

    return result


def deepest_path(paths):
    if len(paths) == 0:
        return ""

    best_path = paths[0]
    max_slashes = best_path.count('/')

    for path in paths:
        current_slashes = path.count('/')
        if current_slashes > max_slashes:
            max_slashes = current_slashes
            best_path = path
        elif current_slashes == max_slashes:
            if path < best_path:
                best_path = path

    return best_path


def human_size(n_bytes):
    if n_bytes < 1024:
        return str(n_bytes) + " Б"
    size = n_bytes / 1024
    if size < 1024:
        return f"{size:.1f} КБ"

    size = size / 1024
    if size < 1024:
        return f"{size:.1f} МБ"

    size = size / 1024
    if size < 1024:
        return f"{size:.1f} ГБ"

    size = size / 1024
    return f"{size:.1f} ТБ"