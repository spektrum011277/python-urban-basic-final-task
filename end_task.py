
import csv
from typing import List, Dict

def read_file(filename: str) -> List[Dict]:
    houses = []
    with open(filename, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            house = dict(area_id=row['area_id'], house_address=row["house_address"],
                         floor_count=int(row["floor_count"]), heating_house_type=row["heating_house_type"],
                         heating_value=float(row["heating_value"]), area_residential=float(row["area_residential"]),
                         population=int(row["population"]))
            houses.append(house)
        return houses

def classify_house(floor_count: int) -> str:
    if not isinstance(floor_count, int):
        raise TypeError("Количество этажей должно принадлежать к целому классу чисел.")
    elif floor_count <= 0:
        raise ValueError("Количество этажей должно быть положительным числом.")


    if floor_count <= 5:
        return "Малоэтажный"
    elif 6 <= floor_count <= 16:
        return "Среднеэтажный"
    else:
        return "Многоэтажный"



def get_classify_houses(houses: List[Dict]) -> List[str]:
    categories = []
    for house in houses:
        categories.append(classify_house(house["floor_count"]))
    return categories


def get_count_house_categories(categories: List[str]) -> Dict[str, int]:
    categories_count = {}
    for category in categories:
        categories_count[category] = categories_count.get(category, 0) + 1
    return categories_count


def min_area_residential(houses: List[Dict]) -> str:
    min_avg_area_residential = float('inf')
    min_avg_area_residential_house = ""

    for house in houses:
        avg_area_residential = house["area_residential"] / house["population"]
        if avg_area_residential < min_avg_area_residential:
            min_avg_area_residential = avg_area_residential
            min_avg_area_residential_house = house["house_address"]

    return min_avg_area_residential_house






if __name__ == "__main__":
    houses_data = read_file("housing_data.csv")
    classified_houses = get_classify_houses(houses_data)
    categories_count = get_count_house_categories(classified_houses)

    print("Количество домов в каждой категории:")
    for category, count in categories_count.items():
        print(f"{category}:  {count} домов")

    # :return: Адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.

    min_area_house_address = min_area_residential(houses_data)
    print(f"\nДом с наименьшим средним \n"
          f"количеством квадратных метров жилой площади \n"
          f"на одного жильца находится \n"
          f"по адресу : {min_area_house_address}")
