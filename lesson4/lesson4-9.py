# タプル→文字列→リスト→タプルの変換
countries=("Japan", "USA", "France")
print(countries)

countries_str=",".join(countries)
print(countries_str)

countries_list=countries_str.split(",")
print(countries_list)

countries_tuple=tuple(countries_list)
print(countries_tuple)