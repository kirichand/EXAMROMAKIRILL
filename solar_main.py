# coding: utf-8
# license: GPLv3
import math
import tkinter
from tkinter.filedialog import *
from solar_vis import *
from solar_model import *
from solar_input import *

perform_execution = False
"""Флаг цикличности выполнения расчёта"""

physical_time = 0
"""Физическое время от начала расчёта.
Тип: float"""

displayed_time = None
"""Отображаемое на экране время.
Тип: переменная tkinter"""

time_step = None
"""Шаг по времени при моделировании.
Тип: float"""

space_objects = []


"""Список космических объектов."""

class exe():
    
    def execution():
        """Функция исполнения -- выполняется циклически, вызывая обработку всех небесных тел,
        а также обновляя их положение на экране.
        Цикличность выполнения зависит от значения глобальной переменной perform_execution.
        При perform_execution == True функция запрашивает вызов самой себя по таймеру через от 1 мс до 100 мс.
        """
        
        
        global physical_time
        global displayed_time
        physic_realization.recalculate_space_objects_positions(space_objects, time_step.get())
        if orbit_button['text']=='show orbits':
            for body in space_objects:
                update.object_position(space, body)
                update.update_orbit(space, body,res=False)
                update.clear_orbit(space,body)

                # удаление орбит планет   
            physical_time += time_step.get()
            displayed_time.set("%.1f" % physical_time + " seconds gone")
        elif orbit_button['text']=='delete orbits':
            check=0
            for body in space_objects:
               
               #### check+=1
               
              ####  if check  1:
                ##update.clear_orbit(space,body)
               
                update.object_position(space, body)
                update.update_orbit(space,body,res=True)
                
                
            physical_time += time_step.get()
            displayed_time.set("%.1f" % physical_time + " seconds gone")
        if perform_execution:
            space.after(101 - int(time_speed.get()), exe.execution)

    def draw_orbit_stop():
        for body in space_objects:
           # update.clear_orbit(space,body)
            update.optimisation(space,body)
            
            
        opti_button['text'] = "Start draw"
        opti_button['command'] = exe.draw_orbit_start
    
    def draw_orbit_start():
        for body in space_objects:
               
               #### check+=1
               
              ####  if check  1:
                update.object_position(space, body)
                update.clear_orbit(space,body)
                
                
                
        opti_button['text'] = "Stop draw"
        opti_button['command'] = exe.draw_orbit_stop
        

    def start():
        """Обработчик события нажатия на кнопку Start.
        Запускает циклическое исполнение функции execution.
        """
        global perform_execution
        perform_execution = True
        start_button['text'] = "Pause"
        start_button['command'] = exe.stop

        exe.execution()
        print('Started execution...')


    def stop():
        """Обработчик события нажатия на кнопку Start.
        Останавливает циклическое исполнение функции execution.
        """
       
        global perform_execution
        perform_execution = False
        start_button['text'] = "Start"
        start_button['command'] = exe.start
        print('Paused execution.')



    def clear_orbiit():

        orbit_button['text']='show orbits'
        orbit_button['command'] = exe.show_orbit

    def show_orbit():
    
        orbit_button['text']='delete orbits'
        orbit_button['command'] = exe.clear_orbiit

class file_dialog():
    def open():
        """Открывает диалоговое окно выбора имени файла и вызывает
        функцию считывания параметров системы небесных тел из данного файла.
        Считанные объекты сохраняются в глобальный список space_objects
        """
        
        global space_objects
        global perform_execution
        perform_execution = False
        for obj in space_objects:
            

            space.delete(obj.image)
            # удаление старых изображений планет
    
           
            
               
        in_filename = askopenfilename(filetypes=(("Text file", ".txt"),))
        space_objects = file_management.read_space_objects_data_from_file(in_filename)
        max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in space_objects])
        scale.calculate_scale_factor(max_distance)

        for obj in space_objects:
            if obj.type == 'star':
                update.create_object_image(space, obj)
            elif obj.type == 'planet':
                update.create_object_image(space, obj)
                
            elif obj.type == 'satellite':
                update.create_object_image(space, obj)
            else:
                raise AssertionError()

    def save():
        """Открывает диалоговое окно выбора имени файла и вызывает
        функцию считывания параметров системы небесных тел из данного файла.
        Считанные объекты сохраняются в глобальный список space_objects
        """
        out_filename = asksaveasfilename(filetypes=(("Text file", ".txt"),))
        file_management.write_space_objects_data_to_file(out_filename, space_objects)


def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """
    global physical_time
    global displayed_time
    global time_step
    global time_speed
    global space
    global start_button
    global orbit_button
    global opti_button

    print('Modelling started!')
    physical_time = 0

    root = tkinter.Tk()
    # космическое пространство отображается на холсте типа Canvas
    space = tkinter.Canvas(root, width=window_width, height=window_height, bg="black")
    space.pack(side=tkinter.TOP)
    # нижняя панель с кнопками
    frame = tkinter.Frame(root)
    frame.pack(side=tkinter.BOTTOM)

    start_button = tkinter.Button(frame, text="Start", command=exe.start, width=6)
    start_button.pack(side=tkinter.LEFT)

    orbit_button = tkinter.Button(frame,text = "delete orbits",command=exe.clear_orbiit,width=6)
    orbit_button.pack(side=tkinter.LEFT)

    """ opti_button = tkinter.Button(frame,text = "Stop draw",command=exe.draw_orbit_stop,width=6)
    opti_button.pack(side=tkinter.LEFT)"""

    time_step = tkinter.DoubleVar()
    time_step.set(1)
    time_step_entry = tkinter.Entry(frame, textvariable=time_step)
    time_step_entry.pack(side=tkinter.LEFT)

    time_speed = tkinter.DoubleVar()
    scale = tkinter.Scale(frame, variable=time_speed, orient=tkinter.HORIZONTAL)
    scale.pack(side=tkinter.LEFT)

    load_file_button = tkinter.Button(frame, text="Open file...", command=file_dialog.open)
    load_file_button.pack(side=tkinter.LEFT)
    save_file_button = tkinter.Button(frame, text="Save to file...", command=file_dialog.save)
    save_file_button.pack(side=tkinter.LEFT)

    displayed_time = tkinter.StringVar()
    displayed_time.set(str(physical_time) + " seconds gone")
    time_label = tkinter.Label(frame, textvariable=displayed_time, width=30)
    time_label.pack(side=tkinter.RIGHT)

    root.mainloop()
    print('Modelling finished!')

if __name__ == "__main__":
    main()
