import typing as t


def permute(list, strings):
   if list == 1:
      return strings

   return [
      y + x
      for y in permute(1, strings)
      for x in permute(list - 1, strings)
   ]


def main():
   print(permute(1, ["a", "b", "c"]))

   # print(permute(2, ["a", "b", "c"]))


if __name__ == '__main__':
    main()
