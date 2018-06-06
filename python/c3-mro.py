def linearize(cls):
    if cls is object:
        return [cls]
    ret = list()
    ret.append(cls)
    ret.extend(merge(cls))
    return ret


def merge(cls):
    linear_list = list()
    parent_list = list()
    ret = list()
    for base in cls.__bases__:
        linear_list.append(linearize(base))
        parent_list.append(base)
    linear_list.append(parent_list)
    while linear_list:
        good_head = look_good_head(linear_list)
        if good_head is None:
            raise Exception(cls)
        ret.append(good_head)
        linear_list = remove_good_head(linear_list, good_head)
    return ret


def look_good_head(linear_list):
    for l in linear_list:
        head = l[0]
        is_good = True
        for k in linear_list:
            if k is l:
                continue
            if head in k[1::]:
                is_good = False
                break
        if is_good:
            return head
    return None


def remove_good_head(linear_list, head):
    ret = list()
    for l in linear_list:
        if l[0] == head:
            del l[0]
    for l in linear_list:
        if l:
            ret.append(l)
    return ret

class Ex1:
    class O: pass

    class F(O): pass

    class E(O): pass

    class D(O): pass

    class C(D, F): pass

    class B(D, E): pass

    class A(B, C): pass


class Ex2:
    class O: pass

    class F(O): pass

    class E(O): pass

    class D(O): pass

    class C(D, F): pass

    class B(E, D): pass

    class A(B, C): pass


print('Ex1:')
print(Ex1.A.__mro__)
print(linearize(Ex1.A))

print()
print('Ex2:')
print(Ex2.A.__mro__)
print(linearize(Ex2.A))