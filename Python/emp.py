from collections import defaultdict

managers = ["Manager1", "Manager2", "Manager3"]
employees = [f"Emp{i}" for i in range(1, 13)]

office = defaultdict(list)

list(
    map(
        lambda pair: office[pair[0]].append(pair[1]),
        zip(
            map(lambda i: managers[i % len(managers)], range(len(employees))),
            employees
        )
    )
)

print(dict(office))
