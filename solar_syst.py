import random
import math


def generate_star_system():
    # Параметры
    stars_count = 7
    planets_count = [30, 15, 30, 15, 30, 15, 30]
    satellites_odd_planets = [5, 10, 15]
    satellites_even_planets = [10, 20, 30]
    max_planets_odd_orbit = 4
    max_planets_even_orbit = 3
    system_distance = 10000000000000  # Расстояние между центрами звёздных систем
    G = 667408  # Условная гравитационная постоянная для целых чисел

    # Массив строк для записи в файл
    lines = []

    # Генерация звёзд
    star_coords = set()
    for star_index in range(1, stars_count + 1):
        # Координаты центра звёздной системы
        system_x = (star_index - 1) * system_distance
        system_y = 0

        # Генерация координат звезды, чтобы они не совпадали с другими звёздами
        star_x = system_x
        star_y = system_y
        star_mass = 1988920000000000000000000000000
        star_coords.add((star_x, star_y))

        # Добавляем звезду
        star_line = f"Star 8 red {star_mass} {star_x} {star_y} 0 0"
        lines.append(star_line)

        # Генерация планет для текущей звезды
        planet_coords = set()
        planet_count = planets_count[star_index - 1]
        for planet_index in range(1, planet_count + 1):
            orbit_number = (planet_index - 1) // (
                max_planets_odd_orbit if star_index % 2 != 0 else max_planets_even_orbit) + 1
            distance = orbit_number * 100000000000 + random.randint(0, 50000000000)

            # Генерация координат планеты, чтобы они не совпадали с другими планетами
            while True:
                angle = random.uniform(0, 2 * 3.141592653589793)
                planet_x = star_x + int(distance * math.cos(angle))
                planet_y = star_y + int(distance * math.sin(angle))
                if (planet_x, planet_y) not in planet_coords:
                    planet_coords.add((planet_x, planet_y))
                    break

            planet_mass = random.randint(100000000000000000000000, 10000000000000000000000000)
            speed = int(math.sqrt(G * star_mass / distance))

            # Начальная скорость перпендикулярна радиусу
            if angle < math.pi / 2 or (angle > math.pi and angle < 3 * math.pi / 2):
                planet_vx = -speed * math.sin(angle)
                planet_vy = speed * math.cos(angle)
            else:
                planet_vx = speed * math.sin(angle)
                planet_vy = -speed * math.cos(angle)

            planet_line = f"Planet {random.randint(2, 8)} {random.choice(['orange', 'blue', 'green', 'red', 'yellow', 'white', 'gray'])} {planet_mass} {planet_x} {planet_y} {int(planet_vx)} {int(planet_vy)}"
            lines.append(planet_line)

            # Генерация спутников для планет
            satellite_coords = set()
            if star_index % 2 == 0 and planet_index in satellites_odd_planets:
                while True:
                    sat_angle = random.uniform(0, 2 * 3.141592653589793)
                    satellite_x = planet_x + random.randint(1000000000, 2000000000) * random.choice([-1, 1])
                    satellite_y = planet_y + random.randint(1000000000, 2000000000) * random.choice([-1, 1])
                    if (satellite_x, satellite_y) not in satellite_coords:
                        satellite_coords.add((satellite_x, satellite_y))
                        break
                satellite_line = f"Satellite {random.randint(1, 8)} blue {random.randint(10000000000000000000000, 1000000000000000000000000)} {satellite_x} {satellite_y} 0 {abs(speed) + random.randint(100, 1000)}"
                lines.append(satellite_line)
            elif star_index % 2 != 0 and planet_index in satellites_even_planets:
                for _ in range(2):
                    while True:
                        sat_angle = random.uniform(0, 2 * 3.141592653589793)
                        satellite_x = planet_x + random.randint(1000000000, 2000000000) * random.choice([-1, 1])
                        satellite_y = planet_y + random.randint(1000000000, 2000000000) * random.choice([-1, 1])
                        if (satellite_x, satellite_y) not in satellite_coords:
                            satellite_coords.add((satellite_x, satellite_y))
                            break
                    satellite_line = f"Satellite {random.randint(1, 8)} blue {random.randint(10000000000000000000000, 1000000000000000000000000)} {satellite_x} {satellite_y} 0 {abs(speed) + random.randint(100, 1000)}"
                    lines.append(satellite_line)

    return lines


def save_to_file(filename, lines):
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')


# Генерация системы
lines = generate_star_system()

# Сохранение в файл
save_to_file("solar_system.txt", lines)



