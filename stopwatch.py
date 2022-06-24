import PySimpleGUI as sg
from time import time


def create_window():
    w = 500
    h = 500
    sg.theme('NeutralBlue')
    layout = [
        [sg.Push(), sg.Image('cross.png', pad=0, enable_events=True, key='-CLOSE-')],
        [sg.VPush()],
        [sg.Text('0.0', font='Young 70', key='-TIME-')],
        [  # buttons
            sg.Button('Start', font='Young 20', button_color=('#FFFFFF', '#000080'), border_width=0, key='-STARTSTOP-'),

            sg.Button('Lap', font='Young 20', button_color=('#FFFFFF', '#000080'), border_width=0, key='-LAP-',
                      visible=False)
        ],
        [sg.Column([[]], key='-LAPS-')],
        [sg.VPush()],
    ]
    return sg.Window('StopWatch (beta)',
                     layout,
                     size=(w, h),
                     no_titlebar=True,
                     element_justification='center')


def run_stopwatch():
    window = create_window()
    start_time = 0
    active = False
    lap_count = 1
    while True:
        event, values = window.read(timeout=10)
        if event in (sg.WIN_CLOSED, '-CLOSE-'):
            break
        if event == '-STARTSTOP-':
            if active:
                active = False
                window['-STARTSTOP-'].update('Reset')
                window['-LAP-'].update(visible=False)
            else:

                if start_time > 0:
                    window.close()
                    window = create_window()
                    start_time = 0
                    lap_count = 1
                else:
                    start_time = time()
                    active = True
                    window['-STARTSTOP-'].update('Stop')
                    window['-LAP-'].update(visible=True)

        if active:
            elapsed_time = round(time() - start_time, 1)
            window['-TIME-'].update(elapsed_time)

        if event == '-LAP-':
            window.extend_layout(window['-LAPS-'], [
                [sg.Text(lap_count, font='Young 15'), sg.VSeparator(), sg.Text(elapsed_time, font='Young 15')]])
            lap_count += 1
    window.close()


if __name__ == '__main__':
    run_stopwatch()
