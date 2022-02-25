import os
import csv
import PySimpleGUI as simpleGUI

# Get relative directory.
relativeDir = os.path.dirname(__file__)

# Set GUI theme.
simpleGUI.theme("LightGrey1")

# Builds the layout.
layout = [

    # Gather all of the necessary files for merging and scaling for the unreal engine.
    [simpleGUI.Text("")],
    [simpleGUI.Text("Please specify the path to pipe '.csv' delimited file you wish to convert: ", size=(53, 1),),
     simpleGUI.Input(), simpleGUI.FileBrowse(key="csv_file")],
    [simpleGUI.Button("Submit"), simpleGUI.Exit()]

]

# Building window.
window = simpleGUI.Window("Delimiter Conversion", layout, size=(875, 100))

# Application run.
while True:

    event, values = window.read()

    if event == simpleGUI.WIN_CLOSED or event == "Exit":

        break

    # Run merge scripts and produce files in a 'Data' directory.
    elif event == "Submit":

        # Obtain a '.txt' file name equivalent.
        base_name = os.path.splitext(values["csv_file"])[0]
        pipe_name = base_name + ".txt"

        # Convert the '.csv' file into pipe delimited format.
        with open(values['csv_file']) as csv_file:

            with open(pipe_name, "w", newline="") as pipe_file:

                reader = csv.DictReader(csv_file, delimiter=",")
                writer = csv.DictWriter(pipe_file, reader.fieldnames, delimiter="|")

                writer.writeheader()
                writer.writerows(reader)

        # Stop the program.
        break

