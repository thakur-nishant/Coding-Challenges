def solution(L):
    # write your code in Python 3.6
    counts = {}

    for email in L:
        local_name, domain_name = email.split('@')
        if local_name and domain_name:
            # rule 1 of domain name
            local_name = local_name.replace('.', '')
            # rule 2 of domain name
            index = local_name.find('+')
            if index != -1:
                local_name = local_name[:index]

            unique_email = local_name+'@'+domain_name

            if unique_email in counts:
                counts[unique_email] += 1
            else:
                counts[unique_email] = 1
    print(counts)
    return max(counts, key=counts.get)


L = ['djfab@sdb.com', 'ssd.adf.adf@fsdfa.com', 'absdfdf+fsd.fsdf@fdsda.com', '@', 'fasfsda@', '@sdfsdf', 'dj..f..ab@sdb.com','djfab+extra@sdb.com', 'nishant@gmail.com' ]

x = solution(L)
print(x)
