import cx_Freeze

executables = [cx_Freeze.Executable("simon.py")]

cx_Freeze.setup(
    name = "Simon",
    options = {"build_exe": {"packages":["pygame"],
                             "include_files":["blue.wav","game_over.wav","green.wav",
                                               "play_button.png","Quicksand-Bold.ttf",
                                               "Quicksand-Regular.ttf","red.wav","sound_off.png",
                                               "sound_on.png","yellow.wav"]}},
    
    executables = executables

    )
