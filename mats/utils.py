def validate_mat(required_properties, mat):
    mat_keys = set(mat.keys())
    if mat_keys != required_properties:
        missing_properties = ", ".join(required_properties.difference(mat_keys))
        error_message = "Mat does not meet requirements."
        if missing_properties:
            error_message += f"\n  Missing properties: {missing_properties}"
        extra_properties = ", ".join(mat_keys)
        if missing_properties:
            error_message += f"\n  Extra properties: {extra_properties}"
        raise Exception(error_message)
