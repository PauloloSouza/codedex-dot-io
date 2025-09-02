# Moon Phases 🌕

def moon_phases(name):
    moon_phases = [
        "New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
        "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"
    ]
    moon_emojis = ["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"]
    
    if name in moon_phases:
        phase = moon_phases.index(name)
        return moon_emojis[phase]
    else:
        return "Invalid Moon Phase"

print(moon_phases("Waning Gibbous"))


#Another resolution for Challenge (This one from codedex.io)

#def moon_phase(phase):
#  Phases = ['New Moon','Waxing Crescent','First Quarter','Waxing Gibbous','Full Moon','Waning Gibbous','Last Quarter','Waning Crescent']
#  phase_image = ['🌑','🌒','🌓','🌔','🌕','🌖','🌗','🌘']
#  return(phase_image[Phases.index(phase)])
#answer = moon_phase("New Moon")
#print(answer)