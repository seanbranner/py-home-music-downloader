def try_dict(dictionary_name, key):
    try:
        value = dictionary_name[key]
        return value
    except:
        print(f"Dictionary key: {key} doesn't exist in given dictionary.")
        return