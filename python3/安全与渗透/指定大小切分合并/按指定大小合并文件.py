def join_binary_files(chunk_files, joined_file_path):
    with open(joined_file_path, 'wb') as joined_file:
        for chunk_file_path in chunk_files:
            with open(chunk_file_path, 'rb') as chunk_file:
                chunk = chunk_file.read()
                joined_file.write(chunk)


chunk_files = ['chunk1', 'chunk2', 'chunk3']
join_binary_files(chunk_files, '/path/to/joined_file')
