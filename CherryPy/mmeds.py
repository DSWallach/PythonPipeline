from subprocess import system_check_call


def check_metadata(file_fp):
    """
    Execute QIIME to check the metadata file provided.
    """
    call_string = 'validate_mapping_file.py ' + file_fp
    try:
        system_check_call(call_string, shell=True)
        return 0
    except ValueError:
        return 1
