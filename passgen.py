import random
import string

SPECIAL_LIST = "[!%@$^]"
lowers = string.ascii_lowercase
uppers = string.ascii_uppercase
nums = string.digits

def gen_pass(length=20, min_char=5, max_char=6, min_num=2, max_num=3,
             min_special_char=1, max_special_char=1, special_list=None,
             max_upper=2, min_upper=1, max_lower=5, min_lower=2, padding=lowers):

    if max_char < (min_lower + min_upper):
        raise Exception("max_char set to {0} but min_upper + min_lower exceeds"
                        " that: {1}".format(max_char, (max_upper+max_lower)))
    if special_list is None:
        specials = SPECIAL_LIST
    else:
        if isinstance(special_list, str):
            specials = list(special_list)
        else:
            raise Exception("Unknown type passed for special_list. "
                            "Received {0} expected string".format(type(
                                special_list))
                            )

    passlen = min_char + min_num + min_special_char
    if passlen > length:
        raise Exception("Min fields totaled exceed specified length. "
                        "length={0}, mins_total={1}".format(length, passlen))
    passlen = max_char + max_num + max_special_char

    u_lowers = "".join(random.choice(lowers) for i in range(min_lower))
    u_uppers = "".join(random.choice(uppers) for i in range(min_upper))
    u_nums = "".join(random.choice(nums) for i in range(min_num))
    u_specials = "".join(random.choice(specials) for i in range(min_special_char))
    mypass = u_lowers + u_uppers + u_nums + u_specials
    if len(mypass) < length:
        more = length - len(mypass)
        mypass += "".join(random.choice(padding) for i in range(more))
    mypass = list(mypass)
    random.shuffle(mypass)
    return ''.join(mypass)


if __name__ == "__main__":
    print(gen_pass())
