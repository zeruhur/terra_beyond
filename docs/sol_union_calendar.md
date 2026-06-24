# Sol Union Standard Calendar

**Version 1.0 — Terra Beyond Reference Document**

---

## Background

The Sol Union Standard Calendar was ratified as part of the Federated Autonomy Treaty (Year 133 SA). It replaced the Gregorian calendar across all Sol Union jurisdictions for civil and administrative purposes.

The reform was driven by two practical failures of the Gregorian system in a spacefaring context. First, the 7-day week carried religious associations incompatible with the secular federal framework, and its length had no basis in astronomy or administrative logic. Second, the leap year correction mechanism existed solely to keep the calendar synchronized with Earth's seasonal cycle -- a concern irrelevant to orbital habitats, deep-space installations, and colonies on other bodies. Imposing it on the entire Sol Union was recognized as a form of cultural parochialism embedded in administrative law.

The reform was deliberately conservative in all other respects. Month names, day names, and the 24-hour day were retained. The intent was standardization, not reinvention.

---

## Year Structure

| Element | Count | Notes |
|---|---|---|
| Months | 12 | 30 days each |
| Days per regular year | 360 | |
| Weeks per regular year | 72 | 5 days each |
| Foundation Week | 5 days | Week 73, intercalary, not assigned to any month |
| Total days per year | 365 | Fixed, no leap correction |

The year is defined as exactly 365 days of 86,400 SI seconds each, for a total of 31,536,000 SI seconds. This value was fixed at ratification and does not drift or correct. Over centuries, the calendar accumulates a slow displacement against Earth's tropical year (approximately one day every four years). This is accepted as an intentional consequence: the Sol Union calendar is an administrative instrument, not an astronomical one.

---

## Months

Month names are carried forward from the Gregorian calendar without modification, including their historical irregularities. The numerical mismatch of September through December (whose Latin roots name them the 7th through 10th months) was preserved as a fossil of Earth's pre-Julian calendar. The reform committee judged that correcting the names would be more disruptive than retaining them.

Each month is exactly 30 days, divided into 6 weeks of 5 days.

| Number | Name | Gregorian Correspondence (Year 1 SA) |
|---|---|---|
| I | January | Jan 1 -- Jan 30 |
| II | February | Jan 31 -- Mar 1 |
| III | March | Mar 2 -- Mar 31 |
| IV | April | Apr 1 -- Apr 30 |
| V | May | May 1 -- May 30 |
| VI | June | May 31 -- Jun 29 |
| VII | July | Jun 30 -- Jul 29 |
| VIII | August | Jul 30 -- Aug 28 |
| IX | September | Aug 29 -- Sep 27 |
| X | October | Sep 28 -- Oct 27 |
| XI | November | Oct 28 -- Nov 26 |
| XII | December | Nov 27 -- Dec 26 |
| -- | Foundation Week | Dec 27 -- Dec 31 |

Note: Gregorian correspondence shifts by approximately one day every four years due to the absence of leap correction. The values above apply only at the epoch. By 2400 CE the correspondence has displaced by roughly 75 days.

---

## The Week

The 7-day week was reduced to 5 days. Saturday and Sunday were retired. Monday through Friday were retained in order and without renaming.

Friday is the designated rest day. The standard civil and administrative work cycle is Monday through Thursday (four days on, one day off).

| Day | Position | Status |
|---|---|---|
| Monday | 1 | Working day |
| Tuesday | 2 | Working day |
| Wednesday | 3 | Working day |
| Thursday | 4 | Working day |
| Friday | 5 | Rest day |

Because every month is exactly 30 days (6 complete weeks), and the year is 72 complete weeks plus Foundation Week, every date falls on the same day of the week every year without exception. The calendar is fully perpetual from Year 1 SA onward.

---

## Foundation Week

Foundation Week is the 5-day intercalary period at the end of each year, following December 30 and preceding January 1 of the following year. It is Week 73. Its days are not assigned to any month.

The days of Foundation Week use the standard weekday names (Monday through Friday). All five are non-working days across all jurisdictions.

Foundation Week Wednesday is the Sol Union's civic birthday and the single largest public holiday in the calendar. Foundation Week Friday ends at .999, the last moment of the year.

---

## Decimal Civil Time

Civil timekeeping uses a decimal division of the day. The day runs from .000 to .999, representing 1,000 equal units of 86.4 SI seconds each. Time is expressed as a three-digit decimal with a leading point: .347, .000, .999.

This system is timezone-free. Every point in the Sol Union reads the same civil time simultaneously, referenced to the SI second at UTC. Coordination across habitats, planets, and deep-space installations requires no conversion.

SI seconds remain the standard unit for all scientific, navigational, and engineering purposes. The two systems coexist without formal unification. Civil clocks show decimal time; spacecraft computers and physics instruments run on SI seconds. Conversion is handled at the interface layer and is not surfaced to general users.

The decimal time unit is the mil (abbreviation: ml), representing one thousandth of a day (86.4 SI seconds). Time is read aloud as a three-digit number: .347 is "three forty-seven mils."

---

## Date Notation

**Full form:** Year SA, Month name, Week number, Day name, Time

> 312 SA, March, Week 4, Wednesday, .631

**Compact numeric form:** Year.Month.Week.Day.Time

> 312.3.4.3.631

In compact form, days of the week are numbered 1 (Monday) through 5 (Friday). Foundation Week is Week 73:

> 312.73.3 (Foundation Week Wednesday, Year 312 SA)

**Pre-Space Age dates** retain Gregorian notation for historical documents:

> 14 March 1945

---

## Epoch and Era Notation

| Notation | Meaning |
|---|---|
| SA | Space Age. Years from the launch of Sputnik 1 on October 4, 1957. |

Year 1 SA = 1957 CE. The Federated Autonomy Treaty falls around Year 133 SA. The Five Galaxies era falls around Year 5440 SA. Gregorian years appear only in historical and archaeological contexts predating the Space Age.
