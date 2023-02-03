def split_binary_file(file_path, chunk_size):
    with open(file_path, 'rb') as binary_file:
        chunk = binary_file.read(chunk_size)
        chunk_index = 1
        while chunk:
            with open(f'chunk{chunk_index}', 'wb') as chunk_file:
                chunk_file.write(chunk)
            chunk = binary_file.read(chunk_size)
            chunk_index += 1


split_binary_file('D:\\a.jpg', 1024 * 1024)  # split the binary file into chunks of 1 MB each
