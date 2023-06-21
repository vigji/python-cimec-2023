from psychopy import visual, event, clock

# Create a window to display the stimulus
win = visual.Window(size=(800, 600), fullscr=False)

# create a clock
clock = clock.Clock()

# Create a stimulus
stimulus = visual.TextStim(win, text='Press space key', height=0.1)

# Display the stimulus:
stimulus.draw()
win.flip()

clock.reset()
response = None
# Wait for a response
while response != "space":
    response = event.waitKeys()[0]  # this is a list of presses
    if response != "":
        stimulus.setText(f'Press space key\n\nYou pressed {response}!')

    stimulus.draw()
    win.flip()

# Compute the reaction time in seconds:
reaction_time = clock.getTime()

# Print the reaction time:
print(f"Reaction time: {reaction_time:.3f} seconds")

# Close the window
win.close()
