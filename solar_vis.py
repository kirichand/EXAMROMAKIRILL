# coding: utf-8
# license: GPLv3

"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие графические объекты и перемещающие их на экране, принимают физические координаты
"""
import math
import tkinter as tk

header_font = "Arial-16"
"""Шрифт в заголовке"""

window_width = 800
"""Ширина окна"""

window_height = 800
"""Высота окна"""

scale_factor = None
"""Масштабирование экранных координат по отношению к физическим.
Тип: float
Мера: количество пикселей на один метр."""




class scale():
    def calculate_scale_factor(max_distance):
        """Вычисляет значение глобальной переменной **scale_factor** по данной характерной длине"""
        global scale_factor
        scale_factor = 0.4*min(window_height, window_width)/max_distance
        print('Scale factor:', scale_factor)


    def scale_x(x):
        """Возвращает экранную **x** координату по **x** координате модели.
        Принимает вещественное число, возвращает целое число.
        В случае выхода **x** координаты за пределы экрана возвращает
        координату, лежащую за пределами холста.

        Параметры:

        **x** — x-координата модели.
        """

        return int(x*scale_factor) + window_width//2


    def scale_y(y):
        """Возвращает экранную **y** координату по **y** координате модели.
        Принимает вещественное число, возвращает целое число.
        В случае выхода **y** координаты за пределы экрана возвращает
        координату, лежащую за пределами холста.
        Направление оси развёрнуто, чтобы у модели ось **y** смотрела вверх.

        Параметры:

        **y** — y-координата модели.
        """

        return int(y*scale_factor) + window_height//2
    

    def scale_min_distance(min_distance):
        """Возвращает экранную **y** координату по **y** координате модели.
        Принимает вещественное число, возвращает целое число.
        В случае выхода **y** координаты за пределы экрана возвращает
        координату, лежащую за пределами холста.
        Направление оси развёрнуто, чтобы у модели ось **y** смотрела вверх.

        Параметры:

        **y** — y-координата модели.
        """

        return int(min_distance*scale_factor) + window_height//2


class update():
    global res 
        
    

    def create_object_image(space, self):
        global previous_x
        global previous_y
        """Создаёт отображаемый объект космического тела (звезды или планеты спутника).

        Параметры:

        **space** — холст для рисования.
        **self** — объект космического тела (звезды или планеты).

        """
        
        x = scale.scale_x(self.x)
        y = scale.scale_y(self.y)
        previous_x=x
        previous_y=y
        r = self.R
        self.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=self.color)
        self.orbit = []  # массив для хранения координат орбиты
        self.orbit_lines = []  # массив для хранения линий орбиты
        self.min_distance = 1
        
    
        
    
    
         
        

    def system_name(space, system_name):
        """Создаёт на холсте текст с названием системы небесных тел.
        Если текст уже был, обновляет его содержание.

        Параметры:

        **space** — холст для рисования.
        **system_name** — название системы тел.
        """
        space.create_text(30, 80, tag="header", text=system_name, font=header_font)

    def clear_orbit(space,self):
        
        for line in self.orbit_lines:
            space.delete(line)
        self.orbit.clear()
        self.orbit_lines.clear()
    
    
    
        
    def optimisation(space,self):
        global index_to_delete
        n = 1
        index_to_delete = n
        while index_to_delete < len(self.orbit):
            del self.orbit[index_to_delete]
            del self.orbit_lines[index_to_delete]
            
            index_to_delete += n
        
    

    def object_position(space, self):
        

        
        """Перемещает отображаемый объект на холсте и обновляет его орбиту.

        Параметры:

        **space** — холст для рисования.
        **self** — тело, которое нужно переместить.
        """
        x = scale.scale_x(self.x)
        y = scale.scale_y(self.y)
        r = self.R
        if x + r < 0 or x - r > window_width or y + r < 0 or y - r > window_height:
            space.coords(self.image, window_width + r, window_height + r,
                         window_width + 2*r, window_height + 2*r)
        
        space.coords(self.image, x - r, y - r, x + r, y + r)


    def update_orbit(space,self,res):
        x = scale.scale_x(self.x)
        y = scale.scale_y(self.y)
        
            # обновляем орбиту
        
        if self.orbit and res==True:
            
            previous_x, previous_y = self.orbit[-1]
            distance = math.sqrt((x - previous_x) ** 2 + (y - previous_y) ** 2)
        
        
            if distance > self.min_distance:
                line = space.create_line(previous_x, previous_y, x, y, fill='white')
                self.orbit_lines.append(line)
                if distance <= self.min_distance:
                    for line in self.orbit_lines:
                        space.delete(line)
        self.orbit.append((x, y))

            
            



        """
            if self.orbit and res==True:
                    previous_x, previous_y = self.orbit[-1]
                    line = space.create_line(previous_x, previous_y, x, y, fill='white')
                    self.orbit_lines.append(line)
        self.orbit.append((x, y))"""

        
        
            
            
            
            
            
            
if __name__ == "__main__":
    
    print("This module is not for direct call!")


    


