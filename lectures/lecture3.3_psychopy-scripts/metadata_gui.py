import json
from pathlib import Path
from psychopy import gui

EXPERIMENT_DIRECTORY = Path(r"C:\Users\SNeurobiology\Desktop\temp_dir")

# Create a dialog window
dlg = gui.Dlg(title="Metadata Input")
dlg.addText('Experiment Information')
dlg.addField('Participant ID:')
dlg.addField('Date:')

# Show the dialog window
dlg.show()

# Check if the user clicked 'OK'
if not dlg.OK:
    raise ValueError("User canceled the dialog")

# Retrieve the entered values in a dictionary:
metadata_dict = dict()
metadata_dict["participant_id"] = dlg.data[0]
metadata_dict["date"] = dlg.data[1]


# Save the experiment metadata in a json file:
with open(EXPERIMENT_DIRECTORY / "metadata.json", "w") as f:
    json.dump(metadata_dict, f)

# Here goes the rest of your experiment...
...