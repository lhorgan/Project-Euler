def go(n):
  counts = {}
  first_cubes = {}

  i = 2
  while True:
    x = i**3
    x_digits = "".join(sorted([c for c in str(x)]))
    if x_digits not in counts:
      counts[x_digits] = 0
      first_cubes[x_digits] = i
    counts[x_digits] += 1
    if counts[x_digits] == n:
      print(first_cubes[x_digits])
      break
    i += 1

go(5)