import fastf1

# https://docs.fastf1.dev/getting_started/basics.html
# ~~~~ Getting started with the basics ~~~~#

## Loading a session
session = fastf1.get_session(2021, 7, "Q")
print(session.name)
print(session.date)

## Loading an event (an event can be a race weekend or testing event consisting of multiple sessions)
print(session.event)
# The Event object is a subclass of a pandas.Series, so the individual values can be accessed as Pandas objects:
print(session.event["EventName"])
print(session.event["EventDate"])
# Load an event directly:
event = fastf1.get_event(2021, 7)
print(event)

## Loading a session or an event by name
event2 = fastf1.get_event(2021, "French Grand Prix")
print(event2["EventName"])

## Working with the event schedule
schedule = fastf1.get_event_schedule(2025)
print(schedule)
print(schedule.columns)
# The event schedule provides methods for selecting specific events:
gp_12 = schedule.get_event_by_round(12)
print(gp_12["Country"])
gp_austin = schedule.get_event_by_name("Austin")
print(gp_austin["Country"])

## Displaying driver info and session results
session.load()
print(session.results)
# The results object (fastf1.core.SessionResults) is a subclass of a pandas.DataFrame.
# Therefore, we can take a look at what data columns there are:
print(session.results.columns)
# As an example, let’s display the top ten drivers and their respective Q3 times. The results are sorted by finishing position:
print(session.results.iloc[0:10].loc[:, ["Abbreviation", "Q3"]])

## Working with laps and lap times
# All individual laps of a session can be accessed through the property Session.laps.
# The laps are represented as Laps object which again is a subclass of a pandas.DataFrame:
session.load()
print(session.laps)
print(session.laps.columns)
# These aren't just DFs though, they have F1-specific methods that can be called:
fastest_lap = session.laps.pick_fastest()
print(fastest_lap["LapTime"])
print(fastest_lap["Driver"])
