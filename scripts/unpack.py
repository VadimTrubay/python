import shutil
filename = r"vad.zip"
extract_dir = r"\work_it\GitHub\GoIt_school\vad"

shutil.unpack_archive(filename, extract_dir)

print("Archive file unpacked successfully.")
# archive_format = "rar"
# Unpack the archive file
# shutil.unpack_archive(filename, extract_dir)
# def unpack(archive_dir, path_to_unpack):
# shutil.unpack_archive(r'\work_it\GitHub\GoIt_school\vad.rar', r'\work_it\GitHub\GoIt_school\vad')


# unpack()