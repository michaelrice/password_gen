import random
import string

SPECIAL_LIST = "[!%@$^]"


def gen_pass(length=10, chars=7, req_nums=2, special_chars=1,
             special_char_list=None, upper=2, lower=5, padding=None):

    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    nums = string.digits

    if padding is None:
        padding = lowers
    max_char = upper + lower
    if max_char > chars:
        raise Exception("chars set to {0} but upper + lower exceeds"
                        " that: {1}".format(chars, max_char))

    if special_char_list is None:
        specials = SPECIAL_LIST
    else:
        if isinstance(special_char_list, str):
            specials = list(special_char_list)
        else:
            raise Exception("Unknown type passed for special_list. "
                            "Received {0} expected string".format(type(
                                special_char_list))
                            )

    passlen = chars + req_nums + special_chars
    if passlen > length:
        raise Exception("chars + nums + special_chars total exceeds specified length. "
                        "length={0}, total={1}".format(length, passlen))
    u_lowers = "".join(random.choice(lowers) for i in range(lower))
    u_uppers = "".join(random.choice(uppers) for i in range(upper))
    u_nums = "".join(random.choice(nums) for i in range(req_nums))
    u_specials = "".join(random.choice(specials) for i in range(special_chars))
    mypass = u_lowers + u_uppers + u_nums + u_specials
    if len(mypass) < length:
        more = length - len(mypass)
        mypass += "".join(random.choice(padding) for i in range(more))
    mypass = list(mypass)
    random.shuffle(mypass)
    return ''.join(mypass)


if __name__ == "__main__":
    print(gen_pass(length=20))
