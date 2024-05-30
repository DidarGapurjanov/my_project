



def camel_to_snake_case(input_string: str) -> str:
    """
    >>> camel_to_snake_case("SomeSDK")
    'some_sdk'
    >>> camel_to_snake_case("RServoDrive")
    'r_servo_drive'
    >>> camel_to_snake_case("SDKDemo")
    'sdk_demo'
    """
    chars = []
    for c_idx, char in enumerate(input_string):
        if c_idx and char.isupper():
            nxt_idx = c_idx + 1
            #
            #
            flag = nxt_idx >= len(input_string) or input_string[nxt_idx].isupper()
            prev_char = input_string[c_idx - 1]
            if prev_char.isupper() and flag:
                pass
            else:
                chars.append("_")
        chars.append(char.lower())
    return "".join(chars)
