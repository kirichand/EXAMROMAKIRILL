# v0.1

#parse_star_parameters

from solar_objects import Star, Planet
with open("solar_system.txt") as input_file:
    for line in input_file:
        if len(line.strip()) == 0 or line[0] == '#':
            continue
        object_type = line.split()[0].lower()
        if object_type == "star":
            print(line)
            star = Star()
            star.R = line.split()[1]
            star.color = line.split()[2]
            star.m = line.split()[3]
            star.x = line.split()[4]
            star.y = line.split()[5]
            star.vx = line.split()[6]
            star.vy = line.split()[7]
            print(star.type, star.R, star.color, star.m, star.x, star.y, star.Vx, star.Vy)