from psychopy import visual, core, event

# Create a window to display the stimulus
win = visual.Window(monitor="TestMonitor", size=(800, 600), fullscr=False)

# Define stimulus properties:
grating = visual.GratingStim(win, size=1, sf=3, ori=45)

mouse = event.Mouse()

# Set initial parameters
stimulus_duration = 0.5  # Duration of the static stimulus in seconds
movement_duration = 4  # Duration of stimulus movement in seconds

# Display the static grating
grating.draw()
win.flip()
core.wait(stimulus_duration)

reaction_time = None
# Start stimulus movement
start_time = core.getTime()  # initial time
while core.getTime() - start_time < movement_duration:
    # Update stimulus phase
    grating.setPhase(core.getTime() - start_time)

    # Check for mouse click
    if mouse.getPressed()[0]:
        response = mouse.getPressed()[0]
        reaction_time = core.getTime() - start_time
        break

    # Draw the updated stimulus
    grating.draw()
    win.flip()

# Print the reaction time
print(f"Reaction time: {reaction_time:.3f} seconds")

# Close the window
win.close()