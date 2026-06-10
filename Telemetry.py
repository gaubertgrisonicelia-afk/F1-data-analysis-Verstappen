import fastf1
import matplotlib.pyplot as plt
import fastf1.plotting
fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme='fastf1')

session = fastf1.get_session(2025, 'Singapore Grand Prix', 'R')
session.load()
ver_lap = session.laps.pick_drivers('VER').pick_fastest()
rus_lap = session.laps.pick_drivers('RUS').pick_fastest()
ver_tel = ver_lap.get_car_data().add_distance()
rus_tel = rus_lap.get_car_data().add_distance()
rbr_color = fastf1.plotting.get_team_color(ver_lap['Team'], session=session)
mer_color = fastf1.plotting.get_team_color(rus_lap['Team'], session=session)

fig, ax = plt.subplots()
ax.plot(ver_tel['Distance'], ver_tel['Speed'], color=rbr_color, label='VER')
ax.plot(rus_tel['Distance'], rus_tel['Speed'], color=mer_color, label='RUS')

ax.set_xlabel('Distance in m')
ax.set_ylabel('Speed in km/h')

ax.legend()
plt.suptitle(f"Fastest Lap Comparison \n "
             f"{session.event['EventName']} {session.event.year} Qualifying")

plt.savefig(
    "outputs/Verstappen VS Russel.png", 
    dpi=150, 
    bbox_inches='tight'
)
plt.show()