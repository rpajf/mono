def divide_into_batches(file_infos, batch_size_bytes):
    """
    Divide a list of file info dicts (with 'name' and 'size' keys) into batches of similar total size.
    Returns a list of batches, each a list of file info dicts.
    """
    batches = []
    current_batch = []
    current_size = 0
    for info in file_infos:
        if current_size + info['size'] > batch_size_bytes and current_batch:
            batches.append(current_batch)
            current_batch = []
            current_size = 0
        current_batch.append(info)
        current_size += info['size']
    if current_batch:
        batches.append(current_batch)
    return batches 